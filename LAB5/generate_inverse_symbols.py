from PIL import Image
import os

# Папки с изображениями
images_dir = 'LAB5/generated_images_letters'
output_dir = 'LAB5/generated_images_inverse_letters'
os.makedirs(output_dir, exist_ok=True)

# Грузинский алфавит
alphabet = 'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'


def invert_image(image_path, save_path):
    img = Image.open(image_path).convert('L')  # Преобразование в оттенки серого

    img = Image.eval(img, lambda x: 255 - x)  # Инвертирование изображения

    img.save(save_path)  # Сохранение результата


# Инвертирование изображений всех букв
for symbol in alphabet:
    image_path = os.path.join(images_dir, f'{symbol}.png')
    if os.path.exists(image_path):
        save_path = os.path.join(output_dir, f'{symbol}.png')
        invert_image(image_path, save_path)

print("Инверсия изображений завершена!")