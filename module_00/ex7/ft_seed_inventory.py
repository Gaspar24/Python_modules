
def ft_seed_inventory(seed_type,quantity,unit):
    try:
        if unit == "packets":
            print(f"{str.capitalize(seed_type)} seeds : {int(quantity)} {unit} available")
        elif unit == "grams":
            print(f"{str.capitalize(seed_type)} seeds : {int(quantity)} {unit} total")
        elif unit == "area":
            print(f"{str.capitalize(seed_type)} seeds : covers {int(quantity)} square meters")


    except ValueError:
        print("Bad parameter!")

if __name__ == "__main__":
    ft_seed_inventory("tomato",15,"area")