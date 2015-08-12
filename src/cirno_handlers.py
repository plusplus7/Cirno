#-*- coding: UTF-8 -*-
import json
from Crypto.Cipher import AES
import time
import base64
import uuid
import tornado.web
import tornado.gen
import tornadoredis

g_rclient = tornadoredis.Client()
g_rclient.connect()

def check_password(ciphertext, password):
    if ciphertext == None or password == None:
        return (False, "No enough parameters")

    try:
        ciphertext = ciphertext.decode('hex')
        decryptor = AES.new(password, AES.MODE_CBC, b'0000000000000000')
        plaintext = decryptor.decrypt(ciphertext)
        timestamp = int(plaintext)
        if timestamp+30 >= int(time.time()):
            return (True, "")
        else:
            return (False, "Too old password")
    except Exception, e:
        print e

    return (False, "Invalid password")

def construct_renders(all_area_json):
    area_list = []
    side_list = []
    top_list  = []
    all_area_list = json.loads(all_area_json)

    for area in all_area_list:
        if area['type'] == 1:
            top_list.append(area)
        elif area['type'] == 0:
            area_list.append(area)
        elif area['type'] == -1:
            side_list.append(area)
    return (area_list, side_list, top_list)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class BlogIndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, area_id = "index"):
        pipe = g_rclient.pipeline()
        pipe.get('blog:arealist')
        pipe.get('area:' + area_id)
        all_area_json, area_info_json = yield tornado.gen.Task(pipe.execute)
        (area_list, side_list, top_list) = construct_renders(all_area_json)

        if area_info_json == None:
            self.render("error_page.html", error_info = "该分类不存在", top_list = top_list)
        area_info_list = json.loads(area_info_json)
        for doc in area_info_list[0:5]:
            pipe.get('prev:' + doc)
        prev_list = yield tornado.gen.Task(pipe.execute)

        self.render("blog_index.html", area_list = area_list, prev_list = prev_list, side_list = side_list, top_list = top_list)

class BlogMainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, post_id):
        pipe = g_rclient.pipeline()
        pipe.get('blog:arealist')
        pipe.get('post:' + post_id)
        all_area_json, post_code = yield tornado.gen.Task(pipe.execute)
        (area_list, side_list, top_list) = construct_renders(all_area_json)

        if post_code == None:
            self.render("error_page.html", error_info = "该文章不存在", top_list = top_list)

        self.render("blog_main.html", post_code = post_code, top_list = top_list)

class StorageIndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        pipe = g_rclient.pipeline()
        pipe.get('blog:arealist')
        [all_area_json,] = yield tornado.gen.Task(pipe.execute)
        (area_list, side_list, top_list) = construct_renders(all_area_json)

        self.render("storage_index.html", top_list = top_list)

class AboutmeIndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        pipe = g_rclient.pipeline()
        pipe.get('blog:arealist')
        [all_area_json,] = yield tornado.gen.Task(pipe.execute)
        (area_list, side_list, top_list) = construct_renders(all_area_json)

        self.render("about_me.html", top_list = top_list)
        
class GetPostJsonHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, post_id):
        pipe = g_rclient.pipeline()
        pipe.get('post:' + post_id)
        pipe.get('prev:' + post_id)
        prevcode, postcode = yield tornado.gen.Task(pipe.execute)
        self.finish(json.dumps({"prevcode" : prevcode, "postcode" : postcode}))

class AdminMainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, mode = "raw"):
        pipe = g_rclient.pipeline()
        pipe.get('blog:arealist')
        pipe.get('game:arealist')
        [all_blog_json, all_game_json] = yield tornado.gen.Task(pipe.execute)
        (b_area_list, b_side_list, b_top_list) = construct_renders(all_blog_json)
        (g_area_list, g_side_list, g_top_list) = construct_renders(all_game_json)
        area_list = b_top_list + b_area_list + b_side_list + g_top_list + g_area_list + g_side_list
        pipe = g_rclient.pipeline()
        for i in area_list:
            pipe.get('area:' + i["id"])
        all_areainfo = yield tornado.gen.Task(pipe.execute)
        for i in range(len(all_areainfo)):
            area_list[i]["value"] = all_areainfo[i]
        self.render("admin_main.html", area_list = area_list, co_area_list = b_area_list, side_list = b_side_list, blog_arealist_json = all_blog_json, game_arealist_json = all_game_json, mode = mode)

class AdminDoorHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self, action):
        password = self.get_argument('password')
        pipe = g_rclient.pipeline()
        pipe.get('user:plusplus7')
        [res, ] = yield tornado.gen.Task(pipe.execute)
        code, result = check_password(password, res)
        if  code == False:
            self.finish("<script>alert('%s');window.location = '/nimda';</script>" % result)
            return
            

        if action == "add_post":
            postid  = self.get_argument('postid')
            preview = self.get_argument('preview')
            area    = self.get_argument('area')
            post    = self.get_argument('post')

            pipe = g_rclient.pipeline()
            pipe.get('area:' + area)
            [area_list_json,] = yield tornado.gen.Task(pipe.execute)
            area_list = json.loads(area_list_json)
            area_list.insert(0, postid)
            new_area_list_json = json.dumps(area_list)

            pipe = g_rclient.pipeline()
            pipe.set('area:' + area, new_area_list_json)
            pipe.set('prev:' + postid, preview)
            pipe.set('post:' + postid, post)
            result = yield tornado.gen.Task(pipe.execute)

            self.finish("<script>alert('Success');window.location = '/nimda';</script>")

        elif action == "add_area":
            areaid   = self.get_argument('areaid')
            areaname = self.get_argument('areaname')
            type     = self.get_argument('type')
            section  = self.get_argument('section')

            area_info = {}
            area_info["id"]   = areaid
            area_info["name"]   = areaname
            area_info["type"]   = int(type)

            pipe = g_rclient.pipeline()
            pipe.get(section + ':arealist')
            [section_list_json,] = yield tornado.gen.Task(pipe.execute)

            section_list = json.loads(section_list_json)
            section_list.insert(0, area_info)
            new_section_list = json.dumps(section_list)

            pipe = g_rclient.pipeline()
            pipe.set(section + ':arealist', new_section_list)
            pipe.set('area:' + areaid,  "[]")
            result = yield tornado.gen.Task(pipe.execute)

            self.finish("<script>alert('Success');window.location = '/nimda';</script>")

        elif action == "set_blog_arealist":
            areainfo = self.get_argument('areainfo')
            pipe = g_rclient.pipeline()
            pipe.set('blog:arealist', areainfo)
            result = yield tornado.gen.Task(pipe.execute)

            self.finish("<script>alert('Success');window.location = '/nimda';</script>")

        elif action == "set_game_arealist":
            areainfo = self.get_argument('areainfo')
            pipe = g_rclient.pipeline()
            pipe.set('game:arealist', areainfo)
            result = yield tornado.gen.Task(pipe.execute)

            self.finish("<script>alert('Success');window.location = '/nimda';</script>")

        elif action == "set_areainfo":
            areaid   = self.get_argument('areaid')
            areainfo = self.get_argument('areainfo')

            pipe = g_rclient.pipeline()
            pipe.set('area:' + areaid, areainfo)
            result = yield tornado.gen.Task(pipe.execute)

            self.finish("<script>alert('Success');window.location = '/nimda';</script>")
        else:
            self.finish("<script>alert('Invalid action');window.location = '/nimda';</script>")
