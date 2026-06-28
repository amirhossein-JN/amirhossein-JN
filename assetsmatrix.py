from PIL import Image, ImageDraw
import random

WIDTH = 900
HEIGHT = 300

frames = []

for x in range(40):

    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)

    for i in range(60):
        text = random.choice([
            "0","1","A","M","I","R",
            "Amirhossein"
        ])

        draw.text(
            (random.randint(0,850), i*10),
            text,
            fill=(0,255,70)
        )

    frames.append(img)


frames[0].save(
    "matrix.gif",
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0
)