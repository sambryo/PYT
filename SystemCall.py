#!/usr/bin/python3

__author__ = "Samuel"

import os
from subprocess import call 

print(os.getcwd())
print(os.getuid())
print(os.getenv("PATH"))

#option 1
os.system("ls -la")
in_put = input("Hit Enter")
#option 2
call(["ls", "-la"])
