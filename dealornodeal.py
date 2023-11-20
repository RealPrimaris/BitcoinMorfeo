import random

greeting_intro = print("My name is Howie, and this is Deal or No Deal! Boy, have we got a great show for you tonight!")

print(greeting_intro)
player_name = input("Our next contestant is about to take the stage for their chance to win ONE MILLION DOLLARS! Contestant, come on up! Tell me a little about yourself, what's your name?:\n ")

prize_money = 0
highest_amount = []
opened_cases = []
opened_amounts = []
decision = ""
case_amounts = [1, 250, 500, 1000, 10000, 50000, 100000, 250000, 500000, 1000000]
prize = 0
assigned_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




class Case:
    def __init__(self, case_number, index):
        self.case_number = case_number
        self.case_index = index
        self.case_amount = case_amounts[index]


case_index = random.sample(range(0, len(case_amounts)), 10)


case1 = Case(1, case_index[0])

case2 = Case(2, case_index[1])

case3 = Case(3, case_index[2])

case4 = Case(4, case_index[3])

case5 = Case(5, case_index[4])

case6 = Case(6, case_index[5])

case7 = Case(7, case_index[6])

case8 = Case(8, case_index[7])

case9 = Case(9, case_index[8])

case10 = Case(10, case_index[9])
    








player_case = input("It's a pleasure to meet you " + player_name + ". Welcome to Deal or No Deal! Are you ready to play for your chance to win ONE MILLION DOLLARS!? To get started, please pick a case from 1-10: ")
while int(player_case) > 10 or int(player_case) < 1:
    player_case = input("I'm sorry, you need to choose a case between 1-10, please try again: ") 

print("You've chosen case number " + player_case + ". Let's hope it's got the million dollars in it!")



    

def round():
    counter = 0
    choice = input("In order to find out what your case has in it, we need to find out what's in the remaining cases. Please pick a case:  ") 
    while choice == player_case or int(choice) < 1 or int(choice) > 10 or choice in opened_cases:
        choice = input("You have to choose a case other than your own, from 1-10. Please choose another: ")
    print("You've picked case number " +  choice + ". Let's find out if that was a good choice... ladies, please open the case...")
    opened_cases.append(choice)
    
    prizes = [case1.case_amount, case2.case_amount, case3.case_amount, case4.case_amount, case5.case_amount, case6.case_amount, case7.case_amount, case8.case_amount, case9.case_amount, case10.case_amount]

    indice = int(choice)
    new_string = prizes[indice]
    prize = int(new_string)
 
    opened_amounts.append(prize)

    print("Case number " + choice + " has... $" + str(prize) + "!")
    if prize >= 25000:
        print("Oh boy... that's a big number! But there are still some great numbers left in play...")
    elif prize < 25000:
        print("Wow... that was a good choice!")

    print("What's this? The Banker is calling... he's going to make you an offer to buy your case and get you out of this game!")
    remaining_cases = (10 - len(opened_cases))
    total_cash = (1 + 10 + 100 + 500 + 1000 + 10000 + 25000 + 50000 + 100000 + 1000000)
    remaining_cash = total_cash - int(prize)
    new_list = []
    max_num = 0
    for amount in case_amounts:
        if amount not in opened_amounts:
            new_list.append(amount)
            for number in new_list:
                if number > max_num:
                    max_num = number


    offer = int(max_num / remaining_cases)
    
    print("The Banker says that he thinks that you don't have the guts to go all the way! So he's offering you: $" + str(offer))
    decision = input("Remember, if you accept the offer, it's game over and you walk away with $" + str(offer) + " but you'll miss out on the chance for the big prize... so, DEAL OR NO DEAL? (D / N): ")
    acceptable_decisions = ["D", "N"]
    while decision not in acceptable_decisions:
        decision = input("I'm sorry, I didn't understand your decision... DEAL OR NO DEAL!? (D / N): ")  

    if decision == "D":
        print("Congratulations! You've won $" + str(offer) + "!!!")
    else:
        print("Alright! On we go! Such a gutsy move!")
        counter += 1
        if remaining_cases == 2:
            for case in assigned_cases:
                if case not in opened_cases:
                    penultimate_case = case
                    pindice = int(penultimate_case) - 1

                    
            print("You are down to your last two cases! You originally picked case number " + str(player_case) + "... and you're left with " + str(penultimate_case))
            last_call = input("One of these cases has $" + str(max_num) + " in it... will you stick with your case, or would you like to switch it?(K for keep / S for switch):  ")
            while last_call != "K" and last_call != "S":
                last_call = input("I'm sorry, I didn't understand your answer... please type K to keep your original case, or S to switch it with the last case: ")
            if last_call == "K":
                if player_case == 1:
                    prize = case1.case_amount    
                elif player_case == 2:
                    prize = case2.case_amount
                elif player_case == 3:
                    prize = case3.case_amount
                elif player_case == 4:
                    prize = case4.case_amount
                elif player_case == 5:
                    prize = case5.case_amount
                elif player_case == 6:
                    prize = case6.case_amount
                elif player_case == 7:
                    prize = case7.case_amount
                elif player_case == 8:
                    prize = case8.case_amount
                elif player_case == 9:
                    prize = case9.case_amount
                else:
                    prize = case10.case_amount
                print("Let's find out what's in your case! *** Your case has $" + str(prize) + "!!!")
                print("Well, that's all for tonight folks! " + player_name + "has won $" + str(prize) + "! I hope you've enjoyed the show, tune in next time for more Deal or No Deal!")

            elif last_call == "S":
                prize = prizes[pindice]
                print("Wow! That's bold! Let's find out what's in the other case... it has $" + str(prize) + "!!!")
                print("Well, that's all for tonight folks! " + player_name + "has won $" + str(prize) + "! I hope you've enjoyed the show, tune in next time for more Deal or No Deal!")
        else:
            round()            
                


    
round()

