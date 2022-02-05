import random as r


def get_random_list(num, cutoff, lottery_type):
    lottery_list =[]
    x=0

    while x < num:
       rand = r.randrange(1, cutoff)

       if (rand in lottery_list)==False:
           lottery_list.append(rand)
           x = x + 1

    print("The numbers for next {0} Jackpot are:".format(lottery_type))
    print(lottery_list)



def playLottoMax():
    get_random_list(7, 59, "Lotto Max")


def play649():
    get_random_list(6, 49, "Lotto 6/49")


def playOntario49():
    get_random_list(6, 49, "Ontario 49")


playLottoMax()
play649()
playOntario49()



