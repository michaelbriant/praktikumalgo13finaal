# kasus 1
# Nilai ujian
nilai_siswa = [90, 99, 97, 96, 98]

# Menghitung rata-rata nilai kelas
rata_rata_nilai_kelas = sum(nilai_siswa) / len(nilai_siswa)

# Menentukan siswa yang mendapatkan nilai di atas rata-rata kelas
nilai_di_atas_rata_rata = [nilai for nilai in nilai_siswa if nilai > rata_rata_nilai_kelas]

print(f"Rata-rata nilai kelas: {rata_rata_nilai_kelas:.2f}")
print(f"Siswa yang mendapatkan nilai di atas rata - rata: {nilai_di_atas_rata_rata}")


# kasus 2
# fungsi untuk mengkonversi rupiah ke dolar
def konversi_mata_uang (jumlah_rupiah, kurs_dolar):
    jumlah_dolar = jumlah_rupiah / kurs_dolar
    return jumlah_dolar

# menginput rupiah dan kurs dolar
jumlah_rupiah = float(input("Masukkan jumlah uang dalam rupiah: "))
kurs_dolar = float(input("Masukkan kurs Dolar terhadap rupiah: "))


jumlah_dolar = konversi_mata_uang(jumlah_rupiah, kurs_dolar)
print(f"Jumlah uang dalam Dolar: ${jumlah_dolar:.2f}")


# kasus 3
proyek_list = [
    {"nama": "Proyek A", "status": "Selesai", "estimasi_waktu": 10},
    {"nama": "Proyek B", "status": "Dalam Pengerjaan", "estimasi_waktu": 20},
    {"nama": "Proyek C", "status": "Dalam Pengerjaan", "estimasi_waktu": 15},
    {"nama": "Proyek D", "status": "Selesai", "estimasi_waktu": 8},
]
proyek_dalam_pengerjaan = [proyek for proyek in proyek_list if proyek["status"] == "Dalam Pengerjaan"]

def bubble_sort_proyek(proyek_list):
    n = len(proyek_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if proyek_list[j]["estimasi_waktu"] > proyek_list[j + 1]["estimasi_waktu"]:
                proyek_list[j], proyek_list[j + 1] = proyek_list[j + 1], proyek_list[j]

print("Proyek yang masih dalam pengerjaan:")
for proyek in proyek_dalam_pengerjaan:
    print(f"Nama: {proyek['nama']}, Estimasi Waktu: {proyek['estimasi_waktu']} hari, Status: {proyek['status']}")

bubble_sort_proyek(proyek_dalam_pengerjaan)

print("\nProyek dalam pengerjaan yang diurutkan berdasarkan estimasi waktu:")
for proyek in proyek_dalam_pengerjaan:
    print(f"Nama: {proyek['nama']}, Estimasi Waktu: {proyek['estimasi_waktu']} hari, Status: {proyek['status']}")
