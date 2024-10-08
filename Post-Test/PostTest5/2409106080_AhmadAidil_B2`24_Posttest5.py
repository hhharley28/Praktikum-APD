

users = [["aidil", "aidil1232", "admin"]]  # Data pengguna (username, password, role)
menu = [["Tahu Bacem", 3000, 10 ],
["Tempe Bacem", 3000, 7 ],
["Sate kulit", 2000, 6],
["Nasi Kucing", 7000 , 5],
["Sate Hati", 2500 , 8]]  # Data menu (nama, harga, stok)

print("Selamat datang di Angkringan Mama Aidil LOVE")
print("Silahkan Register Terlebih dahulu,jika belum mempunyai akun")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        # Register
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        role = input("Masukkan role (admin/pembeli): ")
        
        if role == "admin" or role == "pembeli":
            users.append([username, password, role])
            print(f"Pengguna {username} berhasil didaftarkan.")
        else:
            print("Role tidak valid. Harus admin atau pembeli.")

    elif pilihan == "2":
        # Login
        username = input("Username: ")
        password = input("Password: ")
        user = None
        
        for i in users:
            if i[0] == username and i[1] == password:
                user = i
                break
        
        if user is None:
            print("Login gagal, username atau password salah.")
        else:
            print(f"Selamat datang, {username}!")
            while True:
                if user[2] == "admin":
                    print("\n--- Menu Admin ---")
                    print("1. Tampilkan Menu")
                    print("2. Tambah Menu")
                    print("3. Update Menu")
                    print("4. Hapus Menu")
                    print("5. Logout")
                    pilihan_admin = input("Pilih menu: ")

                    if pilihan_admin == "1":
                        # Tampilkan Menu
                        if len(menu) == 0:
                            print("Menu kosong.")
                        else:
                            for i, item in enumerate(menu):
                                print(f"{i + 1}. {item[0]} - Harga: {item[1]} - Stok: {item[2]}")

                    elif pilihan_admin == "2":
                        # Tambah Menu
                        nama = input("Masukkan nama menu: ")
                        harga = input("Masukkan harga: ")
                        stok = input("Masukkan stok: ")

                        # Validasi input angka secara manual
                        if (harga) and (stok):
                            menu.append([nama, int(harga), int(stok)])
                            print(f"Menu {nama} berhasil ditambahkan.")
                        else:
                            print("Input harga dan stok harus berupa angka.")

                    elif pilihan_admin == "3":
                        # Update Menu
                        if len(menu) == 0:
                            print("Menu kosong.")
                        else:
                            for i, item in enumerate(menu):
                                print(f"{i + 1}. {item[0]} - Harga: {item[1]} - Stok: {item[2]}")

                            index = input("Masukkan nomor menu yang ingin diupdate: ")

                            if (index) and 0 < int(index) <= len(menu):
                                index = int(index) - 1
                                nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
                                harga_baru = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")
                                stok_baru = input("Masukkan stok baru (kosongkan jika tidak ingin mengubah): ")

                                if nama_baru:
                                    menu[index][0] = nama_baru
                                if (harga_baru):
                                    menu[index][1] = int(harga_baru)
                                if (stok_baru):
                                    menu[index][2] = int(stok_baru)

                                print("Menu berhasil diupdate.")
                            else:
                                print("Nomor menu tidak valid.")

                    elif pilihan_admin == "4":
                        # Hapus Menu
                        if len(menu) == 0:
                            print("Menu kosong.")
                        else:
                            for i, item in enumerate(menu):
                                print(f"{i + 1}. {item[0]} - Harga: {item[1]} - Stok: {item[2]}")

                            index = input("Masukkan nomor menu yang ingin dihapus: ")

                            if(index) and 0 < int(index) <= len(menu):
                                index = int(index) - 1
                                del menu[index]
                                print("Menu berhasil dihapus.")
                            else:
                                print("Nomor menu tidak valid.")

                    elif pilihan_admin == "5":
                        break

                    else:
                        print("Pilihan tidak valid.")

                else:
                    # Menu untuk pembeli angkringan
                    print("\n--- Menu Pembeli ---")
                    print("1. Tampilkan Menu")
                    print("2. Beli Barang")
                    print("3. Logout")
                    pilihan_pembeli = input("Pilih menu: ")

                    if pilihan_pembeli == "1":
                        if len(menu) == 0:
                            print("Menu kosong.")
                        else:
                            for i, item in enumerate(menu):
                                print(f"{i + 1}. {item[0]} - Harga: {item[1]} - Stok: {item[2]}")

                    elif pilihan_pembeli == "2":
                        # Beli Barang
                        if len(menu) == 0:
                            print("Menu kosong.")
                        else:
                            for i, item in enumerate(menu):
                                print(f"{i + 1}. {item[0]} - Harga: {item[1]} - Stok: {item[2]}")

                            index = input("Masukkan nomor menu yang ingin dibeli: ")

                            if(index) and 0 < int(index) <= len(menu):
                                index = int(index) - 1
                                jumlah_beli = input(f"Masukkan jumlah {menu[index][0]} yang ingin dibeli: ")

                                if (jumlah_beli) and int(jumlah_beli) <= menu[index][2]:
                                    menu[index][2] -= int(jumlah_beli)
                                    print(f"Anda membeli {jumlah_beli} {menu[index][0]}. Stok tersisa: {menu[index][2]}")
                                else:
                                    print("Jumlah pembelian tidak valid atau stok tidak mencukupi.")
                            else:
                                print("Nomor menu tidak valid.")

                    elif pilihan_pembeli == "3":
                        break

                    else:
                        print("Pilihan tidak valid.")

    elif pilihan == "3":
        # Keluar dari program
        print("Terima kasih telah sudah mampir ke tempat ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

