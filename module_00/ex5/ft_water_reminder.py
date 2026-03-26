
def ft_water_reminder():
    days = input("Days since last watering: ")
    try:
        if (int(days) > 2):
            print("Water the plants!")
        else:
            print("Plants are fine")
    except ValueError:
        print(f"bad input: {days}")

if __name__ == "__main__":
    ft_water_reminder()