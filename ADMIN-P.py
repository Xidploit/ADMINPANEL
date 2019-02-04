#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "ketemu bray, Ok>> ",req_link

def Credit()

Space(9); print "__ ____     __  _____ ____"
Space(9); print "|  \/  |  _ \    \ \/ /_ _|  _ \"
Space(9); print "| |\/| | |_) |    \  / | || | | |"
Space(9); print "| |  | |  _ <     /  \ | || |_| |"
Space(9); print "|_|  |_|_| \_\___/_/\_\___|____/"
           Space(9); print " |_____|"
	Space(9); print "_____________________________________"
	Space(9); print "|   *** Admin Panel V 0.0.1  ***    |"
	Space(9); print "|Autor     : MR_XID                 |"
	Space(9); print "|Thanks to : D35TR0Y SQUAD          |"
	Space(9); print "_____________________________________"

Credit()
findAdmin()
