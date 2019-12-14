import random
import time
# Time module is added for suspense so that there is a small gap between the question asked and the answer options. 

def begin_quiz():
    begin_quiz_options = ["A", "B", "C", "D", "E"]
    user_choice = ""
    # The quiz taker will have five options to choose from to determine compatibility!
    while user_choice not in begin_quiz_options:
        print("Have you ever wondered which One Direction member you are most compatible with? Well, fear no more! Take this quiz to find out more!")
        # One Direction is a former British-Irish boy band that took the world by storm from 2010 until 2015. The band consists of five members - Louis, Zayn, Liam, Niall, and Harry. Zayn was the first person to leave the band in March of 2015, and the band took a definite hiatus in December of 2015. Each member is currently focusing on solo work.
        print("Let's begin! Here's your first question - What do you like to do for fun?")
        time.sleep(3)
        print("A. Stay up all night until you see the sun")
        print("B. Get some and live while you're young")
        print("C. Dance all night to the best song ever")
        print("D. Go out and change into something red")
        print("E. Cause trouble up in hotel rooms")
        # The while loop prints the questions for the quiz taker to answer.
        
        user_choice = str(input("Choose a letter: "))
    print("You chose letter " + user_choice)
    if user_choice == begin_quiz_options[0:]:
        question_two()
        # After inputting your answer, with the exception of the final question, the code takes you directly to the next question. It's important to use the correct character (in this case, choosing a letter from A-E, remembering to use caps lock) because if you don't, you will be asked the same question repeatedly until you correctly input your answer. 
        
def question_two():
    question_two_options = ["A", "B", "C", "D", "E"]
    user_choice = ""
    while user_choice not in question_two_options:
        print("Right on! Here's the second question - How would you describe yourself?")
        time.sleep(3)
        print("A. Smart")
        print("B. Leader")
        print("C. Funny")
        print("D. Vain")
        print("E. Flirt")
        user_choice = str(input("Choose a letter: "))
    print("You chose letter " + user_choice)
    if user_choice == question_two_options[0:]:
        question_three()
        
def question_three():
    question_three_options = ["A", "B", "C", "D", "E"]
    user_choice = ""
    while user_choice not in question_three_options:
        print("Very well! Here's the third question - What do you look for in a person?")
        time.sleep(3)
        print("A. Nice eyes")
        print("B. Someone who eats carrots")
        print("C. Cute and good personality")
        print("D. Smile and intelligence")
        print("E. Nice, pretty face")
        
        user_choice = str(input("Choose a letter: "))
    print("You chose letter " + user_choice)
    if user_choice == question_three_options[0:]:
        question_four()
        
def question_four():
    question_four_options = ["A", "B", "C", "D", "E"]
    user_choice = ""
    while user_choice not in question_four_options:
        print("Interesting! Here's the fourth question - If you had a superpower, what would it be?")
        time.sleep(3)
        print("A. Be invisible")
        print("B. Fly")
        print("C. I don't know")
        print("D. Stay young forever")
        print("E. Time travel")
        
        user_choice = str(input("Choose a letter: "))
    print("You chose letter " + user_choice)
    if user_choice == question_four_options[0:]:
        final_question()
        
def final_question():
    final_question_options = ["A", "B", "C", "D", "E"]
    user_choice = ""
    while user_choice not in final_question_options:
        print("Almost there fellow Directioner! Here's the final question - If you could be any member of One Direction for a day,  who would you choose?")
        time.sleep(3)
        print("A. Niall")
        print("B. Harry")
        print("C. Liam")
        print("D. Louis")
        print("E. Zayn")
        
        user_choice = str(input("Choose a letter: "))
    print("You chose letter " + user_choice)
    # This conditional statement determines who the quiz taker is most compatible with.
    if user_choice == final_question_options[0]:
        print("Congrats fellow Directioner! You are most compatible with Liam!")
    elif user_choice == final_question_options[1]:
        print("Congrats fellow Directioner! You are most compatible with Louis!")
    elif user_choice == final_question_options[2]:
        print("Congrats fellow Directioner! You are most compatible with Niall!")
    elif user_choice == final_question_options[3]:
        print("Congrats fellow Directioner! You are most compatible with Zayn!")
    elif user_choice == final_question_options[4]:
        print("Congrats fellow Directioner! You are most compatible with Harry!")
        
begin_quiz()
question_two()
question_three()
question_four()
final_question()

assert callable(begin_quiz)
assert callable(question_two)
assert callable(question_three)
assert callable(question_four)
assert callable(final_question)