import requests
import xlsxwriter

city = input('Input City: ')
url_city = f'https://developers.zomato.com/api/v2.1/cities?q={city}'
keys = 'b567fe1dac64fd218ff1f82befc5f272'
head_info = {
    'user-key':keys
}
data_city = requests.get(url_city, headers=head_info)
city_id = data_city.json()['location_suggestions'][0]['id']

food = input('What do you want to eat?: ')
url_food = f'https://developers.zomato.com/api/v2.1/search?entity_id={city_id}&entity_type=city&q={food}'
data_food = requests.get(url_food, headers=head_info)

food_list = [['No', 'Restaurant_Name', 'Restaurant_Address', 'Cuisines', 'Rating']]
result_found = data_food.json()['results_shown']
for i in range(result_found):
    rest_list = []
    rest_list.append(i+1)
    rest_list.append(data_food.json()['restaurants'][i]['restaurant']['name'])
    rest_list.append(data_food.json()['restaurants'][i]['restaurant']['location']['address'])
    rest_list.append(data_food.json()['restaurants'][i]['restaurant']['cuisines'])
    rest_list.append(data_food.json()['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
    food_list.append(rest_list)

data_xlsx = xlsxwriter.Workbook(f'{food}_at_{city}.xlsx')
sheet1 = data_xlsx.add_worksheet(f'list of {food}')
for r in range(len(food_list)):
    for c in range(len(food_list[0])):
        sheet1.write(r,c,food_list[r][c])

data_xlsx.close()