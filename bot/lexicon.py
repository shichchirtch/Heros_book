LEXICON: dict[str, str] = {
    'forward': '>>',

    'backward': '<<',

    '/start': '<b>Привет, читатель!</b>\n\n'
              'Это бот, в котором ты можешь прочитать тестовый текст \n\n'
              'Чтобы посмотреть список доступных команд - набери /help',


    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel_text': '/continue - продолжить чтение'
}

language_kit = (
'rus', 'eng', 'en', 'de', 'енг', 'an', 'кгы', 'утп', 'ву', '/eng',
'/en', '/rus', '/de', 'нем', 'анг', 'рус', 'ge', 'pyc', 'рус')

language_responce = ('',
                     'Выбран русский язык',
                     'Reading goes in English',
                     'Lesung gehts auf Deutsch')

continue_ans = ('',
                'Продолжаем чтение !',
                'Carry reading on !',
                'Lese weitermachen !')

other_ant = (
    '',
    'Давайте лучше продолжим чтение ?',
    'Let\'s better reading on ?',
    'Lass uns weiterlesen ?'
)

dlina_doc = ('',
             'Количество страниц в докладе ',
             'Report has pages ',
             'Nummer Seiten ist ')

bookmark_10 = ('',
               'Можно добавить не более 10 разных закладок',
               'You can add up to 10 different bookmarks',
               'Sie können bis zu 10 verschiedene Lesezeichen hinzufügen')

bookmark_add = ('',
                'Страница добавлена в закладки !',
                'Page added to bookmarks !',
                'Seite zu Lesezeichen hinzugefügt !'
                )

bookmark_list = ('',
                 '<b>Это список ваших закладок:</b>                    🔴',
                 '<b>Your bookmarks list:</b>                 🔴',
                 '<b>Eure Lesezeichen:</b>               🔴')

no_bookmarks = ('',
                'У вас пока нет ни одной закладки.\n\n'
                'Чтобы добавить страницу в закладки - во время чтения '
                'книги нажмите на кнопку с номером этой '
                'страницы\n\n'
                '/continue - продолжить чтение',

                'You don\'t have any bookmarks yet.\n\n'
                'To bookmark a page - while reading'
                'books click on the button with the number of this one'
                'pages\n\n/continue - carry reading on',

                'Sie haben noch keine Lesezeichen.\n\n '
                'Um eine Seite zu Ihren Lesezeichen hinzuzufügen, '
                'klicken Sie beim Lesen eines Buches auf die Schaltfläche '
                'mit der Nummer dieser Seite\n\n'
                '/continue - für weiterlesen')

edit_bookmarks_button = ('', 'Редактировать закладки', 'Edit bookmarks', 'Lesezeichen bearbeiten')

cancel = ('', 'Вернуться к чтению', 'Return to read', 'weiterlesen')

edit_bookmarks = ('', 'Удалите ненужные закладки', 'delete useless bookmarks', 'löschen nutzloss Lesezeichen')

text_for_send_refferal = ('',
                          'Напишите и отправьте ваш отзыв в следующем сообщении !',
                          'Write and send your review in next massages',
                          'Bitte geben Sie in Ihrem nächsten Beitrag Feedback.')

success_send = ('',
                'Ваш отзыв успешно отправлен !',
                'Your feedback was successfuly sent !',
                'Ihre Bewertung wurde erfolgreich versendet!')

