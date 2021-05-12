import datetime as dt

class JeronimoMartins:
    def __init__(self):
        self.channels_info = {}
        self.banned_tags = ['yaoi', 'bara']
        self.UserCustomMentions = {}
        self.humour = []
        #flags
        self.already_written_flag = False

    def message_counter(self, channelID):
        if channelID in self.channels_info:
            self.channels_info[channelID].messages_count += 1
        else:
            pass

    def store_data(self):
        #channel data
        with open("saved_counter.txt", 'w') as file:
            _formattedString = ''
            for ID in self.channels_info:
                _formattedString += f'{ID} {self.channels_info[ID].messages_count}\n'
            file.write(_formattedString)

        #user mentions
        with open("custom_mentions.txt", 'w') as file:
            formatted_string = ''
            for ID in self.UserCustomMentions:
                temporary_string = ''
                for item in self.UserCustomMentions[ID]:
                    temporary_string += f' {item}'
                formatted_string += f'{ID}{temporary_string}\n'
            file.write(formatted_string)

        #humorous sentences
        with open("humorous_messages.txt", 'w') as file:
            formatted_string = ''
            for sentence in self.humour:
                formatted_string += sentence+'\n'
            file.write(formatted_string)
        return


    def recall_data(self, text_channels):
        # tworzy listę aktualnych kanałów
        for channel in text_channels:
            self.channels_info[channel.id] = ChannelData(channel.name, 0)
        # sprawdza czy zachowały się kanały o tym samym id, i dodaje info o wiadomościach
        with open('saved_counter.txt', 'r') as file:
            file = file.readlines()
        for line in file:
            stripped_line = line.rstrip().split(' ')
            ID = int(stripped_line[0])
            if ID in self.channels_info:
                self.channels_info[ID] = ChannelData(self.channels_info[ID].name, int(stripped_line[1]))

        #load stored user mentions
        with open("custom_mentions.txt", 'r') as file:
            file = file.readlines()
        for line in file:
            splitted = line.split()
            ID = int(splitted[0])
            slowa = set(word for word in splitted[1:])
            self.UserCustomMentions[ID] = slowa

        # load humour
        with open("humorous_messages.txt", 'r') as file:
            file = file.readlines()
        for line in file:
            self.humour.append(line)
        return


    @property
    def counter_status_single_string(self):
        _AnswerString = f''
        for ID in self.channels_info:
            _AnswerString = _AnswerString + f'{self.channels_info[ID].name}: {self.channels_info[ID].messages_count}, '
        return _AnswerString
    
    @property
    def counter_status(self):
        _AnswerString = f'Dziś na kanałach wysłano:\n'
        for ID in self.channels_info:
            _AnswerString = _AnswerString + f'{self.channels_info[ID].name}: {self.channels_info[ID].messages_count}\n'
        _AnswerString = _AnswerString + f'wiadomości.'

        return _AnswerString

    def clear_data(self):
        for ID in self.channels_info:
            self.channels_info[ID].messages_count = 0
        self.store_data()

    @property
    def avaliable_commands(self) -> dict:
      avaliable_commands = {
        "!help":"Shinsha wyświetli listę komend",
        "!hello":"Shinsha odpisze - Hello",
        "!message_count":"Shinsha wyświetli ilość wiadomości wysłanych na poszczególnych kanałach dzisiaj.",
        "!tao":"Shinsha podzieli się cytatem z Tao Te Ching",
        "!danbo tag1 tag2": "Shinsha wyświetli losowy obrazek z tymi tagami",
        "!danbo_count tag1 tag2": "Shinsha poda liczbę postów na danbooru zawierających podane tagi",
        "!arr tags": "Shinsha wyruszy w podróż po siedmiu morzach",
        "!graph": "Shinsha wyśle graficzne podsumowanie aktywności kanałów",
        "!add_mentions słowa": "Shinsha zapisze słowa i poinformuje Cię jeśli zostaną użyte (limit 10)",
        "!my_mentions": "Shinsha powie Ci jakie wzmianki masz zapisane",
        "!delete_mentions słowa": "Shinsha usunie wybrane wzmianki",
        "!add_humour text": "Shinsha zapamieta twój tekst na później (limit znaków 500)"
      }
      return avaliable_commands

    def store_week_data_vector(self, wdv):
        with open("wdv.txt", 'w') as file:
            _formattedString = ''

            for ID in wdv:
                vec = ''
                for item in wdv[ID]:
                    vec += f' {item}'
                _formattedString += f'{ID} {vec}\n'

            if dt.datetime.today().weekday() == 0 and self.already_written_flag is False:
                with open("wdv.txt", 'w') as file:
                    _formattedString = ''

                    for ID in wdv:
                        vec = ''
                        for item in wdv[ID]:
                            vec += f' {item}'
                        _formattedString += f'{ID} {vec}\n'
                    file.write(_formattedString)

                with open("wdv_archive.txt", 'a') as file:
                    _formattedString = ''

                    for ID in wdv:
                        vec = ''
                        for item in wdv[ID]:
                            vec += f' {item}'
                        _formattedString += f'{ID} {vec}\n'
                    _formattedString += f'new_week {dt.date.today()}\n'
                    file.write(_formattedString)

                self.already_written_flag = True
                return

            elif dt.datetime.today().weekday() != 0 and self.already_written_flag is True:
                self.already_written_flag = False

            file.write(_formattedString)
        return

    def recall_week_data_vector(self):
        wdv = {}
        with open("wdv.txt", 'r') as file:
            file = file.readlines()
        for line in file:
            splitted = line.split()
            ID = int(splitted[0])
            staty_dni = [int(x) for x in splitted[1:8]]
            wdv[ID] = staty_dni
        return wdv

    def __repr__(self):
        return f'channels_info={self.channels_info}'

    def __str__(self):
        return 'Klasa przechowująca informacje i metodę ich modyfikacji "message_counter"'

class ChannelData:
    def __init__(self, name, messages_count):
        self.name = name
        self.messages_count = messages_count


