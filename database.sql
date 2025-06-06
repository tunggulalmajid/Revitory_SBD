DROP TABLE IF EXISTS peraturan;
DROP TABLE IF EXISTS pengembalian;
DROP TABLE IF EXISTS status_pengembalian;
DROP TABLE IF EXISTS jenis_pelanggaran;
DROP TABLE IF EXISTS denda_peminjam;
DROP TABLE IF EXISTS detail_peminjaman;
DROP TABLE IF EXISTS peminjaman;
DROP TABLE IF EXISTS status_peminjaman;
DROP TABLE IF EXISTS alat_kesenian;
DROP TABLE IF EXISTS kondisi_alat;
DROP TABLE IF EXISTS status_alat_kesenian;
DROP TABLE IF EXISTS alamat;
DROP TABLE IF EXISTS peminjam;
DROP TABLE IF EXISTS jalan;
DROP TABLE IF EXISTS Kecamatan;
DROP TABLE IF EXISTS kabupaten;
DROP TABLE IF EXISTS provinsi;
DROP TABLE IF EXISTS Admin;

-- Tabel Admin
CREATE TABLE admin (
    id_admin SERIAL PRIMARY KEY,
    nama VARCHAR(255) NOT NULL,
    username_admin VARCHAR(100) NOT NULL,
    password_admin VARCHAR(100) NOT NULL
);

-- Tabel provinsi
CREATE TABLE provinsi (
    id_provinsi SERIAL PRIMARY KEY,
    provinsi VARCHAR(255) NOT NULL
);

-- Tabel kabupaten
CREATE TABLE kabupaten (
    id_kabupaten SERIAL PRIMARY KEY,
    kabupaten VARCHAR(225) NOT NULL,
    id_provinsi INTEGER NOT NULL,
    FOREIGN KEY (id_provinsi) REFERENCES provinsi(id_provinsi)
);

-- Tabel kecamatan
CREATE TABLE kecamatan (
    id_kecamatan SERIAL PRIMARY KEY,
    kecamatan VARCHAR(255) NOT NULL,
    id_kabupaten INTEGER NOT NULL,
    FOREIGN KEY (id_kabupaten) REFERENCES kabupaten(id_kabupaten)
);

-- Tabel jalan
CREATE TABLE jalan (
    id_jalan SERIAL PRIMARY KEY,
    jalan VARCHAR(255) NOT NULL,
    id_kecamatan INTEGER NOT NULL,
    FOREIGN KEY (id_kecamatan) REFERENCES kecamatan(id_kecamatan)
);

-- Tabel peminjam
CREATE TABLE peminjam (
    id_peminjam SERIAL PRIMARY KEY,
    nama_peminjam VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    nomor_telepon NUMERIC(28,0) NOT NULL,
    username VARCHAR(100) NOT NULL,
    password_user VARCHAR(100) NOT NULL,
    is_banned BOOLEAN NOT NULL
);

-- Tabel alamat
CREATE TABLE alamat (
    id_alamat SERIAL PRIMARY KEY,
    id_peminjam INTEGER NOT NULL,
    id_jalan INTEGER NOT NULL,
    FOREIGN KEY (id_jalan) REFERENCES jalan(id_jalan),
    FOREIGN KEY (id_peminjam) REFERENCES peminjam(id_peminjam)
);

-- Tabel kondisi_alat
CREATE TABLE kondisi_alat (
    id_kondisi_alat SERIAL PRIMARY KEY,
    kondisi_alat VARCHAR(100) NOT NULL
);

-- Tabel status_alat_kesenian
CREATE TABLE status_alat_kesenian (
    id_status_alat SERIAL PRIMARY KEY,
    status_alat VARCHAR(100) NOT NULL
);

-- Tabel alat_kesenian
CREATE TABLE alat_kesenian (
    id_alat_kesenian SERIAL PRIMARY KEY,
    nama_alat VARCHAR(255) NOT NULL,
    deskripsi TEXT,
    id_status_alat INTEGER NOT NULL,
    id_kondisi_alat INTEGER NOT NULL,
    FOREIGN KEY (id_kondisi_alat) REFERENCES kondisi_alat(id_kondisi_alat),
    FOREIGN KEY (id_status_alat) REFERENCES status_alat_kesenian(id_status_alat)
);

