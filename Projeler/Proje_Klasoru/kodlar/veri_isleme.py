import pandas as pd

# CSV dosyasının yolunu belirtin
dosya_yolu = 'veri/buyuk_veri_dosyasi.csv'

# CSV dosyasını okuyun
veri = pd.read_csv(dosya_yolu)

# Verinin ilk birkaç satırını görüntüleyin
print("İlk birkaç satır:")
print(veri.head())

# Temel veri işlemleri
# Eksik verileri kontrol edin
print("\nEksik veri sayısı:")
print(veri.isnull().sum())

# Eksik verileri çıkarın
veri_temiz = veri.dropna()

# Temizlenmiş verinin ilk birkaç satırını görüntüleyin
print("\nTemizlenmiş verinin ilk birkaç satırı:")
print(veri_temiz.head())
