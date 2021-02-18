#!usr/bin/env python

import subprocess
import urllib2

def update_client_version(version):
				with open("version.txt", "r") as vnum:
								if vnum.read() != version:
												return True
								else:
												return False

def main():
				version = urllib2.urlopen("https://github.com/cactusjackk7/Reverse-Engineering
