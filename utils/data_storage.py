class jeronimo_martins():
    def __init__(self):
        self.messages_in_channel = {
            602620718441693303: 0,
            719290056031862817: 0,
            726218082066104350: 0,
            748478326934470678: 0,
            755492710797934602: 0,
            762589721120997386: 0,
            790949987609608212: 0,
            789418296591384576: 0
        }

    def message_counter(self, channelID):
        if channelID in self.messages_in_channel:
            self.messages_in_channel[channelID] = self.messages_in_channel[channelID] + 1
        else:
            pass

    @property
    def store_data(self):
        with open("saved_counter.txt", 'w') as self.file:
            self.file.write(str(self.messages_in_channel))

    @property
    def recall_data(self):
        with open("saved_counter.txt", 'r') as self.file:
            self.messages_in_channel = eval(self.file.read())

    @property
    def counter_status(self):
        return f'''
        Dziś na kanałach wysłano:
        ogólny: {self.messages_in_channel[602620718441693303]}
        dnd: {self.messages_in_channel[719290056031862817]}   
        memery: {self.messages_in_channel[726218082066104350]}
        nsfr: {self.messages_in_channel[748478326934470678]}
        vtube: {self.messages_in_channel[755492710797934602]}
        gacha-impact_asia: {self.messages_in_channel[762589721120997386]}
        kucowanie: {self.messages_in_channel[790949987609608212]}
        cyberbullying-2077: {self.messages_in_channel[789418296591384576]}
        
        wiadomości.
        '''

    def clear_data(self):
        for channel in self.messages_in_channel:
            self.messages_in_channel[channel]=0

    @property
    def avaliable_commands(self) -> dict:
      avaliable_commands = {
        "!commands":"Shinsha wyświetli listę komend",
        "!hello":"Shinsha odpisze - Hello",
        "!message_count":"Shinsha wyświetli ilość wiadomości wysłanych na poszczególnych kanałach dzisiaj.",
        "!tao":"Shinsha podzieli się cytatem z Tao Te Ching",
        "!danbo tag1 tag2": "Shinsa wyświetli losowy obrazek z tymi tagami",
        "!arr tags": "Shinsha wyruszy w podróż po siedmiu morzach"
      }
      return avaliable_commands

    def __repr__(self):
        return f'messages_in_channel={self.messages_in_channel}'

    def __str__(self):
        return 'Klasa przechowująca informacje i metodę ich modyfikacji "message_counter"'




