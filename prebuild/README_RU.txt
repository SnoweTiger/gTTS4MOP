Copyright (c) 2020 under GPLv3. Author: Snowetiger
Скрипт использует:
gTTS Copyright 2014-2020 Pierre Nicolas Durette (gtts.readthedocs.io)
LAME 3.100  от  lame.sourceforge.io и https://www.rarewares.org/mp3-lame-bundle.php
Oggenc2.88 copyright 2002 by Segher Boessenkool (segher@xiph.org) от https://www.rarewares.org/ogg-oggenc.php

Описание:
gTTS4MOP v1.01 - скрипт генерирующий tar.gz для робота пылесоса Xiaomi MOP (1C)
со звуковыми файлами, произнесенными Google Text-To-Speech
Server for MOP v1.01 -  Генерирует main.bundle и sounpackage.json из всех tar.gz в
папке upload для пылесоса Xiaomi MOP (1C) и запустить файловый сервер для их раздачи

Инструкция:
1.  Установите MiHome от vevs
2.  Откройте phrases.json с помощью текстового редактора (рекомендуется Notepad++)
3.  Отредактируйте фразы которые хотите изменить
    Остальные фразы можно удалить. Важно сохранить спец. символы (" " , :)
4.  Запустите gTTS4MOP.exe
    Скрипт прочитает phrases.json. Найдет в нем измененные фразы.
    Для измененных фраз будет генерируются аудио файлы и помещяются в temp
    Для неизмененных фраз оригинальные аудио файлы будут помещяются в temp
    Собирается tts4mop.tar.gz
    Собираются main.bundle soundpackage.json (из всех архивов в папке upload)
    Запускается сервер
5.  Со смартфона с установленым MiHome от vevs заходим по адресу указаному скриптом
6.  Скачиваем main.bundle и заменяем стоковый по адресу
    Android/data/com.xiaomi.smarthome/files/plugin/install/rn/1000004/1003860/android
7.  Заходим в MiHome, иконка пылесоса, голосовые оповещения и выбираем нужный пакет.
    Если новые пакеты не появились, зайдите в настройки/приложения/всеприложения/MiHome
    и очистите кэш
8.  Профит. Пылесос говорит то что хотите вы




