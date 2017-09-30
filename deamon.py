#!/usr/bin/python
import os
import time
from daemon import runner

class App():
    def __init__(self):
        self.root = os.path.abspath(os.path.dirname(__file__))
        #Root directory
        self.run_dir = os.path.join(self.root, "run")
        self.stdin_path = '/dev/null'
        #File logs
        self.stdout_path = os.path.join(self.run_dir, 'stdout.txt') #this file is the output of deamon
        self.stderr_path = os.path.join(self.run_dir, 'stderr.txt') #If you have a error
        self.pidfile_path = os.path.join(self.run_dir,'test.pid') #Deamon Process ID
        self.pidfile_timeout = 5
    def run(self):
        while True:
            print("Hi I'am a Deamon... Created in Python....")
            time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
