import csv
import re
import os

# Daftar pengguna
users = {
    "admin": {"password": "admin", "role": "admin", "gender": "Laki-Laki"}
}

# Daftar menu
menu = {
    "Tahu Bacem": {"harga": 3000, "stok": 10},
    "Tempe Bacem": {"harga": 3000, "stok": 7},
    "Sate Kulit": {"harga": 2000, "stok": 6},
    "Nasi Kucing": {"harga": 7000, "stok": 5},
    "Sate Hati": {"harga": 2500, "stok": 8}
}

# Riwayat pembelian
riwayat_pembelian = {}

# Fungsi untuk memvalidasi bahwa input hanya mengandung huruf dan angka
def validasi_input(input_text):
    return re.match("^[a-zA-Z0-9]*$", input_text) is not None

def pembersihan():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk membaca data pengguna dari file CSV
def baca_user_csv():
    try:
        with open('users.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Lewati header
            for row in reader:
                if len(row) == 4:
                    username, password, role, gender = row
                    users[username] = {"password": password, "role": role, "gender": gender}
    except FileNotFoundError:
        pass  # Jika file tidak ditemukan, biarkan daftar users tetap seperti awal


# Fungsi untuk menyimpan pengguna ke dalam file CSV dengan append
def simpan_user_csv():
    with open('users.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Hanya menulis header jika file masih kosong
        if file.tell() == 0:
            writer.writerow(["Username", "Password", "Role", "Gender"])
        for username, data in users.items():
            writer.writerow([username, data['password'], data['role'], data['gender']])
    
    # input("Tekan Enter untuk kembali...")


# Fungsi menampilkan menu angkringan
def tampilkan_menu():
    print("\n------------- Daftar Menu --------------")
    print(f"{'No':<3} {'Nama Menu':<20} {'Harga':<10} {'Stok':<5}")
    print("-" * 40)
    for i, (nama, info) in enumerate(menu.items(), start=1):
        print(f"{i:<3} {nama:<20} Rp{info['harga']:<10} {info['stok']:<5}")
    input("\nTekan Enter untuk kembali...")

#Fungsi menampilkan menu angkringan yang hanya untuk beli menu
def tampilkan_menu_singkat():
    print("\n------------- Daftar Menu --------------")
    print(f"{'No':<3} {'Nama Menu':<20} {'Harga':<10} {'Stok':<5}")
    print("-" * 40)
    for i, (nama, info) in enumerate(menu.items(), start=1):
        print(f"{i:<3} {nama:<20} Rp{info['harga']:<10} {info['stok']:<5}")


# Fungsi menghitung total stok semua barang
def hitung_total_stok():
    pembersihan()
    total_stok = sum(item["stok"] for item in menu.values())
    print(f"Total stok seluruh barang adalah: {total_stok}")
    input("Tekan Enter untuk kembali...")
    return total_stok


# Fungsi login dengan validasi karakter khusus
def login(username, password):
    if not username or not password:
        print("Username dan password tidak boleh kosong.")
        return None
    if not validasi_input(username) or not validasi_input(password):
        print("Username dan password hanya boleh mengandung huruf dan angka.")
        return None
    user = users.get(username)
    if not user:
        print("Akun belum ada. Silakan registrasi terlebih dahulu.")
        input("enter...")
        return None
    if user["password"] != password:
        print("Login gagal, password salah.")
        return None
    print(f"Selamat datang, {username}!")
    return user

# Fungsi logout
def logout():
    print("Anda berhasil logout.")

# Fungsi menghitung diskon
def hitung_diskon(total_belanja, hari, dengan_pasangan):
    diskon = 0
    if hari.lower() == "minggu":
        diskon += 0.03
    if dengan_pasangan.lower() == "ya":
        diskon += 0.05
    if total_belanja > 100000:
        diskon += 0.07
    return diskon

# Fungsi menyimpan riwayat pembelian
def lihat_riwayat_pembelian(username):
    if username in riwayat_pembelian:
        print("\n--- Riwayat Pembelian ---")
        print(f"{'No':<3} {'Tanggal':<15} {'Items Dibeli':<25} {'Total Belanja':<15} {'Diskon':<10} {'Total Setelah Diskon':<20}")
        print("-" * 90)

        for idx, transaksi in enumerate(riwayat_pembelian[username], 1):
            # Menyusun item-item yang dibeli
            items = ", ".join([f"{item}: {jumlah} pcs" for item, jumlah in transaksi["items_dibeli"].items()])
            print(f"{idx:<3} {transaksi['tanggal']:<15} {items:<25} Rp{transaksi['total_belanja']:<15} {int(transaksi['diskon'] * 100):<10}% Rp{transaksi['total_setelah_diskon']:<20}")
    else:
        print("Belum ada riwayat pembelian.")

    # Tunggu hingga pengguna menekan enter sebelum melanjutkan
    # input("Tekan enter untuk kembali ke menu...")



# Fungsi menampilkan riwayat pembelian
def lihat_riwayat_pembelian(username, items_dibeli, total_belanja, diskon):
    print("\n=== Riwayat Pembelian ===")
    print(f"Pembeli : {username}")
    print("---------------------------------------------")
    
    if items_dibeli:
        print(f"{'No.':<4}{'Nama Barang':<20}{'Jumlah':<10}")
        print("---------------------------------------------")
        for i, (item, jumlah) in enumerate(items_dibeli.items(), 1):
            print(f"{i:<4}{item:<20}{jumlah:<10}")
        print("---------------------------------------------")
        print(f"{'Total Belanja':<20}: Rp{total_belanja:>10,}")
        print(f"{'Diskon':<20}: {int(diskon * 100):>10}%")
        print(f"{'Total Setelah Diskon':<20}: Rp{(total_belanja - (total_belanja * diskon)):>10,}")
    else:
        print("Belum ada riwayat pembelian.")
    
    input("Tekan Enter untuk kembali ke menu...")
    print("=============================================")



# Fungsi registrasi pengguna baru dengan validasi karakter khusus
def registrasi():
    while True:
        pembersihan()  # Membersihkan layar
        username = input("Masukkan username baru (hanya huruf dan angka): ").strip()

        # Cek apakah username kosong
        if not username:
            print("Username tidak boleh kosong. Silakan coba lagi.")
            continue  # Kembali ke awal loop jika username kosong

        # Cek apakah username hanya mengandung huruf dan angka
        if not validasi_input(username):
            print("Username hanya boleh mengandung huruf dan angka. Silakan coba lagi.")
            continue  # Kembali ke awal loop jika username tidak valid

        # Cek apakah username sudah terdaftar
        if username in users:
            print("Nama pengguna sudah ada. Silakan gunakan username lain.")
            input("enter...")
            continue  # Kembali ke awal loop jika username sudah terdaftar

        # Jika username valid, lanjutkan untuk meminta password dan gender
        password = input("Masukkan password baru (hanya huruf dan angka): ").strip()
        if not password:
            print("Password tidak boleh kosong. Silakan coba lagi.")
            continue  # Kembali ke awal loop jika password kosong

        if not validasi_input(password):
            print("Password hanya boleh mengandung huruf dan angka. Silakan coba lagi.")
            continue  # Kembali ke awal loop jika password tidak valid

        gender = input("Masukkan gender (L/P): ").strip().upper()

        if gender not in ["L", "P"]:
            print("Gender tidak valid. Silakan coba lagi.")
            continue  # Kembali ke awal loop jika gender tidak valid

        # Tentukan gender lengkap
        gender_full = "Laki-Laki" if gender == "L" else "Perempuan"
        
        # Simpan data pengguna ke dalam dictionary users
        users[username] = {"password": password, "role": "pembeli", "gender": gender_full}
        print(f"Pengguna {username} berhasil didaftarkan sebagai pembeli.")
        
        # Simpan ke file CSV setelah registrasi
        simpan_user_csv()
        break  # Keluar dari loop setelah pendaftaran berhasil


# Fungsi untuk menampilkan daftar pembeli (khusus admin)
def tampilkan_pembeli():
    pembersihan()
    print("\n--- Daftar Pembeli ---")
    pembeli_terdaftar = False
    for username, info in users.items():
        if info['role'] == 'pembeli':
            pembeli_terdaftar = True
            print(f"Username: {username}, Gender: {info['gender']}")
    
    if not pembeli_terdaftar:
        print("Belum ada pembeli yang terdaftar.")
    
    input("Tekan Enter untuk kembali...")


# Fungsi menu admin
def menu_admin():
    while True:
        pembersihan()
        print("""
                       
█▀▄▀█ █▀▀ █▄░█ █░█   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█
█░▀░█ ██▄ █░▀█ █▄█   █▀█ █▄▀ █░▀░█ █ █░▀█
──────────────── ⋆⋅☆⋅⋆ ─────────────────── 
          1. Tampilkan Menu   
          2. Tambah Menu                
          3. Update Menu      
          4. Hapus Menu  
          5. Hitung Total Stok        
          6. Lihat Daftar Pengguna
          7. Logout             
""")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            tambah_menu()
        elif pilihan == "3":
            update_menu()
        elif pilihan == "4":
            hapus_menu()
        elif pilihan == "5":
            print(f"Total stok seluruh barang: {hitung_total_stok()}")
        elif pilihan == "6":
            tampilkan_pembeli()
        elif pilihan == "7":
            logout()
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi menu pembeli
def menu_pembeli(username):
    items_dibeli = {}  # Variabel untuk menyimpan barang yang dibeli
    total_belanja = 0  # Total belanja awal
    diskon = 0         # Diskon awal

    while True:
        pembersihan()
        print("""

█▀▄▀█ █▀▀ █▄░█ █░█   █▀█ █▀▀ █▄░█ █▀▀ █▀▀ █░█ █▄░█ ▄▀█
█░▀░█ ██▄ █░▀█ █▄█   █▀▀ ██▄ █░▀█ █▄█ █▄█ █▄█ █░▀█ █▀█
─────────────────────── ⋆⋅☆⋅⋆ ───────────────────────── 
                1. Tampilkan Menu
                2. Beli Menu 
                3. Lihat Riwayat Pembelian
                4. Logout                       
""")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            hasil_belanja, diskon_pembelian = beli_barang(username)
            if hasil_belanja:  # Jika ada barang yang dibeli
                for item, jumlah in hasil_belanja.items():
                    items_dibeli[item] = items_dibeli.get(item, 0) + jumlah
                total_belanja += sum(menu[item]["harga"] * jumlah for item, jumlah in hasil_belanja.items())
                diskon = diskon_pembelian
        elif pilihan == "3":
            lihat_riwayat_pembelian(username, items_dibeli, total_belanja, diskon)
        elif pilihan == "4":
            logout()
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi membeli barang
def beli_barang(username):
    pembersihan()
    hari = input("Masukkan hari pembelian (misalnya: Senin, Selasa, dst.): ")
    pasangan = input("Apakah Anda berbelanja dengan pasangan? (Ya/Tidak): ").strip().lower()
    items_dibeli = {}
    total_belanja = 0

    while True:
        tampilkan_menu_singkat()  # Ganti dengan menu tanpa input
        try:
            pilihan = int(input("Masukkan nomor menu yang ingin dibeli (atau '0' untuk mengakhiri): ").strip())
            
            if pilihan == 0:
                break

            if pilihan < 1 or pilihan > len(menu):
                print("Pilihan tidak valid.")
                continue

            nama_barang = list(menu.keys())[pilihan - 1]
            jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin dibeli: "))
            if jumlah <= menu[nama_barang]["stok"]:
                menu[nama_barang]["stok"] -= jumlah
                items_dibeli[nama_barang] = items_dibeli.get(nama_barang, 0) + jumlah
                total_belanja += menu[nama_barang]["harga"] * jumlah
                print(f"Berhasil membeli {jumlah} {nama_barang}.")
            else:
                print(f"Stok {nama_barang} tidak mencukupi.")
        except ValueError:
            print("Input tidak valid. Pastikan memasukkan angka dengan benar.")

    if items_dibeli:
        diskon = hitung_diskon(total_belanja, hari, pasangan)
        return items_dibeli, diskon

    # Jika tidak ada barang yang dibeli
    return {}, 0


# Fungsi menambah menu baru
def tambah_menu():
    pembersihan()
    nama = input("Masukkan nama menu baru: ")
    
    while True:
        try:
            harga = int(input("Masukkan harga menu baru: "))
            break  # Keluar dari loop jika input valid
        except ValueError:
            print("Harga harus berupa angka. Silakan coba lagi.")
    
    while True:
        try:
            stok = int(input("Masukkan jumlah stok menu baru: "))
            break  # Keluar dari loop jika input valid
        except ValueError:
            print("Stok harus berupa angka. Silakan coba lagi.")
    
    if nama not in menu:
        menu[nama] = {"harga": harga, "stok": stok}
        print(f"Menu {nama} berhasil ditambahkan.")
    else:
        print("Menu tersebut sudah ada.")

# Fungsi untuk mengupdate menu
def update_menu():
    pembersihan()
    print("\n--- Update Menu ---")
    # Tampilkan daftar menu terlebih dahulu
    if not menu:
        print("Menu kosong. Tidak ada yang bisa diupdate.")
        return

    # Tampilkan daftar menu dengan angka, konsisten dengan tampilkan_menu
    print("\nDaftar Menu:")
    print(f"{'No':<3} {'Nama Menu':<20} {'Harga':<10} {'Stok':<5}")
    print("-" * 40)
    menu_list = list(menu.keys())
    for i, nama in enumerate(menu_list, start=1):
        info = menu[nama]
        print(f"{i:<3} {nama:<20} Rp{info['harga']:<10} {info['stok']:<5}")

    try:
        # Pilih menu berdasarkan angka
        pilihan = int(input("\nMasukkan nomor menu yang ingin diupdate: ").strip())
        if pilihan < 1 or pilihan > len(menu_list):
            print("Pilihan tidak valid.")
            return

        nama_menu = menu_list[pilihan - 1]

        # Input pembaruan
        harga_baru = int(input("Masukkan harga baru: ").strip())
        stok_baru = int(input("Masukkan stok baru: ").strip())

        if harga_baru <= 0 or stok_baru < 0:
            print("Harga harus lebih besar dari 0, dan stok tidak boleh negatif.")
            return

        # Update data menu
        menu[nama_menu]["harga"] = harga_baru
        menu[nama_menu]["stok"] = stok_baru
        print(f"Menu '{nama_menu}' berhasil diperbarui!")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan angka dengan benar.")

# Fungsi menghapus menu
def hapus_menu():
    pembersihan()
    print("\n--- Hapus Menu ---")
    # Tampilkan daftar menu terlebih dahulu
    if not menu:
        print("Menu kosong. Tidak ada yang bisa dihapus.")
        return

    # Tampilkan daftar menu dengan format yang konsisten
    print(f"{'No':<3} {'Nama Menu':<20} {'Harga':<10} {'Stok':<5}")
    print("-" * 40)
    
    menu_list = list(menu.keys())
    for i, nama in enumerate(menu_list, start=1):
        info = menu[nama]
        print(f"{i:<3} {nama:<20} Rp{info['harga']:<10} {info['stok']:<5}")

    try:
        # Pilih menu berdasarkan angka
        pilihan_menu = int(input("\nMasukkan nomor menu yang ingin dihapus: ").strip())
        if pilihan_menu < 1 or pilihan_menu > len(menu_list):
            print("Pilihan tidak valid.")
            return

        nama_menu = menu_list[pilihan_menu - 1]

        # Konfirmasi penghapusan
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus menu '{nama_menu}'? (y/n): ").strip().lower()
        if konfirmasi == 'y':
            del menu[nama_menu]
            print(f"Menu '{nama_menu}' berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan angka dengan benar.")

# Fungsi utama program
def main():
    while True:
        pembersihan()
        print("""
▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀▀█▀▀   ▒█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ 
░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ░▒█░░   ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ 
▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ░▒█░░   ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▒█▄▄█
""")
        print("""\033[38;2;0;255;255m
                        \033[38;2;255;255;0m---------------------------\033[38;2;0;255;255m
                /|  /|  \033[38;2;255;255;0m|    \033[0m ANGKRINGAN ADA ADA \033[38;2;0;255;255m \033[38;2;255;255;0m|\033[38;2;0;255;255m  
                ||__||  \033[38;2;255;255;0m|-------------------------|\033[38;2;0;255;255m
               /   O O\\__    \033[0m   1. Login\033[38;2;0;255;255m          \033[38;2;255;255;0m|\033[38;2;0;255;255m
              /          \\   \033[0m   2. Register\033[38;2;0;255;255m       \033[38;2;255;255;0m|\033[38;2;0;255;255m
             /      \\     \\  \033[0m   3. Keluar\033[38;2;0;255;255m         \033[38;2;255;255;0m|\033[38;2;0;255;255m
            /   _    \\     \\ \033[38;2;255;255;0m----------------------\033[38;2;0;255;255m
           /    |\\____\\     \\      \033[38;2;255;255;0m||\033[38;2;0;255;255m
          /     | | | |\\____/      \033[38;2;255;255;0m||\033[38;2;0;255;255m
         /       \\| | | |/ |     __\033[38;2;255;255;0m||\033[38;2;0;255;255m
        /  /  \\   -------  |_____| \033[38;2;255;255;0m||\033[38;2;0;255;255m
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \\----
       /\\                  |
      / /\\        |        /
     / /  |       |       |
 ___/ /   |       |       |
|____/    c_c_c_C/ \\C_c_c_c
              \033[0m""")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            user = login(username, password)
            if user:
                if user["role"] == "admin":
                    menu_admin()
                elif user["role"] == "pembeli":
                    menu_pembeli(username)
            else:
             print("Akun belum ada atau username/password salah.")
        elif pilihan == "2":
            registrasi()
        elif pilihan == "3":
            # Simpan data pengguna saat keluar dari program
            simpan_user_csv()
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Klik enter untuk kembali ke menu...")

# Panggil fungsi baca_user_csv sebelum memulai main loop
baca_user_csv()
main()

while True:
    print("""\033[38;2;0;255;255m
                        \033[38;2;255;255;0m---------------------------\033[38;2;0;255;255m
                /|  /|  \033[38;2;255;255;0m|    \033[0m ANGKRINGAN ADA ADA \033[38;2;0;255;255m    \033[38;2;255;255;0m|\033[38;2;0;255;255m  
                ||__||  \033[38;2;255;255;0m|-------------------------|\033[38;2;0;255;255m
               /   O O\\__    \033[0m   1. Login\033[38;2;0;255;255m          \033[38;2;255;255;0m|\033[38;2;0;255;255m
              /          \\   \033[0m   2. Register\033[38;2;0;255;255m       \033[38;2;255;255;0m|\033[38;2;0;255;255m
             /      \\     \\  \033[0m   3. Keluar\033[38;2;0;255;255m         \033[38;2;255;255;0m|\033[38;2;0;255;255m
            /   _    \\     \\ \033[38;2;255;255;0m----------------------\033[38;2;0;255;255m
           /    |\\____\\     \\      \033[38;2;255;255;0m||\033[38;2;0;255;255m
          /     | | | |\\____/      \033[38;2;255;255;0m||\033[38;2;0;255;255m
         /       \\| | | |/ |     __\033[38;2;255;255;0m||\033[38;2;0;255;255m
        /  /  \\   -------  |_____| \033[38;2;255;255;0m||\033[38;2;0;255;255m
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \\----
       /\\                  |
      / /\\        |        /
     / /  |       |       |
 ___/ /   |       |       |
|____/    c_c_c_C/ \\C_c_c_c
              \033[0m""")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        registrasi()
    elif pilihan == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        user = login(username, password)
        if user:
            if user["role"] == "admin":
                menu_admin()
            elif user["role"] == "pembeli":
                menu_pembeli(username)
    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem ini!")
        break
    else:
        print("Pilihan tidak valid.")
