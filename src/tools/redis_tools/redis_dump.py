# -*- coding: utf-8 -*-
import redis
import json
import sys

r = redis.Redis(password = sys.argv[1])

key_list = r.keys('*')

dict = {}
for key in key_list:
    value = r.get(key)
    dict[key] = value
print json.dumps(dict, indent = 1)
