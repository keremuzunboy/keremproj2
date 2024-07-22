import pandas as pd
import numpy as np

# Rastgele veri oluşturma
np.random.seed(0)

# Örnek veri boyutu
num_rows = 10000

# Rastgele isim ve soyisim oluşturma
isimler = ['Ahmet', 'Ayşe', 'Mehmet', 'Elif', 'Ali', 'Zeynep', 'Fatma', 'Emre', 'Hüseyin', 'Selin']
soyisimler = ['Yılmaz', 'Kaya', 'Demir', 'Çelik', 'Şahin', 'Güler', 'Öztürk', 'Arslan', 'Doğan', 'Korkmaz']

# Rastgele yaş, gelir ve satın alma miktarı oluşturma
yaslar = np.random.randint(18, 70, size=num_rows)
gelirler = np.random.randint(20000, 150000, size=num_rows)
satin_alma_miktari = np.random.randint(1, 20, size=num_rows)

# İsim ve soyisimleri rastgele seçme
random_isimler = np.random.choice(isimler, num_rows)
random_soyisimler = np.random.choice(soyisimler, num_rows)

# DataFrame oluşturma
veri = pd.DataFrame({
    'id': np.arange(1, num_rows + 1),
    'isim': random_isimler,
    'soyisim': random_soyisimler,
    'yas': yaslar,
    'yillik_gelir': gelirler,
    'satin_alma_miktari': satin_alma_miktari
})

# CSV dosyasını yazma
veri.to_csv('veri/buyuk_veri_dosyasi.csv', index=False)

print("Veri dosyası 'buyuk_veri_dosyasi.csv' oluşturuldu.")