help_command = ('AgACAgIAAxkBAAIC9GaAg7HdIRGcpkPtoKCVB-R-ZvRlAAKZ4TEb_wEBSOvvjLbUFAKPAQADAgADeQADNQQ',

              '<b>Как пользоваться Ботом</b>\n\n'
              'Доступные команды:\n\n'
              '/about_project - перейти в начало\n\n'
              '/faces - перейти к списку заключенных\n\n'
              '/continue - продолжить чтение\n\n'
              '/bookmarks - посмотреть список закладок\n'
              '/exit - вернуться к основному содержанию доклада\n'
              'Доклад доступен на трех языках     /rus    /en    /de\n\n'
              'Чтобы сохранить закладку - нажмите на кнопку с номером '
              'страницы\n\n'
              'У некоторых героев можно прочитать их последнее слово в суде,\n нажав на /Фамилию\n\n'
              'Чтобы написать отзыв нажмите /otzyv\n\n'
              '/contacts  - Наши контакты\n\n'
              '<b>Приятного чтения!</b>',

              '<b>Instructions</b>\n\n'
              'Available commands:\n\n'
              '/about_project - go to start\n\n'
              '/faces - go to faces list\n\n'
              '/continue - carry reading on\n\n'
              '/bookmarks - show a bookmarck\'s list\n\n'
              '/exit - return to core report\n\n'
              'Enter page number if you know \n\n'
              'To write a review click   /otzyv\n\n'
              'The report is available in three languages     /en    /de    /rus\n\n' 
              '/contacts  - our contacts\n\n\n'
              '<b>Enjoy reading!</b>',

              '<b>Anweisungen</b>\n\n'
              'Verfügbare Befehle:\n\n'
              '/about_project  -  Über das Projekt\n\n'
              '/faces - go to faces list\n\n'
              '/continue - weiterlesen\n\n'
              '/bookmarks - Lesezeichen anzeigen\n\n'
              '/exit  -  zurück zum grund Vortrag\n\n\n'
              'Geben Sie die Seitenzahl ein, wenn Sie sie kennen \n\n'
              'Um eine Bewertung zu schreiben,\n klicken Sie   /otzyv\n\n'
              'Der Bericht ist in drei Sprachen verfügbar     /de    /en   /rus\n\n'
              '/contacts   - unsere Kontakten\n\n'
              '<b>Viel Spaß beim Lesen!</b>'
              )

contacts = ('AgACAgIAAxkBAAIJsGaEhvzHk4FQoUAsZ01Lu4bD2t-5AAI26TEbzfEhSBF2IsJ0obusAQADAgADeAADNQQ',
            '<b>Свяжитесь с нами</b>\n\n'
            'Подписывайтесь на наши страницы в социальных сетях:\n\n'
            '<a href="https://www.facebook.com/facesofrussianresistance">Facebook</a>\n\n'
            '<a href="https://instagram.com/facesofrussianresistance">Instagram</a>\n\n'
            '<a href="https://twitter.com/facesresistance">Twitter</a>\n\n'
            '<a href="https://twitter.com/facesresistance">Телеграм</a>\n\n'
            'Вы можете связаться с нами одним из этих способов:\n\n'
            'Телеграм:  @ElenaFilina_mundep\n\n'
            'Почта:  faceofrr@gmail.com\n\n'
            '/continue     Вернуться к чтению',

            '<b>Comtact us</b>\n\n'
            'Follow us in SocialMedia\n\n'
            '<a href="https://www.facebook.com/facesofrussianresistance">Facebook</a>\n\n'
            '<a href="https://instagram.com/facesofrussianresistance">Instagram</a>\n\n'
            '<a href="https://twitter.com/facesresistance">Twitter</a>\n\n'
            '<a href="https://twitter.com/facesresistance">Телеграм</a>\n\n'
            'You can contact us in one of these ways:\n\n'
            'Telegram:  @ElenaFilina_mundep\n\n'
            'email:  faceofrr@gmail.com\n\n'
            '/continue      return to reading',

            '<b>Kontaktiren  uns</b>\n\n'
            'Folgen Sie uns auf Social Median\n\n'
            '<a href="https://www.facebook.com/facesofrussianresistance">Facebook</a>\n\n'
            '<a href="https://instagram.com/facesofrussianresistance">Instagram</a>\n\n'
            '<a href="https://twitter.com/facesresistance">Twitter</a>\n\n'
            '<a href="https://twitter.com/facesresistance">Телеграм</a>\n\n'
            'Sie können uns auf eine der folgenden Arten kontaktieren:\n\n'
            'Telegram:  @ElenaFilina_mundep\n\n'
            'email:  faceofrr@gmail.com\n\n'
            '/continue   weiterlesen'
            )

waiting_15 = ('', 'Вы сможете продолжить чтение через 15 минут',
              'You can reading on in 15 minut',
              'Sie können in 15 Minuten mit dem Lesen fortfahren')

just_waitng = ('', 'Подождтите пожалуйста, бот обрабатывает ваш отзыв ! '
                               'Это может занять какое-то время',
               'Waiting for some times, please. Bot is processing your feedback !',
               'Warten Sie bitte am bisschen !')

last_words_russian_only = ('', 'Последнее слово доступно только на русском языке, к сожалению\n\n'
                               'Для переключения языка в разделах help и contacts перейдите '
                               'к основному содержанию, потом выбирете язык',
                           'Only in Russian language available\n'
                           'Change language on pages help and contacts is impossible',
                           'Nur auf russische Sprache\n'
                           'Auswählen Sprache auf eiten help und contacts ist unmöglich')