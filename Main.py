import os
import termcolor
from tabulate import tabulate
import psycopg2
import time

def clear():
    os.system("cls")

def pagar():
    print("-"*64)

def KoneksiDB():
    try:
        Koneksi = psycopg2.connect(host="localhost",user="postgres", password="lubia2341", database="REVITORY")
        kursor = Koneksi.cursor()
        # print("Koneksi Berhasil")
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
        query = f"SELECT * from admins where username = '{username}' and password = '{password}' "

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
    pass

def Menu_admin():
    # print("Berhasil Login!")
    while True:
        clear()
        logo()
        print()
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

        

def TambahAlat():
    pass

def HapusAlat():
    pass

def UpdateAlat():
    pass

def menu_peminjam():
    print("Berhasil Login")

if __name__ == "__main__":
    Main()