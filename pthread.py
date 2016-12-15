#!/usr/bin/python3
__author__ = "Samuel"

import math
import threading

class aThread(threading.Thread):
	def __init__(self, num, val):
		threading.Thread.__init__(self)
		self.thread_num = num
		self.loop_count = val

	def run(self):
		print ("Thread Starting: ", self.thread_num)
		myfunc(self.thread_num, self.loop_count)
	
def myfunc(num, val):
	count = 0
	while count < val:
		print ("factorial", num + val , " : ", math.factorial(val+count)) 
		count = count + 1

thread_one = aThread(1,15)
thread_two = aThread(2,20)
thread_three = aThread(3,10)
thread_four = aThread(4,25)

thread_one.start();
thread_two.start();
thread_three.start();
thread_four.start();
