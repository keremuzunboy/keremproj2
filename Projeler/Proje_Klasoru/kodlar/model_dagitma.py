from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

# Eğitilen modeli yükleyin
model = GPT2LMHeadModel.from_pretrained('./results')
tokenizer = GPT2Tokenizer.from_pretrained('./results')

#
