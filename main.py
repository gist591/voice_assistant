import tasks
import main_apps
import recognition
import speech_recognition
import os
import time
from threading import Thread
from threading import Event
import torch
import sounddevice as sd
from queue import Queue

queue = Queue()

def record_and_recognize_audio(microphone, recognizer, *args: tuple):

    recognized_data = ''
    recognizer.adjust_for_ambient_noise(microphone, duration=5)

    try:
        print('Слушаю...')
        audio = recognizer.listen(microphone)

        with open('microphone-results.wav', 'wb') as file:
            file.write(audio.get_wav_data())

    except speech_recognition.WaitTimeoutError:
        print('Я Вас не слышу, Вы уверены, что Ваш микрофон работает?')

    print('Осмысляю ваши слова...')

    recognized_data = recognition.use_recognition()

    queue.put(recognized_data)


# TTS from https://www.silero.ai
def speaker(text):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = './models/model.pt'

    model = torch.package.PackageImporter(
        local_file).load_pickle('tts_models', 'model')
    model.to(device)

    sample_rate = 48000
    speaker = 'baya'

    audio_paths = model.apply_tts(text=text,
                                  speaker=speaker,
                                  sample_rate=sample_rate)

    sd.play(audio_paths, sample_rate)
    sd.wait()


def calendar_init(): # позже будет сделан полный функционал календаря
    events = main_apps.calendar()
    [speaker('у вас на сегодня запланировано '+event[1]) for event in events]

if __name__ == '__main__':

    #calendar_init()

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()


    while True:
        with microphone:
            th_record = Thread(target=record_and_recognize_audio, args=(microphone, recognizer), daemon=True)
            th_record.start()
            th_record.join()

            voice_input = queue.get()

            if voice_input == '':
                continue
            print('\n'+voice_input+'\n')

            if (tasks.execute_command_with_name(voice_input)):
                continue
