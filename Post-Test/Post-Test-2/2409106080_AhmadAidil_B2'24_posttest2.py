print(" Selamat Datang di SWALAYAN UNMUL ")
nama = input ("Masukkan Nama Barang = ")
harga = float(input("Masukkan Harga Barang = "))
jumlah = int(input("Masukkan Jumlah Barang = "))
print("Selamat Anda dapat Diskon 80%")
diskon = float(input("Masukkan diskon = "))


#Menghitung total harga sebelum diskon
harga_barang = jumlah * harga

#Menghitung total diskon
total_diskon = (diskon/100) * harga_barang

#Menghitung total harga setelah diskon
totalharga_setelahdiskon = harga_barang - total_diskon

#Hitung sisa pembagian diskon
sisa_diskon = int(diskon) % 3

print(f"Anda Membeli {jumlah:.0f} {nama} Dengan Harga Satuan {harga:.0f}, Total Sebelum Diskon Adalah {harga_barang:.0f}, Total Diskon adalah {total_diskon:.0f} dan Total yang Harus dibayar Adalah {totalharga_setelahdiskon:.0f}.""\n"
      f"{diskon:.0f} Dibagi Dengan 3 Sisanya {sisa_diskon}")