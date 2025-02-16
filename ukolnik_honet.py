vsechny_ukoly=[]
popisy_ukolu={}

def odstranit_ukol(vsechny_ukoly,popisy_ukolu):
   
    if not vsechny_ukoly:
        print("Nemáte žádné úkoly!")
        menu(vsechny_ukoly, popisy_ukolu, show_intro=True)
        return
    else:
        print("\nSeznam úkolů:")
        for index, ukol in enumerate(vsechny_ukoly):
            print(f"{index+1}. {ukol} - {popisy_ukolu.get(ukol,{index+1})}")
    while True:
        try:
            cislo_ukolu=int(input("\nZadejte číslo úkolu, který chcete odstranit:"))
            if 0 < cislo_ukolu <= len(vsechny_ukoly):
                break
            else:
                print("Úkol nenalezen. Zadejte platné číslo!")
        except ValueError:
            print("Prosím, zadejte číslo!")
    del popisy_ukolu[vsechny_ukoly[cislo_ukolu-1]]

    popis_ukolu=vsechny_ukoly[cislo_ukolu-1]
    vsechny_ukoly.pop(cislo_ukolu-1)
   
    print(f"Úkol {popis_ukolu} byl odstraněn.")
    menu(vsechny_ukoly, popisy_ukolu, show_intro=True)


def zobrazit_ukoly(vsechny_ukoly, popisy_ukolu):
    #displayTask
    print("\nSeznam úkolů:")
    if len(vsechny_ukoly)<=0:
        print("\nNemáte žádné úkoly!")
    else:
        for index, ukol in enumerate(vsechny_ukoly):
            print(f"{index+1}. {ukol} - {popisy_ukolu.get(ukol,{index+1})}")
    menu(vsechny_ukoly, popisy_ukolu,show_intro=True)

def pridat_ukol(vsechny_ukoly, popisy_ukolu):
    while True:
        novy_ukol=input("\nZadejte název úkolu:")
        if len(novy_ukol)==0:
            print("Nezadal jste název úkolu!")
        if novy_ukol in vsechny_ukoly:
                    print ("Tento úkol již existuje.")
        else:
            vsechny_ukoly.append(novy_ukol)
            while True:
                popis_ukolu=input("Zadejte popis úkolu:")
                if len(popis_ukolu)==0:
                    print("Nezadal jste popis úkolu!")
                else:
                    popisy_ukolu[novy_ukol] = popis_ukolu
                    print(f"Úkol '{novy_ukol}' byl přidán.")            
                    menu(vsechny_ukoly, popisy_ukolu, show_intro=True)

def menu(vsechny_ukoly, popisy_ukolu, show_intro=True):
    if show_intro:
        print("\nSprávce úkolů - Hlavní menu",
            "\n1. Přidat nový úkol",
            "\n2. Zobrazit všechny úkoly",
            "\n3. Odstranit úkol",
            "\n4. Konec programu")

    volba=input("Vyberte možnost (1-4):")
    
    if volba=="1":
        pridat_ukol(vsechny_ukoly, popisy_ukolu)
    elif volba=="2":
        zobrazit_ukoly(vsechny_ukoly, popisy_ukolu)
    elif volba=="3":
        odstranit_ukol(vsechny_ukoly, popisy_ukolu)
    elif volba=="4":
        print("Konec programu.")
        exit()
    else:
        print("Zadejte číslo volby od 1 do 4!")
        menu (vsechny_ukoly, popisy_ukolu, show_intro=False)

menu(vsechny_ukoly, popisy_ukolu)