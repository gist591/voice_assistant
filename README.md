# Голосовой ассистент


Голосовой ассистент на Python для GNU/Linux систем.

____
## Оглавление

* [Зависимости](#Зависимости)
* [Установка](#Установка)
* [Функционал](#Функционал)
* [Планы на будущее](#Планы-на-будущее)

____
## Зависимости

Проект авп для GNU/Linux систем, возможна работа на MacOS, но поддержки других систем на данный момент нет.
Для запуска голосового ассистента необходим Python >= 3.9.
Необходимые библиотеки: `fuzzywuzzy` `vosk` `torch` `sounddevice` `SpeechRecognition`

____
## Установка и использование

Предпологается, что на устройстве установлена система GNU/Linux и уже установлен Python >= 3.9

Для установки зависимостей необходима утилита pip.

После скачивания проекта, через терминал переходим в директорию проекта, все дальнейшие действия предпологают, что вы находитесь в корневой папке проекта. После этого пишем следующую команду:

`pip install -r requirements.txt`

После удачного завершения установки все зависимости будут установлены.

Перед первым запуском стоит запустить файл *init.py* командой `python init.py` для конфигурации. Сам голосовой ассистент запускается командой `python main.py`

____
## Функционал

На данный момент функционал крайне скромен, но в ближайшее время будет значительно пополняться.

Сейчас голосовой ассистент имеет следующие функции:

  * открывать ряд программ (терминал, браузер, среду разработки, телеграм и файловый менеджер) -- "открой {название программы}", например, `открой терминал`

  * ставить таймер -- "таймер {временной промежуток}"

  * искать информацию по вашему запросу -- "найди/найти {поисковый запрос}"

  * Также умеет здороваться и прощаться -- ('привет', 'лиза', 'доброе утро', 'здравствуй') и ('пока', 'прощай', 'увидимся') соответсвенно

Также голосовой ассистент может обрабатывать несколько команд сразу, если между командами сказать "а ещё/и"

____
## Планы на будущее

- [ ] определение местоположения по желанию (добавить в кофигурационный файл), понадобится для прогноза

- [ ] прогоноз через api

- [ ] календарь с информацией о событиях

- [ ] "планы" - замена заметкам, наговорить что-то голосовому ассистенту, голосовой ассистент переведет это в текст и сохранит

- [ ] версия под андроид

- [ ] нейронная сеть для определения команд

- [ ] demons' analytic - создать механизм администрирования
 пользовательских "демонов", процессов, которые запускаются вместе с запуском устройства -- **в данный момент не имеет смысла**

- [ ] оповещение в телеграм -- **нет необходимости на данном этапе, лишь после добавления возможности создания сети устройств с одним голосовым ассистентом**

- [ ] пересмотреть механизм удаления ('мне', 'пожалуйста', 'можешь')

- [ ] пересмотреть неделимые выражения ('а еще', 'прогноз погоды')

- [ ] добавить текст напоминания в таймер
