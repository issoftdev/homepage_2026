import os
from PIL import Image

folder = r"C:\Users\kukky\.gemini\antigravity-ide\brain\94018755-1af5-48bb-a839-06d51a31b99b"
files = [
    "media__1783904435098.png",
    "media__1783904435109.png",
    "media__1783904435129.png"
]

for f in files:
    path = os.path.join(folder, f)
    if os.path.exists(path):
        try:
            img = Image.open(path)
            rgb_img = img.convert('RGB')
            width, height = rgb_img.size
            gray_score = 0
            for x in range(width):
                for y in range(height):
                    r, g, b = rgb_img.getpixel((x, y))
                    if r < 240 or g < 240 or b < 240: # Ignore white background
                        # Check if pixel is gray (R, G, B are very close and not white/black)
                        if abs(r - g) < 15 and abs(g - b) < 15 and abs(r - b) < 15:
                            # And ensure it's not too light (white) or too dark (black)
                            if 30 < r < 180:
                                gray_score += 1
            print(f"{f}: size={img.size}, gray_score={gray_score}")
        except Exception as e:
            print(f"Error reading {f}: {e}")
