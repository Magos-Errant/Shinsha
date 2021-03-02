# from pybooru import Danbooru
#
# banned_tags = ['animal_ears', 'blonde_hair']
# _tags = "yakumo_ran"
# danbo_client = Danbooru('danbooru')
# 
# def picture_generator(_tags):
#     while 1:
#         picture = danbo_client.post_list(tags=_tags, limit=1, random=True)
#         yield picture
#
# def picture_filter():
#     picture = picture_generator(_tags)
#     current_picture = next(picture)
#     x = 0
#     check_counter = 0
#     while x < len(banned_tags):
#         if banned_tags[x] in current_picture[0]['tag_string']:
#             x = 0
#             print('Found tag!')
#             check_counter += 1
#             print(f'On try: {check_counter}')
#             print(current_picture[0]['tag_string'])
#             current_picture = next(picture)
#
#         if banned_tags[x] not in current_picture[0]['tag_string']:
#             x += 1
#         if check_counter == 10:
#             await message.channel.send("Po 10 próbach gejoza dalej obecna, zmień tagi ( ͡° ͜ʖ ͡°)")
#             break
#         else:
#             return current_picture
#
# def send_picture(message):
#     _i = 20
#     while len(posts) == 0 and _i != 0:
#         await asyncio.sleep(1)
#         _i -= 1
#     if len(posts) == 0:
#         message = await message.channel.send('¯\_(ツ)_/¯')
#     else:
#         message = await message.channel.send(posts[0]['large_file_url'])





