import os
from tabulate import tabulate
import psycopg2
import time
import datetime

def clear():
    os.system("cls")

def pagar():
    print("═"*64)    
def KoneksiDB():
    valueHost = "localhost"
    valueUser = "postgres"
    valuePassword = "Gunungsari"
    valueDatabase = "REVITORY"
    try:
        Koneksi = psycopg2.connect(host=valueHost,user=valueUser, password= valuePassword, database=valueDatabase)
        kursor = Koneksi.cursor()
        return Koneksi, kursor
    except Exception:
        print("Koneksi Gagal, Silahkan Check Ulang")
        return None

def enter ():
    input ("Tekan [Enter] untuk melanjutkan >> ")

def logo():
    pagar()
    print("""
 ██████╗ ███████╗██╗   ██╗██╗████████╗ ██████╗ ██████╗ ██╗   ██╗
 ██╔══██╗██╔════╝██║   ██║██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
 ██████╔╝█████╗  ██║   ██║██║   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
 ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
 ██║  ██║███████╗ ╚████╔╝ ██║   ██║   ╚██████╔╝██║  ██║   ██║   
 ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ """)
    pagar()

def Main():
    while True:
        kon, kur = KoneksiDB()
        clear()
        logo()
        print("SELAMAT DATANG".center(55))
        pagar()
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
                raise ValueError("Pilihan tidak ada")
        except ValueError:
            print("Inputan tidak valid")
            enter()

def Login_admin():
    idMimin = 0
    while True:
        clear()
        logo()
        Kon, Kur = KoneksiDB()
        username = input("Masukkan Username >> ")
        password = input("Masukkan Password >> ") 
        query = f"SELECT id_admin from admins where username = '{username}' and password = '{password}'"
        try:
            Kur.execute(query,(username,password))
            Pencocokan = Kur.fetchone()

            if Pencocokan is not None:
                clear()
                idMimin += Pencocokan[0]
                time.sleep(1.5)
                Menu_admin(idMimin)
                Kon.close()
                break
            else:
                print("Username Atau Password Salah!")
                enter()
        except Exception as e:
            print(f"Terjadi Kesalahan : {e}")
            enter()

def Login_user():
    idPeminjam = 0
    while True:
        clear()
        logo()
        Kon, Kur = KoneksiDB()
        username = input("Masukkan Username >> ")
        password = input("Masukkan Password >> ")
        query = f"SELECT id_peminjam from peminjam where username = '{username}' and password_user = '{password}'"
        try:
            Kur.execute(query,(username,password))
            pencocokan = Kur.fetchone()

            if pencocokan is not None:
                clear()
                idPeminjam += pencocokan
                print("LOGIN BERHASIL!!")
                time.sleep(1.5)
                Kon.close()
                menu_peminjam(username)
                break
            else:
                clear()
                print("LOGIN GAGAL!!")
                time.sleep(1)
                enter()
                
        except Exception as e:
            print(f"Terjadi Kesalahan: {e}")
            enter()

def Register():
    while True:
        clear()
        logo()
        print("REGISTRASI AKUN REVITORY".center(75))
        pagar()
        while True:
            try :
                namaPeminjam = input ("Masukkan Nama Anda >> ")
                if len(namaPeminjam) > 3 :
                    break
                else :
                    raise ValueError ("Nama Harus Lebih Dari 3 Karakter")
                    enter()
            except Exception as e :
                print(f"Terjadi Kesalahan: {e}")
                enter()

        while True:
            try :
                email = input ("Masukkan Nama Anda >> ")
                if "@" in email and "." in email:
                    break
                else :
                    raise ValueError ("email tidak valid")
                    enter()
            except Exception as e :
                print(f"Terjadi Kesalahan: {e}")
                enter()

        while True:
            try :
                nomorTelepon = input("Masukkan Nomor Telepon >> ")
                if len(nomorTelepon) > 10 and len(nomorTelepon) < 15:
                    nomorTelepon = int(nomorTelepon)
                    break
                else :
                    raise ValueError ("Nomor telepon tidak valid")
                    enter()
            except Exception as e :
                print(f"Terjadi Kesalahan: {e}")
                enter()

        while True:
            try :
                username = input("Masukkan Username >> ")
                if len(username) > 3:
                    break
                else :
                    raise ValueError ("Panjang username tidak boleh kurang dari 4 karakter")
                    enter()
            except Exception as e :
                print(f"Terjadi Kesalahan: {e}")
                enter()

        while True:
            try :
                password = input("Masukkan Password >> ")
                if len(password) > 7:
                    break
                else :
                    raise ValueError ("Panjang Password tidak boleh kurang dari 8 karakter")
            except Exception as e :
                print(f"Terjadi Kesalahan: {e}")
                enter()

        while True:
            try :
                konfirmasiPassword = input("Masukkan Password >> ")
                if konfirmasiPassword == password:
                    break
                else :
                    raise ValueError ("Password tidak sama, masukkan kembali")
                    enter()
            except Exception as e :
                print(f"Terjadi Kesalahan: {e}")
                enter()
        
        Kon, Kur = KoneksiDB()
        # query = """
        # insert into peminjam(nama_peminjam,email,nomor_telepon, username, password_user, is_banned) 
        # values ('Tunggul', 'tunggul@gmail.com', 088888888123, 'tung',123, false )
        # """

