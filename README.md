# Сайт онлайн библиотеки
Создан как офлайн интерфейс для использования контента онлайн библиотеки, которая была собрана [вот этим скриптом](https://github.com/ArtemVolik/online_library).
### Как работает 
Работает с контентом предоставленным парсером. Подробнее [тут](https://github.com/ArtemVolik/online_library/blob/master/README.md).   
Посмотреть как выглядит интерфейс можно [тут](https://artemvolik.github.io/Website_Online_Library/pages/index1.html).
Проект создан в учебных целях.

## Установка для пользователя
1. Скопировать папки `books`, `images`, `pages`, `static`.
2. Открыть любую html страницу браузером.

##Установка для разработчика
- Скопировать все файлы и папки.
- Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки 
зависимостей:  
```
pip install -r requirements.txt
```

## Изменение контента   
- Для смены контента - предварительно подготовьте его с помощью [парсера](https://github.com/ArtemVolik/online_library/).
- Скопируйте полученные в результате парсинга папку с текстами и папку с изображениями в корень сайта.
- Создайте файл .env и укажите в нем путь до файла каталога json:
```
SOURCE_JSON='books_info.json'
```
- Если не будет указано, скрипт будет использовать стандартный файл `books_info.json` в корне сайта

- Выполните в командной строке
```
python render-website.py
```

## Изменение шаблона
Шаблон - `template.py`. Для того чтобы изменения шаблона вступили в силу, выполните:
```
python render-website.py
```
Для удобства, чтобы не выполнять команду-рендер, при каждом внесении правок в шаблон, выполните
```
python server.py 
```
С момента запуска сервера файлы страниц будут рендерится автоматически при изменениях в файле `template.py`.