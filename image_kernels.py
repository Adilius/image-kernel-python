import numpy as np
import cv2 as cv 
from skimage import io # Utilities to read and write images in various formats

def img_to_rgb(image):
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image_rgb

def img_to_gray(image):
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return image_gray

def resize_scaling_image(image, scaling):
    # Get new height and width
    width = int(image.shape[0] * scaling/100)
    height = int(image.shape[1] * scaling/100)
    dsize = (width, height)

    # Resize the image
    image_resized = cv.resize(image, dsize)
    return image_resized

def show_image(image):
    #print(f'Image shape: {image.shape}')
    io.imshow(image)
    io.show()

def convolution(image, kernel):
    image_x, image_y = image.shape

    new_image = np.zeros((image_x, image_y), dtype=np.uint8)

    for x in range(image_x):
        for y in range(image_y):
            new_pixel_value = 0

            if x != 0 and y != 0:
                top_left_value = image[x-1][y-1] * kernel[0][0]
                new_pixel_value += top_left_value

            if x != 0:
                top_middle_value = image[x-1][y] * kernel[0][1]
                new_pixel_value += top_middle_value

            if x != 0 and y != image_y-1:
                top_right_value = image[x-1][y+1] * kernel[0][2]
                new_pixel_value += top_right_value

            if y != 0:
                left_middle_value = image[x][y-1] * kernel[1][0]
                new_pixel_value += left_middle_value

            middle_value = image[x][y] * kernel[1][1]
            new_pixel_value += middle_value

            if y != image_y-1:
                right_middle_value = image[x][y+1] * kernel[1][2]
                new_pixel_value += right_middle_value

            if x != image_x-1 and y != 0:
                bottom_left_value = image[x+1][y-1] * kernel[2][0]
                new_pixel_value += bottom_left_value

            if x != image_x-1:
                bottom_middle_value = image[x+1][y] * kernel[2][1]
                new_pixel_value += bottom_middle_value
                
            if x != image_x-1 and y != image_y-1:
                bottom_right_value = image[x+1][y+1] * kernel[2][2]
                new_pixel_value += bottom_right_value

            if new_pixel_value > 255:
                new_pixel_value = 255
            if new_pixel_value < 0:
                new_pixel_value = 0
            new_image[x][y] = int(new_pixel_value)

    return new_image

image = io.imread('Lenna.png')
show_image(image)

#image_rgb = img_to_rgb(image)
#show_image(image_rgb)

image_gray = img_to_gray(image)
show_image(image_gray)


image_scaled = resize_scaling_image(image_gray, 50)
show_image(image_scaled)
#print(image_scaled)

kernel_sharpen = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]

image_sharpen = convolution(image_scaled, kernel_sharpen)
show_image(image_sharpen)
#print(new_image)

kernel_blur = [
    [0.05, 0.1, 0.05],
    [0.1, 0.4, 0.1],
    [0.05, 0.1, 0.05]
]

image_blur = convolution(image_scaled, kernel_blur)
show_image(image_blur)
