
from PIL import Image
import matplotlib.pyplot as plt
import math

# ===== SETTINGS =====
file_name = r"C:\Users\Rishi\Documents\Rishi\Personal\Sarah 2026\Image.txt"
columns = 262          # Change this to control the image width
pixel_size = 1         # Size of each pixel in the final image
# ====================

# Read the binary data
with open(file_name, "r") as f:
    binary = "".join(f.read().split())

# Keep only binary digits
binary = "".join(bit for bit in binary if bit in "01")

if not binary:
    raise ValueError("No binary digits (0 or 1) found in the file.")

if columns <= 0:
    raise ValueError("Number of columns must be positive.")

# Calculate the number of rows needed
rows = math.ceil(len(binary) / columns)

# Pad the last row with white pixels (0)
binary = binary.ljust(rows * columns, "0")

# Convert binary digits into pixel values:
# 1 = black (0), 0 = white (255)
pixels = [
    0 if bit == "1" else 255
    for bit in binary
]

# Create the image
img = Image.new("L", (columns, rows))
img.putdata(pixels)

# Enlarge the image without smoothing the pixels
img = img.resize(
    (columns * pixel_size, rows * pixel_size),
    Image.Resampling.NEAREST
)

# Save and display
# img.save("binary_image.png")

plt.figure(figsize=(12, 8))
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.axis("off")
plt.title(f"Binary image: {columns} columns")
plt.show()

# print(f"Image saved as binary_image.png")
# print(f"Original bits: {len(binary)}")
print(f"Image dimensions: {columns} columns × {rows} rows")
