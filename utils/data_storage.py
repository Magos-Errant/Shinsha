class JeronimoMartins:
    def __init__(self):
        self.channels_info = {}
        self.banned_tags = ['yaoi', 'bara']

    def update_channels(self, text_channels):
        #tworzy listę aktualnych kanałów   
        for channel in text_channels:
            self.channels_info[channel.id] = [0, channel.name]
        #sprawdza czy zachowały się kanały o tym samym id, i dodaje info o wiadomościach
        with open('saved_counter.txt', 'r') as file:
            file = eval(file.read())
            for key in file:
                if key in self.channels_info:
                    self.channels_info[key] = [file[key][0], self.channels_info[key][1]]

    def message_counter(self, channelID):
        if channelID in self.channels_info:
            self.channels_info[channelID][0] += 1
        else:
            pass

    def store_data(self):
        with open("saved_counter.txt", 'w') as file:
            file.write(str(self.channels_info))
        return

    def recall_data(self):
        with open("saved_counter.txt", 'r') as file:
            self.channels_info = eval(file.read())
            print(self.channels_info)
        return

    @property
    def counter_status_single_string(self):
        _AnswerString = f''
        for channel in self.channels_info:
            _AnswerString = _AnswerString + f'{self.channels_info[channel][1]}: {self.channels_info[channel][0]}, '
        return _AnswerString
    
    @property
    def counter_status(self):
        _AnswerString = f'Dziś na kanałach wysłano:\n'
        for channel in self.channels_info:
            _AnswerString = _AnswerString + f'{self.channels_info[channel][1]}: {self.channels_info[channel][0]}\n'
        _AnswerString = _AnswerString + f'wiadomości.'

        return _AnswerString


    def clear_data(self):
        for channel in self.channels_info:
            self.channels_info[channel][0]=0
            self.store_data()

    @property
    def avaliable_commands(self) -> dict:
      avaliable_commands = {
        "!commands":"Shinsha wyświetli listę komend",
        "!hello":"Shinsha odpisze - Hello",
        "!message_count":"Shinsha wyświetli ilość wiadomości wysłanych na poszczególnych kanałach dzisiaj.",
        "!tao":"Shinsha podzieli się cytatem z Tao Te Ching",
        "!danbo tag1 tag2": "Shinsa wyświetli losowy obrazek z tymi tagami",
        "!arr tags": "Shinsha wyruszy w podróż po siedmiu morzach",
        "!UpdateChannels": "Shinsha zaktualizuje stan kanałów zachowując stan liczników"
      }
      return avaliable_commands

    def __repr__(self):
        return f'channels_info={self.channels_info}'

    def __str__(self):
        return 'Klasa przechowująca informacje i metodę ich modyfikacji "message_counter"'




