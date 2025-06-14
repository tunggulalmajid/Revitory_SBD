import os
from tabulate import tabulate
import psycopg2
import time
import datetime

def clear():
    os.system("cls")

def pagar():
    print("-"*64)

def KoneksiDB():
    try:
        Koneksi = psycopg2.connect(host="localhost",user="postgres", password="lubia2341", database="REVITORY")
        kursor = Koneksi.cursor()
        return Koneksi, kursor
    except Exception:
        print("Koneksi Gagal, Silahkan Check Ulang")
        return None


def logo():
    pagar()
    print("""
 ██████╗ ███████╗██╗   ██╗██╗████████╗ ██████╗ ██████╗ ██╗   ██╗
 ██╔══██╗██╔════╝██║   ██║██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
 ██████╔╝█████╗  ██║   ██║██║   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
 ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
 ██║  ██║███████╗ ╚████╔╝ ██║   ██║   ╚██████╔╝██║  ██║   ██║   
 ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                                                            
""")
    pagar()

def Main():
    while True:
        kon, kur = KoneksiDB()
        clear()
        logo()
        print("SELAMAT DATANG".center(55))
        print("""
    1. Pengurus
    2. Anggota atau Umum
    3. Register
    4. Exit          
    """)
        try:
            pilih = int(input("Pilih Login Sebagai >> "))
            if pilih == 1:
                Login_admin()
                break
            elif pilih == 2:
                Login_user()
                break
            elif pilih == 3:
                Register()
                break
            elif pilih == 4:
                clear()
                exit()
            else:
                print("Pilihan tidak ada")
        except ValueError:
            print("Inputan tidak valid")
            time.sleep(1.5)
            continue

def Login_admin():
    while True:
        clear()
        logo()
        Kon, Kur = KoneksiDB()
        username = input("Masukkan Username >> ")
        password = input("Masukkan Password >> ") 
        query = f"SELECT * from admin where username_admin = '{username}' and password_admin = '{password}' "

        Kur.execute(query,(username,password))
        Pencocokan = Kur.fetchone()

        if Pencocokan is not None:
            Menu_admin()
            Kon.close()
            break
        else:
            print("Username Atau Password Salah!")
            continue

def Login_user():
    while True:
        clear()
        logo()
        Kon, Kur = KoneksiDB()
        username = input("Masukkan Username >> ")
        password = input("Masukkan Password >> ")
        query = f"SELECT * from peminjam where username = '{username}' and password '{password}'"
        try:
            Kur.execute(query,(username,password))
            pencocokan = Kur.fetchone()

            if pencocokan is not None:
                clear()
                print("LOGIN BERHASIL!!")
                time.sleep(1.5)
                menu_peminjam()
                Kon.close()
                break
            else:
                clear()
                print("LOGIN GAGAL!!")
                time.sleep(1)
                continue
        except Exception as e:
            print(f"Terjadi Kesalahan: {e}")
            continue

def Register():
    while True:
        clear()
        logo()
        print("REGISTRASI AKUN REVITORY".center)
        username = input("Masukkan Username >> ")
        password = input("Masukkan Password >> ")

        Kon, Kur = KoneksiDB()
        query = "INSERT"

def Menu_admin():
    while True:
        clear()
        logo()
        print("Selamat Datang Di Menu Admin")
        print("""
1. Kelola Alat
2. Kelola Aturan
3. Lihat Alat Terpinjam
4. Lihat History
5. Lihat User
6. Konfirmasi
""")
        pilih = input("Silahkan Pilih >> ")
        match pilih:
            case '1':
                KelolaAlat()
                break
            case '2':
                break
            case '3':
                break
            case '4':
                break
            case '5':
                break
            case '6':
                break
            case _:
                print("Pilihan Tidak ada")

def KelolaAlat():
    while True:
        clear()
        logo()
        print("KELOLAT ALAT KESENIAN REOG")
        print("Selamat Datang Di Menu Admin")
        print("""
1. Tambah Alat Kesenian
2. Lihat Alat Kesenian
3. Hapus Alat Kesenian
4. Ubah Alat Kesenian
""")
        pilih = input("Silahkan Pilih >> ")
        match pilih:
            case '1':
                clear()
                nama = input("Masukkan Nama Alat >> ")
                deskripsi = input("Masukkan Deskripsi Alat >> ")

                while True:
                    try:
                        status = int(input("Masukkan Status Alat Tersedia, Waiting, atau Terpinjam [1/2/3] >>"))
                        if status < 1 or status > 3:
                            raise ValueError("Inputan Berupa [1/2/3]")
                        break
                    except ValueError:
                        print("Inputan Berupa [1/2/3]")
                
                while True:
                    try:
                        kondisi = int(input("Masukkan Kondisi Alat baik, kurang baik, atau rusak [1/2/3]"))
                        if kondisi < 1 or kondisi > 2:
                            raise ValueError("Inputan Berupa [1/2/3]")
                        break
                    except ValueError:
                        print("Inputan Berupa [1/2/3]")
                
                TambahAlat(nama, deskripsi,status,kondisi)
                break

            case '2':
                break
            case '3':
                break
            case '4':
                UpdateAlat()
                break
            case _:
                print("Pilihan Tidak ada")

