import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0').read()
soup = bs.BeautifulSoup(source,'lxml')

## Our most popular products based on sales. Updated hourly 
## best sellers
#pageUrl =https://www.amazon.ca/Best-Sellers-generic/zgbs/?ref_=nav_cs_bestsellers
#
## best sellers in beauty and personal care
# beautyhtml= lxml.html.parse("https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0")

##best sellers in skin care under beauty and personal care
## beautySkinCarehtml= lxml.html.parse("https://www.amazon.ca/Best-Sellers-Beauty-Skin-Care-Products/zgbs/beauty/6344740011/ref=zg_bs_nav_beauty_1_beauty")

## best sellers in facial skin care
# facialSkinCarehtml= lxml.html.parse("https://www.amazon.ca/Best-Sellers-Beauty-Facial-Skin-Care-Products/zgbs/beauty/6344751011/ref=zg_bs_nav_beauty_2_6344740011")

# best sellers in eye treatment 
# eyeTreatmentHtml= lxml.html.parse("https://www.amazon.ca/Best-Sellers-Beauty-Eye-Treatment-Products/zgbs/beauty/6344747011/ref=zg_bs_nav_beauty_2_6344740011")

# body care
# bodyCarehtml= lxml.html.parse("https://www.amazon.ca/Best-Sellers-Beauty-Body-Skin-Care-Products/zgbs/beauty/6344741011/ref=zg_bs_nav_beauty_3_6344789011")

# hands feet and nails
# handsFeetNailshtml= lxml.html.parse("https://www.amazon.ca/Best-Sellers-Beauty-Hand-Feet-Nail-Care-Products/zgbs/beauty/6344773011/ref=zg_bs_nav_beauty_2_6344740011")

# lip care
#- lipCarehtml= lxml.html.parse("https://www.amazon.ca/Best-Sellers-Beauty-Lip-Care-Products/zgbs/beauty/6371149011/ref=zg_bs_nav_beauty_2_6344740011") 

# skin care sets
# setshtml= lxml.html.parse("https://www.amazon.ca/Best-Sellers-Beauty-Skin-Care-Sets/zgbs/beauty/6344789011/ref=zg_bs_nav_beauty_2_6344740011")

#am_pageUrl = 'https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0'





# title of the page
print(soup.title)
#
## get attributes:
#print(soup.title.name)
#
## get values:
print(soup.title.string)
#
## beginning navigation:
#print(soup.title.parent.name)

# getting specific values:
#print(soup.p)
#
#print(soup.find_all('p'))
#
#for paragraph in soup.find_all('p'):
#    print(paragraph.string)
#    print(str(paragraph.text))
# #li class zg-item-immersion 
#for li in soup.find_all('li'):
#    print(li.string)
#    
#    print(soup.get_text())
f = open("beautyAmazonSoupTest.txt","w") #open file with name test.txt
f.write(soup.title.string)
for li in soup.find_all('li', class_='zg-item-immersion'):
    print(li.text)
    f.write(li.text)
f.close()