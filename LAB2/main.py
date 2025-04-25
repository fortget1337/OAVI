import os
import numpy as np
import cv2
import copy
import time

input_folder = 'LAB2/pictures_src/'
output_folder = 'LAB2/pictures_results/'

def load_image(image_name):
    return cv2.imread(os.path.join(input_folder, image_name))

def save_image(image, image_name):
    output_path = os.path.join(output_folder, image_name)
    cv2.imwrite(output_path, image)

# Приведение изображения к полутоновому
def to_grayscale(image):
    grayscale = 0.299 * image[:, :, 2] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 0]
    return grayscale.astype(np.uint8)

# Бинаризация изображения
def binarize_image(grayscale_image, threshold=128):
    binary_image = grayscale_image > threshold
    return binary_image.astype(np.uint8) * 255

# Адаптивная бинаризация Брэдли и Рота
def bradley_roth_binarization(image, window_size=15, threshold_coeff=0.85):
    # Преобразование в оттенки серого, если необходимо
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
    
    height, width = gray.shape
    
    # Установка размера окна (1/8 минимального размера изображения)
    if window_size is None:
        window_size = max(1, min(width, height) // 8)
    
    # Создание интегрального изображения
    integral_image = cv2.integral(gray, cv2.CV_64F)
    
    # Вычисление половины размера окна
    half_window = window_size // 2
    
    # Инициализация бинарного изображения
    binary = np.zeros_like(gray, dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            # Определение границ окна
            x1 = max(0, x - half_window)
            x2 = min(width, x + half_window + 1)
            y1 = max(0, y - half_window)
            y2 = min(height, y + half_window + 1)
            
            # Вычисление суммы в окне
            total = integral_image[y2, x2] - integral_image[y1, x2] - integral_image[y2, x1] + integral_image[y1, x1]
            
            # Количество пикселей в окне
            count = (x2 - x1) * (y2 - y1)
            
            # Расчет порога
            threshold = total / count * threshold_coeff
            
            # Применение порога
            if gray[y, x] < threshold:
                binary[y, x] = 0
            else:
                binary[y, x] = 255
                
    return binary

image_name = 'x-ray.png'

image = load_image(image_name)

grayscale_image = to_grayscale(image)
save_image(grayscale_image, 'grayscale_' + image_name)

binary_image = binarize_image(grayscale_image, threshold=108)
save_image(binary_image, 'binary_' + image_name)

bradley_roth_binary_image = bradley_roth_binarization(image, window_size=15)
save_image(bradley_roth_binary_image, 'bradley_roth_binary_' + image_name)

image_name = 'text.png'

image = load_image(image_name)

grayscale_image = to_grayscale(image)
save_image(grayscale_image, 'grayscale_' + image_name)

binary_image = binarize_image(grayscale_image, threshold=108)
save_image(binary_image, 'binary_' + image_name)

bernsen_binary_image = bradley_roth_binarization(image, window_size=5)
save_image(bernsen_binary_image, 'bradley_roth_binary_' + image_name)

image_name = 'photo.png'

image = load_image(image_name)

grayscale_image = to_grayscale(image)
save_image(grayscale_image, 'grayscale_' + image_name)

binary_image = binarize_image(grayscale_image, threshold=108)
save_image(binary_image, 'binary_' + image_name)

bernsen_binary_image = bradley_roth_binarization(image, window_size=5)
save_image(bernsen_binary_image, 'bradley_roth_binary_' + image_name)

image_name = 'map.png'

image = load_image(image_name)

grayscale_image = to_grayscale(image)
save_image(grayscale_image, 'grayscale_' + image_name)

binary_image = binarize_image(grayscale_image, threshold=108)
save_image(binary_image, 'binary_' + image_name)

bernsen_binary_image = bradley_roth_binarization(image, window_size=5)
save_image(bernsen_binary_image, 'bradley_roth_binary_' + image_name)

image_name = 'house.png'

image = load_image(image_name)

grayscale_image = to_grayscale(image)
save_image(grayscale_image, 'grayscale_' + image_name)

binary_image = binarize_image(grayscale_image, threshold=108)
save_image(binary_image, 'binary_' + image_name)

bernsen_binary_image = bradley_roth_binarization(image, window_size=5)
save_image(bernsen_binary_image, 'bradley_roth_binary_' + image_name)

image_name = 'anime.png'

image = load_image(image_name)

grayscale_image = to_grayscale(image)
save_image(grayscale_image, 'grayscale_' + image_name)

binary_image = binarize_image(grayscale_image, threshold=108)
save_image(binary_image, 'binary_' + image_name)

bernsen_binary_image = bradley_roth_binarization(image, window_size=5)
save_image(bernsen_binary_image, 'bradley_roth_binary_' + image_name)