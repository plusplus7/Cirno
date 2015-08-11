import tornado.web
import tornado.ioloop
import os
from cirno_handlers import *

urls = [
    (r'/', IndexHandler),
    (r'/blog', BlogIndexHandler),
    (r'/blog/area/(?P<area_id>[a-zA-Z0-9-_]+)', BlogIndexHandler),
    (r'/blog/post/(?P<post_id>[a-zA-Z0-9-_]+)', BlogMainHandler),
    (r'/get_post_json/(?P<post_id>[a-zA-Z0-9-_]+)', GetPostJsonHandler),
    (r'/nimda', AdminMainHandler),
    (r'/nimda/(?P<action>[a-zA-Z0-9-_]+)', AdminDoorHandler),
    (r'/storage', StorageIndexHandler),
    (r'/aboutme', AboutmeIndexHandler),
    (r'.*', StorageIndexHandler),
]

settings = {
    "static_path"   : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
    "debug"         : True,
    "gzip"          : True,
}

def main(host="0.0.0.0", port=8080):
    app = tornado.web.Application(urls, **settings)
    app.listen(port, host)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
