# Aufgabe 1_1 Pi - Berechnen mit Leibniz-Reihe

# Aufgabe 1_2 Eingabe zweier Zahlen, Vergleich, arithmetische Berechnungen

# Schreiben sie ein Phyton-Programm, das:
# 1) den Benutzer Begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechtnet und ausgibt
# 5) die Differenz der beiden Zahlen berechnet und Ausgibt
# 6) das Produkt der beiden Zahlen berechnet und Ausgibt
# 7) den Quotient der beiden Zahlen berechnet und Ausgibt (inkl. Nachkommastellen)
'''
print("Ich wünsche Ihnen einen schönen Tag")

Zahl_1 = int(input("Eingabe der ersten Zahl:"))
Zahl_2 = int(input("Eingabe der zweiten Zahl:"))

Addition = (Zahl_1 + Zahl_2)
print("Ihr Ergebnis ist:", Addition)
    
Subtraktion = (Zahl_1 - Zahl_2)
print("Ihr Ergebnis ist:" , Subtraktion)

Multiplikation = (Zahl_1 * Zahl_2)
print("Ihr Ergebnis ist:", Multiplikation)

Division = (Zahl_1 / Zahl_2)
print("Ihr Ergebnis ist:", Division)
'''

# 8) die Differenz der kleineren Zahle von der größeren berechnet und Ausgibt
# 9) den Quotient kleinere Zahl durch die größere Zahl berechnen und ausgeben (inkl. Nachkommastellen)
'''
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

'''
# Aufgabe 1_3 while - Schleife zur Summenbildung (Leibniz-Reihe)

iterations = int(input("Anzahl der Durchläufe angeben: "))
i = 0
counter = 0
while i < iterations:
    counter += (((-1)**i)/(2*i+1))
    i += 1
print(counter*4)






















