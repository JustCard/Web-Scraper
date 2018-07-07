import bs4 as bs
import urllib
from urllib.request import Request


#Site to be Scraped
url = "url"   

#A list of User Agents
uagents = ["Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
                  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0)", "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"]
    
#IURL Opener
page = urllib.request.urlopen(Request(url, headers={'User-Agent': random.choice(uagents)}))
html = page.read()

#Instantiate a BeautifulSoup Object
soup = bs.BeautifulSoup(html, 'lxml')
