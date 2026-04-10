
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
    # def age(self,it):
    #     self.days+=1



def ft_plant_factory():
    types = [("rose",15,25), ("bamboo",100,60)]
    my_garden = [Plant(name,height,days) for name,height,days in types]
    for flower in my_garden:
        print(f"created: {flower.name}: {flower.height}cm, {flower.days} days old")


def main():
	ft_plant_factory()

if __name__ == "__main__":
	main()