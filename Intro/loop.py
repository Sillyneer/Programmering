

sentance =" hej på dig! "
"""""
for letter in sentance:
    print(letter)
"""""

for i in range(1, 11):
    

    if i == 5:
        continue

    print(i)

gambling = True 

while gambling:
    print("$$$")

    if input() == "stop":
        break



while True:
    print (" mata in ett nummer ")

    number_1 = input()

    try:
        number_1 = int(number_1)
        break
    except:
        print ("försök igen")


word_1 ="hassan"

if "a" in word_1:
    print("Ja, a finns")

else:
    print( "nej, det finns inte")