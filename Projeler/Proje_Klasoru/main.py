import os

if __name__ == "__main__":
    print("Veri oluşturuluyor...")
    os.system('python kodlar/veri_olustur.py')
    
    print("Veri işleniyor...")
    os.system('python kodlar/veri_isleme.py')
    
    print("Model eğitiliyor...")
    os.system('python kodlar/model_egitme.py')
    
    print("Model değerlendiriliyor...")
    os.system('python kodlar/model_degerlendirme.py')
    
    print("Model dağıtılıyor ve metin üretiliyor...")
    os.system('python kodlar/model_dagitma.py')
