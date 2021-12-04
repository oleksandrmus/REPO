user_integers = []
def print_sum_avg(user_integers):
    summury =sum(user_integers)
    avarage = summury/len(user_integers)
    print("Summery",summury)
    print("Avarage",avarage )
def collect_user_input():
    for round in range (3):
        user_input = int(input("please , enter the integer :"))
        user_integers.append (user_input)
    print_sum_avg(user_integers)
collect_user_input()

