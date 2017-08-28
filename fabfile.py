#!/usr/bin/env python2

# from fabric.api import *
from fabric.api import run, local

def who():
    local('whoami')

def host_type():
    run('uname -s')

def hello():
    print("Hello, hi!")

def hi(name="Josef"):
    print("Hi %s!" % name)

def disk():
    run('df -h')

def env():
    run('printenv')

def uptime():
    uptime = run('uptime -p')
    print("Host is %s" % uptime)

def load():
    la = run('uptime').split('average:')[1].split()
    print("Load average for past  1 min: %s" % la[0])
    print("Load average for past  5 min: %s" % la[1])
    print("Load average for past 15 min: %s" % la[2])

def la():
    la = run('cat /proc/loadavg').split()
    print("Load average for past  1 min: %s" % la[0])
    print("Load average for past  5 min: %s" % la[1])
    print("Load average for past 15 min: %s" % la[2])
    proc = la[3].split('/')
    print("Currently running processes: %s" % proc[0])
    print("Total number of processes: %s" % proc[1])
