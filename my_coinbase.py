from coinbase.wallet.client import Client

#Introducid vuestros valores en lugar de las XXXXXXXXXXX
api_key = 'XXXXXXXXXXXXXX'
api_secret = 'XXXXXXXXXXXXXXXXXXXXXXX'
client = Client(api_key, api_secret)

cambio_actual = client.get_spot_price(currency_pair = "BTC-EUR")
cambio_actual = cambio_actual["amount"]
posicion = cambio_actual.find(".")
cambio_actual = cambio_actual[0:(posicion + 3)]
print("EUR", cambio_actual, "el BIT")

mi_cartera = client.get_account("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(mi_cartera["native_balance"], "en la cartera")
