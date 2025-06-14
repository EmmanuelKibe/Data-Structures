#create a dictionary of questions, choices and correct answers

quiz = {'What is the capital city of Saudi Arabia?: [a)Riyadh b)Kathmandu c)AbuDhabi]' : 'Riyadh', 'Which YouTube channel has the most subscribers?: [a)PewDiePie b)Mr Beast c)UrCristiano]' : 'Mr Beast', 'What is the largest land mammal?: [a)Buffalo b)Rhinoceros c)Elephant]' : 'Elephant'}

#Initialize a score variable


#Iterate through the quiz dictionary
for key in quiz:
    global score
    score = 0
    print(key)
    answer = input('Answer: ')
    
    if answer.strip() == quiz[key]:
        print('Correct!')
        score = score + 1
    else:
        print("Incorrect!")
        score = score + 0

# Use match-case to provide feedback based on the score    
match score:
    case _ if score == 0:
        print(f"Your score is {score}. That is too low. Try harder")
        
    case _ if score == 1:
        print(f"Your score is {score}. Great effort. Better luck next time")
        
    case _ if score == 2:
        print(f"Your score is {score}. Almost there. You'll definitely get it next time")
        
    case _ if score == 3:
        print(f"Excellent! You aced the test!")