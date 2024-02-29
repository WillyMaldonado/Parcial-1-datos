from polynomial import Polynomial
from circular_list import Circular_list

def main():
    a = Circular_list()
    b = Circular_list()
    a.insert_at_beginning(-10)
    a.insert_at_beginning(18)
    a.insert_at_beginning(3)
    b.insert_at_beginning(25)
    b.insert_at_beginning(0)
    b.insert_at_beginning(4)
    b.insert_at_beginning(-17)
    # while True:
    #     user_choice = int(input("1) Add components to polynomial \n"
    #                             "2) Add and subtract \n"
    #                             "3) Evaluate \n"
    #                             "4) Exit\n"))
    #     if user_choice == 1:
    #         polynomial_choice = input("Which polynomial you wanna add components? \n"
    #                                     "'a)' or 'b)'\n")
    #         if polynomial_choice == "a":
    #             amount = int(input("How many components you wanna add?\n"))
    #             for i in range(amount):
    #                 component = int(input("Insert the component you wanna add \n"))
    #                 a.insert_at_beginning(component)
    #         else:
    #             amount = int(input("How many components you wanna add?\n"))
    #             for i in range(amount):
    #                 component = int(input("Insert the component you wanna add \n"))
    #                 b.insert_at_beginning(component)  
    # #     elif user_choice == 2:
    # #         pass
    # #     elif user_choice == 3:
    # #         pass
    #     elif user_choice == 4:
    #         break
    # # first = Circular_list()
    # # first.insert_at_beginning(-10)
    # # first.show_list()
    # # first.insert_at_beginning(+18)
    # # first.show_list()
    # # first.insert_at_beginning(3)
    # # first.show_list()
    a.show_list()
    b.show_list()
    a.evaluate_polynomial(3)

main()