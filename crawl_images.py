import requests

from bs4 import BeautifulSoup

def Lay_Hinh_Anh():
    url = "https://vn.images.search.yahoo.com/search/images?p=đại+nội+huế"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # 
    t = str(soup)[str(soup).find("/images/view"):str(soup).find("/images/view")+1500]
    t = t[:t.find("crumb")+11]
    t = "https://vn.images.search.yahoo.com/" + t


    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    
    print(str(soup).find("http://"))
    imgs = soup.findAll(class_='process')
    poster_link = []
    for img in imgs:
        poster_link.append(img.get('data-src'))

    return poster_link


Lay_Hinh_Anh()