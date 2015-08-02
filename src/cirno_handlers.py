#-*- coding: UTF-8 -*-
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class BlogIndexHandler(tornado.web.RequestHandler):
    def get(self, area_id = "index"):
        print area_id
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
        <h1 class="post-title"><a href="/post/install-and-run-laravel-5-x-on-windows/">在 Windows 上快速安装并运行 Laravel 5.x</a></h1>
        <div class="post-meta">
        <span class="author">作者：<a href="/author/wangsai/">王赛</a></span> •
        <time class="post-date" datetime="2015年6月26日星期五下午4点15" title="2015年6月26日星期五下午4点15">2015年6月26日</time>
        </div>
        </div>
        <div class="post-content">
        <p>安装 PHP   注意一：Laravel 5.0 开始对 PHP 版本的要求是 &gt;=5.4，Laravel 5.1 要求 PHP 版本 &gt;=5.5.9，所以，建议大家尽量安装 5.5.x 的最新版本，写此文章时，最新版本是 5.5.27。        注意二：PHP 5.4 是最后一个支持 Windows</p>
        </div>
        <div class="post-permalink">
        <a href="/post/install-and-run-laravel-5-x-on-windows/" class="btn btn-default">阅读全文</a>
        </div>

        <footer class="post-footer clearfix">
        <div class="pull-left tag-list">
        <i class="fa fa-folder-open-o"></i>
        <a href="/tag/laravel-5-1/">Laravel 5.1</a>, <a href="/tag/artisan/">Artisan</a>
        </div>
        <div class="pull-right share">
        </div>
        </footer>
        </article>"""
        prev_list.append(prev)

        side_list = []
        side_list.append(area)
        side_list.append(area2)
        side_list.append(area3)
        self.render("blog_index.html", area_list = area_list, prev_list = prev_list, side_list = side_list, top_list = area_list)
