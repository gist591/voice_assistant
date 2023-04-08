import main
import main_apps
import webbrowser as browser
from fuzzywuzzy import fuzz
from threading import Thread
from threading import Event
import random
import subprocess
import re
import time
import pickle

try:
    with open('config.pkl', 'rb') as config:
        settings = pickle.load(config)
except: Thread(target=main.speaker, args=('''кажется, вы не создали
 конфигурационный файл, запустите для этого файл инит точка пай''')).start()


first_part_composite_combinations = ('а', 'прогноз')
composite_combinations = ('а ещё', 'прогноз погоды')


def composite_words(r, request):
    index = request.index(r)
    r1 = r + ' ' + request[index+1]

    return r1


def pre_order_processing(voice_input):
    several_commands_bool = 0
    superfluous_words = ('мне', 'пожалуйста', 'можешь')
    args = voice_input.split(' ')
    request = args.copy()
    for r in args:
        if r in first_part_composite_combinations:
            r1 = composite_words(r, request)
            if r1 in composite_combinations:
                index = request.index(r)
                del request[index], request[index]
                del args[index]
                request.insert(index, r1)
                r = r1
        if r in ('а ещё', 'и'):
            several_commands_bool = 1

    return request, several_commands_bool


def greetings(*args: list):
    if not args:
        Thread(target=main.speaker, args=(random.choice(('рада вас приветствовать', 'здравствуй',
                                       'привет', 'приветствую',
                                       'рада тебя видеть вновь')),)).start()


def parting(*args: list):
    Thread(target=main.speaker, args=(random.choice(
        ('буду ждать тебя', 'надеюсь, еще увидимся', 'до скорого', 'пока',
         'всего хорошего')),)).start()
    exit(1)


def opening_program(*args: list, settings=settings):
    list_software = {
        'атом': settings[0],
        'терминал': settings[1],
        'менеджер': settings[2],
        'браузер': settings[3],
        #'дискорд': 'discord',
        'телеграм': 'telegram-desktop',
    }
    for a in args:
        for name_software in list_software.keys():
            if fuzz.WRatio(a, name_software) > 85:
                subprocess.Popen(
                    list_software[name_software], shell=True,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                break
        else:
            continue
        break


def get_weather_forecast(*args: list):
    browser.get().open('https://www.gismeteo.ru/weather-krasnodar-5136/')


def search(*args: list):
    args = ' '.join(args)
    browser.get().open(
        f'https://duckduckgo.com/?q={args}&ia=web')

# (слова, которые вызывают команду) (команда) (ее нужно вызывать в отдельном потоке?)
commands = {('привет', 'лиза', 'доброе утро', 'здравствуй'): (greetings, 0),
            ('пока', 'прощай', 'увидимся'): (parting, 0),
            ('прогноз'): (get_weather_forecast, 0),
            ('открой'): (opening_program, 1),
            ('найди', 'найти'): (search, 1),
            ('таймер'): (main_apps.timer, 1)
            }

def timer(*args:list):
    print('timer')
    digits = {'полминуты': 0.5 ,'одну': 1, 'две': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'шестьдесят': 60}
    time_notation = {'секунд': 1, 'секунды': 1, 'минут': 60, 'минуты': 60, 'час': 3600, 'часов': 3600}
    for arg in args:
        if arg in digits:
            interval = digits.get(arg)
            interval_word = arg
        else:
            if arg in time_notation:
                k = time_notation.get(arg)
                k_word = arg
            else:
                k = 60
                k_word = 'минут'
    interval *= k

    Thread(target=main.speaker(), args=(f'таймер заведен на {interval_word} {k_word}',)).start()
    time.sleep(interval)
    Thread(target=main.speaker(), args=(f'таймер на {interval_word} {k_word} вышел',)).start()

def several_commands(request: list):
    for r in request:
        if r in ('а ещё', 'и'):
            request = ' '.join(request)
            request = re.split('а ещё|\sи\s', request)

            [request.insert(i, request.pop(i).split())
             for i in range(len(request))]
            break
    return request



def execute_command_with_name(voice_input):
    task_bool = 0
    request, several_commands_bool = pre_order_processing(voice_input)
    if several_commands_bool == 1:
        request = several_commands(request)
    else:
        request.insert(0, [request[i] for i in range(len(request))])
        request = request[:1]

    for r in request:
        for k in r:
            for key in commands.keys():
                if fuzz.WRatio(k, key) > 85:
                    last_command = key
                    r.remove(k)
                    args = r

                    print('key: '+str(key))
                    print('command: '+str(last_command))
                    print('WRatio: '+str(fuzz.WRatio(k, key)))
                    print('args: '+str(args))

                    if commands[key][1] == 0:
                        commands[key][0](*args)
                    else:
                        th = Thread(target=commands[key][0], args=(args))
                        th.start()

                    task_bool = 1

    if task_bool == 0:
        Thread(target=main.speaker, args=('я тебя не поняла',)).start()

    return True
