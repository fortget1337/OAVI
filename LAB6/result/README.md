# Лабораторная работа №5. Сегментация текста

Лабораторная работа выполнена для:
    - Алфавит - грузинский
    - Шрифт - Arial
    - Размер шрифта - 40

## Сегментация символов

### Исходное изображение

![imgOriginal](../pictures_results/1_inverted.png)
### Выделенные символы в строке
![imgOut](../pictures_results/symbols/1.png) ![imgOut](../pictures_results/symbols/2.png) ![imgOut](../pictures_results/symbols/3.png) ![imgOut](../pictures_results/symbols/4.png) ![imgOut](../pictures_results/symbols/5.png) ![imgOut](../pictures_results/symbols/6.png) ![imgOut](../pictures_results/symbols/7.png) ![imgOut](../pictures_results/symbols/8.png) ![imgOut](../pictures_results/symbols/9.png) ![imgOut](../pictures_results/symbols/10.png) ![imgOut](../pictures_results/symbols/11.png) ![imgOut](../pictures_results/symbols/12.png) ![imgOut](../pictures_results/symbols/13.png) ![imgOut](../pictures_results/symbols/14.png) ![imgOut](../pictures_results/symbols/15.png) ![imgOut](../pictures_results/symbols/16.png) ![imgOut](../pictures_results/symbols/17.png) ![imgOut](../pictures_results/symbols/18.png) ![imgOut](../pictures_results/symbols/19.png) ![imgOut](../pictures_results/symbols/20.png) ![imgOut](../pictures_results/symbols/21.png) ![imgOut](../pictures_results/symbols/22.png) 

### Анализ

Можно заметить, что алгоритм хорошо справился с грузинским алфавитом.

## Сегментация текстовой области

### Исходное изображение

![imgOriginal](../pictures_results/1_inverted.png)

### Сегментированное изображение

![imgOut](../pictures_results/1_cutted.png)

### Анализ

Алгоритм сегментации текстовой области выделяет текст на основе профилей, в связи с чем может появиться ненатурально "высокая" область, так как в профили будут попадать маленькие части текста, по типу верхушек некоторых букв.