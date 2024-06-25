CREATE TABLE jumlah_pencari_kerja (
    no SERIAL PRIMARY KEY,
    kode_wilayah VARCHAR(50),
    wilayah VARCHAR(100),
    tahun INTEGER,
    jumlah_pencari_kerja INTEGER
);

CREATE TABLE sekolah_dasar (
    id SERIAL PRIMARY KEY,
    kode_wilayah VARCHAR(50),
    wilayah VARCHAR(255),
    tahun INTEGER,
    jumlah_sekolah INTEGER
);

