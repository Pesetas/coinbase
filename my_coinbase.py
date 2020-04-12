from coinbase.wallet.client import Client

#Introducid vuestros valores en lugar de las XXXXXXXXXXX
api_key = 'XXXXXXXXXXXXXX'
api_secret = 'XXXXXXXXXXXXXXXXXXXXXXX'
cuenta = 'XXXXXXXXXXXXXXXXXXXXX'
client = Client(api_key, api_secret)

def cambio_actual():
  cambio_actual = client.get_spot_price(currency_pair = "BTC-EUR")["amount"]
  cambio_actual = cambio_actual[0:(cambio_actual.find(".") + 3)]
  return "EUR" + cambio_actual

def mi_cartera():
  mi_cartera = client.get_account(cuenta)
  return mi_cartera["native_balance"]