def Menu_admin(idMimin):
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
        pagar()
        pilih = input("Silahkan Pilih >> ")
        match pilih:
            case '1':
                KelolaAlat(idMimin)
                break
            case '2':
                KelolaAturan(idMimin)
                break
            case '3':
                LihatAlatTerpinjamForAdmin(idMimin)
                break
            case '4':
                HisttoryForAdmin(idMimin)
                break
            case '5':
                LihatPeminjamForAdmin(idMimin)
                break
            case '6':
                KonfirmasiForAdmin(idMimin)
                break
            case _:
                print("Pilihan Tidak ada")
                enter()

def KelolaAlat(idMimin):
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
5. Kembali
""")
        pilih = input("Silahkan Pilih >> ")
        match pilih:
            case '1':
                clear()
                try:
                    nama = input("Masukkan Nama Alat >> ")

                    if not nama.strip():
                        raise ValueError("Inputan Tidak Boleh Kosong!")
                    print("Inputan Anda:", nama)
                except ValueError as e:
                    print("Terdapat Kesalahan Inputan:", e)

                try:
                    deskripsi = input("Masukkan Deskripsi Alat >> ")

                    if not deskripsi.strip():
                        raise ValueError("Inputan Tidak Boleh Kosong!")
                    print("Inputan Anda:", deskripsi)
                except ValueError as e:
                    print("Terdapat Kesalahan Inputan:", e)

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
                        if kondisi < 1 or kondisi > 3:
                            raise ValueError("Inputan Berupa [1/2/3]")
                        break
                    except ValueError:
                        print("Inputan Berupa [1/2/3]")
                TambahAlat(nama, deskripsi,status,kondisi)
            case '2':
                clear()
                LihatAlatAdmin()
                enter()

            case '3':
                clear()
                HapusAlat()
            case '4':
                UpdateAlat()
            case '5':
                Menu_admin(idMimin)
                break
            case _:
                print("Pilihan Tidak ada")
                enter()

def TambahAlat(nama, deskripsi,status,kondisi):
    Kon, Kur = KoneksiDB()
    queryTambah = "INSERT INTO alat_kesenian (nama_alat,deskripsi, id_status_alat, id_kondisi_alat) VALUES(%s, %s, %s, %s)"
    Kur.execute(queryTambah,(nama, deskripsi,status,kondisi))
    Kon.commit()
    print("Alat Berhasil Ditambahkan!")
    enter()


def HapusAlat():
    Kon, Kur = KoneksiDB()
    clear()
    logo()
    LihatAlatAdmin()
    try:
        id = int(input("Masukkan ID Alat yang ingin dihapus >> "))
        Kur.execute("SELECT COUNT(*) FROM alat_kesenian WHERE id_alat_kesenian = %s", (id,))
        if Kur.fetchone()[0] == 0:
            print("ID Alat tidak ditemukan.")
        else:
            Kur.execute("DELETE FROM alat_kesenian WHERE id_alat_kesenian = %s", (id,))
            Kon.commit()
            print("Alat berhasil dihapus.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        Kon.close()
    enter()

def UpdateAlat():
    Kon, Kur = KoneksiDB()
    clear()
    logo()
    LihatAlatAdmin()
    try:
        id = int(input("Masukkan ID Alat yang ingin diubah >> "))
        Kur.execute("SELECT COUNT(*) FROM alat_kesenian WHERE id_alat_kesenian = %s", (id,))
        if Kur.fetchone()[0] == 0:
            print("ID Alat tidak ditemukan.")
            enter()
            return

        nama = input("Masukkan Nama Baru >> ").strip()
        deskripsi = input("Masukkan Deskripsi Baru >> ").strip()

        while True:
            try:
                status = int(input("Masukkan Status [1: Tersedia, 2: Waiting, 3: Terpinjam] >> "))
                if status < 1 or status > 3:
                    raise ValueError
                break
            except:
                print("Masukkan nilai antara 1 hingga 3.")

        while True:
            try:
                kondisi = int(input("Masukkan Kondisi [1: Baik, 2: Kurang Baik, 3: Rusak] >> "))
                if kondisi < 1 or kondisi > 3:
                    raise ValueError
                break
            except:
                print("Masukkan nilai antara 1 hingga 3.")

        Kur.execute("""
            UPDATE alat_kesenian 
            SET nama_alat = %s, deskripsi = %s, id_status_alat = %s, id_kondisi_alat = %s 
            WHERE id_alat_kesenian = %s
        """, (nama, deskripsi, status, kondisi, id))
        Kon.commit()
        print("Alat berhasil diperbarui.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        Kon.close()
    enter()


def LihatAlatAdmin():
    Kon, Kur = KoneksiDB()
    query = "SELECT * from alat_kesenian"
    try: 
        Kur.execute(query)
        alat_list = Kur.fetchall()
        print(tabulate(alat_list, headers=["ID", "Nama Alat", "Deskripsi", "Status", "Kondisi"], tablefmt="fancy_outline"))
    except Exception as e:
        print(f"Database Gagal: {e}")
    finally:
        Kon.close()

def KelolaAturan(idMimin):
    while True:
        clear()
        logo()
        print("KELOLAT Peraturan KESENIAN REOG")
        print("Selamat Datang Di Menu Admin")
        print("""
