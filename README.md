# gTTS4MOP
Script for generating an archive of phrases said by GoogleTTS for Xiaomi robot vacuum cleaner 1C/MOP STYTJ01ZHM
Скрипт для генерации архива с фразами произнесенными GoogleTTS для робота-пылесоса Xiaomi 1C / MOP STYTJ01ZHM

Requirements / Требования:
* Windows 7 or newer
* Python 3.x.x
* gTTS 
  
Script contains and uses / Скрипт содержит и использует:
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
2. Устанавливаем зависимости `pip install -r requirements.txt`
3. Открываем `phrases.json` любимым текстовым редактором
4. Изменяем интересующие нас фразы. (остальные можно удалить)
5. Запускаем скрипт `py gTTS4MOP.py`
6. Заходим со смартфона на указангый скриптом IP адрес. 
7. Заменяем `main.bundle`
8. Заходим в MiHome от vevs и выбираем озвучку gTTS4MOP

Instructions for use:

Option 1 Use a ready script
1. Download all the contents of the dist folder
2. Open phrases.json with your favorite text editor
3. Change the phrases that interest us. (the rest can be deleted)
4. Run gTTS4MOP.exe
5. We go from the smartphone to the IP address specified by the script.
6. Replace main.bundle
7. Go to MiHome from Vevs and select the voice acting gTTS4MOP

Option 2 Using a python script
1. Download all contents of the scr folder
2. Install dependencies pip install -r requirements.txt
3. Open phrases.json with your favorite text editor
4. Change the phrases that interest us. (the rest can be deleted)
5. Run the py script gTTS4MOP.py
6. We go from the smartphone to the IP address specified by the script.
7. Replace main.bundle
8. Go to MiHome from vevs and select the voice acting gTTS4MOP
