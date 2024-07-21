from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

# Eğitilen modeli yükleyin
model = GPT2LMHeadModel.from_pretrained('./results')
tokenizer = GPT2Tokenizer.from_pretrained('./results')

# Metin oluşturma pipeline'ı oluşturma
text_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# Metin üretme
generated_text = text_generator("Merhaba, nasılsın?", max_length=50)
print(generated_text)
