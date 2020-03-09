import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

urlLink = 'https://www.amazon.com/FEICE-Stainless-Leathers-Waterproof-Business/dp/B074MWWTVL'
urlLink2 = 'https://www.amazon.com/ZOTAC-GeForce-128-Bit-Graphics-ZT-T16500F-10L/dp/B07QF1H9YR/ref=sxin_0_ac_d_rm?ac_md=0-0-Z3R4IDE2NTA%3D-ac_d_rm&crid=VIKK28PMLWYE&cv_ct_cx=gtx+1650&keywords=gtx+1650&pd_rd_i=B07QF1H9YR&pd_rd_r=2193b6dc-a98d-490a-a2b1-ed061779b818&pd_rd_w=1A0As&pd_rd_wg=apW3M&pf_rd_p=ec111f65-4a46-499c-be78-f47997212bd0&pf_rd_r=1ARPC3YJKGRHDDQ75R83&psc=1&qid=1583787604&sprefix=gtx%2Caps%2C864'
urlLink3 = 'https://www.amazon.com/s?k=gtx+1650&i=electronics&ref=nb_sb_noss'
urlLink4 = 'https://www.amazon.com/s?k=gtx+1650&i=electronics&rh=p_72%3A1248879011%2Cp_36%3A1253506011&dc&qid=1583787867&rnid=386442011&ref=sr_nr_p_36_4'

page = requests.get(urlLink4, headers=headers)
print(page)