# import random as rnd
#
#
# class FiascoDiscord:
#     def __init__(self):
#         self.white_dice = []
#         self.black_dice = []
#         self.dices = [self.white_dice, self.black_dice]
#
#     def set_game(self, num_of_players: int):
#         for dice in self.dices:
#             for _w in range(0, num_of_players * 2):
#                 _w = rnd.randint(1, 6)
#                 dice.append(_w)
#
#         print(f"Białe kości: {'|'.join(map(str, self.white_dice))}")
#         print(f"Czarne kości: {'|'.join(map(str, self.black_dice))}")
#         return
#
#
#     def wprowadzenie(self):
#         return """
# - Wie pan, co to jest?
# - Co to jest?
# - Tłumik.
# - Nie bardzo rozumiem szanownego pana.
# - Czy zapakuje pan to wszystko już teraz czy mam do tego dokręcić rewolwer?
# - To oznacza, że… prawdopodobnie jest… napad?
# - Nie da się ukryć.
#
# Ah Fiasco! Od zadymioncyh barów Hollywood, po swojskiego Gruchę. Czarna komedia i kiepska kontrola impusów, to
# elementy definiujące posiacie w jakie wcielą się gracze Fiasco.
#         """
#
#     def setting_relationships(self):
#         return """
# Relacje (liczba oznacza wartość na kostce, którą trzeba zużyć):
# 1 Rodzina: 1 Rodzic/syn lub synowa; 2 Kuzyni; 3 Rodzeństwo; 4 Rodzic / dziecko lub pasierb; 5 Wujek / siostrzeniec lub ciocia / siostrzenica; 6 Niepowiązani, ale bliscy sobie jak bracia
# 2 Praca: 1 Pracownic rancha; 2 Górnicy; 3 Przełożony / pracownik; 4 Handlarz / klient; 5 Sprzedawca / klient; 6 Specjalista / klient
# 3 Przeszłość: 1 Kryminalista i detektyw; 2 Dorastali razem na wschodzie; 3 Po odsiadce; 4 Przeciwnicy na wojnie; 5 Oboje w związku małżeńskim z tym samym małżonkiem; 6 Złe relacje rodzinne
# 4 Romans: 1 Byli małżonkowie; 2 Obecni małżonkowie; 3 Niepohamowana żądza; 4 Przelotny romans; 5 Żona z zamówienia i jej mąż; 6 Byli kochankowie
# 5 Zbrodnia: 1 Szef mafii i lizus; 2 Hazardziści; 3 Złodzieje; 4 Uzdrawiający wiarą i pacjent; 5 Banici; 6 Sprzedawca / Uzależniony od Chińskiego opium
# 6 Społeczność: 1 Wysocy urzędnicy; 2 Klub społeczny; 3 Wolontariusze kościelni; 4 Firma / Obywatel; 5 Rząd / Obywatel; 6 Szeryf i zastępca
# """
#
#     def setting_needs(self):
#         return """
# Potrzeby (liczba oznacza wartość na kostce, którą trzeba zużyć):
# 1 Uwolnić się od: 1 tego miasta, zanim wszyscy się o tobie dowiedzą; 2 obowiązku rodzinnego; 3 zobowiązania biznesowego; 4 związku z kochankiem; 5 Twojego losu w życiu; 6 druzgocącego zadłużenia, którego termin wrótce upływa
# 2 Wyrównać rachunki: 1 z tym miastem i jego małostkowymi mieszkańcami; 2 z miejscowym szefem przestępczości; 3 z szeryfem; 4 z członkiem rodziny; 5 z Chińczykami; 6 z rywalem
# 3 Wzbogacić się: 1 przez okradanie dyliżansu; 2 poprzez okradanie firmy; 3 poprzez oszustwa i fraud; 4 poprzez kupowanie różnych urzędników; 5 przemocą; 6 przez zagubiony kufer pełen złota
# 4 Zdobyć szacunek: 1 tego miasta, niszcząc maszynę; 2 tego miasta, pokazując wszystkim, kto tu rządzi; 3 od swojego kochanka, wykazując się; 4 od szeryfa, donosząc na swoich przyjaciół; 5 członka rodziny, ratując go od ruiny; 6 od siebie, w końcu robiąc to
# 5 Wykręcić się: 1 od wyjących psów prawa; 2 z morderstwa; 3 z twardej zemsty; 4 od uczciwej kobiety, zrujnowanej; 5 wymyśleniem siebie na nowo; 6 wspaniałym oszustwem
# 6 Zaliczyć: 1 kogokolwiek i gdziekolwiek, aby uśmierzyć ból; 2 biletem z tego miasta; 3 ambitną i piękną dziewczynę z salonu; 4 aby udowodnić, że się mylili; 5 współmałżonka twojego przyjaciela; 6 aby nie umrzeć jako dziewica
# """
#
#     def setting_locations(self):
#         return """
# Lokacje (liczba oznacza wartość na kostce, którą trzeba zużyć):
# 1 Rezydencje : 1 Brudny wagon z podnośnikiem z poszarpaną markizą i beczkami zamiast ścian; 2 Schludny dom kupiony przez Sears, starannie pomalowany; 3 Stałe pomieszczenie w pensjonacie Belle-Union; 4 Krzykliwa rezydencja obok ziemi, przypominająca park; 5 Melina opium za pralnią White Star; 6 Brudne mieszkanie nad biurem z gazetami
# 2 Hotel Bradford: 1 Piwnica burzowa; 2 Pokój urzędnika, sejf i biuro przewozowe; 3 Burdelowy salon bilardowy; 4 Salon; 5 Bar "Dziewczynki"; 6 Apartament gubernatora
# 3 Dobra część miasta: 1 Bank; 2 Galanteria Sinclair'a; 3 Biuro prasowe i drukarnia Territorial Sentinel; 4 Pierwszy Kościół Chrystusa Odkupiciela; 5 Zajezdnia kolejowa i telegraf; 6 Salon Dentystyczny
# 4 Poprzez tory: 1 Braterski Zakon w sali loży Frontier; 2 chińskie pranie White Star; 3 Pensjonat Belle-Union; 4 Miejskie więzienie; 5 Sprzęt, uprząż i stajnia Eycka; 6 Boot Hill
# 5 W górach: 1 Obóz chiński; 2 Wiszące drzewo; 3 Droga wagonowa; 4 Gold Creek Shanty Town; 5 Ranczo Circle S.; 6 Sekretna jaskinia
# 6 Ziemie indian: 1 Wypalona chata z bali; 2 Kryjówka bandytów; 3 Obóz Hunkpatila Sioux; 4 Chata poszukiwacza; 5 Pilot rock; 6 Misja prezbiteriańska w Broken Arrow
# """
#
#     def setting_objects(self):
#         return """
# Obiekty (liczba oznacza wartość na kostce, którą trzeba zużyć):
# 1 Niespodziewane: 1 Żeton burdelu za trzy dolary „całą noc”; 2 Czarna torba przedsiębiorcy pogrzebowego i dzbanek kwasu fenolowego; 3 Wulkanizowana gumowa „welon łonowy”; 4 Szkielet Mescalero Apache; 5 Torba spirytualistów z magicznymi sztuczkami; 6 Narzędzia aborcjonisty
# 2 Transport: 1 Wagon kolejowy Kansas-Pacific; 2 Czterokonny powóz pocztowy; 3 Bezpieczny rower; 4 Wagon kolejowy; 5 Strzeżomy dyliżans; 6 Wagon kolejowy St. Louis i San Francisco
# 3 Broń: 1 Szczypce kowalskie; 2 Karabin Sharps z dźwignią; 3 Dopasowany zestaw rewolwerów Colt; 4 Pałka wojenna Siouxów; 5 Skrzynia starego dynamitu; 6 12-funtowa haubica górska
# 4 Informacja: 1 Notatka z testu dotycząca minerałów w glebie rancza Circle S.; 2 Podsłuchana rozmowa o strajku Gold Creek; 3 Dokumenty zwolnienia wyzwoleńca; 4 Pamiętnik pani; 5 Wyblakły list gończy; 6 Umowa z Agencją Detektywistyczną Pinkerton
# 5 Kosztowności: 1 Umowa dotycząca towarów suchych i handlowych firmy Sinclair; 2 Weksel na dwa tysiące dolarów ; 3 Zwitek federalnych znaczków pocztowych zawinięty w chustkę; 4 Klatka Napaeozapus insignis, skaczących myszy leśnych; 5 Ciężki worek złotego pyłu; 6 Kasa z burdelu hotelu Bradford
# 6 Sentymentalia: 1 Noworodek; 2 Ładny medalion z kosmykiem włosów w środku; 3 Malutki, olejny portret przystojnego żołnierza; 4 Poplamiony łzami list miłosny; 5 Srebrny kielich grawerowany; 6 Ostatnie słowa umierającego człowieka
# """
#
#
#
# game = FiascoDiscord()
# game.set_game(3)
