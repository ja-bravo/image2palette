from PIL import Image, ImageDraw
import webcolors


def get_colors(img, colors=10):
    resized = img.resize((255, 255))
    # Quantize to 10 colors, turn it back into RGB for easier convertion to HEX
    converted = resized.convert('P', palette=Image.ADAPTIVE, colors=colors).convert('RGB')

    def get_first_item(a):
        return a[0]
    colors = converted.getcolors()
    colors.sort(key=get_first_item, reverse=True)
    colors = [webcolors.rgb_to_hex(color[1]) for color in colors]
    return colors


def getWithPalette(baseImage):
    # Get 10 main colors in HEX
    colors = get_colors(baseImage)

    # Create a new blank image
    baseWidth, baseHeight = baseImage.size
    spaceBetweenColors = 20 if baseWidth >= 1500 else 20 if baseWidth >= 1000 else 5
    colorsLen = len(colors)
    colorSize = round(
        (baseWidth - (spaceBetweenColors * colorsLen)) / colorsLen)
    newImage = Image.new(
        'RGBA', (baseWidth, baseHeight + colorSize + (spaceBetweenColors * 2)), (197, 197, 197, 1))

    # Paste the original image
    newImage.paste(baseImage, (0, 0))

    # Draw the palette on the bottom of the image
    context = ImageDraw.Draw(newImage)
    x0 = spaceBetweenColors
    y0 = baseHeight + spaceBetweenColors
    x1 = colorSize
    y1 = baseHeight + spaceBetweenColors + colorSize

    for color in colors:
        context.rectangle([(x0, y0), (x1, y1)], color, '#333', 3)
        x0 += colorSize + spaceBetweenColors
        x1 += colorSize + spaceBetweenColors

    return (newImage, colors)
