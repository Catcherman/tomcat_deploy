#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import argparse
import requests
from requests.auth import HTTPBasicAuth

def deploy(url,user,passwd,warfile):
    s = requests.session()
    r = s.get(url,auth=(user,passwd))
    if r.status_code == requests.codes.ok:
        m = re.findall(r'/manager/html/upload(.*?)\"',r.text)
        if m:
            upload_url = '%s/upload%s' %(url,m[0])
            files = {'deployWar':open(warfile,'rb')}
            r = s.post(upload_url,files=files,auth=(user,passwd))
            if r.status_code == requests.codes.ok:
                print 'success!'
            else:
                print 'fail!'
        else:
            print 'there no upload form exist!'
    else:
        print 'username or password fail!'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help='tomcat host and port(eg -> 172.16.80.1:8080)', required=True)
    parser.add_argument('-u', '--user', help='tomcat admin user,default is tomcat',default='tomcat',required=False)
    parser.add_argument('-p', '--passwd', help='tomcat password,default is tomcat',default='tomcat',required=False)
    parser.add_argument('-f', '--warfile',help='the war file to deploy',default='no.war',required=False)
   
    args = parser.parse_args()

    url = 'http://%s/manager/html'%(args.target)
    deploy(url,args.user,args.passwd,args.warfile)

if __name__ == '__main__':
    main()

