import main
from threading import Thread
import time
from fuzzywuzzy import fuzz
import os
import pickle

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
    th_speaker = Thread(target=main.speaker, args=((f'таймер заведен на {interval_word} {k_word}'),))
    th_speaker.start()
    time.sleep(interval)
    Thread(target=main.speaker, args=((f'таймер на {interval_word} {k_word} вышел'),)).start()



'''
def calendar(purpose='', *args:list):
    #if os.path.exists(os.getcwd()+'events.pkl'):
    with open('events.pkl', 'rb+') as file:
        events = pickle.load(file)
    #else:
    #    with open('events.pkl', 'wb+') as file:
    #        events = [['', '', '']]
    #        pickle.dump(events, file)
    print(events)
    if purpose != '':
        if purpose == 'deleting':
            events.pop(([i for i in range(len(events)) \
             for k in args if fuzz.WRatio(events[i][1], k) > 80])[0])
            print(events)
            with open('events.pkl', 'wb') as file:
                pickle.dump(events, file)
    return events
'''