1. Tambah Peraturan
2. Hapus Peraturan
3. Ubah Peraturan
4. Lihat Peraturan
5. Kembali
""")
        pilih = input("Silahkan Pilih >> ")
        match pilih:
            case '1':
                Tambah_peraturan(idMimin)
            case '2':
                Hapus_peraturan()
            case '3':
                Update_Peraturan(idMimin)
            case '4':
                LihatPeraturan()
                enter()
            case '5':
                Menu_admin(idMimin)
                break
            case _:
                print("Pilihan Tidak ada")
                enter() 

def Tambah_peraturan(idMimin):
    kon, kur = KoneksiDB()
    try:
        peraturan = input("Masukkan peraturan baru: ")
        kur.execute("INSERT INTO peraturan (id_admin, peraturan) VALUES (%s, %s)", (idMimin, peraturan))
        kon.commit()
        print("Peraturan ditambah.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    input("Tekan Enter")

def Hapus_peraturan():
    Kon, Kur = KoneksiDB()
    clear()
    logo()
    LihatPeraturan()
    try:
        id = int(input("Masukkan ID Alat yang ingin dihapus >> "))
        Kur.execute("SELECT COUNT(*) FROM peraturan WHERE id_peraturan = %s", (id,))
        if Kur.fetchone()[0] == 0:
            print("ID Alat tidak ditemukan.")
        else:
            Kur.execute("DELETE FROM peraturan WHERE id_peraturan = %s", (id,))
            Kon.commit()
            print("Peraturan berhasil dihapus.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        Kon.close()
    enter()

def Update_Peraturan(idMimin):
    Kon, Kur = KoneksiDB()
    clear()
    logo()
    LihatPeraturan()
    try:
        id_peraturan = int(input("Masukkan ID Peraturan yang ingin diubah >> "))

        Kur.execute("SELECT COUNT(*) FROM peraturan WHERE id_peraturan = %s AND id_admin = %s", (id_peraturan, idMimin))
        if Kur.fetchone()[0] == 0:
            print("ID tidak ditemukan atau bukan milik Anda.")
            enter()

        peraturan_baru = input("Masukkan isi peraturan baru >> ").strip()
        if not peraturan_baru:
            print("Isi peraturan tidak boleh kosong.")
            enter()
        
        Kur.execute("UPDATE peraturan SET peraturan = %s WHERE id_peraturan = %s", (peraturan_baru, id_peraturan))
        Kon.commit()
        print("Peraturan berhasil diperbarui.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        Kon.close()
        enter()


def LihatPeraturan():
    kon, kur = KoneksiDB()
    try:
        kur.execute("""
            SELECT id_peraturan,peraturan
            FROM peraturan p
            ORDER BY id_peraturan
        """)
        data = kur.fetchall()
        if data:
            print(tabulate(data, headers=["No", "Peraturan"], tablefmt="fancy_outline"))
        else:
            print("Belum ada peraturan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close() 


def LihatAlatTerpinjamForAdmin(idMimin):
    kon, kur = KoneksiDB()
    try:
        kur.execute("""
        SELECT ak.id_alat_kesenian, ak.nama_alat, ak.deskripsi, ka.kondisi_alat, sak.status_alat 
        FROM alat_kesenian ak
        JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
        JOIN kondisi_alat ka ON ak.id_kondisi_alat = ka.id_kondisi_alat 
        WHERE sak.status_alat = 'Terpinjam'
        ORDER BY ak.id_alat_kesenian
        """)
        alat = kur.fetchall()
        if not alat:
            pagar()
            print("Tidak Ada Alat Yang Sedang Terpinjam".center(60))
            pagar()
            enter()
            Menu_admin(idMimin)
        print(tabulate(alat, headers=["ID", "Nama Alat", "Deskripsi", " Kondisi", "Status"], tablefmt="fancy_outline"))
        enter()
        Menu_admin(idMimin)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def HisttoryForAdmin(idMimin):
    while True:
        clear()
        logo()
        print("""
