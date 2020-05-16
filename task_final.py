'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

ODDELOVAC = '='*33
privitani = "Vitejte v programu Analyza textu!"
reg_uzivatele = {'bob': 123, 'ann': 'pass123', 'mike': 'password123', 'lizz': 'pass123'}

print(ODDELOVAC)
print(privitani)
print(ODDELOVAC)

uzivatel = input("Prihlaste se prosim!\nVase uzivatelske jmeno: ")
heslo = input("Vase heslo: ")

#PRIHLASENI UZIVATELE
if uzivatel in reg_uzivatele:
    print("Prihlaseni probehlo uspesne. Vitejte zpatky!")
    print(ODDELOVAC)
else:
    print("Neplatne prihlaseni, ukoncuji.")
    exit()

#VYBER TEXTU
vyber_uzivatele = int(input("Vyberte si prosim text cislo 1,2 nebo 3: "))

vyber_uzivatele -= 1
print(ODDELOVAC)
print(TEXTS[vyber_uzivatele])

#OCISTENI TEXTU
bez_carek = TEXTS[vyber_uzivatele].strip(',')
bez_tecek = bez_carek.strip('.')
rozdeleno = bez_tecek.split()

#ANALYZA
zac_velke = 0
velke = 0
male = 0
cisla = 0
for word in rozdeleno:
    if word[0].isupper() == True:
        zac_velke += 1
    elif word.isupper()== True:
        velke += 1
    elif word.islower() == True:
        male += 1
    elif word.isnumeric() == True:
        cisla += 1

print(ODDELOVAC)
print("Celkovy pocet slov v textu je ", len(rozdeleno))
print("Celkovy pocet slov zacinajici velkym pismenem je ", zac_velke)
print("Celkovy pocet slov napsan velkymi pismeny je ", velke)
print("Celkovy pocet slov napsan malymi pismeny je ", male)
print("Celkovy pocet cisel, ktere se nachazeji v textu je", cisla)
print(ODDELOVAC)

#GRAF
cetnost = {}
for slovo in rozdeleno:
    if len(slovo) not in cetnost:
        cetnost[len(slovo)] = 0
    cetnost[len(slovo)] += 1

for key, value in sorted(cetnost.items()):
    print(key, int(value) * '*', value)

#SOUCET CISEL
soucet_cisel = 0
for soucet in rozdeleno:
    if soucet.isnumeric() == True:
        soucet_cisel += int(soucet)
print(ODDELOVAC)
print("Soucet vsech cisel v textu dohromady dava", soucet_cisel)
print(ODDELOVAC)


