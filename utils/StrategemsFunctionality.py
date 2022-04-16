# Functionality file that allows Shinsha to
# provide random strategem from one of 6 categories
import random
import asyncio
from .IDnames import *
from .Parameters import *
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select


async def strategems(self, message):
    strategem_dict = {
        'Winning Strategems':
            ['Deceive the heavens to cross the sea',
             'Besiege Wei to rescue Zhao',
             'Kill with a borrowed knife',
             'Wait at leisure while the enemy labors',
             'Loot a burning house',
             'Make a sound in the east, then strike in the west',
             ],
        'Enemy Dealing Stratagems':
            ['Create something from nothing',
             'Openly repair the gallery roads, but sneak through the passage of Chencang',
             'Watch the fires burning across the river',
             'Hide a knife behind a smile',
             'Sacrifice the plum tree to preserve the peach tree',
             'Take the opportunity to pilfer a goat',
             ],
        'Offensive Stratagems':
            ['Stomp the grass to scare the snake',
             'Borrow a corpse to resurrect the soul',
             'Lure the tiger down the mountain',
             'In order to capture, one must let loose',
             'Tossing out a brick to get a jade gem',
             'Defeat the enemy by capturing their chief',
             ],
        'Melee Stratagems':
            ['Remove the firewood from under the pot',
             'Disturb the water and catch a fish',
             'Slough off the cicada golden shell',
             'Shut the door to catch the thief',
             'Befriend a distant state and strike a neighbouring one',
             'Obtain safe passage to conquer the State of Guo',
             ],
        'Combined Stratagems':
            ['Replace the beams with rotten timbers',
             'Point at the mulberry tree while cursing the locust tree',
             'Feign madness but keep your balance',
             'Remove the ladder when the enemy has ascended to the roof',
             'Decorate the tree with false blossoms',
             'Make the host and the guest exchange roles',
             ],
        'Defeat Stratagems':
            ['The beauty trap (Honeypot)',
             'The empty fort strategy',
             'Let the enemy own spy sow discord in the enemy camp',
             'Inflict injury on oneself to win the enemy trust',
             'Chain stratagems',
             'If all else fails, retreat',
             ],
    }

    if message.channel.id == bot_channel or message.guild:
        message = message
        key_list = list(strategem_dict.keys()[0])
        await message.channel.send('What strategem do you desire?', components=[
            Select(
                placeholder="Select something!",
                options=[
                    SelectOption(label=key_list[0], value=strategem_dict[key_list[random.randint(0,5)]]),
                    SelectOption(label=key_list[0], value=strategem_dict[key_list[random.randint(0,5)]]),
                    SelectOption(label=key_list[0], value=strategem_dict[key_list[random.randint(0,5)]]),
                    SelectOption(label=key_list[0], value=strategem_dict[key_list[random.randint(0,5)]]),
                    SelectOption(label=key_list[0], value=strategem_dict[key_list[random.randint(0,5)]]),
                    SelectOption(label=key_list[0], value=strategem_dict[key_list[random.randint(0,5)]]),
                ]
            )
        ])

        select_interaction = await self.wait_for("select_option")
        await select_interaction.send(content = f"{select_interaction.values[0]} selected!", ephemeral = False)