from fabric.api import run

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
