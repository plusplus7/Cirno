import tornado.web
import tornado.options
import logging
import tornado.ioloop
import os
from cirno_handlers import *

urls = [
    (r'/', IndexHandler),
    (r'/game', GameIndexHandler),
    (r'/game/area/(?P<area_id>[a-zA-Z0-9-_]+)', GameIndexHandler),
    (r'/game/post/(?P<post_id>[a-zA-Z0-9-_]+)', GameMainHandler),
    (r'/blog', BlogIndexHandler),
    (r'/blog/area/(?P<area_id>[a-zA-Z0-9-_]+)', BlogIndexHandler),
    (r'/blog/post/(?P<post_id>[a-zA-Z0-9-_]+)', BlogMainHandler),
    (r'/nimda', AdminMainHandler),
    (r'/nimda_(?P<mode>[a-zA-Z0-9-_]+)', AdminMainHandler),
    (r'/nimda/(?P<action>[a-zA-Z0-9-_]+)', AdminDoorHandler),
    (r'/storage', StorageIndexHandler),
    (r'/aboutme', AboutmeIndexHandler),
]

settings = {
    "static_path"   : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
    "debug"         : True,
    "gzip"          : True,
}

def main(host="0.0.0.0", port=8080):
    tornado.options.parse_command_line()
    access_log = logging.getLogger("tornado.access")
    app_log = logging.getLogger("tornado.application")
    gen_log = logging.getLogger("tornado.general")
    app = tornado.web.Application(urls, **settings)
    app.listen(port, host)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
