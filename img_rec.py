from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys


color = [0,0,0]
def draw_rec(image_path, recs):
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw the rectangle on the image
    font = ImageFont.truetype("Courier.ttc", 40)
    for i, rec in enumerate(recs):
        draw.rectangle(rec, outline='red', width=5)

        # 模糊
        #blurred_rectangle = image.crop(rec).filter(ImageFilter.GaussianBlur(radius=10))
        #image.paste(blurred_rectangle, rec)

        ## Calculate the center of the rectangle for placing the text
        #center_x = (rec[0] + rec[2]) // 2
        #center_y = (rec[1] + rec[3]) // 2
        ## Add text to the image
        #text = f"Rectangle {i}"
        #draw.text((center_x, center_y), text, fill="black", font=font)

    # Save or display the modified image
    #image.save("")
    image.show()

colors = [
    (0,0,0),
    (100,100,100),
    (200,200,200),
    (100,0,0),
    (0,100,0),
    (0,0,100),
]

def draw_blocks(image_path, blocks):
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw the rectangle on the image
    font = ImageFont.truetype("Courier.ttc", 40)
    for i, block in enumerate(blocks):
        color = colors[i%(len(colors))]
        for rec in block:
            draw.rectangle(rec, outline=color, fill=color, width=5)

            # blur
            #blurred_rectangle = image.crop(rec).filter(ImageFilter.GaussianBlur(radius=10))
            #image.paste(blurred_rectangle, rec)
        ## Calculate the center of the rectangle for placing the text
        #center_x = (rec[0] + rec[2]) // 2
        #center_y = (rec[1] + rec[3]) // 2

        ## Add text to the image
        #text = f"Rectangle {i}"
        #draw.text((center_x, center_y), text, fill="black", font=font)

    # Save or display the modified image
    #image.save("")
    image.show()


if __name__ == '__main__':
    image_path = sys.argv[1]
    rectangle_list = [(50, 50, 200, 200), (250, 100, 400, 250), (100, 300, 250, 450)]
    #draw_rec(image_path, rectangle_list)
    draw_blocks(image_path, [rectangle_list])