1. History Peminjaman
2. History Pengembalian
3. Kembali Ke Menu
""")
        pagar()
        pilih = input("Silahkan Pilih >> ")
        match pilih:
            case '1':
                HistoryPeminjamanForAdmin(idMimin)
                break
            case '2':
                HistoryPengembalianForAdmin(idMimin)
                break
            case '3':
                Menu_admin(idMimin)
                break
            case _:
                print("Pilihan Tidak ada")
                enter()

def HistoryPeminjamanForAdmin(idMimin):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        SELECT pn.id_peminjaman, pn.tanggal_peminjaman, pn.tenggat_pengembalian,p.nama_peminjam, ak.nama_alat, spn.status_peminjaman
        FROM alat_kesenian ak
        JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
        JOIN kondisi_alat ka ON ak.id_kondisi_alat = ka.id_kondisi_alat
        JOIN detail_peminjaman dp using(id_alat_kesenian)
        JOIN peminjaman pn using (id_peminjaman)
        JOIN status_peminjaman spn using(id_status_peminjaman)
        JOIN peminjam p using (id_peminjam)
        order by pn.id_peminjaman desc
        """)
        Peminjaman = kur.fetchall()
        if not Peminjaman:
            print("Anda Belum Pernah Melakukan Peminjaman")
            enter()
            HisttoryForAdmin(idMimin)
        print(tabulate(Peminjaman, headers=["ID Peminjaman", "Tanggal Peminjaman", "Tenggat Peminjaman", "Peminjam", "Alat", "Status Peminjaman"], tablefmt="fancy_outline"))
        enter()
        HisttoryForAdmin(idMimin)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def HistoryPengembalianForAdmin(idMimin):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        select pg.id_pengembalian, pg.id_peminjaman,pn.tanggal_peminjaman, pn.tenggat_pengembalian, pg.tanggal_pengembalian, ka.kondisi_alat, sp.status_pengembalian, jp.jenis_pelanggaran, JP.denda 
        from pengembalian pg
        JOIN peminjaman pn using (id_peminjaman)
        JOIN kondisi_alat ka using(id_kondisi_alat)
        JOIN status_pengembalian sp using (id_status_pengembalian)
        JOIN jenis_pelanggaran jp using (id_jenis_pelanggaran)
        ORDER BY pg.id_pengembalian desc
        """)
        pengembalian = kur.fetchall()
        if not pengembalian:
            print("Anda Belum Pernah Melakukan Pengembalian")
            enter()
            HisttoryForAdmin(idMimin)
        print(tabulate(pengembalian, headers=["ID Pengembalian", "ID Peminjaman","Tanggal Peminjaman", "Tenggat Pengembalian", "Tanggal Pengembalian", "Kondisi ", "Status Pengembalian", "Keterangan", "Denda"], tablefmt="fancy_outline"))
        enter()
        HisttoryForAdmin(idMimin)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def LihatPeminjamForAdmin(idMimin):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        select id_peminjam,nama_peminjam,email,nomor_telepon 
        from peminjam
        """)
        peminjam = kur.fetchall()
        if not peminjam:
            print("Belum Ada Peminjam Yang Terdaftar")
            enter()
            Menu_admin(idMimin)
        print(tabulate(peminjam, headers=["ID Peminjam", "Nama","email", "Nomor Telepon"], tablefmt="fancy_outline"))
        enter()
        Menu_admin(idMimin)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def KonfirmasiForAdmin(idMimin):
     while True:
        clear()
        logo()
        print("""
1. Konfirmasi Peminjaman
2. Konfirmasi Pengembalian
3. Kembali Ke Menu
""")
        pagar()
        pilih = input("Silahkan Pilih >> ")
        match pilih:
            case '1':
                KonfirmasiPeminjamanForAdmin(idMimin)
                break
            case '2':
                KonfirmasiPengembalianForAdmin(idMimin)
                break
            case '3':
                Menu_admin(idMimin)
                break
            case _:
                print("Pilihan Tidak ada")
                enter()

def KonfirmasiPeminjamanForAdmin(idMimin):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        SELECT pn.id_peminjaman, pn.tanggal_peminjaman, pn.tenggat_pengembalian,p.nama_peminjam, pn.keterangan,ak.nama_alat, spn.status_peminjaman
        FROM alat_kesenian ak
        JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
        JOIN kondisi_alat ka ON ak.id_kondisi_alat = ka.id_kondisi_alat
        JOIN detail_peminjaman dp using(id_alat_kesenian)
        JOIN peminjaman pn using (id_peminjaman)
        JOIN status_peminjaman spn using(id_status_peminjaman)
        JOIN peminjam p using (id_peminjam)
        WHERE pn.id_status_peminjaman = 1
        ORDER by pn.id_peminjaman
        """)
        Peminjaman = kur.fetchall()
        if not Peminjaman:
            print("Anda Belum Pernah Melakukan Peminjaman")
            enter()
            KonfirmasiForAdmin(idMimin)
        print(tabulate(Peminjaman, headers=["ID Peminjaman", "Tanggal Peminjaman", "Tenggat Peminjaman", "Peminjam","Keterangan", "Alat", "Status Peminjaman"], tablefmt="fancy_outline"))
        tampunganIdPeminjaman = [] 
        for value in Peminjaman:
            tampunganIdPeminjaman.append(value[0])
            
        while True :
            try:
                idPeminjaman = int(input("Masukkan ID Peminjaman Yang ingin di konfirmasi >> "))
                if idPeminjaman not in tampunganIdPeminjaman : 
                    raise ValueError ("Id Peminjaman Tidak Tersedia")
                else :
                    break
            except Exception as e :
                print (f"terjadi error : {e}")
                enter()
        print ("""
