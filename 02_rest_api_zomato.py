# api_keys: b567fe1dac64fd218ff1f82befc5f272

import requests

host = 'https://developers.zomato.com/api/v2.1'
category = '/categories'
keys = 'b567fe1dac64fd218ff1f82befc5f272'
head_info = {
    'user-key':keys
}
url = host+category
data = requests.get(url, headers=head_info)
print(data.json()['categories'])