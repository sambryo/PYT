#!/usr/bin/python3

__author__ = "Samuel"

import os
from subprocess import call 

print(os.getcwd())
print(os.getuid())
print(os.getenv("PATH"))

os.system("ls -la")
in_put = input("Hit Enter")
call(["ls", "-la"])
