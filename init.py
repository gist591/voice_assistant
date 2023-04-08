import pickle
from main import speaker
from threading import Thread
import os

detail_about_me = '''меня зовут
 Лиза. этот скрипт нацелен на определение некоторых индивидуальных настроек и
 знакомство со мной. можете настраивать все под себя, а я пока буду Вам
 рассказывать. я голосовой ассистент на раннем этапе разработки, за мой
 синтэз речи, о чем это я, за мой голос, я благодарна сил+еро. за
 распознование речи благодарна проекту воск. в будущем хочу обзавестись простой
 нейронной сетью для лучшего понимания команд и восприятия речи, обрести
 кроссплатформенность и начать работать на андроид смартфонах, а также в
 скором времени обрести широкий функционал и легкую настройку, однако на
 данный момент б+ольший акцент имеет работа над моей логикой.'''

def init_config():
    browser = input('введите команду для вызова вашего браузера > ')
    terminal = input('введите команду для вызова вашего терминала > ')
    manager = input('введите команду для вызова вашего файлового менеджера > ')
    text_editor = input('введите команду для вызова вашего текстового редактора/среды разработки > ')
    settings = [browser, terminal, manager, text_editor]

    with open('config.pkl', 'wb+') as config:
        pickle.dump(settings, config)

    thread_speaker = Thread(target=speaker, args=('''конфигурационный файл
     изменен''',))

    thread_speaker.start()
    thread_speaker.join()

thread_speaker = Thread(target=speaker, args=('''приветствую Вас. вы хотите.
 первое - узнать информацию обо мне и настроить конфигурационный файл.
 второе - просто изменить конфигурационный файл.
 третье - просто узнать информацию обо мне.
 предупреждаю, конфигурационный файл необходим, без него моя работа будет
 нестабильна, также хочу обратить ваше внимание, что, возможно, вам придется
 вручную изменить громкость вашего микрофона,
 это единственная возможная причина проблем с распознованием''',))

thread_speaker.start()
thread_speaker.join()

print('1 - узнать информацию обо мне и настроить конфигурационный файл.\n2 - просто изменить конфигурационный файл.\n3 - просто узнать информацию обо мне.')
action = input('> ')

if action == '1':
    thread_speaker = Thread(target=speaker, args=(detail_about_me,))
    thread_speaker.start()

    init_config()
    thread_speaker.join()

if action == '2':
    init_config()

if action == '3':
    thread_speaker = Thread(target=speaker, args=(detail_about_me,))
    thread_speaker.start()
    thread_speaker.join()


thread_speaker = Thread(target=speaker, args=('''настройка завершена, теперь Вы
 можете приступить к моему использованию''',))

thread_speaker.start()
thread_speaker.join()
