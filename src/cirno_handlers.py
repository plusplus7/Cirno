#-*- coding: UTF-8 -*-
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class BlogIndexHandler(tornado.web.RequestHandler):
    def get(self, area_id = "index"):
        area_list = []
        area = {}
        area2 = {}
        area3 = {}
        area['current'] = True
        area['id'] = "test_area_id"
        area['name'] = r"生活日常"
        area_list.append(area)
        area2['current'] = False
        area2['id'] = "test_area_id2"
        area2['name'] = r"生活日常2"
        area_list.append(area2)
        area3['current'] = False
        area3['id'] = "test_area_id3"
        area3['name'] = "生活日常2"
        area_list.append(area3)
        prev_list = []
        prev = """<article id="52" class="post tag-laravel-5-1 tag-artisan">

        <div class="post-head">
        <h1 class="post-title"><a href="./blog/post/asdf">云服务器ECS</a></h1>
        <div class="post-meta">
        <span class="author">作者：<a href="plusplus7.com/blog">plusplus7</a></span> •
        <time class="post-date" datetime="2015年6月26日星期五下午4点15" title="2015年6月26日星期五下午4点15">2015.06.26</time>
        </div>
        </div>
        <div class="post-content">
        <p> 云服务器（Elastic Compute Service 简称ECS）是一种简单高效，处理能力可弹性伸缩的计算服务助您快速构建更稳定、安全的应用。提升运维效率，降低IT成本，使您更专注于核心业务创新</p>
        </div>
        <div class="post-permalink">
        <a href="./blog/post/asdf" class="btn btn-default">阅读全文</a>
        </div>

        </article>"""
        prev_list.append(prev)

        side_list = []
        side_list.append(area)
        side_list.append(area2)
        side_list.append(area3)
        self.render("blog_index.html", area_list = area_list, prev_list = prev_list, side_list = side_list, top_list = area_list)

class BlogMainHandler(tornado.web.RequestHandler):
    def get(self, post_id):
        area_list = []
        area = {}
        area2 = {}
        area3 = {}
        area['current'] = True
        area['id'] = "test_area_id"
        area['name'] = r"生活日常"
        area_list.append(area)
        area2['current'] = False
        area2['id'] = "test_area_id2"
        area2['name'] = r"生活日常2"
        area_list.append(area2)
        area3['current'] = False
        area3['id'] = "test_area_id3"
        area3['name'] = "生活日常2"
        area_list.append(area3)

        post_list = []
        post = "My article"
        post_list.append(post)
        self.render("blog_main.html", area_list = area_list, post_list = post_list, top_list = area_list)

class AdminMainHandler(tornado.web.RequestHandler):
    def get(self):
        area_list = []
        area = {}
        area2 = {}
        area3 = {}
        area['current'] = True
        area['id'] = "test_area_id"
        area['name'] = r"生活日常"
        area_list.append(area)
        area2['current'] = False
        area2['id'] = "test_area_id2"
        area2['name'] = r"生活日常2"
        area_list.append(area2)
        area3['current'] = False
        area3['id'] = "test_area_id3"
        area3['name'] = "生活日常2"
        area_list.append(area3)

        side_list = []
        side_list.append(area)
        side_list.append(area2)
        side_list.append(area3)

        self.render("admin_main.html", area_list = area_list, side_list = side_list, top_list = side_list)