def TambahAlat(nama, deskripsi,status,kondisi):
    Kon, Kur = KoneksiDB()
    queryTambah = "INSERT INTO alat_kesenian (nama_alat,deskripsi, id_status_alat, id_kondisi_alat) VALUES(%s, %s, %s, %s)"

    Kur.execute(queryTambah,(nama, deskripsi,status,kondisi))
    Kon.commit()
    print("Alat Berhasil Ditambahkan!")


def HapusAlat():
    pass

def UpdateAlat():
    clear()
    logo()
    LihatAlat()

def LihatAlat():
    Kon, Kur = KoneksiDB()
    query = "SELECT * from alat_kesenian"

    try: 
        Kur.execute(query)
        alat_list = Kur.fetchall()
        print(tabulate(alat_list, headers=["ID", "Nama Alat", "Deskripsi", "Status", "Kondisi"], tablefmt="pretty"))
    except Exception as e:
        print(f"Database Gagal: {e}")
    finally:
        Kon.close()


def menu_peminjam(username):
    while True:
        clear()
        logo()
        print("Menu Anggota/Umum")
        print("""
1. Lihat Denda & Bayar
2. Pinjam Alat
3. Kembalikan Alat
4. Kembali
""")
        pilih = input("Pilih menu >> ")
        match pilih:
            case '1':
                denda_peminjam(username)
            case '2':
                pinjam_alat(username)
            case '3':
                kembalikan_alat(username)
            case '4':
                break
            case _:
                print("Pilihan tidak ada.")
                time.sleep(1)


