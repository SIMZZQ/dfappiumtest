from PIL import Image
import os,pytesseract

cp = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','codepic'))
try:
    os.makedirs(cp)
except:
    pass
codeimage = Image.open(cp+'/code.png')
image = codeimage.convert('L')
image.save(cp + '/code1.png')
table = []
for i in range(256):
    if i < 223:
        table.append(0)
    else:
        table.append(1)
# print(table)
image1 = image.point(table, '1')
image1.save(cp+'/code2.png')
# erzhiimage = Image.open(cp+'/code2.png')
# image1.show()
imagesize = image1.size
imagew = imagesize[0]
imageh = imagesize[1]
try:
    for x in range(1,imagew):
        for y in range(1,imageh):
            # xx.getpixel((x,y))获取目标像素点颜色。
            # xx.putpixel((x,y),255)更改像素点颜色，255代表颜色。
            if x<=2 or x>=(imagew-2):
                image1.putpixel((x,y),255) #x=1，2，大于等于宽-2的列设置白色
            elif y<=2 or y>=(imageh-2):
                image1.putpixel((x,y),255) #y=1,2,大于等于高-2的行设置白色
            elif image1.getpixel((x,y)) == 0:
                # 以目标像素点为起始点，获取下方4个点的颜色
                # 0为黑色，1为白色
                down_color = image1.getpixel((x,y+1))
                # print(down_color)
                down2_color = image1.getpixel((x,y+2))
                down3_color = image1.getpixel((x,y+3))
                down4_color = image1.getpixel((x,y+4))
                if down_color == 1:
                    image1.putpixel((x,y),255)
                elif down2_color == 1:
                    image1.putpixel((x,y),255)
                elif down3_color == 1:
                    image1.putpixel((x,y),255)
                elif down4_color == 1:
                    image1.putpixel((x,y),255)
                else:
                    pass
            else:
                pass
    image1.save(cp+'/code3.png')
except:
    raise
# image1.show()
rep = {'O':'0',
       'I':'1',
       'L':'1',
       'Z':'2',
       'S':'8',
       'Q':'0',
       '}':'7',
       '*':'',
       'E':'6',
       ']':'0',
       '`':'',
       'B':'8',
       '\\':'',
       ' ':'',
       '\'':''
       }

res = pytesseract.image_to_string(image1,lang='eng')
res.strip()
res.upper()
for r in rep:
    res = res.replace(r,rep[r])
print(res)