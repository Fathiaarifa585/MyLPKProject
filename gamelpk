def tampilkan_menu_utama():
    print("\n=== Game Uji Kualitatif Senyawa Organik dan Anorganik ===")
    print("1. Materi")
    print("2. Latihan")
    print("3. Keluar")

def tampilkan_materi():
    while True:
        print("\n=== Menu Materi ===")
        print("1. Materi Organik")
        print("2. Materi Anorganik")
        print("3. Kembali")
        pilihan = input("Pilih: ")

        if pilihan == '1':
            print("\n--- Materi Organik ---")
            print("Senyawa organik mengandung karbon, seperti alkohol, karbohidrat, dan protein.")
        elif pilihan == '2':
            print("\n--- Materi Anorganik ---")
            print("Senyawa anorganik seperti garam, asam, basa, dan oksida logam.")
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")

def latihan_soal():
    soal = {
        "pertanyaan": "Senyawa manakah yang termasuk senyawa organik?",
        "pilihan": ["NaCl", "C6H12O6", "FeSO4", "CuO"],
        "jawaban": 2,
        "pembahasan": "C6H12O6 adalah glukosa, senyawa organik karena mengandung karbon dan hidrogen."
    }

    print("\n=== Latihan Soal ===")
    print(soal["pertanyaan"])
    for i, opsi in enumerate(soal["pilihan"], start=1):
        print(f"{i}. {opsi}")

    try:
        jawaban = int(input("Jawaban Anda (1-4): "))
        if jawaban == soal["jawaban"]:
            print("Jawaban kamu BENAR!")
        else:
            print("Jawaban kamu SALAH.")
        print("Pembahasan:", soal["pembahasan"])
    except:
        print("Input tidak valid.")

def main():
    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_materi()
        elif pilihan == '2':
            latihan_soal()
        elif pilihan == '3':
            print("Terima kasih telah bermain!")
            break
        else:
            print("Pilihan tidak valid.")

if _name_ == "_main_":
    main()
