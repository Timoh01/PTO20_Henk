wörterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
wörterbuch_englisch =["apple", "pear", "cherry", "melon", "apricot", "peach"]

max = len(wörterbuch_deutsch)

eingabe = input("Begriff:")

index = 0

while index < max:
    if wörterbuch_deutsch[index].lower() == eingabe.lower():
        print(wörterbuch_englisch[index], "[en]")
        break
    index +=1
    
if index == max:
    index = 0
    while index < max:
        if wörterbuch_englisch[index].lower() == eingabe.lower():
            print(wörterbuch_deutsch[index], "[de]")
            break
        index +=1

if index == max:
    print("Wort nicht gefunden!")
    
    



























