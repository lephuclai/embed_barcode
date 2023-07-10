from barcode import EAN8
from barcode.writer import ImageWriter
import PIL
from PIL import Image

for i in range(4800):
    number = str(i)
    if len(number) < 7:
        add = 7 - len(number)
        for j in range(add):
            number = '0' + number
    my_code = EAN8(number, writer=ImageWriter())
    my_code.save("Code/new_code" + str(i), {"module_width":0.35, "module_height":10})
    
    to_be_resized = Image.open('Code/new_code' + str(i) + '.png') # open in a PIL Image object

    newSize = (200, 90) # new size will be 500 by 300 pixels, for example
    resized = to_be_resized.resize(newSize, resample=PIL.Image.NEAREST) # you can choose other :resample: values to get different quality/speed results

    resized.save('Code/new_code' + str(i) + '.png') # save the resized image
    
     