Konfirmasi Untuk :
1.Dipinjamkan
2.Tidak Dipinjamkan
""")
        while True :
            pilih = input("Konfirmasi Untuk >> ")
            match pilih:
                case "1":
                    KonfirmasiUntukDipinjamkan(idPeminjaman)
                    KonfirmasiForAdmin(idMimin)
                    break
                case "2":
                    KonfirmasiTidakDipinjamkan(idPeminjaman)
                    KonfirmasiForAdmin(idMimin)
                case _ :
                    print("Silahkan Pilih Opsi Yang benar")
                    enter()        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def KonfirmasiUntukDipinjamkan(idPeminjaman):
    kon,kur = KoneksiDB()
    try:
        kur.execute(f"select id_alat_kesenian from detail_peminjaman where id_peminjaman = {idPeminjaman}")
        idAlat = kur.fetchall()
        kur.execute(f"update peminjaman set id_status_peminjaman = 2 where id_peminjaman = {idPeminjaman}")
        kur.execute(f"UPDATE alat_kesenian SET id_status_alat = 2 WHERE id_alat_kesenian = {idAlat[0][0]}")
        kon.commit()
        print("Konfirmasi Telah Berhasil")
        enter()
    except Exception as e :
        print(f"Terjadi kesalahan: {e}")
        enter()

def KonfirmasiTidakDipinjamkan(idPeminjaman):
    kon,kur = KoneksiDB()
    try:
        kur.execute(f"update peminjaman set id_status_peminjaman = 3 where id_peminjaman = {idPeminjaman}")
        kon.commit()
        print("Konfirmasi Telah Berhasil")
        enter()
    except Exception as e :
        print(f"Terjadi kesalahan: {e}")
        enter()
    

def KonfirmasiPengembalianForAdmin(idMimin):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        select pg.id_pengembalian, pg.id_peminjaman,pn.tanggal_peminjaman, pn.tenggat_pengembalian, pg.tanggal_pengembalian, ka.kondisi_alat, sp.status_pengembalian, jp.jenis_pelanggaran, JP.denda 
        from pengembalian pg
        JOIN peminjaman pn using (id_peminjaman)
        JOIN kondisi_alat ka using(id_kondisi_alat)
        JOIN status_pengembalian sp using (id_status_pengembalian)
        JOIN jenis_pelanggaran jp using (id_jenis_pelanggaran)
		WHERE pg.id_status_pengembalian = 1
        ORDER BY pg.id_pengembalian 
        """)
        pengembalian = kur.fetchall()
        if not pengembalian:
            print("Anda Belum Pernah Melakukan Pengembalian")
            enter()
            HisttoryForAdmin()
        print(tabulate(pengembalian, headers=["ID Pengembalian", "ID Peminjaman","Tanggal Peminjaman", "Tenggat Pengembalian", "Tanggal Pengembalian", "Kondisi ", "Status Pengembalian", "Keterangan", "Denda"], tablefmt="fancy_outline"))
        tampunganIdPengembalian = [] 
        for value in pengembalian:
            tampunganIdPengembalian.append(value[0])
            
        while True :
            try:
                idPengembalian = int(input("Masukkan ID Peminjaman Yang ingin di konfirmasi >> "))
                if idPengembalian not in tampunganIdPengembalian : 
                    raise ValueError ("Id Peminjaman Tidak Tersedia")
                else :
                    break
            except Exception as e :
                print (f"terjadi error : {e}")
                enter()
    
        print ("""
    Kondisi :
            1. Bagus
            2. Kurang Baik
            3. Rusak
    """)
        
        while True :
                try:                
                    kondisi = int(input("Kondisi Alat >> "))
                    if kondisi > 0 and kondisi < 4:
                        break
                    else:
                        raise ValueError ("Silahkan Pilih Opsi Yang Benar")
                except Exception as e :
                    print(f"Terjadi kesalahan: {e}")
                    enter()

        keterangan = 0
        kur.execute(f"""
        select pn.tenggat_pengembalian, pg.tanggal_pengembalian
        from pengembalian pg
        JOIN peminjaman pn using (id_peminjaman)
        WHERE pg.id_status_pengembalian = 1 and pg.id_pengembalian = {idPengembalian}
        """)
        dataTanggal = kur.fetchall()
        batasPengembalian = dataTanggal[0][0]
        tanggalPengembalian = dataTanggal[0][1]

        terlambatKembali = False
        if tanggalPengembalian > batasPengembalian:
            terlambatKembali = True
        
        if terlambatKembali == True and kondisi ==3:
            keterangan += 3
        elif terlambatKembali == True :
            keterangan += 1
        elif kondisi == 3:
            keterangan += 2
        else :
            keterangan += 5

        kur.execute(f"""
        update pengembalian set id_kondisi_alat = {kondisi}, id_jenis_pelanggaran = {keterangan}, id_status_pengembalian = 2 where id_pengembalian = {idPengembalian}
        """)
        # kur.execute()
        kon.commit()
        print("Pengembalian Berhasil Dikonfirmasi")
        enter()
        Menu_admin(idMimin)

    except Exception as e :
        print(f"Terjadi kesalahan: {e}")
        enter()


