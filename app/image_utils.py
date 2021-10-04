from PIL import Image
import math
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def crop_image(new_image, crop_width=1200, crop_height=800):
    width, height = new_image.size  # Get dimensions
    left = (width - crop_width) / 2
    top = (height - crop_height) / 2
    right = (width + crop_width) / 2
    bottom = (height + crop_height) / 2
    cropped_image = new_image.crop((left, top, right, bottom))
    return cropped_image


def image_reshape(uploaded_image):
    image = Image.open(uploaded_image)
    if image.size[0] > image.size[1]:
        if image.size[0] / image.size[1] < 1.5:
            scale = 1200 / image.size[0]
            new_width = math.ceil(image.size[0] * scale)
            new_height = math.ceil(image.size[1] * scale)
            new_image = image.resize((new_width, new_height), Image.ANTIALIAS)
            cropped_image = crop_image(new_image)
        if image.size[0] / image.size[1] >= 1.5:
            scale = 800 / image.size[1]
            new_width = math.ceil(image.size[0] * scale)
            new_height = math.ceil(image.size[1] * scale)
            new_image = image.resize((new_width, new_height), Image.ANTIALIAS)
            cropped_image = crop_image(new_image)

    image_io = BytesIO()
    cropped_image.save(image_io, image.format)
    return image_io
