class QuizBrain:
    def __init__(self):
        self.question_number = 0 
        self. question_list = question_list
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)    
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"q.{self.qurstion_number}: {current_question.text} (True/False): ")    