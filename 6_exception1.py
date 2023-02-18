questions_and_answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Что?": "Что?"}

def hello_user(answers_dict):
    while True:
        try:
            question = input('Введите вопрос: ',)
            print(answers_dict.get(question, "Не знаю"))
        except KeyboardInterrupt: 
            print('\nПока')
            break
   
if __name__ == "__main__":
    hello_user(questions_and_answers)