
class Plant:
    def __init__(self, name,height,age):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        try:
            print(f"{self.name} : {int(self.height)}cm {int(self.age)} days old!")
        except ValueError:
            print("Bad input")
            exit(1)
   
def ft_garden_data():
    plant1 = Plant("rose",15,5)
    plant1.show()
    plant2 = Plant("sunflower",80,45)
    plant2.show()

def main():
    ft_garden_data()

if __name__ == "__main__":
    main()