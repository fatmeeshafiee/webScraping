import re
import requests
import bs4
from urllib.parse import urljoin

url = "https://webscraper.io/test-sites/e-commerce/allinone"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
data=response.text
if response.status_code == 200:
    newData=bs4.BeautifulSoup(data, 'html.parser')
    title=newData.find("title").text

    caption=newData.find_all(attrs={'class':'title'})
    allImg=newData.find_all(attrs={'class':'img-fluid'})

    mylist=[]
    print(title)
    for i in caption:
        mylist.append(i.text)
    mylist_clean = [re.sub('[\n\t]', ' ', i).strip() for i in mylist]
    print(mylist_clean)

    for num,i in enumerate(allImg,1):
        urlImg=i.get('src')
        full_img_url = urljoin(url,urlImg)
        print(f"url of images {num}= {full_img_url}")

else:
    print("error in loading page")


# meta=newData.find("meta",attrs={'name':'keywords'})
#
# script=newData.find_all("script",src=True)
#
# meta2=newData.find_all('meta',content=True)


# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     if soup.title:
#         title = soup.find('title').text
#     else:
#         title = 'NOT found Title'
#     print("Title of page:", title)
#
#     product_titles = soup.select("a.title")
#     print("\nProducts Title:")
#     for i, product in enumerate(product_titles, 1):
#         print(f"{i}. {product.get_text(strip=True)}")
#
#     images = soup.select("img.img-responsive")
#     print("\nImage links:")
#     for i, img in enumerate(images, 1):
#         img_url = img.get('src')
#         if img_url:
#             full_img_url = urljoin(url, img_url)
#             print(f"{i}. {full_img_url}")
#
# else:
#     print("Error in loading:", response.status_code)
