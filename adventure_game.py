import time
import random
monsters = ["Black Bear", "Wild Tiger", "Wild Lion", "Giant Dragon"]
R_monsters = random.choice(monsters)


bag = []


def print_time(m):
    print(m)
    time.sleep(0.5)


def intro():
    print_time("")
    print_time("Hello and wellcom :")
    print_time("You are the greatest warrior in the the Universe")
    print_time("and you want to save yor doughter.")
    print_time("you was known that she is in the fotest,")
    print_time("now you are in the forest")
    print_time("You can see two roads, on the right you can see a river,")
    print_time("on the left you can see a mountain")
    print_time("")


def ch_play_again():
    print_time("would you like to play again ?")
    D = input("1.YAS\n"
              "2.NO\n"
              "Your choice :")
    return D


def play_again():
    game()


def make_choice():
    print_time("where do you want go ?")
    C = input("1. the river\n"
              "2. the mountain\n"
              "your choice :")
    return C


def river_choice():
        x = input(f"1. attack on the {R_monsters}\n"
                  "2. get in to the cave \n"
                  "Your choice :")
        return x


def game():
    intro()
    while True:
        answer = make_choice()
        if answer == "1":
            print_time("")
            print_time("You went across the river an at the end of it")
            print_time(f"you found a {R_monsters}")
            print_time(", and it want to attack on you")
            print_time("you can see a cave ")
            print_time("")
            while True:
                river = river_choice()
                if river == "1":
                    print_time("")
                    print_time(f"{R_monsters} attacked on you and")
                    print_time("it killed you")
                    print_time("game over !!!")
                    print_time("")
                    while True:
                        A = ch_play_again()
                        if A == "1":
                            play_again()
                        elif A == "2":
                            print_time("thank you for playing")
                            exit()
                        else:
                            print_time("")
                            print_time("wrong answer !!!")
                            print_time("")

                elif river == "2":
                    while True:
                        if "sword" in bag:
                            print_time("")
                            print_time("You interd the cave befor")
                            print_time("and you have got the sword")
                            print_time("Now the cave is empity")
                            print_time("go to save your dughter !!!")
                            print_time("")

                        else:
                            print_time("")
                            print_time("You entered the cave")
                            print_time("and you found a magic sword")
                            print_time("Now you have a magic sword")
                            print_time("You went back")
                            print_time("")
                            river = river_choice()
                            if river == "1":
                                print_time("")
                                print_time(f"You attacked on the {R_monsters}")
                                print_time("and it tried to kill you")
                                print_time(f"but you used the sword")
                                print_time("and finally")
                                print_time(f"you killed the {R_monsters}")
                                print_time("Now")
                                print_time("you are ready")
                                print_time("to save your dughter")
                                print_time("you returned black to the forest")
                                print_time("what is next !")
                                print_time("")
                                answer = make_choice()
                                if answer == "2":
                                    print_time("")
                                    print_time("You went to the mountain")
                                    print_time("and after along trip")
                                    print_time("you found your doughter")
                                    print_time("who was kidnapped by bad guys")
                                    print_time("you fight bad guys")
                                    print_time("after along time fighting")
                                    print_time("finally")
                                    print_time("you saved your doughter")
                                    print_time("")
                                    print_time("YOU WIN !!!!")
                                    print_time("")
                                    while True:
                                        A = ch_play_again()
                                        if A == "1":
                                            play_again()
                                        elif A == "2":
                                            print_time("thank you for playing")
                                            exit()
                                        else:
                                            print_time("")
                                            print_time("wrong answer !")
                                            print_time("")

                            elif river == "2":
                                print_time("")
                                print_time("You interd the cave befor")
                                print_time("and you have got the sword")
                                print_time("Now the cave is empity")
                                print_time("Now you return back to the forest")
                                print_time("")
                                answer = make_choice()
                                if answer == "2":
                                    print_time("")
                                    print_time("You went to the mountain")
                                    print_time("and after along trip")
                                    print_time("you found your doughter")
                                    print_time("who was kidnapped by bad guys")
                                    print_time("you fight bad guys")
                                    print_time("after along time fighting")
                                    print_time("you saved your doughter")
                                    print_time("")
                                    print_time("YOU WIN !!!!!!")
                                    print_time("")
                                    while True:
                                        A = ch_play_again()
                                        if A == "1":
                                            play_again()
                                        elif A == "2":
                                            print_time("thank you for playing")
                                            exit()
                                        else:
                                            print_time("")
                                            print_time("wrong answer !")
                                            print_time("")

                            else:
                                    print_time("")
                                    print_time("Wrong Answer !!!!")
                                    print_time("")

        elif answer == "2":
            print_time("")
            print_time("you went to the mountain and and after along trip")
            print_time("you found your doughter who was kidnapped by bad guys")
            print_time("you tried to fight bad guys")
            print_time("but you could not win and the bad guys killed you")
            print_time("")
            print_time("game over !!!")
            while True:
                A = ch_play_again()
                if A == "1":
                    play_again()
                elif A == "2":
                    print_time("thank you for playing")
                    exit()
                else:
                    print_time("")
                    print_time("wrong answer !")
                    print_time("")

        else:
            print_time("")
            print_time("wrong answer !!!!!")
            print_time("")
game()
