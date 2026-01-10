from PIL import Image, ImageFont, ImageDraw, ImageText
import random
import messages
import textwrap

font = ImageFont.truetype("default.ttf", 20)

# create image object
motd = Image.new("RGBA", (640, 480))

# add random background
randomBG = Image.open(random.choice(['bg/ran_bg01.jpg', 'bg/ran_bg02.jpg', 'bg/ran_bg03.jpg', 'bg/ran_bg04.jpg', 'bg/ran_bg05.jpg', 'bg/ran_bg06.jpg']))
motd.paste(randomBG)

# add random sprite
randomSprite = Image.open(random.choice(['sprites/ran_t01.png', 'sprites/ran_t02.png', 'sprites/ran_t03.png', 'sprites/ran_t04.png', 'sprites/ran_t05.png', 'sprites/ran_t06.png', 'sprites/ran_t07.png']))
motd = Image.alpha_composite(motd, randomSprite)

# draw the text
message = random.choice(messages.messages)
text = ImageText.Text(message, font)
text.embed_color()

d = ImageDraw.Draw(motd)
if "Today's" in message:
    d.text((102, 91), text, "#000000")
    d.text((101, 90), text, "#FFFFFF")
else:
    charcount = 40
    margin = offset = charcount
    for line in textwrap.wrap(message, width=charcount):
        d.text((102, (91-charcount)+offset), line, font=font, fill="#000000")
        d.text((101, (90-charcount)+offset), line, font=font, fill="#FFFFFF")
        # draw.text((margin, offset), line, font=font, fill="#aa0000")
        offset += font.getbbox(line)[3]

motd.save("test_image.png", format="PNG")

# post it to tumblr