-- Tabel status_peminjaman
CREATE TABLE status_peminjaman (
    id_status_peminjaman SERIAL PRIMARY KEY,
    status_peminjaman VARCHAR(100) NOT NULL
);

-- Tabel peminjaman
CREATE TABLE peminjaman (
    id_peminjaman SERIAL PRIMARY KEY,
    tanggal_peminjaman TIMESTAMP NOT NULL,
    tenggat_pengembalian TIMESTAMP NOT NULL,
    keterangan TEXT NOT NULL,
    id_peminjam INTEGER NOT NULL,
    id_admin INTEGER NOT NULL,
    id_status_peminjaman INTEGER NOT NULL,
    FOREIGN KEY (id_admin) REFERENCES admin(id_admin),
    FOREIGN KEY (id_peminjam) REFERENCES peminjam(id_peminjam),
    FOREIGN KEY (id_status_peminjaman) REFERENCES status_peminjaman(id_status_peminjaman)
);

-- Tabel detail_peminjaman
CREATE TABLE detail_peminjaman (
    id_peminjaman INTEGER NOT NULL,
    id_alat_kesenian INTEGER NOT NULL,
    FOREIGN KEY (id_peminjaman) REFERENCES peminjaman(id_peminjaman),
    FOREIGN KEY (id_alat_kesenian) REFERENCES alat_kesenian(id_alat_kesenian)
);

-- Tabel jenis_pelanggaran
CREATE TABLE jenis_pelanggaran (
    id_jenis_pelangaran SERIAL PRIMARY KEY,
    jenis_pelanggaran VARCHAR(255) NOT NULL,
    denda NUMERIC(19,4) NOT NULL
);

-- Tabel status_pengembalian
CREATE TABLE status_pengembalian (
    id_status_pengembalian SERIAL PRIMARY KEY,
    status_pengembalian VARCHAR(100) NOT NULL
);

-- Tabel pengembalian
CREATE TABLE pengembalian (
    id_pengembalian SERIAL PRIMARY KEY,
    tanggal_pengembalian TIMESTAMP NOT NULL,
    id_peminjaman INTEGER NOT NULL,
    id_kondisi_alat INTEGER NOT NULL,
    id_status_pengembalian INTEGER NOT NULL,
    id_jenis_pelangaran INTEGER NOT NULL,
    FOREIGN KEY (id_peminjaman) REFERENCES peminjaman(id_peminjaman),
    FOREIGN KEY (id_kondisi_alat) REFERENCES kondisi_alat(id_kondisi_alat),
    FOREIGN KEY (id_status_pengembalian) REFERENCES status_pengembalian(id_status_pengembalian),
    FOREIGN KEY (id_jenis_pelangaran) REFERENCES jenis_pelanggaran(id_jenis_pelangaran)
);

-- Tabel denda_peminjam
CREATE TABLE denda_peminjam (
    id_denda_peminjam SERIAL PRIMARY KEY,
    denda NUMERIC(19,2) NOT NULL,
    id_peminjam INTEGER NOT NULL,
    FOREIGN KEY (id_peminjam) REFERENCES peminjam(id_peminjam)
);

-- Tabel peraturan
CREATE TABLE peraturan (
    id_peraturan SERIAL PRIMARY KEY,
    id_admin INTEGER NOT NULL,
    peraturan TEXT NOT NULL,
    FOREIGN KEY (id_admin) REFERENCES admin(id_admin)
);


-- Admin
INSERT INTO Admin (nama, username_admin, password_admin)
VALUES 
('Yanto', 'admin', '111'),
('Tunggul', 'adad', '222'),
('Rafi', 'mimin', '333');

-- Provinsi
INSERT INTO provinsi (provinsi)
VALUES 
('Jawa Timur'),
('Jawa Tengah'),
('Jawa Barat');

-- Kabupaten
INSERT INTO kabupaten (kabupaten, id_provinsi)
VALUES 
('Jember', 1),
('Malang', 1),
('Bandung', 2);

-- Kecamatan
INSERT INTO Kecamatan (kecamatan,id_kabupaten)
VALUES 
('Kecamatan sumbersari', 1),
('Kecamatan Ambulu', 1),
('Kecamatan Cimahi', 2);

-- Jalan
INSERT INTO jalan (jalan, id_kecamatan)
VALUES 
('Jl. Halmahera', 1),
('Jl. Jawa', 2),
('Jl. Homan', 3);

