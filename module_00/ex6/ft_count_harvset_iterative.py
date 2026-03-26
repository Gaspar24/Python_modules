
def ft_count_harvest_iterative():
    days = input("Days untill harvest: ")
    try:
        for i in range(1,int(days) + 1):
            print(f"Day {i}")
        print("Harvest time!")
    except ValueError:
        print(f"Bad input : {days}")



if __name__ == "__main__":
    ft_count_harvest_iterative()