from rembg import remove
from PIL import Image

print("Opening image...")
inp = Image.open('linda.jpg')

print("Removing background...")
output = remove(inp)

print("Saving output...")
output.save('output_linda.png')

print("Done!")
