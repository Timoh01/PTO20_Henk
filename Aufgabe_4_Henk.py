wörterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
wörterbuch_englisch =["apple", "pear", "cherry", "melon", "apricot", "peach"]

#Erweitern sie das Wörterbuch um die Möglichkeit, Einträge zu ergänzen, bzw. zu löschen

max = len(wörterbuch_deutsch)


running = True
while running:
    auswahl = input("Befehl? \n[E]infügen: \n[L]öschen: \n[A]bfragen:")
    auswahl =  auswahl.upper()
    if auswahl == 'E' or auswahl == 'e':
        Wort_d = input("Bitte geben Sie das Wort ein:")      
        wörterbuch_deutsch.append(Wort_d)
        Wort_e = input("Please type in your word:")
        wörterbuch_englisch.append(Wort_e)
        print(wörterbuch_deutsch)
        print(wörterbuch_englisch)
    
    elif auswahl == 'L' or auswahl == 'l':
        Wort_de = input("Welches Wort soll gelöscht werden? :")      
        wörterbuch_deutsch.remove(Wort_de)
        Wort_en = input("Please type in your word:")
        wörterbuch_englisch.remove(Wort_en)
        print( wörterbuch_deutsch)
        print(wörterbuch_englisch)
    
    else:
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    