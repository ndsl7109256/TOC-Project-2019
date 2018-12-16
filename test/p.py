import requests
import pyimgur
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

locate = 220
w = 175
im = Image.open( "bk.png" )

draw = ImageDraw.Draw( im )
largefont=ImageFont.truetype("setofont.ttf",26)


r = requests.get('http://vote.2018.nat.gov.tw/pc/zh_TW/T1/s63000030000000000.html')

html = r.text
soup = BeautifulSoup(html,'html.parser')



draw.text( (w,locate-60),"No",font=largefont,fill = (255,117,117))#number
draw.text( (w+50,locate-60),"姓名",font=largefont,fill = (255,117,117))#name
draw.text( (w+150,locate-60),"性別",font=largefont,fill = (255,117,117))#gender
draw.text( (w+240,locate-60),"得票數",font=largefont,fill = (255,117,117))#votes
draw.text( (w+360,locate-60),"得票率",font=largefont,fill = (255,117,117))#percent
draw.text( (w+500,locate-60),"政黨",font=largefont,fill = (255,117,117))#party

trT = soup.find_all(class_='trT')
for T in trT:
    td = T.find_all("td")
    draw.text( (w-50,locate),td[0].get_text(),font=largefont,fill = (255,117,117))#number
    draw.text( (w,locate),td[1].get_text(),font=largefont,fill = (255,117,117))#number
    draw.text( (w+40,locate),td[2].get_text(),font=largefont,fill = (255,117,117))#name
    draw.text( (w+160,locate),td[3].get_text(),font=largefont,fill = (255,117,117))#gender
    draw.text( (w+240,locate),td[4].get_text(),font=largefont,fill = (255,117,117))#votes
    draw.text( (w+360,locate),td[5].get_text(),font=largefont,fill = (255,117,117))#percent
    draw.text( (w+460,locate),td[6].get_text(),font=largefont,fill = (255,117,117))#party
    locate = locate + 40

im.save( "text.png" )    


# CLIENT_ID = "f3738cfee1e7d48"
# PATH = "text.png"

# im = pyimgur.Imgur(CLIENT_ID)
# uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
# print(uploaded_image.title)
# print(uploaded_image.link)
# print(uploaded_image.size)
# print(uploaded_image.type)