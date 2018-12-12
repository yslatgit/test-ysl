class A:
    pass

"""***************************************************************常用第三方模块***************************************************************"""
"""pillow"""
from PIL import Image

def func_1():
    """缩放操作"""
    im = Image.open('head.jpg')
    w,h = im.size
    print("Original Size :::width:%s---height:%s"%(w,h))
    print(type(w))
    im.thumbnail((w//2,h//2))
    print("Resize Size %s%s."%(w//2,h//2))
    im.save('thumbnail.jpg','jpeg')
from PIL import ImageFilter

def func_2():
    """模糊图片"""
    im = Image.open('thumbnail.jpg')
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('thumbnail_blur.jpg','jpeg')

from PIL import ImageDraw,ImageFont
import random

def rndChar():
    """随机字母"""
    # print(chr(random.randint(65,90)))
    return chr(random.randint(65,90))
def rndColor1():
    """随机颜色1"""
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndColor2():
    """随机颜色2"""
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
def xuanzhuan(obj):
    """旋转文字"""
    obj.rotate((random.randint(0,90)))
def func_3():
    """自定义图片验证码"""
    width = 60 * 4
    height = 60
    image = Image.new('RGB',(width,height),(255,255,255))
    #创建Font对象
    font = ImageFont.truetype('arial.ttf',36)
    #创建Draw对象
    draw = ImageDraw.Draw(image)
    #填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColor1())
    #输出文字
    for t in range(4):
        draw.text((60 * t + 15,10),rndChar(),font=font,fill=rndColor2())
    image.rotate((random.randint(0,90)))

    image.save('code1.jpg','jpeg')
def func_4():
    """自定义图片验证码（旋转）"""
    width = 60 * 4
    height = 60
    image = Image.new('RGB',(width,height),(255,255,255))
    char = Image.new('RGB',(30,60),(255,255,255))#只有此对象的实例可以旋转
    drawChar = ImageDraw.Draw(char)
    font = ImageFont.truetype('arial.ttf', 36)
    drawChar.text((10,10), rndChar(), font=font, fill=rndColor2())
    char = char.rotate(45)
    #只旋转文字的方法------>不然会有背景跟着旋转
    r,g,b = char.split()
    image.paste(char,(15,15),r)
    image.paste(char,(15,15),g)
    image.paste(char,(15,15),b)

    image.save('code2.jpg','jpeg')

"""request"""
pass

"""chardet"""
import chardet

"""psutil"""
import psutil
def func_5():
    #cpu数量
    # print(psutil.cpu_count())
    # #真实cpu核数
    # print(psutil.cpu_count(logical=False))
    # #硬盘分区情况
    # print(psutil.disk_partitions())
    # #硬盘存储情况
    # print(psutil.disk_usage('/'))
    # for i in psutil.pids():
    #     if i == 668:
    #         print("ysl")
    # psutil.pids().remove(668)
    p = psutil.Process(13276)
    p.terminate()



if __name__ == '__main__':
    func_5()
