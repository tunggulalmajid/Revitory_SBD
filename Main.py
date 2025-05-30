import os
import termcolor
from tabulate import tabulate
import psycopg2

def clear():
    os.system("cls")

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
    print("""
██████╗ ███████╗██╗   ██╗██╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██╔══██╗██╔════╝██║   ██║██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██████╔╝█████╗  ██║   ██║██║   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
██╔══██╗██╔══╝  ╚██╗ ██╔╝██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
██║  ██║███████╗ ╚████╔╝ ██║   ██║   ╚██████╔╝██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                                                            
""")

def Main():
    while True:
        kon, kur = KoneksiDB()
        clear()
        logo()
        print("SELAMAT DATANG".center(50))
        print("""
    1. BPH atau Divisi Properti  
    2. Peminjam atau Umum
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
            continue

def Login_admin():
    while True:
        Kon, Kur = KoneksiDB()
        query = "SELECT username, password from ADMINS"
        # Belum selesai

def Login_user():
    pass

def Register():
    pass

def Menu():
    pass


if __name__ == "__main__":
    Main()