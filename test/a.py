from PIL import Image, ImageDraw, ImageFont

im = Image.open( "bk.png" )

ag = Image.open( "agree.png")
op = Image.open("oppose.png")
                               


f = open('14.ss','r')

AA = 'agree'
c = 0
r = []
for line in f:    
    c = c+1
    r.append(line)
   
if AA == 'agree' :
    i =int(r[0])
    i = i + 1
    r[0] = str(i)
if AA == 'oppose' :
    i =int(r[1])
    i = i + 1
    r[1] = str(i)


t1 = float(r[0])
t2 = float(r[1])
ar = 100*t1/(t2+t1)
opr = 100 - ar

print("ar:"+str(ar))
print("opr:"+str(opr))


n = open('14.ss','w+')
n.seek(0)
n.write(r[0])
n.write("\n")
n.write(r[1])

draw = ImageDraw.Draw( im )
largefont=ImageFont.truetype("rounded-mplus-2m-bold.ttf",28)

draw.text( (95,460),'有'+str(int(ar))+'%的人支持這項公投案',font=largefont,fill=(128,128,128))
draw.text( (475,550),'有'+str(100-int(ar))+'%的人反對這項公投案',font=largefont,fill=(128,128,128))

ag = ag.resize( (7*int(ar), 50), Image.BILINEAR )
op = op.resize( (7*int(opr),50), Image.BILINEAR )
im.paste(ag,(100,500))
im.paste(op,(100+7*int(ar),500))



im.save( "rate.png" )
CLIENT_ID = "f3738cfee1e7d48"
    PATH = "text.png"

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    print(uploaded_image.title)
    return uploaded_image.link