from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
import pandas as pd
from sklearn.model_selection import train_test_split
import torch

# Veriyi yükleyin
data = pd.read_csv('veri/buyuk_veri_dosyasi.csv')

# Metin verilerini birleştirerek eğitim veri setini oluşturun
data['text'] = data['isim'] + ' ' + data['soyisim'] + ', ' + data['yas'].astype(str) + ' yaşında, yıllık geliri ' + data['yillik_gelir'].astype(str) + ' TL.'

# Eğitim ve doğrulama veri setlerine ayırın
train_data, val_data = train_test_split(data['text'], test_size=0.2, random_state=42)

# Tokenizer ve modeli yükleyin
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Veriyi tokenlaştırma
train_encodings = tokenizer(train_data.tolist(), truncation=True, padding=True, max_length=512)
val_encodings = tokenizer(val_data.tolist(), truncation=True, padding=True, max_length=512)

# DataLoader oluşturma
class TextDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}

    def __len__(self):
        return len(self.encodings['input_ids'])

train_dataset = TextDataset(train_encodings)
val_dataset = TextDataset(val_encodings)

# Eğitim argümanlarını belirleme
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy="steps",
)

# Trainer oluşturma
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

# Modeli eğitme
trainer.train()
