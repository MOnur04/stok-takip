import json
import os

DOSYA = "stoklar.json"


def verileri_yukle():
    if not os.path.exists(DOSYA):
        return []
    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)


def verileri_kaydet(veriler):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veriler, f, ensure_ascii=False, indent=2)


def urun_ekle():
    ad = input("Urun adi: ").strip()
    if not ad:
        print("Urun adi bos olamaz.")
        return

    try:
        miktar = int(input("Mevcut stok adedi: "))
        kritik = int(input("Kritik stok esigi: "))
    except ValueError:
        print("Lutfen miktar ve esik icin sayi girin.")
        return

    veriler = verileri_yukle()
    veriler.append({
        "ad": ad,
        "miktar": miktar,
        "kritik": kritik
    })
    verileri_kaydet(veriler)
    print(f"'{ad}' basariyla eklendi.")


def main():
    while True:
        print("\n--- Stok Takip ---")
        print("1. Yeni urun ekle")
        print("0. Cikis")
        secim = input("Seciminiz: ").strip()

        if secim == "1":
            urun_ekle()
        elif secim == "0":
            print("Cikiliyor...")
            break
        else:
            print("Gecersiz secim.")


if __name__ == "__main__":
    main()
