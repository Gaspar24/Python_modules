
def ft_plant_age():
    age = input("Enter plant age in days: ")
    try:
        if int(age) > 60:
            print("Plant is ready to harvest!")
        else:
            print("Plant needs more time to grow!")
    except ValueError:
        print(f"Bad input: {age}")
if __name__ == "__main__":
    ft_plant_age()