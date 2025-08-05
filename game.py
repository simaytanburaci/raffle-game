import random
rastgele_sayi = random.randint(1,100)
hak_sayisi = 6
print("Sayi tahmin oyununa hosgeldiniz")
while hak_sayisi > 0 :
    tahmin = int(input("Tahmininizi giriniz:"))
    if tahmin < rastgele_sayi :
        print("Lütfen daha büyük bir sayi giriniz")
    elif tahmin > rastgele_sayi :
        print("Lütfen daha küçük bir sayi giriniz")
    else:
         print("Tebrikler! dogru sonuca ulaştiniz")
         break
    hak_sayisi -= 1 
    print(f"Kalan hakkiniz : {hak_sayisi}") 
    if hak_sayisi == 0 :
     print(f"Uzgunum hakkiniz bitti. Sayi {rastgele_sayi} idi")

  