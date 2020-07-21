#  Copyright (c) 2020 under GPLv3. Author: Snowetiger
# Function for gTTS4MOP v1.01

import os
import json
import tarfile
from gtts import gTTS


# Проверяем папки, если их нет создаем
def check_dirs(scr_dir,temp_dir,upload_dir, required_file_list):
    errore=[]
    if os.path.isdir(temp_dir):
        files = os.listdir(temp_dir)
        for file in files:
            os.remove(temp_dir+"/"+file)
    else:
        os.mkdir(temp_dir)
    if not os.path.isdir(upload_dir):
        os.mkdir(upload_dir)
    if not os.path.isdir(scr_dir):
        os.mkdir(scr_dir)

    scr_files = os.listdir(scr_dir)
    if not required_file_list[1] in scr_files:
        errore.append(required_file_list[1])
    if not required_file_list[0] in scr_files:
        errore.append(required_file_list[0])
    if not required_file_list[2] in scr_files:
        errore.append(required_file_list[2])
    if not required_file_list[3] in scr_files:
        errore.append(required_file_list[3])

    if not errore:
        print('Папки и необходимые файлы проверены')
    else:
        print('Файл(ы) ',errore,' не найдены!')
        exit(10)

    # Заготовка для закачки недостающих файлов
    # f = open(r'D:\file_bdseo.zip', "wb")  # открываем файл для записи, в режиме wb
    # ufr = requests.get("http://site.ru/file.zip")  # делаем запрос
    # f.write(ufr.content)  # записываем содержимое в файл; как видите - content запроса
    # f.close()

def getandcheck_phrases(phrases_original_path,phrases_json_path):

    if phrases_json_path in os.listdir():
        with open(phrases_json_path, 'r', encoding='utf-8') as f:
            phrases_new = json.load(f)
    else: phrases_new={}

    with open(phrases_original_path, 'r', encoding='utf-8') as f:
        phrases_orig = json.load(f)

    new_phrases = {}
    old_phrase = []

    for n_phrase in phrases_orig:
        if n_phrase in phrases_new:
            phrases_new[n_phrase]=phrases_new[n_phrase].lower().replace('#','').replace('@','').replace('!','').replace('/','').replace('<','')
            if not phrases_new[n_phrase] == phrases_orig[n_phrase]:
                new_phrases[n_phrase] = phrases_new[n_phrase]
            else:
                old_phrase.append(n_phrase)
                # print (f'Фраза:{phrase} найдена, заменена на "{phrases[phrase]}"')
        else:
            old_phrase.append(n_phrase)
            # print (f'Фраза:{phrase} не найдена, оставлена оришинальная "{phrases[phrase]}"')
    print(f'Найдено {len(new_phrases)} новых фраз, оставлено {len(old_phrase)} оригинальных')
    return new_phrases,old_phrase

# Добавляем недостающие или неизмененные фразы из scr\ru.tar.gz
def put_orig_files(scr_dir,temp_dir,old_phrase):
    with tarfile.open(scr_dir+'/ru.tar.gz', "r:gz") as tar:
        for phrase_n in old_phrase:
            tar.extract(phrase_n+'.ogg', path=temp_dir)
    print(f'Добавлено {len(old_phrase)} оригинальных OGG')

#Гугл говорилка. на вход принимает словарь  {номер фразы : "фраза", ....} и адресс папки temp
def put_gsynth_files(phrases, temp_dir):
    if len(phrases) > 0 :
        print('Генерируем фразы - ', end="")
        for key in phrases:
            tts = gTTS(text=phrases[key], lang='ru')
            file_path=temp_dir+'/'+str(key)
            tts.save(file_path+'.mp3')
            print('>', end="")
            #Костыли
            #Преобразуем .mp3 -> .wav
            os.system(f"scr\lame.exe --decode --quiet {file_path}.mp3 {file_path}.wav")
            # Преобразуем .wav -> .ogg
            os.system(f"scr\oggenc2.exe --quiet {file_path}.wav")
            # Чистим .wav -> .ogg
            os.remove(f'{file_path}.wav')
            os.remove(f'{file_path}.mp3')
            print('>', end="")
            # End Костыли

        print(f' {len(phrases)} фраз сгенерировано и добавлено')

    else:
        print('Новых фраз не добавлено')

#Собираем архив
def tar_maker(temp_dir, upload_dir, tar_name,new_phrases,old_phrase):
    import tarfile
    tar_adress=f'{upload_dir}/{tar_name}.tar.gz'
    # ogg_files = os.listdir(temp_dir)
    if len(os.listdir(temp_dir)) == 60:
        with tarfile.open(tar_adress, "w:gz") as tar:
            for ogg_file in old_phrase:
                tar.add(f'{temp_dir}/{ogg_file}.ogg', arcname=f'{ogg_file}.ogg')
                # os.remove(f'{temp_dir}/{ogg_file}.ogg') #очистка папки темп
            for ogg_file in new_phrases:
                tar.add(f'{temp_dir}/{ogg_file}.ogg', arcname=f'{ogg_file}.ogg')
                # os.remove(f'{temp_dir}/{ogg_file}.ogg') #очистка папки темп
            tar_len=len(tar.getnames())
        print(f'Архив собран, всего {tar_len} фраз')
    else:
        print('Нехватает OGG файлов, перезапустите скрипт')
