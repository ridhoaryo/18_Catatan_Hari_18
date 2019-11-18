# rest api sportsdb, daftar pemain suatu klub
# input: klub apa misal: real madrid
# daftar pemain: nama, posisi, usia, negara
# save menjadi real madrid.xlsx, real madrid.json, real madrid.csv

import requests
import datetime as dt
import xlsxwriter
import json
import csv

team = input('Insert team name: ')
url_footbal = f'http://www.thesportsdb.com/api/v1/json/1/searchplayerszzz.php?t={team}'
data = requests.get(url_footbal)
players = data.json()['player']

# print(data.status_code)

header = ['player_name', 'position', 'age', 'nationality']
all_players = []

for player in players:
    player_data = []
    player_data.append(player['strPlayer'])
    player_data.append(player['strPosition'])
    player_data.append(2019 - int(player['dateBorn'][:4]))
    # date = dt.datetime.strptime(date_born, '%Y-%m-%d')
    # player_data.append(date.date())
    player_data.append(player['strNationality'])
    all_players.append(player_data)

# print(all_players)
all_player_json = []
for i in range(len(all_players)):
    x = dict(zip(header, all_players[i]))
    all_player_json.append(x)

# print(all_player_json)
with open(f'{team}.json', 'w') as player_data:
    json.dump(all_player_json, player_data)

with open(f'{team}.csv', 'w', newline='') as csv_player:
    column = header
    y = csv.DictWriter(csv_player, fieldnames = column)
    y.writeheader()
    y.writerows(all_player_json[1:])

union_data = []
union_data.append(header)
for data in all_players:
    union_data.append(data)
print(union_data)
data_xlsx = xlsxwriter.Workbook(f'{team}.xlsx')
sheet1 = data_xlsx.add_worksheet(f"{team}'s squad")
for i in range(len(union_data)):
    for j in range(len(header)):
        sheet1.write(i,j,union_data[i][j])

data_xlsx.close()
