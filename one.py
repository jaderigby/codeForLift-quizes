import re, helpers
import messages as msg

settings = helpers.get_settings()

def execute(ACTION):
    def question1():
        answer = raw_input("Please list the 4 math operators. Use a comma to seperate them: ")
        answerNoSpaces = answer.replace(' ', '')
        answerList = answerNoSpaces.split(',')
        pat = "[\/\*\+\-]"
        score = 0
        if len(answerList) > 4:
            return score
        else:
            for item in list(set(answerList)):
                match = re.search(pat, item)
                if match:
                    score += 1
            return score
    def question2():
        answer = raw_input("Please list the 2 basic comparison operators. Use a comma to seperate them: ")
        answerNoSpaces = answer.replace(' ', '')
        answerList = answerNoSpaces.split(',')
        pat = "[(==)(!=)]"
        score = 0
        if len(answerList) > 2:
            return score
        else:
            for item in list(set(answerList)):
                match = re.search(pat, item)
                if match:
                    score += 1
            return score

    def question3():
        answer = raw_input("Please list the 4 number equivalency operators (excluding the basic comparison operators). Use a comma to seperate them: ")
        answerNoSpaces = answer.replace(' ', '')
        answerList = answerNoSpaces.split(',')
        pat = "[\<\>(<=)(>=)]"
        score = 0
        if len(answerList) > 4:
            return score
        else:
            for item in list(set(answerList)):
                match = re.search(pat, item)
                if match:
                    score += 1
            return score

    def question4():
        answer = raw_input('''
A variable is ...

a) a nice way to say "hello"
b) a container for a value
c) a system for doing math
d) a format for comparing strings

: ''')
        score = 0
        if answer == 'b':
            score += 1
            return score
        else:
            return score

    #= Execute
    q1 = question1()
    q2 = question2()
    q3 = question3()
    q4 = question4()
    finalTally = q1 + q2 + q3 + q4
    pointsPossible = 11

    studentName = helpers.print_score_to_settings(ACTION, finalTally, pointsPossible)
    helpers.print_score_to_scorecard(studentName, ACTION, finalTally, pointsPossible)

    print
    print("You scored {} out of {}".format(finalTally, pointsPossible))
    print
    if finalTally == pointsPossible:
        print("Awesome Job!  You scored 100%")
    elif finalTally == pointsPossible - 1:
        print("Great Job!  You recieve an A.")
    elif finalTally == pointsPossible - 2:
        print("Good Job! You get an A.")
    elif finalTally == pointsPossible - 3:
        print("Not Too Bad! You get a B.")
    elif finalTally == pointsPossible - 4:
        print ("You scored a C.  Looks like you have some work to do.")
    elif finalTally <= pointsPossible - 5:
        print("Yikes!  You didn't pass. You need lots and lots of practice!")
