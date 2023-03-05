from PIL import Image, ImageDraw, ImageFont

# Open the image file
img = Image.open("imagebg.jpg")

# Define the font and size
font = ImageFont.truetype("arial.ttf", 80)

# Define the text to add
text = ""

# Create a drawing context
draw = ImageDraw.Draw(img)

# Define the position to add the text
x = img.width - 20
y = img.height - 20

# Calculate the text size
text_bbox = draw.textbbox((x, y), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Add the text to the image
draw.text((x - text_width, y - text_height), text, font=font, fill=(255, 0, 0))

# Add the logo to the image
logo = Image.open("logo.jpg")
# logo = logo.resize((100, 100)) # Resize the logo if necessary
img.paste(logo, (330, 50))

# Save the output image
img.save("output_image.jpg")
