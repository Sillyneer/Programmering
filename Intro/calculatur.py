def addition(x ,y):
    return x + y 

def subtraction(x , y):
    return x - y 

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Det går inte att dela med 0")
        exit()

def multiplication(x,y):
    return x * y

print("calculator")

number_1 = input()   
try:
    number_1 = float(number_1)
except:
    print("Endast Nummer!")
    exit()


number_2 = input()
try:
    number_2 = float(number_2)
except:
    print("Endast Nummer!")
    exit()

print("What do you want to do?")
print("1. Additioln")
print("2. subtraction")
print("3. division")
print("4. multiplication")

choice = input()

if choice == "1":
    answer = addition (number_1, number_2)
    answer = round (answer ,2)
    print(answer)

elif choice == "2":
    answer = subtraction (number_1, number_2)
    answer = round (answer ,2)
    print(answer)

elif choice == "3":
    answer = division (number_1, number_2)
    answer = round (answer ,2)
    print(answer)


elif choice == "4":
    answer = multiplication (number_1, number_2)
    answer = round (answer ,2)
    print(answer)

