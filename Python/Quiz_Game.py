score = 0
que = 1
name = input ("Enter your name: ")
with open('questions_and_answers.txt', 'r') as data:
    line = data.readlines()
    for part in line:
        part = part.strip().split(';')
        print("---------------------------------------------------------------------------------------------------------")
        print("Question: ",part[0],"\n",part[2],"\n","1.",part[3],"\n","2.",part[4],"\n","3.",part[5])
        try:
            option = int(input(" Enter the option number: "))
            if (int(part[1]) == option):
                print("-------------------------")
                print("Correct option! Let's GO.")
                print("-------------------------")
                score += 1

            elif(int(part[1]) != option):
                if (option >= 4):
                    print("-------------------------------------------------------------")
                    print("The option is not available.The correct option is: ", part[1] )
                    print("-------------------------------------------------------------")
                    score = score - 0.25
                else:
                    print("--------------------------------------")
                    print("Wrong! The correct option is: ", part[1])
                    print("--------------------------------------")
                    score = score - 0.25

            print("-----------------")
            print("Score: ", score)
            print("-----------------")
        except ValueError:
            print("Unattempted Question.")
            print("--------------------------------")
            print("The correct option is: ", part[1])
            print("--------------------------------")
            print("-----------------")
            print("Score: ", score)
            print("-----------------")
if score>40:
    print(name," is a Smart Cookie :) ")
elif score>20:
    print("Average Joe, ", name, "<3")
else:
    print(name, ", dummy work hard :( ")
