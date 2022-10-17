from PIL import Image, ImageDraw, ImageFont, ImageColor
import config

def make_image(dic):
    img_size = config.img_size
    tag_size = config.tag_size
    tag_start = config.tag_start
    contents_size = config.contents_size
    contents_start = config.contents_start
    loc_tag = [0, 0]
    loc_contents = [0, 0]

    img = Image.new(mode = 'RGB', size = img_size, color='#FFF')
    draw = ImageDraw.Draw(img)

    font_tag = ImageFont.truetype('./NanumGothic.ttf', tag_size)
    loc_tag[0] = tag_start[0]
    loc_tag[1] = tag_start[1]
    for tag in dic.keys():
        draw.text(loc_tag, tag, font=font_tag, fill='#000')
        img.save('./images/sample.png', format='PNG')
        loc_tag[0] += tag_size*3

    loc_tag[0] = tag_start[0]
    loc_tag[1] = tag_start[1]
    font_contents = ImageFont.truetype('./NanumGothic.ttf', contents_size)
    for i, tag in enumerate(dic.keys()):
        img_tmp = Image.open('./images/sample.png', mode='r')
        draw = ImageDraw.Draw(img_tmp)
        draw.text(loc_tag, tag, font=font_tag, fill=ImageColor.getrgb("red"))
        loc_tag[0] += tag_size*3
        loc_contents[0] = contents_start[0]
        loc_contents[1] = contents_start[1] + contents_size
        for con in dic[tag]:
            draw.text(loc_contents, con, font=font_contents, fill='#000')
            loc_contents[1] += contents_size*2
        img_tmp.save('./images/%ds.png' % i, format='PNG')    










