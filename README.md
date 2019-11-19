# Quiz Rest API: Get restaurant data for certain food from zomato.com API and save it into .xlsx

Halo, Assalamu'alaykum..
Hari ini saya akan share tentang quiz dari kelas tadi siang di Purwadhika. Judul quiznya seperti di atas. Kita diminta untuk mengakses API dari Zomato.com, dan mencari makanan berdasarkan kota yang kita inginkan. Kemudian kita ambil beberapa data (di sini saya mengambil nama restoran, alamat, sajian dan rating) lalu menyimpannya ke dalam bentuk .xlsx.

File coding bisa diakses di:
- **03_rest_api_search_food.py**

Untuk hasil xlsx ada di:
- **soto_at_jakarta.xlsx**

## Let's breakdown the code
## 1. Import Library
```
import requests
import xlsxwriter
```
Import dulu library yang dibutuhkan.

## 2. Get City ID
```
city = input('Input City: ')
url_city = f'https://developers.zomato.com/api/v2.1/cities?q={city}'
keys = 'b567fe1dac64fd218ff1f82befc5f272'
head_info = {
    'user-key':keys
}
data_city = requests.get(url_city, headers=head_info)
city_id = data_city.json()['location_suggestions'][0]['id']
```
Di zomato kita tidak dapat mengakses API tanpa menggunakan API keys. Oleh karena itu, simpan API Keys dalam variable. Selain itu, untuk bisa mengetahui daftar makanan di suatu kota, tidak semudah menginput kota lalu makanan apa yang dicari. Kita perlu mencari ID kota terlebih dahulu. Maka, minta user untuk menginput nama kota, kemudian kita cari ID nya dengan menggunakan format link API Zomato untuk mencari ID kota

## 3. Combine City ID with Food
```
food = input('What do you want to eat?: ')
url_food = f'https://developers.zomato.com/api/v2.1/search?entity_id={city_id}&entity_type=city&q={food}'
data_food = requests.get(url_food, headers=head_info)

food_list = [['No', 'Restaurant_Name', 'Restaurant_Address', 'Cuisines', 'Rating']]
result_found = data_food.json()['results_shown']
```
Setelah mendapatkan ID kotanya, kita masukkan ID kota tersebut dalam format link untuk mencari daftar makanan.
Di sini saya juga membuat list dalam list dengan index pertama berisi 5 nama kolom(No, Restaurant_Name, Restaurant_Address, Cuisines, Rating), saya namakan listnya `food_list`. Ini adalah langkah awal untuk mengubah data menjadi xlsx.
Lalu saya juga membuat variable `result_found` untuk menyimpan berapa data yang didapat dari API tersebut.

## 4. Input data into list
```
for i in range(result_found):
    rest_list = []
    rest_list.append(i+1)
    rest_list.append(data_food.json()['restaurants'][i]['restaurant']['name'])
    rest_list.append(data_food.json()['restaurants'][i]['restaurant']['location']['address'])
    rest_list.append(data_food.json()['restaurants'][i]['restaurant']['cuisines'])
    rest_list.append(data_food.json()['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
    food_list.append(rest_list)
```
Masukkan data satu per satu ke dalam list.

## 5. Write to xlsx file
```
data_xlsx = xlsxwriter.Workbook(f'{food}_at_{city}.xlsx')
sheet1 = data_xlsx.add_worksheet(f'list of {food}')
for r in range(len(food_list)):
    for c in range(len(food_list[0])):
        sheet1.write(r,c,food_list[r][c])
```
Di sini saya mendeklarasikan nama filenya berdasarkan nama makanan dan kota. Kemudian saya tulis satu per satu ke dalam setial cell dengan menggunakan double for loops.

## 6. Don't forget to save
```
data_xlsx.close()
```
Lalu simpan file tadi dengan menggunakan method .`close()`

Sekian untuk project kecil-kecilan hari ini, terimakasih dan semoga bermanfaat.
