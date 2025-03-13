#Develop by: Furkan emir

import subprocess
import time

print("Ana Menü:")
print("1 - Sayı tahmin oyunu")
print("2 - Hesap Makinesi")
print("3 - Yıl başı ağacı uygulaması")
print("0 - Çıkış ")
print("----------------")
print("Develop by:Furkan Emir")
while True:
    print(" ")
    secim = input("Açmak istediğiniz programın numarasını giriniz: ")
    
    
    if secim == '0':
        print("Çıkılıyor...")
        break  # Programdan çık
    
    elif secim == '1':
        print("sayitahmin.py dosyası çalıştırılıyor...")
        time.sleep(1)
        subprocess.run('python "C:/Users/Furkan Emir/Desktop/dam/sayitahmin.py"') # Dosyayı çalıştır
    
    elif secim == '2':
        print("hesapmakinesi.py dosyası çalıştırılıyor...")
        subprocess.run('python "C:/Users/Furkan Emir/Desktop/dam/hesapmakinesi.py"')  # Dosyayı çalıştır
        
    elif secim == '3':
        print("yilbasicani.py dosyası çalıştırılıyor...")
        time.sleep(1)
        subprocess.run('python "C:/Users/Furkan Emir/Desktop/dam/yilbasicani.py"')
    
    else:
        print("Geçerli numaralardan birini giriniz")
        
#Develop by: Furkan emir     
        
