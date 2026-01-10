from PIL import Image, ImageFont, ImageDraw, ImageText
import random
import messages
import textwrap
import pytumblr

tags = ['t-m-daily']

font = ImageFont.truetype("default.ttf", 20)

# create image object
motd = Image.new("RGBA", (640, 480))

# add random background
randomBG = Image.open(random.choice(['bg/ran_bg01.jpg', 'bg/ran_bg02.jpg', 'bg/ran_bg03.jpg', 'bg/ran_bg04.jpg', 'bg/ran_bg05.jpg', 'bg/ran_bg06.jpg']))
motd.paste(randomBG)

# add random sprite
randomSprite = random.choice(['sprites/ran_t01.png', 'sprites/ran_t02.png', 'sprites/ran_t03.png', 'sprites/ran_t04.png', 'sprites/ran_t05.png', 'sprites/ran_t06.png', 'sprites/ran_t07.png'])
spriteImage = Image.open(randomSprite)
motd = Image.alpha_composite(motd, spriteImage)

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
client = pytumblr.TumblrRestClient(
    '89O643FKzhcfR0KwlyBo78YxgUSZ5qdafsSb1tyG0pG5PiyekP',
    '8fTHUhQu54lJ9bfmEyKrqFa5FnBInh2VdsjjwTL6CReNTIFWm2',
    'A69tVQanL9AnWbytomg97SUm2PZIfJxWAUCBSX5ZRlegLQnOgW',
    'dZAEWcEjCfca2jM5kswtauJISnzkQzwSXrUzHVl1UeTtFNIX99'
)

# add some tags
if "horoscope" in message:
    tags.append('horoscope')
if "lucky item" in message:
    tags.append('lucky item')

match randomSprite:
    case 'sprites/ran_t01.png':
        tags.append('Arcueid')
    case 'sprites/ran_t02.png':
        tags.append('Ciel')
    case 'sprites/ran_t03.png':
        tags.append('Akiha')
    case 'sprites/ran_t04.png':
        tags.append('Hisui')
    case 'sprites/ran_t05.png':
        tags.append('Kohaku')
    case 'sprites/ran_t06.png':
        tags.append('Satsuki')
    case 'sprites/ran_t07.png':
        tags.append('Len')


client.create_photo('type-moon-daily-message', state="published", tags=tags, data="generated.png")