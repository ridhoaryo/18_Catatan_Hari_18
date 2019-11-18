import requests

print('What do you want to convert?')
print('1. USD => IDR')
print('2. IDR => USD')
print('3. USD => Bitcoin')
print('4. IDR => Bitcoin')
choose = int(input('Choose your currency convert (1/2/3/4): '))
if choose == 1:
    bank = input('Input bank name: ')
    usd = int(input('Input USD: '))
    url = f'https://kurs.web.id/api/v1/{bank}'
    data = requests.get(url)
    sell = data.json()['jual']
    buy = data.json()['beli']
    usd_to_idr = int(buy) * usd

    print(f'{usd} USD = Rp {usd_to_idr}\nDari bank{bank.upper()}\nDengan nilai konversi Jual{sell} dan Beli{buy}')
elif choose == 2:
    bank = input('Input bank name: ')
    idr = int(input('Input IDR: '))
    url = f'https://kurs.web.id/api/v1/{bank}'
    data = requests.get(url)
    sell = data.json()['jual']
    buy = data.json()['beli']
    idr_to_usd = round(idr/int(sell), 2)

    print(f'{idr} IDR = {idr_to_usd} USD \nDari bank{bank.upper()}\ndengan nilai konversi Jual {sell} dan Beli {buy}')
elif choose == 3:
    usd = int(input('Input USD: '))
    url = 'https://www.blockchain.com/ticker'
    data = requests.get(url)
    bitcoin_sell = data.json()['USD']['sell']
    bitcoin_buy = data.json()['USD']['buy']
    usd_to_btc = round(bitcoin_sell/usd,2)
    print(f'{usd} USD = {usd_to_btc} B \nDari {bank.upper()}\ndengan nilai konversi Jual {bitcoin_sell} dan Beli {bitcoin_buy}')
elif choose == 4:
    bank = input('Input bank name: ')
    idr = int(input('Input IDR: '))
    url1 = f'https://kurs.web.id/api/v1/{bank}'
    url2 = 'https://www.blockchain.com/ticker'
    data1 = requests.get(url1)
    data2 = requests.get(url2)
    usd_sell = data1.json()['jual']
    idr_to_usd = round(idr//int(usd_sell),2)
    if idr_to_usd < 1:
        print('You are too poor to buy Bitcoin')
    else:
        bitcoin_sell = data2.json()['USD']['sell']
        bitcoin_buy = data2.json()['USD']['buy']
        usd_to_btc = round(bitcoin_sell/idr_to_usd,2)
        print(f'Rp {idr} = {usd_to_btc} B \n melalui penukaran ke USD dahulu dari bank{bank.upper()}\ndengan nilai konversi Jual {bitcoin_sell} dan Beli {bitcoin_buy}')

else:
    print('Only provide USD/IDR/Bitcoin')
