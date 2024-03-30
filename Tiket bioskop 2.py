# Meminta input data diri pembeli
nama = input("Nama: ")
alamat = input("Alamat: ")
usia = int(input("Usia: "))

# Menampilkan daftar genre film
print("\nDaftar Genre Film:")
print("1. Horor\n2. Komedi\n3. Romantis\n4. Action\n5. Anime")

# Meminta input genre film yang dipilih
genre = int(input("Pilih genre film (1-5): "))

# Menampilkan daftar film sesuai genre yang dipilih
if genre == 1:
    films = ["Valak", "The Conjuring", "Annabelle", "The Nun 1", "The Nun 2"]
elif genre == 2:
    films = ["Wakil DKI Reborn", "Ngeri-ngeri Sedap", "Agak Lain", "Guru-guru Masa Kini", "Pasutri Gaje"]
elif genre == 3:
    films = ["Dilan 1990", "Dilan 1991", "Argantara", "Mariposa", "Dear Nathan"]
elif genre == 4:
    films = ["Lift", "Argylle", "Damsel", "Badland Hunters", "Aquaman and Lost Kingdom"]
elif genre == 5:
    films = ["Suzume", "Ocean Waves", "Flavors Of Youth", "A Whisker Away", "A Silent Voice"]

# Validasi usia dan menampilkan film yang dipilih
if usia >= 17:
    print("\nTerima kasih,", nama, "!")
    print("Alamat:", alamat)
    print("Usia:", usia)
    choice = int(input("Pilih nomor film yang ingin ditonton: "))
    if 1 <= choice <= 5:
        print("Anda memilih film:", films[choice - 1])
        print("Harga tiket: Rp50.000,-")
    else:
        print("Pilihan tidak valid.")
else:
    print("Maaf,", nama, "! Anda belum cukup umur untuk menonton film.")
