from PIL import Image, ImageDraw, ImageFont

im = Image.open( "aqours.png" )



draw = ImageDraw.Draw( im )
largefont=ImageFont.truetype("rounded-mplus-2m-bold.ttf",48)
draw.text( (40,200), "TEdddddddddddddddddddddddddXT",fill = (255,117,117))
draw.text( (100,150),"Hello, the ddddddddddworld",font=largefont)

im.save( "text.png" )
