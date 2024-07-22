import random
import json
import time

class EnglishTeacher:
    def __init__(self):
        self.vocab = {
            "hello": "merhaba",
            "goodbye": "hoşça kal",
            "yes": "evet",
            "no": "hayır",
            "thank you": "teşekkür ederim",
            "please": "lütfen",
            "how are you": "nasılsın",
            "what is your name": "adın ne",
            "my name is": "benim adım",
            "nice to meet you": "tanıştığımıza memnun oldum"
        }
        self.sentences = [
            "Hello, how are you?",
            "My name is John.",
            "Thank you very much.",
            "Nice to meet you.",
            "Yes, please.",
            "No, thank you."
        ]
        self.grammar_rules = [
            "İngilizce'de cümleler genellikle 'Özne + Yüklem + Nesne' sırasını takip eder.",
            "Geçmiş zaman için fiilin sonuna genellikle '-ed' eklenir.",
            "Sıfatlar isimlerden önce gelir.",
            "Çoğul isimler genellikle '-s' veya '-es' eki alır.",
            "Olumsuz cümleler 'not' kelimesi kullanılarak yapılır."
        ]
        self.user_progress = {"vocabulary": [], "sentences": [], "grammar": []}
    
    def teach_vocabulary(self):
        word = random.choice(list(self.vocab.keys()))
        print(f"İngilizce kelime: {word}")
        user_translation = input("Türkçe çevirisi nedir? ").lower()
        
        if user_translation == self.vocab[word]:
            print("Doğru! Harika iş.")
            if word not in self.user_progress["vocabulary"]:
                self.user_progress["vocabulary"].append(word)
        else:
            print(f"Yanlış. Doğru cevap: {self.vocab[word]}")
        
        print(f"Şu ana kadar {len(self.user_progress['vocabulary'])} kelime öğrendiniz.")
    
    def teach_sentence(self):
        sentence = random.choice(self.sentences)
        print(f"Bu cümleyi Türkçe'ye çevirin: {sentence}")
        user_translation = input("Çeviriniz: ")
        print("Teşekkürler! Umarım doğru çevirmişsinizdir.")
        if sentence not in self.user_progress["sentences"]:
            self.user_progress["sentences"].append(sentence)
        
        print(f"Şu ana kadar {len(self.user_progress['sentences'])} cümle çalıştınız.")
    
    def teach_grammar(self):
        rule = random.choice(self.grammar_rules)
        print("Gramer kuralı:")
        print(rule)
        input("Anladığınızda Enter tuşuna basın.")
        if rule not in self.user_progress["grammar"]:
            self.user_progress["grammar"].append(rule)
        print(f"Şu ana kadar {len(self.user_progress['grammar'])} gramer kuralı öğrendiniz.")
    
    def practice_exercise(self):
        exercise_type = random.choice(["vocabulary", "sentence", "grammar"])
        if exercise_type == "vocabulary":
            self.teach_vocabulary()
        elif exercise_type == "sentence":
            self.teach_sentence()
        else:
            self.teach_grammar()
    
    def review_progress(self):
        print("\nİlerleme Özeti:")
        print(f"Öğrenilen kelimeler: {len(self.user_progress['vocabulary'])}")
        print(f"Çalışılan cümleler: {len(self.user_progress['sentences'])}")
        print(f"Öğrenilen gramer kuralları: {len(self.user_progress['grammar'])}")
    
    def take_quiz(self):
        print("\nKısa Quiz Başlıyor!")
        score = 0
        total_questions = 5
        
        for _ in range(total_questions):
            question_type = random.choice(["vocabulary", "sentence", "grammar"])
            if question_type == "vocabulary":
                word = random.choice(list(self.vocab.keys()))
                print(f"'{word}' kelimesinin Türkçe karşılığı nedir?")
                answer = input("Cevabınız: ").lower()
                if answer == self.vocab[word]:
                    print("Doğru!")
                    score += 1
                else:
                    print(f"Yanlış. Doğru cevap: {self.vocab[word]}")
            elif question_type == "sentence":
                sentence = random.choice(self.sentences)
                print(f"Bu cümleyi Türkçe'ye çevirin: {sentence}")
                input("Çeviriniz: ")
                print("Umarım doğru çevirmişsinizdir.")
                score += 1
            else:
                rule = random.choice(self.grammar_rules)
                print("Bu gramer kuralını açıklayın:")
                print(rule)
                input("Açıklamanız: ")
                print("Teşekkürler!")
                score += 1
            
            time.sleep(1)
        
        print(f"\nQuiz bitti! Skorunuz: {score}/{total_questions}")
    
    def save_progress(self):
        with open("progress.json", "w") as f:
            json.dump(self.user_progress, f)
    
    def load_progress(self):
        try:
            with open("progress.json", "r") as f:
                self.user_progress = json.load(f)
        except FileNotFoundError:
            print("İlerleme dosyası bulunamadı. Yeni bir ilerleme başlatılıyor.")

def main():
    teacher = EnglishTeacher()
    teacher.load_progress()
    
    print("İngilizce Öğrenme Asistanına Hoş Geldiniz!")
    
    while True:
        print("\n1. Kelime öğren")
        print("2. Cümle çalış")
        print("3. Gramer öğren")
        print("4. Rastgele alıştırma yap")
        print("5. İlerlemeyi gözden geçir")
        print("6. Quiz yap ve Çıkış")
        
        choice = input("Seçiminiz (1-6): ")
        
        if choice == "1":
            teacher.teach_vocabulary()
        elif choice == "2":
            teacher.teach_sentence()
        elif choice == "3":
            teacher.teach_grammar()
        elif choice == "4":
            teacher.practice_exercise()
        elif choice == "5":
            teacher.review_progress()
        elif choice == "6":
            teacher.take_quiz()
            teacher.save_progress()
            print("Quiz tamamlandı. İlerlemeniz kaydedildi. Görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()