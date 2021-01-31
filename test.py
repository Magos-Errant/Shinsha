from __future__ import unicode_literals
from pybooru import Danbooru
import random

tags = "!danbo: asanagi breasts"
tags = tags[8:]
print(tags)

client = Danbooru('danbooru')
posts = client.post_list(tags=f'{tags}', limit=100)
random_pool = {}
i = 0
for post in posts:
    random_pool[i] = post['file_url']
    i += 1

print(random_pool[int(random.randint(0, 99))])
