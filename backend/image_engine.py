from PIL import Image
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

        path=f"img{i}.png"

        img.save(path)

        images.append(path)

    return images