#Role : Peminjam
def menu_peminjam(idPeminjam):
    while True:
        clear()
        logo()
        print("Menu Anggota/Umum")
        print("""
1. Lihat Aturan
2. Lihat Denda & Bayar
3. Lihat Alat Tersedia
4. Pinjam Alat
5. Alat Dipinjam
6. Kembalikan Alat
7. History Peminjaman
8. History Pengembalian 
9. Kembali
""")
        pilih = input("Pilih menu >> ")
        match pilih:
            case '1':
                lihat_aturan(idPeminjam)
            case '2':
                denda_peminjam(idPeminjam)
            case '3':
                LihatAlat(idPeminjam)
            case '4':
                pinjam_alat(idPeminjam)
            case '5':
                LihatAlatDipinjamForPeminjam(idPeminjam)
            case '6':
                kembalikan_alat(idPeminjam)
            case '7':
                HistoryPeminjamanForPeminjam(idPeminjam)
            case '8':
                HistoryPengembalianForPeminjam(idPeminjam)
            case '9':
                clear()
                Main()
                break
            case _:
                print("Pilihan tidak ada.")
                enter()

def denda_peminjam(idPeminjam):
    kon, kur = KoneksiDB()
    while True :
        try:
            kur.execute(f"""
            select p.nama_peminjam, dp.denda
            from peminjam p 
            join denda_peminjam dp using (id_peminjam)
            where p.id_peminjam = {idPeminjam}""")
            value = kur.fetchall()
            nama, denda = value[0]
            print(tabulate(value, headers=["Nama Peminjam", "Denda"], tablefmt="fancy_outline"))
            
            if denda == 0:
                print("Kamu tidak punya denda.")
                enter()
                menu_peminjam(idPeminjam)
                break
            
            print("""
    1. Bayar Denda
    2. Kembali ke Menu
    """)
            pilihan = input("Masukkan Pilihan >> ") 
            if pilihan == "1": 
                bayar = input("Ingin membayar denda (ya/tidak): ").lower()
                if bayar == 'ya':
                    kur.execute(f"""
                    UPDATE denda_peminjam set denda = 0 where id_peminjam = {idPeminjam}
                    """)
                    kon.commit()
                    print("Denda berhasil dibayar. Terima kasih!")
                    enter()
                    menu_peminjam(idPeminjam)
                    break
                else:
                    print("Pembayaran dibatalkan.")
                    enter()
                    menu_peminjam(idPeminjam)
                    break
            elif pilihan == "2":
                enter()
                menu_peminjam(idPeminjam)
                break
            else : 
                raise ValueError ("Pilihan Tidak Tersedia")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            enter()

def LihatAlat(idPeminjam):
    kon, kur = KoneksiDB()
    try:
        # Tampilkan alat yang tersedia
        kur.execute("""
        SELECT ak.id_alat_kesenian, ak.nama_alat, ak.deskripsi, ka.kondisi_alat, sak.status_alat 
        FROM alat_kesenian ak
        JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
        JOIN kondisi_alat ka ON ak.id_kondisi_alat = ka.id_kondisi_alat 
        WHERE sak.status_alat = 'Tersedia'
        ORDER BY ak.id_alat_kesenian
        """)
        alat = kur.fetchall()
        if not alat:
            pagar()
            print("Tidak Ada Alat Yang Tersedia - Semua Alat Sudah Dipinjam".center(60))
            pagar()
            enter()
            menu_peminjam(idPeminjam)
        print(tabulate(alat, headers=["ID", "Nama Alat", "Deskripsi", " Kondisi", "Status"], tablefmt="fancy_outline"))
        enter()
        menu_peminjam(idPeminjam)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    
