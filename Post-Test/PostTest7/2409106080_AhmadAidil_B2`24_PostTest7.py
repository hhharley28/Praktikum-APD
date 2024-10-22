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

# Fungsi tanpa parameter
def tampilkan_menu():
    if not menu:
        print("Menu kosong.")
    else:
        for nama, detail in menu.items():
            print(f"{nama} - Harga: {detail["harga"]} - Stok: {detail["stok"]}")

# Fungsi parameter
def tambah_menu(nama, harga, stok):
    menu[nama] = {"harga": harga, "stok": stok}
    print(f"Menu {nama} berhasil ditambahkan.")

# Fungsi rekursif
def hitung_total_stok(index, items):
    if index >= len(items):
        return 0
    return items[index]["stok"] + hitung_total_stok(index + 1, items)

# Prosedur Log Out
def logout():
    print("Anda berhasil logout.")
    return

def login(username, password):
    user = users.get(username)
    if user and user["password"] == password:
        print(f"Selamat datang, {username}!")
        return user
    else:
        print("Login gagal, username atau password salah.")
        return None


print("Selamat datang di Angkringan Mama Aidil LOVE")
print("Silahkan Register Terlebih dahulu, jika belum mempunyai akun")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        role = input("Masukkan role (admin/pembeli): ")
        
        if role in ["admin", "pembeli"]:
            users[username] = {"password": password, "role": role}
            print(f"Pengguna {username} berhasil didaftarkan.")
        else:
            print("Role tidak valid. Harus admin atau pembeli.")

    elif pilihan == "2":
        username = input("Username: ")
        password = input("Password: ")

        user = login(username, password)  # Menggunakan prosedur login
        
        if user:
            while True:
                if user["role"] == "admin":
                    print("\n--- Menu Admin ---")
                    print("1. Tampilkan Menu")
                    print("2. Tambah Menu")
                    print("3. Hitung Total Stok")
                    print("4. Logout")
                    pilihan_admin = input("Pilih menu: ")

                    if pilihan_admin == "1":
                        tampilkan_menu()

                    elif pilihan_admin == "2":
                        nama = input("Masukkan nama menu: ")
                        harga = input("Masukkan harga: ")
                        stok = input("Masukkan stok: ")

                        
                        if harga.isdigit() and stok.isdigit():
                            tambah_menu(nama, int(harga), int(stok))
                        else:
                            print("Input harga dan stok harus berupa angka.")

                    elif pilihan_admin == "3":
                        total_stok = hitung_total_stok(0, list(menu.values()))
                        print(f"Total stok seluruh barang: {total_stok}")

                    elif pilihan_admin == "4":
                        logout()
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
                        tampilkan_menu()

                    elif pilihan_pembeli == "2":
                        if not menu:
                            print("Menu kosong.")
                        else:
                            tampilkan_menu()

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
                        logout()
                        break

                    else:
                        print("Pilihan tidak valid.")

    elif pilihan == "3":
        print("Terima kasih telah sudah mampir ke tempat ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
