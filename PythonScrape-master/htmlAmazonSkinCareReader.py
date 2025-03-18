import bs4 as bs
import urllib.request

## Our most popular products based on sales. Updated hourly 
## best sellers
#best sellers in beauty 
beautyhtml= urllib.request.urlopen('https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0')
beautySoup = bs.BeautifulSoup(beautyhtml,'lxml')
##best sellers in skin care under beauty and personal care
beautySkinCarehtml= urllib.request.urlopen("https://www.amazon.ca/Best-Sellers-Beauty-Skin-Care-Products/zgbs/beauty/6344740011/ref=zg_bs_nav_beauty_1_beauty")
skinCareSoup = bs.BeautifulSoup(beautySkinCarehtml,'lxml')
## best sellers in facial skin care
facialSkinCarehtml= urllib.request.urlopen("https://www.amazon.ca/Best-Sellers-Beauty-Facial-Skin-Care-Products/zgbs/beauty/6344751011/ref=zg_bs_nav_beauty_2_6344740011")
facialSkinCareSoup = bs.BeautifulSoup(facialSkinCarehtml,'lxml')
# best sellers in eye treatment 
eyeTreatmentHtml= urllib.request.urlopen("https://www.amazon.ca/Best-Sellers-Beauty-Eye-Treatment-Products/zgbs/beauty/6344747011/ref=zg_bs_nav_beauty_2_6344740011")
eyeTreatmentHtmlSoup = bs.BeautifulSoup(eyeTreatmentHtml,'lxml')
# body care
bodyCarehtml= urllib.request.urlopen("https://www.amazon.ca/Best-Sellers-Beauty-Body-Skin-Care-Products/zgbs/beauty/6344741011/ref=zg_bs_nav_beauty_3_6344789011")
bodyCareSoup = bs.BeautifulSoup(bodyCarehtml,'lxml')
# hands feet and nails
handsFeetNailshtml= urllib.request.urlopen("https://www.amazon.ca/Best-Sellers-Beauty-Hand-Feet-Nail-Care-Products/zgbs/beauty/6344773011/ref=zg_bs_nav_beauty_2_6344740011")
handsFeetNailsSoup = bs.BeautifulSoup(handsFeetNailshtml,'lxml')
# lip care
lipCarehtml= urllib.request.urlopen("https://www.amazon.ca/Best-Sellers-Beauty-Lip-Care-Products/zgbs/beauty/6371149011/ref=zg_bs_nav_beauty_2_6344740011") 
lipCareSoup = bs.BeautifulSoup(lipCarehtml,'lxml')
# skin care sets
SkinCareSetshtml= urllib.request.urlopen("https://www.amazon.ca/Best-Sellers-Beauty-Skin-Care-Sets/zgbs/beauty/6344789011/ref=zg_bs_nav_beauty_2_6344740011")
SkinCareSetsSoup = bs.BeautifulSoup(SkinCareSetshtml,'lxml')


# title of the page
print(skinCareSoup.title)
#
## get attributes:
#print(soup.title.name)
#
## get values:
print(skinCareSoup.title.string)
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
f=open("beautyAmazon.txt","w")
f.write(beautySoup.title.string)
for li in beautySoup.find_all('li', class_='zg-item-immersion'):
    print(li.text)
    f.write(li.text)
f.close()

f = open("beautySkinCareAmazon.txt","w") #open file with name test.txt
f.write(skinCareSoup.title.string)
for li in skinCareSoup.find_all('li', class_='zg-item-immersion'):
    print(li.text)
    f.write(li.text)
f.close()

f = open("facialSkinCareAmazon.txt","w") #open file with name test.txt
f.write(facialSkinCareSoup.title.string)
for lifs in facialSkinCareSoup.find_all('li', class_='zg-item-immersion'):
    print(lifs.text)
    f.write(lifs.text)
f.close()

f = open("eyeTreatmentCareAmazon.txt","w") #open file with name test.txt
f.write(eyeTreatmentHtmlSoup.title.string)
for liet in eyeTreatmentHtmlSoup.find_all('li', class_='zg-item-immersion'):
    print(lifs.text)
    f.write(lifs.text)
f.close()

f = open("bodyCareAmazon.txt","w") #open file with name test.txt
f.write(bodyCareSoup.title.string)
for lifs in bodyCareSoup.find_all('li', class_='zg-item-immersion'):
    print(lifs.text)
    f.write(lifs.text)
f.close()

f = open("HandsFeetCareAmazon.txt","w") #open file with name test.txt
f.write(handsFeetNailsSoup.title.string)
for lifs in handsFeetNailsSoup.find_all('li', class_='zg-item-immersion'):
    print(lifs.text)
    f.write(lifs.text)
f.close()

f = open("LipCareAmazon.txt","w") #open file with name test.txt
f.write(lipCareSoup.title.string)
for lifs in lipCareSoup.find_all('li', class_='zg-item-immersion'):
    print(lifs.text)
    f.write(lifs.text)
f.close()

f = open("SkinCareSetsAmazon.txt","w") #open file with name test.txt
f.write(SkinCareSetsSoup.title.string)
for lifs in SkinCareSetsSoup.find_all('li', class_='zg-item-immersion'):
    print(lifs.text)
    f.write(lifs.text)
f.close()