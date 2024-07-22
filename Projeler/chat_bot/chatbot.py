from transformers import AutoModelForCausalLM, AutoTokenizer
import requests
import time

def download_model(retries=3, delay=5):
    for attempt in range(retries):
        try:
            model_name = "microsoft/DialoGPT-small"  # Daha küçük model kullanıyoruz
            print(f"Modeli indirmeye çalışıyorum: {model_name}")
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForCausalLM.from_pretrained(model_name)
            print("Model başarıyla indirildi!")
            return tokenizer, model
        except (requests.exceptions.RequestException, ConnectionError) as e:
            print(f"Bağlantı hatası oluştu (Deneme {attempt + 1}/{retries}): {e}")
            if attempt < retries - 1:
                print(f"{delay} saniye bekleyip tekrar deneyeceğim...")
                time.sleep(delay)
            else:
                print("Maksimum deneme sayısına ulaşıldı. Lütfen internet bağlantınızı kontrol edin.")
                raise

tokenizer, model = download_model()

def chat_with_bot(user_input):
    # Kullanıcı girdisini tokenize edin
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Modelden yanıt alın
    output = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Yanıtı decode edin
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# Sohbet döngüsü
print("Photon: Merhaba! Benimle sohbet etmek ister misiniz? (Çıkmak için 'q' yazın)")
while True:
    user_input = input("Siz: ")
    if user_input.lower() == 'q':
        print("Photon: Görüşmek üzere!")
        break
    response = chat_with_bot(user_input)
    print("Photon:", response)