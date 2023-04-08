from vosk import Model, KaldiRecognizer
import wave
import json


def use_recognition():
    recognized_data = ''
    try:
        wave_audio_file = wave.open('microphone-results.wav', 'rb')
        model = Model('./models/my_vosk_model')
        recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())
        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if recognizer.AcceptWaveform(data):
                recognized_data = recognizer.Result()

                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data['text']
    except:
        print('Прошу прощения, возникли какие-то проблемы с распознованием')

    return recognized_data
