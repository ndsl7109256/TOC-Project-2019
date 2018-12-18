import requests
import pyimgur
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

#from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1njdbmnp042pPbi5jqzCWzu2Ffr0wYOAtQKcJnSMvXwc'
SAMPLE_RANGE_NAME = '14!A1:E'


def candidate(url,toPrint):
    locate = 220
    w = 175
    im = Image.open( "bk.png" )

    draw = ImageDraw.Draw( im )
    largefont=ImageFont.truetype("setofont.ttf",26)
    smallfont=ImageFont.truetype("setofont.ttf",30)

    r = requests.get(url)

    html = r.text
    soup = BeautifulSoup(html,'html.parser')

    draw.text( (w+50,locate-100),toPrint,font=smallfont,fill = (128,128,128))#255,117,117


    draw.text( (w,locate-60),"No",font=largefont,fill = (128,128,128))#number
    draw.text( (w+50,locate-60),"姓名",font=largefont,fill = (128,128,128))#name
    draw.text( (w+150,locate-60),"性別",font=largefont,fill = (128,128,128))#gender
    draw.text( (w+240,locate-60),"得票數",font=largefont,fill = (128,128,128))#votes
    draw.text( (w+360,locate-60),"得票率",font=largefont,fill = (128,128,128))#percent
    draw.text( (w+500,locate-60),"政黨",font=largefont,fill = (128,128,128))#party

    trT = soup.find_all(class_='trT')
    for T in trT:
        td = T.find_all("td")
        draw.text( (w-50,locate),td[0].get_text(),font=largefont,fill = (128,128,128))#number
        draw.text( (w,locate),td[1].get_text(),font=largefont,fill = (128,128,128))#number
        draw.text( (w+40,locate),td[2].get_text(),font=largefont,fill = (128,128,128))#name
        draw.text( (w+160,locate),td[3].get_text(),font=largefont,fill = (128,128,128))#gender
        draw.text( (w+240,locate),td[4].get_text(),font=largefont,fill = (128,128,128))#votes
        draw.text( (w+360,locate),td[5].get_text(),font=largefont,fill = (128,128,128))#percent
        draw.text( (w+460,locate),td[6].get_text(),font=largefont,fill = (128,128,128))#party
        locate = locate + 40

    im.save( "text.png" )    


    CLIENT_ID = "f3738cfee1e7d48"
    PATH = "text.png"

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    print(uploaded_image.title)
    return uploaded_image.link


def opinionPoll(number,AOO,toPrint):
    im = Image.open( "bk.png" )

    ag = Image.open( "agree.png")
    op = Image.open("oppose.png")
                                
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    AA = AOO
    r = [] #int
    a = [] #str
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            r.append(int(row[0]))
            

    if AA == 'agree':
        r[0] = r[0] + 1
    if AA == 'oppose':
        r[1] = r[1] + 1    

    a.append(str(r[0]))
    a.append(str(r[1]))

    values = [
    [
        a[0]
    ],
    [
        a[1]
    ]
    # Additional rows ...
    ]
    body = {
    'values': values
    }
    result = service.spreadsheets().values().update(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
    valueInputOption='RAW', body=body).execute()

    t1 = float(r[0])
    t2 = float(r[1])
    ar = 100*t1/(t1+t2)
    opr = 100 -ar

    draw = ImageDraw.Draw( im )
    
    smallfont=ImageFont.truetype("rounded-mplus-2m-bold.ttf",28)
    largefont=ImageFont.truetype("rounded-mplus-2m-bold.ttf",46)

    draw.text( (30,300),toPrint,font=largefont,fill=(128,128,128))
    draw.text( (95,460),'有'+a[0]+'人支持這項公投案',font=smallfont,fill=(128,128,128))
    draw.text( (475,550),'有'+a[1]+'人反對這項公投案',font=smallfont,fill=(128,128,128))

    print(a[0])
    print(a[1])
    ag = ag.resize( (7*int(ar), 50), Image.BILINEAR )
    op = op.resize( (7*int(opr),50), Image.BILINEAR )
    im.paste(ag,(100,500))
    im.paste(op,(100+7*int(ar),500))



    im.save( "rate.png" )
    CLIENT_ID = "f3738cfee1e7d48"
    PATH = "rate.png"
    
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    print(uploaded_image.title)
    return uploaded_image.link



