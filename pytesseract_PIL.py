import pytesseract as pt
from PIL import Image

#生成图片实例
image=Image.open('识别.jpg')

#调用pytesseract，将图片识别为文字
#返回结果就是转化后的结果
text=pt.Image_to_string(image)

print(text)