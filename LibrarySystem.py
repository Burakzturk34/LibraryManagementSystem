class Library:
    def __init__(self, dosya_yolu="books.txt"):
        self.dosya_yolu = dosya_yolu
        self.dosya = open(self.dosya_yolu, "a+")

    def __del__(self):
        if self.dosya:
            self.dosya.close()

    def kitap_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()
        for kitap in kitaplar:
            bilgiler = kitap.split(',')
            print(f"Kitap Adı: {bilgiler[0]}, Yazar: {bilgiler[1]}")

    def kitap_ekle(self):
        kitap_adi = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yayin_yili = input("Yayın Yılı: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")

        yeni_kitap = f"{kitap_adi},{yazar},{yayin_yili},{sayfa_sayisi}\n"
        self.dosya.write(yeni_kitap)
        print(f"{kitap_adi} adlı kitap başarıyla eklendi.")

    def kitap_sil(self):
        silinecek_kitap_adı = input("Silinecek Kitap Adı: ")
        sonkarar = input("Kitabı silmek istediğinize emin misiniz? (y/n): ")

        if sonkarar.lower() == "y":
            self.dosya.seek(0)
            kitaplar = self.dosya.read().splitlines()

            yeni_kitaplar = [kitap for kitap in kitaplar if silinecek_kitap_adı not in kitap]

            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines('\n'.join(yeni_kitaplar))
            print(f"{silinecek_kitap_adı} adlı kitap başarıyla silindi.")
        elif sonkarar.lower() == "n":
            print(f"{silinecek_kitap_adı} adlı kitap silinmekten vazgeçildi.")
        else:
            print("Hatalı bir değer girildi.")


# objesi oluşturma
lib = Library()

# Menü oluşturma ve kullanıcıdan giriş alma
while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    print("Q) Çıkış")

    secim = input("Lütfen bir seçenek girin: ")

    if secim == "1":
        lib.kitap_listele()
    elif secim == "2":
        lib.kitap_ekle()
    elif secim == "3":
        lib.kitap_sil()
    elif secim == "Q":
        break
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")