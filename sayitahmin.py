import random

def sayi_tahmin_oyunu():
    rastgele_sayi = random.randint(1, 100)  # 1 ile 100 arasında rastgele bir sayı seç
    tahmin_hakki = 7  # Kullanıcının 7 deneme hakkı var

    print("Sayı Tahmin Oyununa Hoş Geldin!")
    print("1 ile 100 arasında bir sayı tuttum, bakalım bulabilecek misin?")

    while tahmin_hakki > 0:
        try:
            tahmin = int(input("Tahmininizi girin: "))

            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue

            if tahmin < rastgele_sayi:
                print("Daha büyük bir sayı gir!")
            elif tahmin > rastgele_sayi:
                print("Daha küçük bir sayı gir!")
            else:
                print(f"Tebrikler! Doğru tahmin: {rastgele_sayi}")
                break

            tahmin_hakki -= 1
            print(f"Kalan hakkın: {tahmin_hakki}")

        except ValueError:
            print("Lütfen geçerli bir sayı girin!")

    if tahmin_hakki == 0:
        print(f"Hakkın bitti! Tutulan sayı: {rastgele_sayi}")

