from wallet import Wallet


jims_wallet = Wallet('Brown', False)
carols_wallet = Wallet('Red', True)

print(jims_wallet.color)
print(jims_wallet.cash)

jims_wallet.put_cash_in_wallet(100)
print(jims_wallet.cash)

print(carols_wallet.color)