from PIL import Image, ImageFilter


def info_image(img):
    # info about the image
    print(img)


# apply a filter effect
def blur_image(img):
    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img.save('./output/blur.png', 'png')


def smooth_image(img):
    filtered_img = img.filter(ImageFilter.SMOOTH)
    filtered_img.save('./output/smooth.png', 'png')


def convert_image_greyscale(img):
    new_img = img.convert('L')  # RGB / CMYK / L
    new_img.save('./output/greyscale.png', 'png')


def rotate_img(img, rotation):
    new_img = img.rotate(rotation)
    new_img.save('./output/rotated.png', 'png')


def resize_img(img, size):
    # size is tuple (w, h)
    # does not respect aspect ratio!
    new_img = img.resize(size)
    new_img.save('./output/resized.png', 'png')


def resize_img_aspectratio(img, size):
    # size is tuple (w, h) and is 'requested size'
    # DOES respect aspect ratio! Resulting size is determined by limiting side
    # resizes image object in place
    img.thumbnail(size)
    img.save('./output/thumbnail.png', 'png')


def crop_img(img, box):
    # box is tuple with 4 coordinates (left, upper, right, lower)
    new_img = img.crop(box)
    new_img.save('./output/cropped.png', 'png')


def show_image(img):
    img.show()


img = Image.open('./pokedex/pikachu.jpg')

# run experiments
# info_image(img)
# blur_image(img)
# smooth_image(img)
# convert_image_greyscale(img)
# rotate_img(img, 180)
# resize_img(img, (300, 300)) # w x h as tuple

# box = (100, 100, 400, 400) # (left, upper, right, lower)
# crop_img(img, box)

# resize a large image taking aspect ratio in account
img = Image.open(
    './input/the-new-york-public-library-kvHhSroTNPY-unsplash.jpg')
print(img.size)
resize_img_aspectratio(img, (300, 200))
