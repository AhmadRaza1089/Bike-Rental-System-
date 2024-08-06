class Bikeshop:
    def __init__(self, stock):
        self.stock = stock
    def display(self):
        print(f"The available bikes are: {self.stock}")
    def rent_bike(self, rent):
        if rent <= 0:
            print("Enter a valid number")
        elif rent > self.stock:
            print("Enter a lesser number")
        else:
            print(f"Your bike is ready and rent is: {rent * 500}")
            self.stock = self.stock-rent
            print(f"The remaining bikes are: {self.stock}")
while True:
    obj = Bikeshop(100)
    uc = int(input("""Enter your choice:
                1: Dispaly Bike
                2:Rent a Bike
                3: Exit\n"""))
    if uc == 1:
        obj.display()
    elif uc == 2:
        n = int(input("Enter the number of bikes to rent: "))
        obj.rent_bike(n)
    else:
        print("Invalid choice, please try again.")
