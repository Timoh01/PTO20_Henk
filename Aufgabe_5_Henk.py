# Wörterbuch mit Dictionaries
woerterbuch_deutsch = {"Apfel": "apple", "Birne": "pear", "Kirsche": "cherry"}
                   
woerterbuch_englisch = {"apple": "Apfel", "pear": "Birne", "cherry": "Kirsche"}
               
try:
    begriff = input("Begriff: ")
    print(woerterbuch_deutsch[begriff], "[en]")
except:
    try:
        print(woerterbuch_englisch[begriff], "[de]")
    except:
        print("Wort existiert nicht")