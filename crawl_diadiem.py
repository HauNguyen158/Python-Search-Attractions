from re import findall
import requests
import scrapy
from bs4 import BeautifulSoup

kieu = "None"
tinh = "None"

def set_Tinh(text):
    global tinh
    tinh = text

def get_Tinh():
    return tinh

def set_Kieu(text):
    global kieu
    kieu = text

def get_Kieu():
    return kieu

def Lay_DS_Bien(text):
    text = text.lower()
    url = "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_b%C3%A3i_bi%E1%BB%83n_%E1%BB%9F_Vi%E1%BB%87t_Nam"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll("li") 
   
    for title in titles:
        if title.text.lower().find(text) != -1:
            dsbaibien = str(title.text).split("\n")
            break
    return dsbaibien[1:]

def Lay_DS_Chua(text):
    text = text.lower()
    if text == "thừa thiên huế":
        text = text[11:]
    url = "https://vi.wikipedia.org/wiki/Ch%C3%B9a_Vi%E1%BB%87t_Nam"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll("li") 
    dschua = []
    for title in titles:
        if title.text.lower().find(text) != -1:
            divs = title.findAll("a")
            for div in divs:
                dschua.append(div.text)
            break
    return dschua[1:]


def lay_Tinh():
    url = "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_Di_t%C3%ADch_qu%E1%BB%91c_gia_Vi%E1%BB%87t_Nam"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll(class_="mw-headline")
    
    list = []
    i = -1
    # 28 0 17 35 44 50 57
    for title in titles:
        i = i + 1
        if i == 0 or i == 17 or i == 28 or i == 35 or i == 44 or i == 50 or i == 57:
            continue
        list.append(str(title.text).lower())
    return list

def Lay_Di_Tich(text):
    text = text.lower()
    url = "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_Di_t%C3%ADch_qu%E1%BB%91c_gia_Vi%E1%BB%87t_Nam"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll(class_="mw-headline")
    
    list = []
    i = -1
    # 28 0 17 35 44 50 57
    for title in titles:
        i = i + 1
        if i == 0 or i == 17 or i == 28 or i == 35 or i == 44 or i == 50 or i == 57:
            continue
        list.append(title.text)
    
    index = -1
    for i in range(len(list)):
        if str(list[i]).lower().find(text) != -1:

            index = i
            break

    bodys = soup.findAll("table")
    
    trs = bodys[index-1].findAll("tr")
    dsditich = []

    for tr in trs:
        td = tr.findAll("td")
        try:
            dsditich.append(td[0].text)
        except:
            continue
    return dsditich


Lay_Di_Tich("bình định")

def Lay_Anh_GG():
    url = "https://www.bing.com/images/search?q=%c4%91%e1%ba%a1i+n%e1%bb%99i+hu%e1%ba%bf&form=QBIR&first=1&tsc=ImageHoverTitle"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    v= str(soup)
    print(v.find("https://th.bing.com"))

def Lay_Thong_Tin(url):
    url = "https://vi.wikipedia.org/w/index.php?search=" + url
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find(class_='mw-search-result-heading')
    try:
        link = titles.find('a').attrs["href"]
        link = "https://vi.wikipedia.org/" + link
    except:
        link = url

    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll('p')
    poster_link = []
    for title in titles:
        text = str(title.text).strip('\n')
        poster_link.append(text.replace('"',''))

    return poster_link
  


def Lay_Hinh_Anh(url):
    url = "https://vn.images.search.yahoo.com/search/images?p=" + url
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # 
    t = str(soup)[str(soup).find("/images/view"):str(soup).find("/images/view")+1500]
    t = t[:t.find("crumb")+11]
    t = "https://vn.images.search.yahoo.com/" + t

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    imgs = soup.findAll(class_='process')
    poster_link = []
    for img in imgs:
        poster_link.append(img.get('data-src'))

    return poster_link

def Ten_Bai_Bien(arr):
    list_bien = []

    for i in range(len(arr[0])):
        temp = str(arr[0][i]).strip()
        temp = temp[4:len(temp)-5]
        temp = temp[temp.find('>')+1:]
        temp = temp[:temp.find('<')]
        list_bien.append(temp)
    list_bien = ''.join(str(x)+"\n" for x in list_bien)
    return list_bien
    
def Hinh_Anh():
    url = "https://www.google.com/maps/place/Bãi+Biển+Hải+Dương"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll(class_='gallery-image-low-res')
    print(soup)

# cào dữ liệu
def crawlData_Bien():
    url = "https://wolverineair.com/bien-o-hue/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # lấy dữ liệu trong class tour
    titles = soup.findAll(class_='the-post')
  
    links = [link.findAll('h2') for link in titles]

    return Ten_Bai_Bien(links)

def Dia_Diem(text):
    url = "https://tutrithuc.com/post/search?w=Nh%E1%BB%AFng+%C4%91%E1%BB%8Ba+%C4%91i%E1%BB%83m+du+l%E1%BB%8Bch+n%E1%BB%95i+ti%E1%BA%BFng+%E1%BB%9F+" + text
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find(class_='post_content_item')
    link = titles.find('a').attrs["href"]
    link = "https://tutrithuc.com/" + link
    
    response = requests.get(link)

    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find(class_='post_detailcontent_content')
    print(titles)

