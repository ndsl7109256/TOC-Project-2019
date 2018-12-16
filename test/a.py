from PIL import Image, ImageDraw, ImageFont

im = Image.open( "bk.png" )

ag = Image.open( "agree.png")
op = Image.open("oppose.png")
                               


f = open('14.ss','r')

AA = 'oppose'
toW=''
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


toW=r[0]+r[1]

t1 = float(r[0])
t2 = float(r[1])
ar = 100*t1/(t2+t1)
opr = 100 - ar

print("ar:"+str(ar))
print("opr:"+str(opr))

print(toW)

n = open('14.ss','w+')
n.seek(0)
n.write(toW)

ag = ag.resize( (5*int(ar), 50), Image.BILINEAR )
op = op.resize( (5*int(opr),50), Image.BILINEAR )
im.paste(ag,(100,500))
im.paste(op,(100+5*int(ar),500))

im.save( "rate.png" )
