#!/usr/bin/env python3
'''
IPCleaner.py - A tool for searching files for IP addresses and performing subnetting on a given IP address and subnet mask.
'''

from classes.ArgumentParser.ArgumentParser import ArgumentParser
from classes.Controller.Controller import Controller
from classes.Output.Output import Output

class IPCleaner():
	def __init__(self):
		self.arguments = ArgumentParser()
		self.output = Output()
		self.controller = Controller(self.arguments, self.output)

if __name__ == '__main__':
	main = IPCleaner()