def saldoDenda(idPeminjam):
    denda = 0
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        select denda from denda_peminjam where id_peminjam = {idPeminjam}
        """)
        value = kur.fetchone()
        if value[0] == 0:
            denda = 0
        else :    
            denda += value[0]
    except Exception as e:
        print (f"Terjadi kesalahan: {e}")
    return denda 


def pinjam_alat(idPeminjam):
    kon, kur = KoneksiDB()
    saldo = saldoDenda(idPeminjam)
    try:
        if saldo > 0:
            print ("Anda Masih Memiliki denda, Silahkan Bayar Denda Terlebih Dahulu")
            enter()
            menu_peminjam(idPeminjam)
        # Tampilkan alat yang tersedia
        kur.execute("""
        SELECT ak.id_alat_kesenian, ak.nama_alat, ak.deskripsi, ka.kondisi_alat, sak.status_alat 
        FROM alat_kesenian ak
        JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
        JOIN kondisi_alat ka ON ak.id_kondisi_alat = ka.id_kondisi_alat 
        WHERE sak.status_alat = 'Tersedia'
        ORDER BY ak.id_alat_kesenian
        """)
        alat = kur.fetchall()
        if not alat:
            pagar()
            print("Tidak Ada Alat Yang Tersedia - Semua Alat Sudah Dipinjam".center(60))
            pagar()
            enter()
            menu_peminjam(idPeminjam)
        print(tabulate(alat, headers=["ID", "Nama Alat", "Deskripsi", " Kondisi", "Status"], tablefmt="fancy_outline"))
        tampunganIdAlat = []
        namaAlat  = []
        deskripsiAlat = []
        kondisiAlat = []
        statusAlat = []
        for value in alat :
            tampunganIdAlat.append(value[0])
            namaAlat.append(value[1])
            deskripsiAlat.append(value[2])
            kondisiAlat.append(value[3])
            statusAlat.append(value[4])

        while True :
            try:
                id_alat = int(input("Masukkan ID alat : "))
                if id_alat not in tampunganIdAlat : 
                    raise ValueError ("Id alat Tidak Tersedia")
                else :
                    break
            except Exception as e :
                print (f"terjadi error : {e}")
                enter()

        while True :
            try:
                keterangan = input("Keterangan peminjaman: ")
                if len(keterangan) < 4 : 
                    raise ValueError ("keterangan tidak valid")
                else :
                    break
            except Exception as e :
                print (f"terjadi error : {e}")
                enter()
        while True :
            try:
                hari_pinjam = int(input("Pinjam berapa hari? "))
                if hari_pinjam > 0 : 
                    break
                else :
                    raise ValueError ("hari pinjam tidak valid")
            except Exception as e :
                print (f"terjadi error : {e}")
                enter()

        tanggal_peminjaman = datetime.datetime.now()
        tenggat_pengembalian = tanggal_peminjaman + datetime.timedelta(days=hari_pinjam)

        kur.execute("SELECT id_admin FROM admin ORDER BY RANDOM() LIMIT 1")
        id_admin = kur.fetchone()[0]

        # Status peminjaman 'Dipinjamkan'

        # Insert ke peminjaman
        kur.execute("""
            INSERT INTO peminjaman (tanggal_peminjaman, tenggat_pengembalian, keterangan, id_peminjam, id_admin, id_status_peminjaman)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_peminjaman
        """, (tanggal_peminjaman, tenggat_pengembalian, keterangan, idPeminjam, id_admin, 1))
        id_peminjaman = kur.fetchone()[0]

        # Insert ke detail_peminjaman
        kur.execute("INSERT INTO detail_peminjaman (id_peminjaman, id_alat_kesenian) VALUES (%s, %s)", (id_peminjaman, id_alat))

       

        kon.commit()
        print("Peminjaman berhasil dilakukan, silahkan menunggu admin untuk mengkonfirmasi")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    enter()

def LihatAlatDipinjamForPeminjam(idPeminjam):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        SELECT pn.id_peminjaman, pn.tanggal_peminjaman, pn.tenggat_pengembalian,p.nama_peminjam, ak.nama_alat
        FROM alat_kesenian ak
        JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
        JOIN kondisi_alat ka ON ak.id_kondisi_alat = ka.id_kondisi_alat
        JOIN detail_peminjaman dp using(id_alat_kesenian)
        JOIN peminjaman pn using (id_peminjaman)
        JOIN status_peminjaman spn using(id_status_peminjaman)
        JOIN peminjam p using (id_peminjam)
        WHERE id_peminjam = {idPeminjam} and pn.id_status_peminjaman = 2
        order by pn.id_peminjaman desc
        """)
        alat = kur.fetchall()
        if not alat:
            print("Alat Tidak Tersedia")
            enter()
            menu_peminjam(idPeminjam)
        print(tabulate(alat, headers=["ID Peminjaman", "Tanggal Peminjaman", "Tenggat Peminjaman", "Peminjam", "Alat"], tablefmt="fancy_outline"))
        enter()
        menu_peminjam(idPeminjam)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def lihat_aturan(idPeminjam):
    kon, kur = KoneksiDB()
    try:
        kur.execute("""
            SELECT id_peraturan,peraturan
            FROM peraturan p
            ORDER BY id_peraturan
        """)
        data = kur.fetchall()
        if data:
            print(tabulate(data, headers=["No", "Peraturan"], tablefmt="fancy_outline"))
        else:
            print("Belum ada peraturan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        kon.close()
    enter()
    menu_peminjam(idPeminjam)

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

def kembalikan_alat(idPeminjam):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        SELECT pn.id_peminjaman, pn.tanggal_peminjaman, pn.tenggat_pengembalian,p.nama_peminjam, ak.nama_alat
        FROM alat_kesenian ak
        JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
        JOIN kondisi_alat ka ON ak.id_kondisi_alat = ka.id_kondisi_alat
        JOIN detail_peminjaman dp using(id_alat_kesenian)
        JOIN peminjaman pn using (id_peminjaman)
        JOIN status_peminjaman spn using(id_status_peminjaman)
        JOIN peminjam p using (id_peminjam)
        WHERE pn.id_peminjam = {idPeminjam} and pn.id_status_peminjaman = 2
        order by pn.id_peminjaman desc
        """)
        alat = kur.fetchall()
        if not alat:
            print("Tidak Ada Alat Yang Perlu Dikembalikan")
            enter()
            menu_peminjam(idPeminjam)
        print(tabulate(alat, headers=["ID Peminjaman", "Tanggal Peminjaman", "Tenggat Peminjaman", "Peminjam", "Alat"], tablefmt="fancy_outline"))
        tampunganIdPeminjaman = []
        for value in alat :
            tampunganIdPeminjaman.append(value[0])
            
        while True :
            try:
                idPeminjaman = int(input("Masukkan ID Peminjaman yang ingin dikembalikan: "))
                if idPeminjaman in tampunganIdPeminjaman :
                    break
                else :
                    raise ValueError("Id Peminjaman tidak valid")
            except Exception as e :
                print(f"Terjadi kesalahan: {e}")
                enter()

        kur.execute(f"""
        INSERT INTO pengembalian (tanggal_pengembalian, id_peminjaman, id_kondisi_alat, id_status_pengembalian, id_jenis_pelanggaran)
        VALUES 
        (NOW(), {idPeminjaman}, 1, 1, 1)
        """)
        kur.execute(f"UPDATE peminjaman SET id_status_peminjaman = 4 WHERE id_peminjaman = {idPeminjaman}")
        kon.commit()
        print("Pengembalian berhasil!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    kon.close()
    enter()
    menu_peminjam(idPeminjam)

def HistoryPeminjamanForPeminjam(idPeminjam):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        SELECT pn.id_peminjaman, pn.tanggal_peminjaman, pn.tenggat_pengembalian,p.nama_peminjam, ak.nama_alat, spn.status_peminjaman
        FROM alat_kesenian ak
        JOIN status_alat_kesenian sak ON ak.id_status_alat = sak.id_status_alat
        JOIN kondisi_alat ka ON ak.id_kondisi_alat = ka.id_kondisi_alat
        JOIN detail_peminjaman dp using(id_alat_kesenian)
        JOIN peminjaman pn using (id_peminjaman)
        JOIN status_peminjaman spn using(id_status_peminjaman)
        JOIN peminjam p using (id_peminjam)
        WHERE pn.id_peminjam = {idPeminjam}
        order by pn.id_peminjaman desc
        """)
        Peminjaman = kur.fetchall()
        if not Peminjaman:
            print("Anda Belum Pernah Melakukan Peminjaman")
            enter()
            menu_peminjam(idPeminjam)
        print(tabulate(Peminjaman, headers=["ID Peminjaman", "Tanggal Peminjaman", "Tenggat Peminjaman", "Peminjam", "Alat", "Status Peminjaman"], tablefmt="fancy_outline"))
        enter()
        menu_peminjam(idPeminjam)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def HistoryPengembalianForPeminjam(idPeminjam):
    kon, kur = KoneksiDB()
    try:
        kur.execute(f"""
        select pg.id_pengembalian, pg.id_peminjaman,pn.tanggal_peminjaman, pn.tenggat_pengembalian, pg.tanggal_pengembalian, ka.kondisi_alat, sp.status_pengembalian, jp.jenis_pelanggaran, JP.denda 
        from pengembalian pg
        JOIN peminjaman pn using (id_peminjaman)
        JOIN kondisi_alat ka using(id_kondisi_alat)
        JOIN status_pengembalian sp using (id_status_pengembalian)
        JOIN jenis_pelanggaran jp using (id_jenis_pelanggaran)
        WHERE id_peminjam = {idPeminjam}
        ORDER BY pg.id_pengembalian desc
        """)
        pengembalian = kur.fetchall()
        if not pengembalian:
            print("Anda Belum Pernah Melakukan Pengembalian")
            enter()
            menu_peminjam(idPeminjam)
        print(tabulate(pengembalian, headers=["ID Pengembalian", "ID Peminjaman","Tanggal Peminjaman", "Tenggat Pengembalian", "Tanggal Pengembalian", "Kondisi ", "Status Pengembalian", "Keterangan", "Denda"], tablefmt="fancy_outline"))
        enter()
        menu_peminjam(idPeminjam)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


if __name__ == "__main__":
    # Main()
    # saldoDenda(idPeminjam=1)
    # menu_peminjam(idPeminjam=1)
    # UpdateAlat()
    Menu_admin(idMimin=1)
    # LihatAlatTerpinjamForAdmin()