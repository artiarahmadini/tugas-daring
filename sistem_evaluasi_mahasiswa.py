# SISTEM EVALUASI MAHASISWA
# Algoritma dan Pemrograman Python

print("=========================================")
print("SISTEM EVALUASI MAHASISWA")
print("=========================================")

# input data mahasiswa

nama = input("Masukkan Nama Mahasiswa: ")
tugas = float(input("Masukkan Nilai Tugas: "))
uts = float(input("Masukkan Nilai UTS: "))
uas = float(input("Masukkan Nilai UAS: "))
kehadiran = float(input("Masukkan Kehadiran (%): "))

#Menghitung Nilai Akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

#Menentukan Status Kelulusan
if nilai_akhir >= 75 and kehadiran >= 80:
    if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir %2 == 0:
        status = "LULUS DENGAN PREDIKAT"
    else:
        status = "LULUS"
else:
    status = "BELUM LULUS"

#Menampilkan Hasil
print("\n================================")
print(" HASIL EVALUASI")
print("==================================")
print("Nama            :", nama)
print("Nilai Akhir     :", round(nilai_akhir, 2))
print("Kehadiran       :", str(kehadiran) + "%")
print("status          :", status)
print("==================================")