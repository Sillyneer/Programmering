print("skriv en mening som innehåller ÅÄÖ")

sentence = input()

new_sentence =""

for letter in sentence: 
    if letter == "ö":
        new_sentence +="o"
    elif letter == "ä" or letter == "å":
        new_sentence += "a"
    else:
        new_sentence += letter

print(new_sentence)
