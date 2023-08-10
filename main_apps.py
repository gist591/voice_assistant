import main
from threading import Thread
import time
from fuzzywuzzy import fuzz
import os
import pickle
from typing import Union

Seconds: Union[float, int]

def timer(*args:list):
    print('timer')
    digits: dict[str, Seconds] = {'полминуты': 0.5 ,'одну': 1, 'две': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'шестьдесят': 60}
    time_notation: dict[str, Seconds] = {'секунд': 1, 'секунды': 1, 'минут': 60, 'минуты': 60, 'час': 3600, 'часов': 3600}
    for arg in args:
        if arg in digits:
            interval: Seconds = digits.get(arg)
            interval_word: str = arg
        else:
            if arg in time_notation:
                k: Seconds = time_notation.get(arg)
                k_word: str = arg
            else:
                k: Seconds = 60
                k_word: str = 'минут'
    interval: Seconds *= k
    th_speaker = Thread(target=main.speaker, args=((f'таймер заведен на {interval_word} {k_word}'),))
    th_speaker.start()
    time.sleep(interval)
    Thread(target=main.speaker, args=((f'таймер на {interval_word} {k_word} вышел'),)).start()
