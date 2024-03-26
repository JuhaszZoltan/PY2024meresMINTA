from random import shuffle

# --- 1. feladat ---------------
def feladat01() -> None:
    nev:str = input('írja be a nevét: ')
    ev:int = int(input('írja be a születési évét: '))
    spc:str = ['#', '&', '@', '!', '%']
    shuffle(spc)
    print(f'generált jelszó: {nev[:4].capitalize()}{ev%100}{spc[0]}{spc[1]}')


# --- 2. feladat ---------------
def feladat02() -> None:
    meret:int = 0
    while meret < 5 or meret > 15:
        meret = int(input('írjon be egy [5, 15] közötti egész számot: '))
    hely:int = int(input(f'írjon be egy [0, {meret}) közötti indexet: '))
    if hely < 0 or hely >= meret:
        print('hibás input!')
        return
    abc:str = 'abcdefghijklmno'
    for i in range(meret):
        if i != hely: print(abc[i], end=' ')
        else: print('#', end=' ')
    valasz:str = input('\nmelyik betű lehet a "#" helyén?: ')
    if valasz == abc[hely]: print('így van!')
    else: print(f'nem, a helyes válasz: {abc[hely]}')

# --- 3. feladat ---------------
class Dijazott:
    def __init__(self, s:str) -> None:
        v:list[str] = s.strip().split(';')
        self.ev:str = v[0]
        self.nev:str = v[1]
        self.orszag:str = v[2]

def feladat03() -> None:
    dijazottak:list[Dijazott] = []
    file = open('dijazottak.txt', 'r', encoding='utf8')
    for s in file: dijazottak.append(Dijazott(s))
    print(f'3.1: az állomány {len(dijazottak)} díjazottat tartalmaz')
    sved_db:int = 0
    for d in dijazottak:
        if d.orszag == 'Svédország': sved_db += 1
    print(f'3.2: összesen {sved_db} alkalommal volt svéd díjazott')
    orszag_ker:str = input(f'3.3: adja meg egy ország nevét: ')
    evek:list[str] = []
    for d in dijazottak:
        if d.orszag == orszag_ker: evek.append(d.ev)
    if len(evek) == 0: print('\tnem volt ebből az országból irodalmi Nobel-díjas!')
    else:
        print('\ta következő években volt díjazott:\n', end='\t')
        for ev in evek: print(ev, end= ' ')
    max_index:int = 0
    for i in range(1, len(dijazottak)):
        if len(dijazottak[i].nev) > len(dijazottak[max_index].nev):
            max_index = i
    print(f'\n3.4: a leghosszabb nevű díjazott:\n\t{dijazottak[max_index].nev}')
