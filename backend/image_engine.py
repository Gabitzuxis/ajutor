from PIL import Image,ImageDraw
import random

def generate_images(prompts):

    images=[]

    for i,p in enumerate(prompts):

        img = Image.new(
            "RGB",
            (1080,1920),
            (
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
            )
        )

        d=ImageDraw.Draw(img)

        d.text((40,900),p,(255,255,255))

        name=f"img{i}.png"

        img.save(name)

        images.append(name)

    return images
