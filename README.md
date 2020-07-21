# gTTS4MOP
Script for generating an archive of phrases said by GoogleTTS for Xiaomi robot vacuum cleaner 1C/MOP STYTJ01ZHM
Скрипт для генерации архива с фразами произнесенными GoogleTTS для робота-пылесоса Xiaomi 1C / MOP STYTJ01ZHM

Requirements/Требования:
* Windows 7 or newer
* Python 3.x.x
* gTTS 
  
Script contains and uses/Скрипт содержит и использует:
* LAME 3.100 from  lame.sourceforge.io
* Oggenc 2.88 from Segher Boessenkool (segher@xiph.org) from https://www.rarewares.org/ogg-oggenc.php
* Archive with original soundpack from Xiaomi

Инструкция по использованию:

Вариант 1 Используем готовый скрипт
1. Скачиваем все содержимое папки dist
2. Открываем phrases.json любимым текстовым редактором
3. Изменяем интересующие нас фразы. (остальные можно удалить)
4. Запускаем gTTS4MOP.exe
5. Заходим со смартфона на указангый скриптом IP адрес. 
6. Заменяем main.bundle
7. Заходим в MiHome от vevs и выбираем озвучку gTTS4MOP

Вариант 2 Используем скрипт на питоне
1. Скачиваем все содержимое папки scr
2.1. Устанавливаем зависимости pip install -r requirements.txt
2.2. Открываем phrases.json любимым текстовым редактором
3. Изменяем интересующие нас фразы. (остальные можно удалить)
4. Запускаем скрипт py gTTS4MOP.py
5. Заходим со смартфона на указангый скриптом IP адрес. 
6. Заменяем main.bundle
7. Заходим в MiHome от vevs и выбираем озвучку gTTS4MOP

