from PIL import Image,ImageDraw,ImageFont
import random,os,base64,StringIO
from django.template import Context, Template

def getCaptcha():
    buffer = StringIO.StringIO()
    image = Image.new('RGB', (68, 37), color=(255,182,193)) #INIT IMAGE
    draw = ImageDraw.Draw(image)
    random_captcha = random.randint(1000, 9999) #CREATE RANDOM NUMBER
    text = str(random_captcha)
    fnt = ImageFont.truetype('static/captcha/FreeMono.ttf', 20) #CALL FONT LIBRARY
    draw.text((11, 11), text,fill=(0,0,0),font=fnt) #DRAW TEXT ON IMAGE

    image.save(buffer, "PNG") #SAVE IMAGE IN TO BUFFER
    img_str = base64.b64encode(buffer.getvalue()) #ENCODE IMAGE IN TO BASE64
    template_code = """<img src="data:image/png;base64,{{ img_str }}">"""

    template = Template(template_code) #CONVERT IN TO TEMPLATE
    context= Context({'img_str': img_str}) #GET IMAGE WITH IMG TAG
    return text,template.render(context)