-- Peminjam
INSERT INTO peminjam (nama_peminjam, email, nomor_telepon, username, password_user, is_banned)
VALUES 
('Lubia Fahri', 'lubia@gmail.com', 8123456789, 'lubi', '1122', false),
('Anon Nimo', 'Anon@gmail.com', 8123456790, 'anon', '2233', false),
('Roi Naz', 'Naz@gmail.com', 8123456790, 'roihan', 'roi', false),
('Dimaz Kanjar', 'Kanjar@gmail.com', 8123456790, 'Dimas', 'mas123', true),
('Firman Abdul', 'Firman@gmail.com', 8123456790, 'kecap', '1111', true);

-- Alamat
INSERT INTO alamat (id_peminjam, id_jalan)
VALUES 
(1, 1),
(2, 2),
(3, 3);
-- sampe sinii terakhir data dummy
-- Status Alat Kesenian
INSERT INTO status_alat_kesenian (status_alat)
VALUES 
('Tersedia'),
('Terpinjam');

-- Kondisi Alat
INSERT INTO kondisi_alat (kondisi_alat)
VALUES 
('Baik'),
('Kurang Baik'),
('Rusak');

-- Alat Kesenian (ganti)
INSERT INTO alat_kesenian (nama_alat, deskripsi, id_status_alat, id_kondisi_alat)
VALUES 
('Dadak Merak', 'Topeng reyog ponorogo', 2, 1),
('Dadak Merak', 'Topeng reyog ponorogo', 1, 2),
('Celana', 'Celana berwarna hitam polos', 1, 3),
('Samiran', 'pedang reyog ponorogo', 1, 2);

-- Status Peminjaman
INSERT INTO status_peminjaman (status_peminjaman)
VALUES 
('Dipinjamkan'),
('Dikembalikan');

-- Peminjaman
INSERT INTO peminjaman (tanggal_peminjaman, tenggat_pengembalian, keterangan, id_peminjam, id_admin, id_status_peminjaman)
VALUES 
(NOW()- INTERVAL '8 days', NOW() + INTERVAL '1 days', 'Latihan Rutinan', 4, 1, 2),
(NOW() - INTERVAL '5 days', NOW() + INTERVAL '2 days', 'Pentas Seni', 2, 2, 2),
(NOW() - INTERVAL '9 days', NOW() + INTERVAL '7 days', 'Lomba', 2, 3, 2),
(NOW(), NOW() + INTERVAL '7 days', 'Latihan Rutinan', 1, 1, 1),
(NOW(), NOW() + INTERVAL '5 days', 'Pentas Seni', 1, 3, 1);
select * from peminjaman
select * from status_peminjaman

-- Detail Peminjaman
INSERT INTO detail_peminjaman (id_peminjaman, id_alat_kesenian)
VALUES 
(1, 3),
(2, 2);
select * from detail_peminjaman
select * from alat_kesenian
select * from peminjaman
select * from status_alat_kesenian
-- Denda Peminjam
INSERT INTO denda_peminjam (denda, id_peminjam)
VALUES 
(50000, 1),
(75000, 2);

-- Jenis Pelanggaran
INSERT INTO jenis_pelanggaran (jenis_pelanggaran, denda)
VALUES 
('Terlambat', 20000),
('Hilang', 300000),
('Rusak', 100000);

-- Status Pengembalian
INSERT INTO status_pengembalian (status_pengembalian)
VALUES 
('Menunggu Konfirmasi'),
('Dikembalikan Baik'),
('Dikembalikan Terlambat'),
('Dikembalikan Rusak');

-- Pengembalian
INSERT INTO pengembalian (tanggal_pengembalian, id_peminjaman, id_kondisi_alat, id_status_pengembalian, id_jenis_pelangaran)
VALUES 
(NOW(), 1, 1, 1, 1),
(NOW(), 2, 2, 2, 2);
select * from pengembalian
-- Peraturan (ganti)
INSERT INTO peraturan (id_admin, peraturan)
VALUES 
(1, 'Peraturan 1 tentang peminjaman'),
(2, 'Peraturan 2 tentang pengembalian');

-- select * from admin
-- select * from peminjam
-- select * from alamat
-- select * from alat_kesenian
-- select * from peraturan
-- select * from denda_peminjam