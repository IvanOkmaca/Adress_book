import json

DATOTEKA_ADRESARA = "adresar.json"

def ucitaj_podatke() -> dict:
    try:
        with open(DATOTEKA_ADRESARA, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}

def spremi_podatke(podaci: dict) -> None:
   with open(DATOTEKA_ADRESARA, "w", encoding="utf-8") as file:
        json.dump(podaci, file, indent=4)

def provjeri_telefon(telefon: str) -> bool:
    return telefon.isdigit()

def provjeri_email(email: str) -> bool:
   return '@' in email

def dodaj_kontakt(ime: str, telefon: str, email: str, adresa: str) -> None:
   
    if not ime:
        print("Ime ne smije biti prazno.")
        return
    if not provjeri_telefon(telefon):
        print("Telefon treba sadržavati brojke.")
        return
    if not provjeri_email(email):
        print("Email mora sadržavati znak '@'.")
        return
    if not adresa:
        print("Adresa ne smije biti prazna.")
        return
    
    podaci = ucitaj_podatke()

    podaci[ime] = {"telefon": telefon,
                   "email": email,
                   "adresa": adresa}
    spremi_podatke(podaci)
    print(f"Kontakt {ime} je uspješno dodan.")

def prikazi_kontakte() -> None:
    podaci = ucitaj_podatke()
    if not podaci:
        print("Adresar je prazan.")
    else:
        for ime, info in podaci.items():
            print(f"\nIme: {ime}")
            print(f"Telefon: {info['telefon']}")
            print(f"Email: {info['email']}")
            print(f"Adresa: {info['adresa']}")

def pretrazi_kontakt(ime: str) -> None:
    podaci = ucitaj_podatke()
    if ime in podaci:
        kontakt = podaci[ime]
        print(f"\nIme: {ime}")
        print(f"Telefon: {kontakt['telefon']}")
        print(f"Email: {kontakt['email']}")
        print(f"Adresa: {kontakt['adresa']}")
    else:
        print(f"Kontakt s imenom {ime} nije pronađen.")

def obrisi_kontakt(ime: str) -> None:
    podaci = ucitaj_podatke()
    if ime in podaci:
        del podaci[ime]
        spremi_podatke(podaci)
        print(f"Kontakt {ime} je uspješno obrisan.")
    else:
        print(f"Kontakt s imenom {ime} nije pronađen.")

def main() -> None:
    """
    Glavna funkcija koja omogućava korisniku da bira opcije u adresaru.
    """
    while True:
        print("\nAdresar - Odaberite opciju:")
        print("1. Dodaj kontakt")
        print("2. Prikaži sve kontakte")
        print("3. Pretraži kontakt")
        print("4. Obriši kontakt")
        print("5. Izlaz")
        
        izbor = input("Unesite broj opcije: ")
        if izbor == "1":
            ime = input("Unesite ime: ")
            telefon = input("Unesite broj telefona: ")
            email = input("Unesite email: ")
            adresa = input("Unesite adresu: ")
            dodaj_kontakt(ime, telefon, email, adresa)
        elif izbor == "2":
            prikazi_kontakte()
        elif izbor == "3":
            ime = input("Unesite ime za pretragu: ")
            pretrazi_kontakt(ime)
        elif izbor == "4":
            ime = input("Unesite ime za brisanje: ")
            obrisi_kontakt(ime)
        elif izbor == "5":
            print("Izlaz iz aplikacije.")
            break
        else:
            print("Pogrešan unos, pokušajte ponovo.")

if __name__ == "__main__":
    main()
