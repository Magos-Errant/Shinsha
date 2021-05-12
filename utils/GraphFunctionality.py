import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import datetime as dt
import asyncio
import discord
from .IDnames import *
from .Parameters import *


def GraphDataCollect(day_changed):
    day = dt.datetime.today().weekday()
    wdv = data_container.recall_week_data_vector()

    for ID in data_container.channels_info:
        if ID not in wdv:
            wdv[ID] = [0, 0, 0, 0, 0, 0, 0]
        elif day_changed:
            day = day - 1
            if day == -1:
                day = 6
            wdv[ID][day] = data_container.channels_info[ID].messages_count
        else:
            wdv[ID] = [data_container.channels_info[ID].messages_count if x == day else wdv[ID][x] for x in
                       range(0, 7)]
    data_container.store_week_data_vector(wdv)


async def GraphMaker(message, day_changed):
    GraphDataCollect(day_changed)
    weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
    wdv = data_container.recall_week_data_vector()
    markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x',
               'X', 'D', 'd', '|', '_']

    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 5), dpi=300)

    evenly_spaced_interval = np.linspace(0, 1, len(data_container.channels_info))
    colors = [cm.get_cmap('tab20')(x) for x in evenly_spaced_interval]

    x = np.arange(len(weekdays))
    bar_width = 0.05
    ax = fig.add_axes([0, 0, 1, 1])
    i = 0
    for ID in data_container.channels_info:

        ax.bar(x-(len(data_container.channels_info)*bar_width*0.5)+bar_width*i, wdv[ID],
                  label=data_container.channels_info[ID].name, color=colors[i], width=bar_width)

        # plt.plot(weekdays, wdv[ID], label=data_container.channels_info[ID].name, marker=markers[i],
        #          markerfacecolor='none', markersize=8, color=colors[i])
        i += 1

    plt.grid()
    plt.legend(title='Kanały:')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.tight_layout()
    plt.title('Aktywność kanałów')
    plt.xlabel('Dni tygodnia')
    ax.set_xticks(x)
    ax.set_xticklabels(weekdays)
    plt.ylabel('Liczba wiadomości')
    plt.gca().get_xticklabels()[dt.datetime.today().weekday()].set_color('red')
    plt.savefig('channelactivity.png', bbox_inches='tight', orientation='landscape', pad_inches=0.2)
    file = discord.File("channelactivity.png", filename="channelactivity.png")
    message = await message.channel.send("Requested graph", file=file)
    plt.clf()
    plt.close()
    os.remove("channelactivity.png")
    return message


async def GraphMessageHandler(message, day_changed=False):
    if message.channel.id == bot_channel or kucowanie_channel:
        await GraphMaker(message, day_changed)
    else:
        await message.delete()
        message = await GraphMaker(message, day_changed)
        await asyncio.sleep(message_timeout)
        await message.delete()
