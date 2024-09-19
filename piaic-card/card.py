from PIL import Image, ImageDraw, ImageFont
from typing import Union

# Step 1: Create a blank canvas for the ID card
card_width, card_height = 700, 480  # Updated height
id_card = Image.new('RGB', (card_width, card_height), 'white')

# Step 2: Load fonts (use explicit type hinting)
try:
    title_font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont] = ImageFont.truetype('arial.ttf', 40)  # Title font for "PIAIC ID Card"
    detail_font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont] = ImageFont.truetype('arial.ttf', 20)  # Font for the details
    q1_font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont] = ImageFont.truetype('arial.ttf', 30)  # Font for "Q1"
    wmd_font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont] = ImageFont.truetype('arial.ttf', 20)  # Smaller font for "WMD"
    signature_font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont] = ImageFont.truetype('arial.ttf', 25)  # Font for "Authorized Signature"
except IOError:
    title_font = ImageFont.load_default()  # Type will be ImageFont.ImageFont
    detail_font = ImageFont.load_default()
    q1_font = ImageFont.load_default()
    wmd_font = ImageFont.load_default()
    signature_font = ImageFont.load_default()

# Step 3: Draw on the image
draw = ImageDraw.Draw(id_card)

# Step 4: Add the title "PIAIC ID Card" on the left side
title_text = "ID Card"
# Use textbbox to get text size
bbox = draw.textbbox((0, 0), title_text, font=title_font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
draw.text((50, 20), title_text, font=title_font, fill="green")  # Adjust x-coordinate for left side

# Step 5: Add the user details on the left side
details = [
    ("Name:", " Aqsa Shah"),
    ("Roll No:", " PIAIC2477"),
    ("Distance learning:", " No"),
    ("City:", " Karachi"),
    ("Center:", " Bahria Auditorium"),
    ("Campus:", " Karsaz"),
    ("Day/Time:", " Sunday-2:00pm to 6:00pm"),
    ("Batch", "61")  # Note: 'Batch' and '61' are now separate
]

x_offset = 50
y_offset = 100
line_height = 40  # Space between lines

for label, value in details:
    if label == "Batch":  # Special handling for "Batch 61"
        # Draw label in green
        draw.text((x_offset, y_offset), f"{label} {value}", font=detail_font, fill="green")
    else:
        # Draw label in green
        draw.text((x_offset, y_offset), label, font=detail_font, fill="green")
        
        # Draw value in black
        draw.text((x_offset + draw.textbbox((0, 0), label, font=detail_font)[2], y_offset), value, font=detail_font, fill="black")
    
    y_offset += line_height

# Step 6: Draw red and green borders at the bottom
border_thickness = 5  # Thickness for the green and red borders

# Draw bottom red border (200 pixels wide)
red_border_height = 40
red_border_width = 200
draw.rectangle([(0, card_height - red_border_height), (red_border_width, card_height)], fill="red")

# Draw green border matching the height of the red border
green_border_width = 200
green_border_start_x = red_border_width
draw.rectangle([(green_border_start_x, card_height - red_border_height), (green_border_start_x + green_border_width, card_height)], fill="green")

# Draw white section on the right side of the green border
draw.rectangle([(green_border_start_x + green_border_width, card_height - red_border_height), (card_width, card_height)], fill="white")

# Add "WMD" text in white on top of the green area
wmd_text = "WMD"
bbox_wmd = draw.textbbox((0, 0), wmd_text, font=wmd_font)
wmd_text_width = bbox_wmd[2] - bbox_wmd[0]
wmd_text_height = bbox_wmd[3] - bbox_wmd[1]
wmd_x = green_border_start_x + (green_border_width - wmd_text_width) / 2
wmd_y = card_height - red_border_height + (red_border_height - wmd_text_height) / 2
draw.text((wmd_x, wmd_y), wmd_text, font=wmd_font, fill="white")

# Add "Q1" text in white on top of the red area
q1_text = "Q1"
bbox_q1 = draw.textbbox((0, 0), q1_text, font=q1_font)
q1_text_width = bbox_q1[2] - bbox_q1[0]
q1_text_height = bbox_q1[3] - bbox_q1[1]
q1_x = (red_border_width - q1_text_width) / 2
q1_y = card_height - red_border_height + (red_border_height - q1_text_height) / 2
draw.text((q1_x, q1_y), q1_text, font=q1_font, fill="white")

# Step 7: Add the passport-size photo at the top right
try:
    photo = Image.open('./piaic-card/image.png')  # Correct image path here
    if isinstance(photo, Image.Image):  # Ensure that the object is of type Image
        photo_resized = photo.resize((150, 200))  # Resize returns Image object
        photo_x = card_width - photo_resized.width - 50  # Adjust for padding on the right
        photo_y = 20  # Position at the top
        id_card.paste(photo_resized, (photo_x, photo_y))  # Paste photo on the card
    else:
        raise ValueError("The object loaded is not an Image.")
except IOError:
    print("Could not load the image, please provide a valid image path.")

# Step 8: Add "Authorized Signature" text in green on the right side
signature_text = "Authorized Signature"
bbox_signature = draw.textbbox((0, 0), signature_text, font=signature_font)
signature_text_width = bbox_signature[2] - bbox_signature[0]
signature_text_height = bbox_signature[3] - bbox_signature[1]

# Move the "Authorized Signature" slightly higher
signature_x = green_border_start_x + green_border_width + (card_width - (green_border_start_x + green_border_width) - signature_text_width) / 2
signature_y = card_height - red_border_height - 20  # Move it higher (20 pixels above the green area)

# Draw the "Authorized Signature" text
draw.text((signature_x, signature_y), signature_text, font=signature_font, fill="green")

# Draw a green border line above the "Authorized Signature" text
border_y = signature_y - 10  # Adjust position of border line
draw.line([(green_border_start_x + green_border_width, border_y), (card_width, border_y)], fill="green", width=2)

# Step 9: Save the ID card
id_card.save('id_card_output.png')

# Step 10: Show the result (optional)
id_card.show()
