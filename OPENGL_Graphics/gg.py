from PIL import Image
img=Image.open('images/grid.png')
img.save('new_img.png', icc_profile=None)