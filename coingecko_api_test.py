from pycoingecko import CoinGeckoAPI
from requests import adapters
cg = CoinGeckoAPI()

coinlist = cg.get_coins_list()
# print(len(coinlist))
coin_symbol = 'bifi'
for i in coinlist:
    if i['symbol'] == coin_symbol:
        coin_info = i
        print(coin_info)
contract_address = cg.get_coin_by_id(coin_info['id'])
# contract_address_eth = contract_address["platforms"]['ethereum']
contract_address_bsc = contract_address
coin_price = contract_address["market_data"]["current_price"]["usd"]
print(contract_address_bsc)
# print(contract_address.keys())
# print(contract_address)
# for key in contract_address.keys():
#     print(contract_address[key])

# seen = {}
# dupes = []

# for x in coinlist:
#     if x['symbol'] not in seen:
#         seen[x['symbol']] = 1
#     else:
#         if seen[x['symbol']] == 1:
#             dupes.append(x)
#         seen[x['symbol']] += 1
# print('\nlist of duplicated ids')
# for i in dupes:
#     print(i['symbol'],  end='', '')
# print()