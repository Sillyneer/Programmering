print("hur gammal är du?")

age = input()
age = int(age)

if age <=6:
    print("din biljett kostar 21kr ")

elif age >= 7 and age <= 19:
    print("din biljett kostar 21kr")

elif age >= 20 and age <= 64:
    print("din biljett kostar 32kr")

elif age >= 65:
    print("din biljett kostar 21kr")