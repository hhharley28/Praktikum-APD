print ("MARI MENGHITUNG BERAT IDEAL ANDA!!!")
print ("Contoh berat anda 50Kg --> 50000000Mg")
BeratMg = float(input("Masukkan berat badan anda (dalam Mg) = "))
#konversi berat dari mg ke kg
Berat = BeratMg / 1000000

print ("Contoh tinggi anda 170Cm --> 1.7m --> 0.0017Km ")
TinggiKm = float(input("Masukkan Tinggi badan anda (dalam Km) = "))
#konversi tinggi dari km ke m
Tinggi = TinggiKm * 1000

#proses
BMI = Berat / (Tinggi ** 2)

#percabangan
if BMI < 18.5:
    print ("Kategori Berat badan anda (UnderWeight)")
elif BMI < 24.9:
    print ("Kategori Berat badan anda (Normal)")
elif BMI < 29.9:
    print ("Kategori Berat badan anda (OverWeight)")
else :
    print ("Kategori Berat Badan Anda (Obesitas)")

print (f"BMI Anda adalah {BMI :.2f}")




