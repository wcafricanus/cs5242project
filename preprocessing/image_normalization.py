from cv2 import resize, imread
import cv2
import os


def resize_image(file_name):
    original = imread(file_name)
    img = resize(original, (512, 512), interpolation=cv2.INTER_AREA)
    return img


def to_grey_scale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def compress_image_files(source_dir_name):
    file_dir_path = os.path.dirname(os.path.realpath(__file__))
    image_dir = file_dir_path + '/../Data/' + source_dir_name
    output_dir = file_dir_path + '/../Data/' + source_dir_name + '_resized'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    file_count = 0
    for filename in os.listdir(image_dir):
        if filename.endswith(".png"):
            resized = resize_image(image_dir + '/' + filename)
            grayed = to_grey_scale(resized)
            cv2.imwrite(os.path.join(output_dir, filename), grayed)
            file_count += 1
        else:
            continue
    print("image file processed: " + str(file_count))


def convert_CXR_files():
    compress_image_files('CXR_png')


def convert_mask_files():
    compress_image_files('masks')


convert_CXR_files()
convert_mask_files()