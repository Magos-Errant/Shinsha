class JeronimoMartins:
    def __init__(self):
        self.channels_info = {}
        self.banned_tags = ['yaoi', 'bara']

    def message_counter(self, channelID):
        if channelID in self.channels_info:
            self.channels_info[channelID].messages_count += 1
        else:
            pass

    def store_data(self):
        with open("saved_counter.txt", 'w') as file:
            _formattedString = ''
            for ID in self.channels_info:
                _formattedString += f'{ID} {self.channels_info[ID].messages_count}\n'
            file.write(_formattedString)
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
        "!arr tags": "Shinsha wyruszy w podróż po siedmiu morzach"
      }
      return avaliable_commands

    def __repr__(self):
        return f'channels_info={self.channels_info}'

    def __str__(self):
        return 'Klasa przechowująca informacje i metodę ich modyfikacji "message_counter"'

class ChannelData:
    def __init__(self, name, messages_count):
        self.name = name
        self.messages_count = messages_count


