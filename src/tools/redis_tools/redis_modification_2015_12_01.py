# -*- coding: utf-8 -*-
import redis
import json
import sys

r = redis.Redis(password = sys.argv[1])
l = json.loads(r.get("game:arealist"))
nd = {"top" : [], "side" : [], "common" : []}
for i in l:
    if i["type"] == 1:
        nd["top"].append({"name" : i["name"], "id" : i["id"]})
    elif i["type"] == 0:
        nd["common"].append({"name" : i["name"], "id" : i["id"]})
    elif i["type"] == -1:
        nd["side"].append({"name" : i["name"], "id" : i["id"]})
    else:
        print i
r.set("game:arealist", json.dumps(nd))
l = json.loads(r.get("blog:arealist"))
nd = {"top" : [], "side" : [], "common" : []}
for i in l:
    if i["type"] == 1:
        nd["top"].append({"name" : i["name"], "id" : i["id"]})
    elif i["type"] == 0:
        nd["common"].append({"name" : i["name"], "id" : i["id"]})
    elif i["type"] == -1:
        nd["side"].append({"name" : i["name"], "id" : i["id"]})
    else:
        print i
r.set("blog:arealist", json.dumps(nd))
