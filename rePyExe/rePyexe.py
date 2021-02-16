#!/usr/bin/env python

import time, os, sys

def clear():
				os.system("clear")


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def heading():
				sys.stdout.write(GREEN + """

 _  .-')    ('-.     _ (`-.                      ('-.  ) (`-.        ('-.  
 ( \( -O ) _(  OO)   ( (OO  )                   _(  OO)  ( OO ).    _(  OO)   
  ,------.(,------. _.`     \ ,--.   ,--.-----.(,------.(_/.  \_)-.(,------. )
	|   /`. '|  .---'(__...--''  \  `.'  / ,-.   \|  .---' \  `.'  /  |  .---' 
	|  /  | ||  |     |  /  | |.-')     /'-'  |  ||  |      \     /\  |  |     
	|  |_.' (|  '--.  |  |_.' (OO  \   /    .'  /(|  '--.    \   \ | (|  '--. 
	|  .  '.'|  .--'  |  .___.'|   /  /\_ .'  /__ |  .--'   .'    \_) |  .--' 
	|  |\  \ |  `---. |  |     `-./  /.__)       ||  `---. /  .'.  \  |  `---. 
	`--' '--'`------' `--'       `--'    `-------'`------''--'   '--' `------'  """ + END + BLUE +  '\n' + '{1}R{0}everse {1}E{0}ngineering {1}Py2Exe{2}{3}'.format(YELLOW, RED, YELLOW, BLUE).center(90) + '\n' + 'by: {0}Alisson Moretto ({1}4w4k3{2})'.format(
					YELLOW, RED, YELLOW, BLUE).center(140) + 
			'\n' + '{0}4w4k3@protonmail.com'.format(
						BLUE).center(140) + '\n' + 'Version: {0}0.4{1}\n'.format(YELLOW, END).center(145))

def optionBanner():
				print("\nChoose option from menu:\n")
				time.sleep(0.2)
				print('\t{0}[{1}1{2}]{3} Reverse Exe -> Py').format(YELLOW, RED, YELLOW, WHITE)
				time.sleep(0.2)
				print('\t{0}[{1}3{2}]{3} Reverse Pyc -> Py').format(YELLOW, RED, YELLOW, WHITE)
				time.sleep(0.2)
				print('\n\t{0}[{1}Q{2}]{3} Quit    {0}[{1}U{2}]{3} Update \n').format(YELLOW, RED, YELLOW, WHITE)

def exe2pyc():
				s = raw_input("Type the path of your exe: ")
				ff = str(s)
				check = os.path.isfile(ff)
				if check == True:
								os.popen('python unpyece.py ' + s)
								c = str(s.split('.exe')[0])
								d = '.py.pyc'
								z = c + d
								os.popen('mv single.py.pyc ' + 2)
								cwd = str(os.getcwd())
								clear()
								heading()
								print ' '
								print 'Processing the EXEcutable..'
								sys.stdout.write(YELLOW + ' [*] Working: ' + END + cwd + '/' + str(s))
								print ''
								time.sleep(5)
								clear()
								heading()
								print ''
								print 'Everything is OK!'
								sys.stdout.write(GREEN + ' [*] Done : ' + END + cwd + '/' + c + ' .py.pyc')
								print ''
								sys.exit(0)
						else:

