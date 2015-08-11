# -*- coding: utf-8 -*-
import json
import redis

r = redis.Redis()

r.flushall()
common_arealist = """
[  
    {"id" : "index", "type":1,"name":"生活日常"}, {"id" : "common2", "type":1,"name":"生活日常2"},{"id" : "common3", "type":1,"name":"生活日常3"},
    {"id" : "common4", "type":0,"name":"生活日常4"},{"id" : "common5", "type":0,"name":"生活日常5"},{"id" : "common6", "type":0,"name":"生活日常6"},
    {"id" : "common7", "type":-1,"name":"生活日常7"},{"id" : "common8", "type":-1,"name":"生活日常8"}
]"""
common_areainfo = """
[
    "%s"
]
"""
blog_arealist = common_arealist.replace("common", "blog")
game_arealist = common_arealist.replace("common", "game")
common_prev = """<article id="52" class="post tag-laravel-5-1 tag-artisan">
<div class="post-head">
<h1 class="post-title"><a href="/blog/post/%s">云服务器ECS</a></h1>
<div class="post-meta">
<span class="author">作者：<a href="plusplus7.com/blog">plusplus7</a></span> •
<time class="post-date" datetime="2015年6月26日星期五下午4点15" title="2015年6月26日星期五下午4点15">2015.06.26</time>
</div>
</div>
<div class="post-content">
<p> 云服务器（Elastic Compute Service 简称ECS）是一种简单高效，处理能力可弹性伸缩的计算服务助您快速构建更稳定、安全的应用。提升运维效率，降低IT成本，使您更专注于核心业务创新</p>
</div>
<div class="post-permalink">
<a href="/blog/post/asdf" class="btn btn-default">阅读全文</a>
</div>
</article>
"""
ba = json.loads(blog_arealist)
ga = json.loads(game_arealist)

r.set("user:plusplus7", "asdfasdfasdfasdf")
r.set("blog:arealist", json.dumps(ba, indent = 1))
r.set("game:arealist", json.dumps(ga, indent = 1))
for sba in ba:
    r.set("area:" + sba["id"], common_areainfo % ("post" + sba["id"]))
    r.set("post:" + "post" + sba["id"], common_prev.decode('UTF-8') % ("post" + sba["id"]))
    r.set("prev:" + "post" + sba["id"], common_prev.decode('UTF-8') % ("post" + sba["id"]))

for sga in ga:
    r.set("area:" + sga["id"], common_areainfo % ("post" + sga["id"]))
    r.set("post:" + "post" + sga["id"], common_prev.decode('UTF-8') % ("post" + sga["id"]))
    r.set("prev:" + "post" + sga["id"], common_prev.decode('UTF-8') % ("post" + sga["id"]))
