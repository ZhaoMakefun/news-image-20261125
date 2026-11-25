"""Draw the news image for 25 November 2026 (build-time tool only).

Not part of the entry program: main.py is the entrypoint and only copies
entry.png to /output/entry.png. This script is how the image itself was
made, with Pillow, so the text stays crisp and legible.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (250, 247, 240)
INK = (24, 28, 36)
NAVY = (18, 38, 66)
RED = (178, 34, 34)
TEAL = (14, 116, 110)
GOLD = (180, 130, 20)
GREY = (90, 96, 106)
CARD = (255, 255, 255)
LINE = (210, 206, 198)

def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

F_TITLE = font("DejaVuSans-Bold.ttf", 64)
F_DATE = font("DejaVuSans-Bold.ttf", 30)
F_TAG = font("DejaVuSans-Bold.ttf", 20)
F_HEAD = font("DejaVuSans-Bold.ttf", 29)
F_BODY = font("DejaVuSans.ttf", 21)
F_FOOT = font("DejaVuSans.ttf", 19)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Header
d.rectangle([0, 0, W, 168], fill=NAVY)
d.text((36, 26), "WORLD NEWS", font=F_TITLE, fill=(255, 255, 255))
d.text((36, 106), "WEDNESDAY  25  NOVEMBER  2026", font=F_DATE, fill=(255, 214, 90))
d.text((36, 138), "Six stories that defined the day", font=F_FOOT, fill=(200, 210, 225))

panels = [
    ("MARKETS", RED, "AI rally fades:\nNvidia falls 7%",
     "Nikkei down 2.8% as investors doubt\nthe AI boom; S&P 500 slips 0.5%."),
    ("STRAIT OF HORMUZ", TEAL, "Tankers hit by mines\nin the Strait of Hormuz",
     "Iran says two tankers were struck;\noil and shipping on alert."),
    ("RIYADH", RED, "Riyadh tower hit again\nin Houthi attack",
     "Saudi capital's tallest skyscraper\nstruck; 11 people hurt."),
    ("GAZA", NAVY, "Israeli strike kills\nHamas security chief",
     "Strike on Gaza City also kills\nhis wife and teenage daughters."),
    ("COLOMBIA", TEAL, "Supermarket hostages\nfreed in Cartagena",
     "Police free about 20 hostages after\na failed armoured-car raid."),
    ("SPACE & SPORT", GOLD, "Pakistan's first astronaut\nreaches China's station",
     "Senegal regain the Africa Cup\nof Nations title."),
]

# 2 columns x 3 rows of cards
x0, y0 = 28, 192
cw, ch, gap = 472, 240, 16
for i, (tag, color, head, body) in enumerate(panels):
    x = x0 + (i % 2) * (cw + gap)
    y = y0 + (i // 2) * (ch + gap)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=14, fill=CARD, outline=LINE, width=2)
    d.rectangle([x, y, x + cw, y + 6], fill=color)
    d.text((x + 20, y + 22), tag, font=F_TAG, fill=color)
    d.text((x + 20, y + 52), head, font=F_HEAD, fill=INK)
    d.text((x + 20, y + 152), body, font=F_BODY, fill=GREY)

# Footer
d.line([28, 958, W - 28, 958], fill=LINE, width=2)
d.text((28, 970), "Reported 25 November 2026  ·  One image, six stories, four continents",
       font=F_FOOT, fill=GREY)

img.save("/home/hatch/workspace/makefun-bounty/news-image-20261125/entry.png", optimize=True)
print("saved, bytes:", len(open("/home/hatch/workspace/makefun-bounty/news-image-20261125/entry.png", "rb").read()))
