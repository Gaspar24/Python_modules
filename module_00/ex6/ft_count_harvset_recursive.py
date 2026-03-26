
def print_days(nb,day):
    if nb <=day:
        print(f"Day {nb}")
        print_days(nb +1,day)

def ft_count_recursive():
    days = input("Days untill harvest: ")
    try:
        print_days(1,int(days))
        print("Harvest time!")
    except ValueError:
        print(f"bad input: {days}")

if __name__ == "__main__":
    ft_count_recursive()