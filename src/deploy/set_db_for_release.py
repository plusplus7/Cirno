# -*- coding: utf-8 -*-
import json
import redis
import sys

r = redis.Redis()
r.auth(sys.argv[1])
r.flushall()

temp_post = """"
<article class="post tag-laravel-5-1 tag-artisan">
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
</article>
"""

r.set("user:plusplus7", sys.argv[2])
r.set("post:aboutme", temp_post % "aboutme")
r.set("post:storage", temp_post % "storage")
r.set("blog:arealist", json.dumps("[]", indent = 1))
r.set("game:arealist", json.dumps("[]", indent = 1))
