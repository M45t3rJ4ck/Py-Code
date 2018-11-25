def get_questions():
    return [["What color is the daytime sky on a clear day? ", "blue"],
            ["What is the answer to life, the universe and everything? ", "42"],
            ["What is a three letter word for mouse trap? ", "cat"]]

def check_question(question_and_answer):
    question = question_and_answer[0]
    answer = question_and_answer[1]
    given_answer = input(question)
    if answer == given_answer:
        print("Correct")
        return True
    else:
        print("Incorrect, correct was: ", answer)
        return False

def run_test(questions):
    if len(questions) == 0:
        print("No questions were given.")
        return
    index = 0
    right = 0
    while index < len(questions):
        if check_question(questions[index]):
            right = right + 1
            index = index + 1
        else:
            index = index + 1
    print("You got", right * 100 / len(questions),\
           "% right out of", len(questions))

run_test(get_questions())
