# TOOL WRITTEN BY @0XJACK
# long live deletehumanity

import requests
import sys
from threading import Thread
from colorama import Fore, init
init()

class c:
	g = Fore.GREEN
	y = Fore.YELLOW
	r = Fore.RED
	w = Fore.WHITE

def getList(list):
	try:
		wlist = open(list, 'r')
		return wlist
	except:
		print 'Unable to open social list'
		sys.exit()
def testMedia(name, social, f, s):
	global num
	try:
		r = requests.get(f.strip() + name.strip() + s.strip())
	except KeyboardInterrupt:
		print
		sys.exit()
	if r.status_code == 200:
		print '"%s" exists on %s'%(c.g+name+c.w, c.g+social+c.w)
		num += 1
	else:
		if '-v' in sys.argv:
			print '"%s" does not exist on %s'%(c.r+name+c.w, c.r+social+c.w)
def parseW(name, list):
	global num
	num = 0
	for line in list:
		if line.strip() != '' and line.strip()[0] != '#':
			social, page = line.split(':', 1)
			f,s = page.split('<user>')
			if '-t' in sys.argv:
				#print c.y + '---[-]' + c.w + ' Scanning %s...'%(page.strip())
				t = Thread(target = testMedia, args=(name,social,f,s))
				t.start()
			else:
				testMedia(name, social, f,s)
	if '-t' not in sys.argv:
		print '%s accounts found with the username: %s'%(c.g+str(num)+c.w, c.g+name+c.w)
def main():
	if len(sys.argv) == 1:
		print 'Usage:\n\tpython %s <username> <socials_wordlist> <-t(hread)> <-v(erbose)>\nExample:\n\tpython %s exampleexample123 socials.txt -v -t\n'%(sys.argv[0], sys.argv[0])
		sys.exit()
	uname = sys.argv[1]
	wlist = getList(sys.argv[2])
	parseW(uname, wlist)

if __name__ == '__main__':
	main()
