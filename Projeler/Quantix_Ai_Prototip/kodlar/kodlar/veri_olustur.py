import pandas as pd
import numpy as np
import os

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
output_dir = '../veri'
output_file = 'buyuk_veri_dosyasi.csv'

# Check if directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

veri.to_csv(os.path.join(output_dir, output_file), index=False)

print(f"Veri dosyası '{output_file}' oluşturuldu.")