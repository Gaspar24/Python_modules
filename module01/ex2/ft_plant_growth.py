
class Plant:
    def __init__(self,name,height,days):
        try:
            self.name = str(name)
            self.height = float(height)
            self.days = int(days)
        except ValueError:
            print("bad input")
    def grow(self):
        self.height+=0.5
    def age(self,it):
        self.days+=1




def ft_plant_growth():
    height = 15
    plant = Plant("rose",height,30)
    print(f"{plant.name}: {plant.height}cm, {plant.days} days old!")
    for i in range(1,7):
        print(f"---DAY {i}---")
        plant.grow()
        plant.age(i)
        print(f"{plant.name}: {plant.height}cm, {plant.days} days old!")
    print(f"growth : {plant.height - height}")

def main():
    ft_plant_growth()

if __name__ == "__main__":
    main()