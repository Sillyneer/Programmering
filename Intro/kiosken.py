print("tjenare välkommen till min kiosk.")
print("vi har:")
print("glass för 20kr")
print("varmkorv för 15kr")
print("läsk för 15kr")
print("godis för 10kr")

print("vad skulle du vilja köpa?")

product = input()

icecream_price = 20
hotdog_price = 15
soda_price = 15
candy_price = 10 

if product == "glass":
    print("hur många glassar vill du ha")
    amount = input()
    amount = int(amount)

    print("det blir", amount * icecream_price,"kr")

elif product == "varmkorv":
    print("hur många varmkorvar vill du ha")
    amount = input()
    amount = int(amount)

    print("det blir", amount * hotdog_price,"kr")

elif product == "läsk":
    print("hur mycket läsk vill du ha")
    amount = input()
    amount = int(amount)

    print("det blir", amount * soda_price,"kr")

elif product == "godis":
    print("hur mycket hg godis vill du ha")
    amount = input()
    amount = int(amount)

    print("det blir", amount * candy_price,"kr")




