# -*- coding: utf-8 -*-
import redis
import json
import sys

r = redis.Redis(password = sys.argv[1])

fp = open(sys.argv[2])
j = json.load(fp)
fp.close()

for key in j.keys():
    r.set(key, j[key])
