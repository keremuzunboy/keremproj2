from transformers import Trainer

# Modeli değerlendirme
results = trainer.evaluate()

# Değerlendirme sonuçlarını yazdırma
print(results)
