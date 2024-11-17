import os
import subprocess

def check_and_request_storage_access():
    # Kullanıcı ana dizinindeki "storage" klasörünü kontrol et
    storage_path = os.path.expanduser("~/storage")
    
    if os.path.exists(storage_path):
        print("✔️ Termux depolama erişimi mevcut.")
    else:
        print("⚠️ Termux depolama erişimi bulunamadı!")
        print("🔄 Depolama erişim izni alınıyor...")
        
        # Termux-setup-storage komutunu çalıştır
        os.system("termux-setup-storage")
        print("✅ İzin talebi gönderildi. Lütfen izni onaylayın.")
        
        # Kullanıcının onayı için bekle
        input("Erişim izni verdikten sonra Enter'a basarak devam edin...")
        
        # Tekrar kontrol et
        if os.path.exists(storage_path):
            print("✔️ Depolama erişimi başarıyla alındı!")
        else:
            print("❌ Depolama erişimi alınamadı! Lütfen manuel olarak izin verin.")
            exit(1)  # Programı sonlandır

if __name__ == "__main__":
    print("Termux dosya erişimi kontrol ediliyor...")
    check_and_request_storage_access()
    print("Devam edebilirsiniz!")
