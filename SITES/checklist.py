import os
import sys
import difflib
import time
from termcolor import colored

def chk():
	q1 = input('Have You Completed -O And -sV Scans: <y/n>  ')

	if q1 == 'y':
		sites = input('Name Of File That Holds The URL And IP You Are Testing: ')
		completed = input('What Site Did You Complete:     ')
		IntPro = input('What Was The IP address:   ')
		OS = input('What Was The Likely OS:    ')
#		vers = input('If You Found A Version, Paste It Here:  With A Port Number (else type.. "version: n/a":   \n')
#		quit = print(colored('PRESS "Q" TO QUIT', 'red'))
		quit = ''
#		sites = input('Name Of File That Holds The URL And IP You Are Testing: ')
		frmt = sites
		while quit != 'q':
			vers = input('After Listing All The Versions With Port Numbers, Press "q" To Quit: ')
			port = input('Port:  ')
			quit = input('[c]ontinue OR [q]uit')

		with open('scans.txt', 'a') as f:
			f.write(completed + '\n' + IntPro + '\n' + OS + '\n' + vers + '\nPort:  ' + port + '\n \n ')
		with open(frmt, 'r') as f1:
			with open('temp.txt', 'w') as f2:
				for line in f1:
					if line.strip('\n') != completed:
						f2.write(line)
		os.replace('temp.txt', 'sitesIP.txt')
		with open('sitesIP.txt', 'r') as f3:
			with open('temp.txt', 'w') as f4:
				for line in f3:
					if line.strip('\n') != IntPro:
						f4.write(line)
		os.replace('temp.txt', 'sitesIP.txt')

		q3 = input('Would You Like To See What Site You Need To Work On Next: <y/n>   ')
		if q3 == 'y':
			c = 'cat sitesIP.txt'
			os.system(c)

	elif q1 == 'n':
		q2 = input('Did You Need To Look At The List Of Sites: <y/n> ')
		if q2 == 'y':
			c = 'cat sitesIP.txt'
			os.system(c)
		elif q2 == 'n':
			print('Well Than You Must Want To See A List Of Sites That You Have Completed!')
			com = 'cat scans.txt'
			os.system(com)


chk()
