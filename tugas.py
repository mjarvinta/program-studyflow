import json
import os
from datetime import datetime

# File untuk menyimpan data
DATA_FILE = "tugas_list.json"


def load_tugas():
    """Load daftar tugas dari file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []


def save_tugas(tugas_list):
    """Simpan daftar tugas ke file"""
    with open(DATA_FILE, "w") as f:
        json.dump(tugas_list, f, indent=2)


def tampilkan_menu():
    """Tampilkan menu utama"""
    print("\n" + "="*50)
    print("        APLIKASI TO-DO LIST SEDERHANA")
    print("="*50)
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas baru")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Hapus semua tugas")
    print("0. Keluar")
    print("="*50)


def lihat_tugas(tugas_list):
    """Tampilkan semua tugas"""
    if not tugas_list:
        print("\n❌ Tidak ada tugas. Mulai buat tugas baru!")
        return
    
    print("\n" + "="*50)
    print("            DAFTAR TUGAS ANDA")
    print("="*50)
    
    for i, tugas in enumerate(tugas_list, 1):
        status = "✅" if tugas["selesai"] else "⭕"
        print(f"{i}. [{status}] {tugas['nama']}")
        print(f"   Dibuat: {tugas['waktu']}")
        if tugas["selesai"]:
            print(f"   Selesai: {tugas['waktu_selesai']}")
        print()


def tambah_tugas(tugas_list):
    """Tambah tugas baru"""
    nama_tugas = input("\n📝 Masukkan tugas baru: ").strip()
    
    if not nama_tugas:
        print("❌ Tugas tidak boleh kosong!")
        return
    
    tugas_baru = {
        "nama": nama_tugas,
        "selesai": False,
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "waktu_selesai": None
    }
    
    tugas_list.append(tugas_baru)
    save_tugas(tugas_list)
    print(f"✅ Tugas '{nama_tugas}' berhasil ditambahkan!")


def tandai_selesai(tugas_list):
    """Tandai tugas sebagai selesai"""
    if not tugas_list:
        print("\n❌ Tidak ada tugas untuk ditandai selesai!")
        return
    
    lihat_tugas(tugas_list)
    
    try:
        nomor = int(input("Masukkan nomor tugas yang selesai: "))
        if 1 <= nomor <= len(tugas_list):
            tugas = tugas_list[nomor - 1]
            if not tugas["selesai"]:
                tugas["selesai"] = True
                tugas["waktu_selesai"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                save_tugas(tugas_list)
                print(f"✅ Tugas '{tugas['nama']}' ditandai selesai!")
            else:
                print("⚠️  Tugas ini sudah selesai sebelumnya.")
        else:
            print("❌ Nomor tugas tidak valid!")
    except ValueError:
        print("❌ Masukkan angka yang valid!")


def hapus_tugas(tugas_list):
    """Hapus satu tugas"""
    if not tugas_list:
        print("\n❌ Tidak ada tugas untuk dihapus!")
        return
    
    lihat_tugas(tugas_list)
    
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(tugas_list):
            nama_tugas = tugas_list[nomor - 1]["nama"]
            tugas_list.pop(nomor - 1)
            save_tugas(tugas_list)
            print(f"✅ Tugas '{nama_tugas}' berhasil dihapus!")
        else:
            print("❌ Nomor tugas tidak valid!")
    except ValueError:
        print("❌ Masukkan angka yang valid!")


def hapus_semua_tugas(tugas_list):
    """Hapus semua tugas"""
    if not tugas_list:
        print("\n❌ Tidak ada tugas untuk dihapus!")
        return
    
    konfirmasi = input("\n⚠️  Apakah Anda yakin ingin menghapus SEMUA tugas? (y/n): ").lower()
    if konfirmasi == 'y':
        tugas_list.clear()
        save_tugas(tugas_list)
        print("✅ Semua tugas berhasil dihapus!")
    else:
        print("❌ Pembatalan. Tugas tidak dihapus.")


def main():
    """Fungsi utama"""
    tugas_list = load_tugas()
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-5): ").strip()
        
        if pilihan == "1":
            lihat_tugas(tugas_list)
        elif pilihan == "2":
            tambah_tugas(tugas_list)
        elif pilihan == "3":
            tandai_selesai(tugas_list)
        elif pilihan == "4":
            hapus_tugas(tugas_list)
        elif pilihan == "5":
            hapus_semua_tugas(tugas_list)
        elif pilihan == "0":
            print("\n👋 Terima kasih telah menggunakan aplikasi To-Do List!")
            break
        else:
            print("❌ Pilihan tidak valid! Silakan coba lagi.")


if __name__ == "__main__":
    main()
