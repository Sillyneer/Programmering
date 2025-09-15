print("Tjenare välkommen till min kiosk.")
print("Vi har:")
print("Glass för 20kr")
print("Varmkorv för 15kr")
print("Läsk för 15kr")
print("Godis för 10kr")

print("Vad skulle du vilja köpa?")

product = input()

icecream_price = 20
hotdog_price = 15
soda_price = 15
candy_price = 10 

if product == "glass":
    print("Hur många glassar vill du ha")
    amount = input()
    amount = int(amount)

    print("Det blir", amount * icecream_price,"kr")

elif product == "varmkorv":
    print("Hur många varmkorvar vill du ha")
    amount = input()
    amount = int(amount)

    print("Det blir", amount * hotdog_price,"kr")

elif product == "läsk":
    print("Hur mycket läsk vill du ha")
    amount = input()
    amount = int(amount)

    print("Det blir", amount * soda_price,"kr")

elif product == "godis":
    print("Hur mycket hg godis vill du ha")
    amount = input()
    amount = int(amount)

    print("Det blir", amount * candy_price,"kr")