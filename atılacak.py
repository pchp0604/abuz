import os

def check_termux_storage():
    # Kullanıcı ana dizinindeki "storage" klasörünü kontrol et
    storage_path = os.path.expanduser("~/storage")
    
    if os.path.exists(storage_path):
        print("✔️ Termux depolama erişimi mevcut.")
    else:
        print("⚠️ Termux depolama erişimi bulunamadı!")
        print("Depolama izni vermek için aşağıdaki komutu çalıştırın:")
        print("\ntermux-setup-storage\n")
        print("Lütfen gerekli izni verdikten sonra tekrar deneyin.")
        exit(1)  # Programı sonlandır

if __name__ == "__main__":
    print("Termux dosya erişimi kontrol ediliyor...")
    check_termux_storage()
    print("Devam edebilirsiniz!")
