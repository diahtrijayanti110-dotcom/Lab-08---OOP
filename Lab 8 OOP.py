class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah(self):
        print("\n=== TAMBAH DATA MAHASISWA ===")
        nim = input("NIM       : ")
        nama = input("Nama      : ")
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))

        nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

        self.data[nama.lower()] = {
            "NIM": nim,
            "Nama": nama,
            "Tugas": tugas,
            "UTS": uts,
            "UAS": uas,
            "Akhir": round(nilai_akhir, 2)
        }

        print(">> Data berhasil ditambahkan!\n")

    def tampilkan(self):
        if not self.data:
            print("\n>> Belum ada data!\n")
            return

        print("\n=== DAFTAR NILAI MAHASISWA ===")
        print("=" * 75)
        print(f"{'NIM':<10} {'Nama':<20} {'Tugas':<8} {'UTS':<8} {'UAS':<8} {'Akhir':<8}")
        print("=" * 75)

        for mhs in self.data.values():
            print(f"{mhs['NIM']:<10} {mhs['Nama']:<20} {mhs['Tugas']:<8} {mhs['UTS']:<8} {mhs['UAS']:<8} {mhs['Akhir']:<8}")

        print("=" * 75 + "\n")

    def hapus(self, nama):
        key = nama.lower()
        if key in self.data:
            del self.data[key]
            print(f">> Data '{nama}' berhasil dihapus.\n")
        else:
            print(">> Nama tidak ditemukan.\n")

    def ubah(self, nama):
        key = nama.lower()
        if key not in self.data:
            print(">> Nama tidak ditemukan.\n")
            return

        print("\n=== UBAH DATA MAHASISWA ===")
        nim = input("NIM baru       : ")
        tugas = float(input("Nilai Tugas baru : "))
        uts = float(input("Nilai UTS baru   : "))
        uas = float(input("Nilai UAS baru   : "))

        nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

        self.data[key] = {
            "NIM": nim,
            "Nama": nama,
            "Tugas": tugas,
            "UTS": uts,
            "UAS": uas,
            "Akhir": round(nilai_akhir, 2)
        }

        print(">> Data berhasil diubah!\n")


# ============================
# PROGRAM UTAMA
# ============================
mhs = DaftarNilaiMahasiswa()
while True:
    print("=== MENU DATA NILAI MAHASISWA ===")
    print("[T] Tambah Data")
    print("[L] Lihat/Tampilkan Data")
    print("[H] Hapus Data")
    print("[U] Ubah Data")
    print("[K] Keluar")
    pilih = input("Pilih menu: ").upper()

    if pilih == "T":
        mhs.tambah()
    elif pilih == "L":
        mhs.tampilkan()
    elif pilih == "H":
        nama = input("Masukkan nama yang ingin dihapus: ")
        mhs.hapus(nama)
    elif pilih == "U":
        nama = input("Masukkan nama yang ingin diubah: ")
        mhs.ubah(nama)
    elif pilih == "K":
        print("Program selesai.")
        break
    else:
        print(">> Pilihan tidak ada, coba lagi.\n")
