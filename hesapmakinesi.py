while True:
    print("1-Toplama")
    print("2-Çıkarma")
    print("3-Bölme")
    print("4-Çarpma")
    print("5-Üs taban hesaplama")
    print("6-Karekök Alma")
    print("--Çıkmak için 0 tuşuna basınız--")
    print("---------------")
    
    secim = int(input("Yapmak istediğiniz işlemi seçin: "))

    if secim == 0:
        print("Çıkış yapılıyor...")
        break  

    if secim >= 1 and secim <= 4:
        sayi1 = float(input("1. sayıyı giriniz: "))  
        sayi2 = float(input("2. sayıyı giriniz: "))

        if secim == 1:
            sonuc = sayi1 + sayi2
            print("Sonuç:", sonuc)

        elif secim == 2:
            sonuc = sayi1 - sayi2
            print("Sonuç:", sonuc)

        elif secim == 3:
            if sayi2 != 0:  
                sonuc = sayi1 / sayi2
                print("Sonuç:", sonuc)
            else:
                print("Hata: 0'a bölme yapılamaz!")

        elif secim == 4:
            sonuc = sayi1 * sayi2
            print("Sonuç:", sonuc)
    
    elif secim == 5:
        taban = float(input("Taban değerini giriniz: "))
        us = float(input("Üs değerini giriniz: "))
        sonuc = taban ** us  # Üstel hesaplama operatör ile
        print("Sonuç:", sonuc)
    
    elif secim == 6:
        sayi = float(input("Karesini almak istediğiniz sayıyı girin: "))
        sonuc = sayi ** 2  # Kare alma işlemi
        print("Sonuç:", sonuc)

    else:
        print("Geçersiz seçim! Lütfen 1-8 arasında bir sayı girin.")

        
        
    break