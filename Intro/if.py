print("hur gammal är du?")

age = input()
age = int(age)

if age < 18: 
    print("du är ett barn.")

elif age == 18:
    print("du är 18")

elif age >= 18 and age < 50:
    print("du är gammal.")

elif age >= 50:
    print("du är snart död.")

elif age !=72:
    print("aaaaaaaaaa")

else:
    print("Jag vet inte.")