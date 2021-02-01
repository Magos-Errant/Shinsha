import NyaaPy

Arr = NyaaPy.Nyaa

x = Arr.search('tatoeba last dungeon 05')
print(x)

_selected_animu = []
for _dict in x:
    if _dict['category'] == 'Anime - English-translated':
        _selected_animu.append(_dict)
    else:
        continue

i = 0
for _dicts in _selected_animu:
    print(f"Name: {x[i]['name']}\nYer booty isle: {x[i]['url']}\nCoffer!: {x[i]['download_url']}\nMayteys: {x[i]['seeders']}\nScallywags: {x[i]['leechers']}\nHeave Ho: {x[i]['size']}\n\n")
    i += 1