def pinjam_alat(username):
    kon, kur = KoneksiDB()
    try:
        # Cari id_peminjam
        kur.execute("SELECT id_peminjam FROM peminjam WHERE username = %s", (username,))
        user = kur.fetchone()
        if not user:
            print("User tidak ketemu.")
            return
        id_peminjam = user[0]

        # Tampilkan alat yang tersedia
        kur.execute("""
            SELECT ak.id_alat_kesenian, ak.nama_alat, ak.deskripsi
            FROM alat_kesenian ak
            JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
            WHERE sak.status_alat = 'Tersedia'
        """)
        alat = kur.fetchall()
        if not alat:
            print("Alat tidak tersedia.")
            return
        print(tabulate(alat, headers=["ID", "Nama Alat", "Deskripsi"], tablefmt="grid"))

        id_alat = int(input("Masukkan ID alat : "))
        keterangan = input("Keterangan peminjaman: ")
        hari_pinjam = int(input("Pinjam berapa hari? "))
        tanggal_peminjaman = datetime.datetime.now()
        tenggat_pengembalian = tanggal_peminjaman + datetime.timedelta(days=hari_pinjam)

        # Pilih admin random (atau bisa pilih sendiri)
        kur.execute("SELECT id_admin FROM admin ORDER BY RANDOM() LIMIT 1")
        id_admin = kur.fetchone()[0]

        # Status peminjaman 'Dipinjamkan'
        kur.execute("SELECT id_status_peminjaman FROM status_peminjaman WHERE status_peminjaman = 'Dipinjamkan'")
        id_status_peminjaman = kur.fetchone()[0]

        # Insert ke peminjaman
        kur.execute("""
            INSERT INTO peminjaman (tanggal_peminjaman, tenggat_pengembalian, keterangan, id_peminjam, id_admin, id_status_peminjaman)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_peminjaman
        """, (tanggal_peminjaman, tenggat_pengembalian, keterangan, id_peminjam, id_admin, id_status_peminjaman))
        id_peminjaman = kur.fetchone()[0]

        # Insert ke detail_peminjaman
        kur.execute("INSERT INTO detail_peminjaman (id_peminjaman, id_alat_kesenian) VALUES (%s, %s)", (id_peminjaman, id_alat))

        # Update status alat menjadi 'Terpinjam'
        kur.execute("UPDATE alat_kesenian SET id_status_alat = 2 WHERE id_alat_kesenian = %s", (id_alat,))

        kon.commit()
        print("Peminjaman berhasil!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    input("Tekan Enter")

def lihat_aturan():
    kon, kur = KoneksiDB()
    try:
        kur.execute("""
            SELECT p.id_peraturan, a.nama, p.peraturan
            FROM peraturan p
            JOIN admin a ON p.id_admin = a.id_admin
            ORDER BY p.id_peraturan
        """)
        data = kur.fetchall()
        if data:
            print(tabulate(data, headers=["ID", "Admin", "Peraturan"], tablefmt="grid"))
        else:
            print("Belum ada peraturan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    input("Tekan Enter")

def kelola_peraturan():
    kon, kur = KoneksiDB()
    try:
        id_admin = int(input("Masukkan ID Admin: "))
        peraturan = input("Masukkan peraturan baru: ")
        kur.execute("INSERT INTO peraturan (id_admin, peraturan) VALUES (%s, %s)", (id_admin, peraturan))
        kon.commit()
        print("Peraturan ditambah.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    input("Tekan Enter")

def kembalikan_alat(username):
    kon, kur = KoneksiDB()
    try:
        # Cari id_peminjam
        kur.execute("SELECT id_peminjam FROM peminjam WHERE username = %s", (username,))
        user = kur.fetchone()
        if not user:
            print("User tidak ketemu.")
            return
        id_peminjam = user[0]

        # Tampilkan alat yang sedang dipinjam user
        kur.execute("""
            SELECT pj.id_peminjaman, ak.id_alat_kesenian, ak.nama_alat, pj.tenggat_pengembalian
            FROM peminjaman pj
            JOIN detail_peminjaman dp ON pj.id_peminjaman = dp.id_peminjaman
            JOIN alat_kesenian ak ON dp.id_alat_kesenian = ak.id_alat_kesenian
            WHERE pj.id_peminjam = %s AND pj.id_status_peminjaman = 1
        """, (id_peminjam,))
        data = kur.fetchall()
        if not data:
            print("Tidak ada alat yang sedang Anda pinjam.")
            return
        print(tabulate(data, headers=["ID Peminjaman", "ID Alat", "Nama Alat", "Tenggat"], tablefmt="grid"))

        id_peminjaman = int(input("Masukkan ID Peminjaman yang ingin dikembalikan: "))
        id_alat = int(input("Masukkan ID Alat yang ingin dikembalikan: "))

        # Update status peminjaman menjadi 'Dikembalikan'
        kur.execute("UPDATE peminjaman SET id_status_peminjaman = 2 WHERE id_peminjaman = %s", (id_peminjaman,))
        # Update status alat menjadi 'Tersedia'
        kur.execute("UPDATE alat_kesenian SET id_status_alat = 1 WHERE id_alat_kesenian = %s", (id_alat,))

        kon.commit()
        print("Pengembalian berhasil!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    input("Tekan Enter")

def denda_peminjam(username):
    kon, kur = KoneksiDB()
    try:
        # Cari id_peminjam berdasarkan username
        kur.execute("SELECT id_peminjam, nama_peminjam FROM peminjam WHERE username = %s", (username,))
        user = kur.fetchone()
        if not user:
            print("User tidak ditemukan.")
            return
        id_peminjam, nama_peminjam = user

        # Tampilkan denda yang harus dibayar
        kur.execute("SELECT id_denda_peminjam, denda FROM denda_peminjam WHERE id_peminjam = %s", (id_peminjam,))
        denda = kur.fetchone()
        if not denda:
            print("Kamu tidak punya denda.")
            return
        id_denda, jumlah_denda = denda
        print(f"Nama: {nama_peminjam}")
        print(f"Denda yang harus dibayar: Rp {jumlah_denda:,.0f}")

        # Konfirmasi pembayaran
        bayar = input("Ingin membayar denda (ya/tidak): ").lower()
        if bayar == 'ya':
            kur.execute("DELETE FROM denda_peminjam WHERE id_denda_peminjam = %s", (id_denda,))
            kon.commit()
            print("Denda berhasil dibayar. Terima kasih!")
        else:
            print("Pembayaran dibatalkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    input("Tekan Enter untuk kembali...")

def denda_peminjam(username):
    kon, kur = KoneksiDB()
    try:
        # Cari id_peminjam berdasarkan username
        kur.execute("SELECT id_peminjam, nama_peminjam FROM peminjam WHERE username = %s", (username,))
        user = kur.fetchone()
        if not user:
            print("User tidak ditemukan.")
            return
        id_peminjam, nama_peminjam = user

        # Tampilkan denda yang harus dibayar
        kur.execute("SELECT id_denda_peminjam, denda FROM denda_peminjam WHERE id_peminjam = %s", (id_peminjam,))
        denda = kur.fetchone()
        if not denda:
            print("Kamu tidak punya denda.")
            return
        id_denda, jumlah_denda = denda
        print(f"Nama: {nama_peminjam}")
        print(f"Denda yang harus dibayar: Rp {jumlah_denda:,.0f}")

        # Konfirmasi pembayaran
        bayar = input("Ingin membayar denda (ya/tidak): ").lower()
        if bayar == 'ya':
            kur.execute("DELETE FROM denda_peminjam WHERE id_denda_peminjam = %s", (id_denda,))
            kon.commit()
            print("Denda berhasil dibayar. Terima kasih!")
        else:
            print("Pembayaran dibatalkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    input("Tekan Enter untuk kembali...")

if __name__ == "__main__":
    # Main()
    UpdateAlat()