from lxml import html
import requests


#from urllib2 import urlopen
#tutorial http://docs.python-guide.org/en/latest/scenarios/scrape/
base_url = 'https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0'

##-----TODO ---- write a loop that loops through each page on directory
## to capture all companies in listing
#count=1
#while (count<5):
## page to scrape
   #urlstring =base_url
   
page = requests.get(base_url)
am_tree = html.fromstring(page.content)
#print (page.content)
am_listItem = am_tree.xpath('//li[@class="zg-item-immersion"]/span[@class="a-list-item"]')
print (am_listItem)
   #get data looking for
#   header = tree.xpath('//header/h1[@class="linked-heading"]/a/text()')# name of company
#   link2 = tree.xpath('//section/a[@class="read-more-link"]/@href')# individual page for website link
#   print (link)
f= open("AmazonBeautyBestSellers.txt","w")#open and write to file
for line in am_listItem:
    print (line)
    f.write(line +"\n")
f.close()
#           
## listing each subcategory's individual website from captured link
#   for link in link2:
#         pageUrl = 'http://www.techvibes.com'
#         page2str =    pageUrl+link
#         #print page2str
#         page2=requests.get(page2str)
#         tree2 = html.fromstring(page2.content)
#         websites=tree2.xpath('//section[@id="content-about"]/dl[@class="dl-horizontal"]/dd/a/text()')
#         f=open("ITConsultantsWebsites.txt","a")
#         for site in websites:
#             print (site)
#             f.write(site+"\n")
#         f.close()   

#count = count+1

