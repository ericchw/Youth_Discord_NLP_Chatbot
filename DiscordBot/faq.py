import requests
from bs4 import BeautifulSoup
def faq(text):
    if 'contact' in text: #if there is keyword with contacts
        response = requests.get("https://www.cyberyouth.sjs.org.hk")

        soup = BeautifulSoup(response.text,'html.parser')
        info = [p.text for p in soup.find_all('span')]
        # Tel = soup.body.find_all(string=re.compile('.*{0}.*'.format('Tel')), recursive=True)
        # Address = soup.body.find_all(string=re.compile('.*{0}.*'.format('Address')), recursive=True)
        # time = soup.body.find_all(string=re.compile('.*{0}.*'.format('服務時間')), recursive=True)
        # print(Tel)
        # print(time)
        # print(info)
        temp =[]
        

        # info = response.text
        for i in info:
            if '地址：' in i:
                temp.append(i)
            elif '電話' in i:
                temp.append(i)
            elif '傳真' in i:
                temp.append(i)
            elif '電郵' in i:
                temp.append(i)
            elif '5933' in i and len(i)<15:
                string = "Whatsapp: " + i
                temp.append(string)
        temp = "\n".join(temp)
        return temp
    elif 'activity' in text:
        response = requests.get("https://www.cyberyouth.sjs.org.hk")

        soup = BeautifulSoup(response.text,'html.parser')
        temp = []
        for p in soup.find_all('a',href=True):
            if 'drive.google.com' in p['href']:
                string = '最新活動可在此連結: '+ "\n" + p['href'] 
                temp.append(string)
        
        temp = "\n".join(temp)
        return temp
    else:
        return None
    