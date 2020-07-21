#  Copyright (c) 2020 under GPLv3. Author: Snowetiger
# Script use:
# gTTS Copyright 2014-2020 Pierre Nicolas Durette (gtts.readthedocs.io)
# LAME 3.100  from  lame.sourceforge.io and https://www.rarewares.org/mp3-lame-bundle.php
# Oggenc2.88 copyright 2002 Segher Boessenkool (segher@xiph.org) from https://www.rarewares.org/ogg-oggenc.php


#  Name: Google Text-to-Speech for MOP (gTTS4MOP)
#  Version: 1.01

#  Description: gTTS4MOP - Script for generation tar.gz for Xiaomi vacuum cleaner MOP (1C)
#  with audio files pronounced by Google Text-To-Speech
#  Описание: gTTS4MOP - скрипт генерирующий tar.gz для робота пылесоса Xiaomi MOP (1C)
#  со звуковыми файлами, произнесенными Google Text-To-Speech

import function as fm
import os

#Константы = параметры
#Задаем адреса папок
TEMP_DIR = 'temp'
UPLOAD_DIR = 'upload'
SCR_DIR = 'scr'
TAR_NAME = 'tts4mop'
PHRASE_FILE_NAME = 'phrases.json'

BUNDLE_FILE='bundle.sdat'
ORIGINAL_PHRASES_FILE='phrases.sdat'
RU_TAR_FILE='ru.tar.gz'
SOUNDPACKAGE_FILE='soundpackage.sdat'

required_file_list = [BUNDLE_FILE,
                      ORIGINAL_PHRASES_FILE,
                      RU_TAR_FILE,
                      SOUNDPACKAGE_FILE
                      ]

# Исполняемый код. Старт
print('Старт скрипта TTS4MOP v1')

fm.check_dirs(SCR_DIR,
              TEMP_DIR,
              UPLOAD_DIR,
              [BUNDLE_FILE,
               ORIGINAL_PHRASES_FILE,
               RU_TAR_FILE,
               SOUNDPACKAGE_FILE
               ])

#Читаем  json. new_phrases - словарь ключ новаЯ фраза, old_phrase - список фраз без изменений
new_phrases,old_phrase = fm.getandcheck_phrases(SCR_DIR+'/'+ORIGINAL_PHRASES_FILE,PHRASE_FILE_NAME)
fm.put_orig_files(SCR_DIR,TEMP_DIR,old_phrase)
fm.put_gsynth_files(new_phrases, TEMP_DIR)

fm.tar_maker(TEMP_DIR,UPLOAD_DIR,TAR_NAME,new_phrases,old_phrase)

#Запуск скрипта сервера
os.system("py Server4MOP.py 1")
# os.system("Server4MOP.exe 1")
