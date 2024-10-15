users = {  
    "aidil": {"password": "aidil1232", "role": "admin"}
}

menu = {  
    "Tahu Bacem": {"harga": 3000, "stok": 10},
    "Tempe Bacem": {"harga": 3000, "stok": 7},
    "Sate kulit": {"harga": 2000, "stok": 6},
    "Nasi Kucing": {"harga": 7000, "stok": 5},
    "Sate Hati": {"harga": 2500, "stok": 8}
}

print("Selamat datang di Angkringan Mama Aidil LOVE")
print("Silahkan Register Terlebih dahulu, jika belum mempunyai akun")

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
        
        if role in ["admin", "pembeli"]:
            users[username] = {"password": password, "role": role}
            print(f"Pengguna {username} berhasil didaftarkan.")
        else:
            print("Role tidak valid. Harus admin atau pembeli.")

    elif pilihan == "2":
        # Login
        username = input("Username: ")
        password = input("Password: ")
        
        user = users.get(username)  # Mendapatkan data pengguna berdasarkan username
        
        if user is None or user["password"] != password:
            print("Login gagal, username atau password salah.")
        else:
            print(f"Selamat datang, {username}!")
            while True:
                if user["role"] == "admin":
                    print("\n--- Menu Admin ---")
                    print("1. Tampilkan Menu")
                    print("2. Tambah Menu")
                    print("3. Update Menu")
                    print("4. Hapus Menu")
                    print("5. Logout")
                    pilihan_admin = input("Pilih menu: ")

                    if pilihan_admin == "1":
                        # Tampilkan Menu
                        if not menu:
                            print("Menu kosong.")
                        else:
                            for i, item in menu.items():
                                print(f"{i} - Harga: {item['harga']} - Stok: {item['stok']}")

                    elif pilihan_admin == "2":
                        # Tambah Menu
                        nama = input("Masukkan nama menu: ")
                        harga = input("Masukkan harga: ")
                        stok = input("Masukkan stok: ")

                        # Validasi input angka secara manual
                        if harga.isdigit() and stok.isdigit():
                            menu[nama] = {"harga": int(harga), "stok": int(stok)}
                            print(f"Menu {nama} berhasil ditambahkan.")
                        else:
                            print("Input harga dan stok harus berupa angka.")

                    elif pilihan_admin == "3":
                        # Update Menu
                        if not menu:
                            print("Menu kosong.")
                        else:
                            for i, item in menu.items():
                                print(f"{i} - Harga: {item['harga']} - Stok: {item['stok']}")

                            nama = input("Masukkan nama menu yang ingin diupdate: ")

                            if nama in menu:
                                nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
                                harga_baru = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")
                                stok_baru = input("Masukkan stok baru (kosongkan jika tidak ingin mengubah): ")

                                if nama_baru:
                                    menu[nama_baru] = menu.pop(nama)  # Mengubah nama menu
                                    if harga_baru.isdigit():
                                        menu[nama_baru]["harga"] = int(harga_baru)
                                    if stok_baru.isdigit():
                                        menu[nama_baru]["stok"] = int(stok_baru)
                                else:
                                    if harga_baru.isdigit():
                                        menu[nama]["harga"] = int(harga_baru)
                                    if stok_baru.isdigit():
                                        menu[nama]["stok"] = int(stok_baru)

                                print("Menu berhasil diupdate.")
                            else:
                                print("Menu tidak ditemukan.")

                    elif pilihan_admin == "4":
                        # Hapus Menu
                        if not menu:
                            print("Menu kosong.")
                        else:
                            for i in menu.keys():
                                print(i)

                            nama = input("Masukkan nama menu yang ingin dihapus: ")

                            if nama in menu:
                                del menu[nama]
                                print("Menu berhasil dihapus.")
                            else:
                                print("Menu tidak ditemukan.")

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
                        if not menu:
                            print("Menu kosong.")
                        else:
                            for i, item in menu.items():
                                print(f"{i} - Harga: {item['harga']} - Stok: {item['stok']}")

                    elif pilihan_pembeli == "2":
                        # Beli Barang
                        if not menu:
                            print("Menu kosong.")
                        else:
                            for i, item in menu.items():
                                print(f"{i} - Harga: {item['harga']} - Stok: {item['stok']}")

                            nama = input("Masukkan nama menu yang ingin dibeli: ")

                            if nama in menu:
                                jumlah_beli = input(f"Masukkan jumlah {nama} yang ingin dibeli: ")

                                if jumlah_beli.isdigit() and int(jumlah_beli) <= menu[nama]["stok"]:
                                    menu[nama]["stok"] -= int(jumlah_beli)
                                    print(f"Anda membeli {jumlah_beli} {nama}. Stok tersisa: {menu[nama]['stok']}")
                                else:
                                    print("Jumlah pembelian tidak valid atau stok tidak mencukupi.")
                            else:
                                print("Menu tidak ditemukan.")

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
