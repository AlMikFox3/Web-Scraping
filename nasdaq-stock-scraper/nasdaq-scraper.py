import urllib
import re

symbolfile = open('symbols.txt')
symbolslist = (symbolfile.read()).split('\n')
f = open('nasdaq-data.txt', 'w')



i = 0
while (i<len(symbolslist)):
	f=open('nasdaq-data.txt','a')
	url = 'http://www.nasdaq.com/symbol/' + symbolslist[i]
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	x = str(symbolslist[i]) + str(price) +'\n'
	f.write(x)
	print "The Price of ", symbolslist[i] , " is ", price
	f.close()
	i = i+1