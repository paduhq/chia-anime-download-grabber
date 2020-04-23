import re
import requests
from translate import *


def hashgrabber(url):
	s=requests.get(url)
	pipesthings=re.findall('\|[a-zA-Z0-9=]{32,}\|',s.text)
	sortedpipesthings=sorted(pipesthings, key=len, reverse=True)
	hash=sortedpipesthings[0][1:-1]
	return(hash)


url=input("Enter chia-anime url of anime\nEg: http://www.chia-anime.me/episode/blade/\nEg: https://m.chia-anime.me/show/blade/\n:")

start=int(input("Enter starting episode no:"))
end=int(input("Enter ending episode no:"))
asktosaveinfile=input("Do you want to save links in a file?\nEnter Y or N:")
if asktosaveinfile == 'Y' or 'y':
	filename=input("Enter filename:")

if 'www.' in url:
	animenamere=re.findall('episode\/(.*)',url)
	animename=animenamere[0]
	if animename[-1] == '/':
		animename=animename.replace('/','')
elif 'm.' in url:
	animenamere=re.findall('show\/(.*)',url)
	animename=animenamere[0]
	if animename[-1] == '/':
		animename=animename.replace('/','')


eplist=[]
def linkgrabber(animename,start,end):
	for i in range(start,(end+1)):
		episodeurl='https://m.chia-anime.me/view/'+animename+'-episode-'+str(i)
		hash=hashgrabber(episodeurl)
		a=str(PyJsHoisted_link_(hash))
		cute=a.replace("'","")
		cuter=re.findall("^(.*)mp4",cute)
		link=cuter[0]+'mp4?download=yes&title='+animename+str(i)+'.mp4'
		print(link)
		eplist.append(link)
	
linkgrabber(animename,start,end)

if asktosaveinfile == 'Y' or 'y':
	eps='\n'.join(eplist)
	f=open(filename,'w+')
	f.write(eps)
	f.close()



		



