# Aufgabe 1:
# Schreiben sie ein Phyton-Programm, das:
# 1) den Benutzer Begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechtnet und ausgibt
# 5) die Differenz der beiden Zahlen berechnet und Ausgibt
# 6) das Produkt der beiden Zahlen berechnet und Ausgibt
# 7) den Quotient der beiden Zahlen berechnet und Ausgibt (inkl. Nachkommastellen)
"""
print("Ich wünsche Ihnen einen schönen Tag")

Zahl_1 = int(input("Eingabe der ersten Zahl:"))
Zahl_2 = int(input("Eingabe der zweiten Zahl:"))

Ergebnis = (Zahl_1 + Zahl_2)
    print("Ihr Ergebnis ist:", Ergebnis)

Ergebnis = Zahl_1 - Zahl_2
    print("Ihr Ergebnis ist:", Ergebnis)

Ergebnis = Zahl_1 * Zahl_2
    print("Ihr Ergebnis ist:", Ergebnis)

Ergebnis = Zahl_1 / Zahl_2
    print("Ihr Ergebnis ist:", Ergebnis)
"""
#---------------------------------------------------------------------------------------------------------------
#Aufgabe 2
# 8) die Differenz der kleineren Zahle von der größeren berechnet und Ausgibt
# 9) den Quotient kleinere Zahl durch die größere Zahl berechnen und ausgeben (inkl. Nachkommastellen)
"""
Zahl_1 = int(input("Eingabe der ersten Zahl:"))
Zahl_2 = int(input("Eingabe der zweiten Zahl:"))

if Zahl_1 > Zahl_2:
    Differenz = (Zahl_2 - Zahl_1)

elif Zahl_1 < Zahl_2:                   
    Differenz = (Zahl_1 - Zahl_2)
    print("Ihre Differenz ist:", Differenz)
else:
    print("bitte UNTERSCHIEDLICHE Zahlen eingeben")


if Zahl_1 > Zahl_2:
    Quotient = (Zahl_1 / Zahl_2)

elif Zahl_1 < Zahl_2:                   
    Quotient = (Zahl_2 / Zahl_1)
    print("Ihr Quotient ist:", Quotient)
else:
    print("bitte UNTERSCHIEDLICHE Zahlen eingeben")
"""
#---------------------------------------------------------------------------------------------------------------
#Aufgabe 3
# 10) Addieren Sie in einer Schleife die Zahlen 1 bis 100 und geben Sie das Ergebnis aus

summe = 0
counter = 0
while counter < 100:
    counter += 1
    print(counter)
    summe += counter
print("Summe:",summe)










