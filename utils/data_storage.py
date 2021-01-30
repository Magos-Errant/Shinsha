class jeronimo_martins():
    def __init__(self):
        self.messages_in_channel = {
            'ogólny':0,
            'dnd':0,
            'memery':0,
            'nsfr':0,
            'vtube':0,
            'gacha-impact_asia':0,
            'kucowanie':0,
            'cyberbullying-2077':0
        }
    def message_counter(self, channel):
        if channel in self.messages_in_channel:
            self.messages_in_channel[channel] = self.messages_in_channel[channel]+1
        else:
            pass

    @property
    def counter_status(self):
        return f'''
        Dziś na kanałach wysłano:
        ogólny: {self.messages_in_channel['ogólny']}
        dnd: {self.messages_in_channel['dnd']}   
        memery: {self.messages_in_channel['memery']}
        nsfr: {self.messages_in_channel['nsfr']}
        vtube: {self.messages_in_channel['vtube']}
        gacha-impact_asia: {self.messages_in_channel['gacha-impact_asia']}
        kucowanie: {self.messages_in_channel['kucowanie']}
        cyberbullying-2077: {self.messages_in_channel['cyberbullying-2077']}
        
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
        "!message_count":"Shinsha wyświetli ilość wiadomości wysłanych na poszczególnych kanałach dzisiaj."
      }
      return avaliable_commands

    def __repr__(self):
        return f'messages_in_channel={self.messages_in_channel}'

    def __str__(self):
        return 'Klasa przechowująca informacje i metodę ich modyfikacji "message_counter"'




