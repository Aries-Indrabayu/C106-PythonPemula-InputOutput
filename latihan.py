# Kasus: Program Pendaftaran Pengguna
#  variabelnya nama, usia, email dan hobi
#  target menampilkan informasi dengan format rapi
nama = input("Masukkan nama lengkap Anda: ")
while True:
    try:
        usia = int(input("Masukkan usia Anda: "))
        if usia <= 0:
            print("Usia harus lebih dari 0. Coba lagi.")
            continue
        break
    except ValueError:
        print("Masukkan angka yang valid untuk usia.")

email = input("Masukkan alamat email Anda: ")
hobi = input("Masukkan hobi Anda: ")

# Menampilkan hasil dengan format string
print("\n📄 Data Pendaftaran Pengguna 📄")
print("=" * 40)
print(f"👨 Nama    : {nama}")
print(f"🎂 Usia     : {usia} tahun")
print(f"✉ Email    : {email}")
print(f"🎨 Hobi    : {hobi}")
print("=" * 40)

# Menampilkan pesan berdasarkan usia
if usia < 18:
    print("👧 Anda masih remaja. Tetap semangat belajar!")
elif usia < 40:
    print("🧔 Anda berada di usia produktif. Tetap berkarya!")
else:
    print("👩‍🦳 Anda memiliki banyak pengalaman hidup. Bagikan dengan generasi muda!")