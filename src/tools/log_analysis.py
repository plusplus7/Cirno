#-*- coding: UTF-8 -*-
import sys
import json
import tornado.template
import urllib2

def create_ipindex(filename):
    reqlist = []
    ipindex = {}
    codeindex = {}
    fp = open(filename, "r")
    for line in fp.readlines():
        res = line.strip().replace("[", "").replace("]", "").replace("(", "").replace(")", "").split(" ")
        if len(res) != 9:
            print "LA fuzz: ", line
        ip = res[7]
        code = res[4]
        if ip not in ipindex:
            ipindex[ip] = []
        if code not in codeindex:
            codeindex[code] = []
        req = {}
        req["date"]     = res[1]
        req["time"]     = res[2]
        req["code"]     = res[4]
        req["method"]   = res[5]
        req["path"]     = res[6]
        req["ip"]       = res[7]
        req["latency"]  = res[8]
        ipindex[ip].append(req)
        codeindex[code].append(req)
        reqlist.append(req)
    return ipindex, codeindex, reqlist

def fetch_geography_info(ipindex):
    ip_geo = {}
    for ip in ipindex.keys():
        url = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=" + ip
        try:
            data = urllib2.urlopen(url)
            data = data.read()
            data = json.loads(data)
            ip_geo[ip] = data["country"] + "," + data["province"] + "," + data["city"]
        except Exception, e:
            ip_geo[ip] = e
    return ip_geo

def analysis(filename):
    loader = tornado.template.Loader(".")
    ipindex, codeindex, reqlist = create_ipindex(filename)
    ip_geo = fetch_geography_info(ipindex)
    print loader.load("analysis_report.tpl").generate(ipindex = ipindex, codeindex = codeindex, reqlist = reqlist, ip_geo = ip_geo)

if __name__ == "__main__":
    analysis(sys.argv[1])
