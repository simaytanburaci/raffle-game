import random
katilimcilar = ["Simay","Gorkem","Ozlem","Asuman", "Melisa","Fatma","Mira","Ozge"]
hediyeler = ["Gozluk", "Kulaklik", "Canta","Bilgisayar","Telefon","Defter","Kalemlik","Ayakkabi"]
kazanan_index = random.randint(0,len(katilimcilar) - 1)
hediye_index = random.randint(0,len(hediyeler) - 1)
kazanan = katilimcilar[kazanan_index]
hediye = hediyeler[hediye_index]
print(f"{kazanan} şu hediyeyi kazandi : {hediye} ")