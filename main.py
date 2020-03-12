import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

# This works, with or without the query after ?. I also had to select the item after searching
urlLink = 'https://www.amazon.com/ZOTAC-GeForce-128-Bit-Graphics-ZT-T16500F-10L/dp/B07QF1H9YR/ref=sr_1_1'
urlLink0 = 'https://www.amazon.com/ZOTAC-GeForce-128-Bit-Graphics-ZT-T16500F-10L/dp/B07QF1H9YR/ref=sr_1_1?dchild=1&keywords=gtx+1650&qid=1584041832&sr=8-1'

# urlLink1 = 'https://pythonprogramming.net/parsememcparseface/'
# urlLink2 = 'https://www.amazon.com/ZOTAC-GeForce-128-Bit-Graphics-ZT-T16500F-10L/dp/B07QF1H9YR/ref=sxin_0_ac_d_rm?ac_md=0-0-Z3R4IDE2NTA%3D-ac_d_rm&crid=VIKK28PMLWYE&cv_ct_cx=gtx+1650&keywords=gtx+1650&pd_rd_i=B07QF1H9YR&pd_rd_r=2193b6dc-a98d-490a-a2b1-ed061779b818&pd_rd_w=1A0As&pd_rd_wg=apW3M&pf_rd_p=ec111f65-4a46-499c-be78-f47997212bd0&pf_rd_r=1ARPC3YJKGRHDDQ75R83&psc=1&qid=1583787604&sprefix=gtx%2Caps%2C864'
# urlLink3 = 'https://www.amazon.com/s?k=gtx+1650&i=electronics&ref=nb_sb_noss'
# urlLink4 = 'https://www.amazon.com/ZOTAC-GeForce-128-Bit-Graphics-ZT-T16500F-10L/dp/B07QF1H9YR/ref=sr_1_1?dchild=1&keywords=gtx+1650&qid=1584041832&sr=8-1'

page = requests.get(urlLink0, headers=headers)
print(page) # Get the response code

# soup = BeautifulSoup(page.content, features='lxml') # Returns an Array
soup = BeautifulSoup(page.content, 'html.parser') # Still works
# print(soup.prettify())

# product_title = soup.select('#productTitle')[0].get_text().strip()
# print(product_title)
title = soup.find(id="productTitle").get_text()
print(title)


# f = open('results.html','w')
# for i in results:
# 	f.write(str(i))
# f.close()