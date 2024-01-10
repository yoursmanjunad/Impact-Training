class Pizza:
    def __init__(self):
        self.P_Id = int(input("Enter Pizza Id"))
        self.rate = 100
    def extraBill_for_topping(self):
        return 50
    def order(self):
        print("Your Order for Pizza: ", self.P_Id)
        qnty = int(input("How many Pizzas you want: "))
        toppings = input("Enter Y/N for Toppings:")
        topping_bill = 0
        if toppings == 'Yes':
            topping_bill = (Pizza.extraBill_for_topping())*qnty
        total_bill = (self.rate*qnty)+topping_bill
        print("Your Total bill - {} is {}".format(self.P_Id,total_bill))
customer1=Pizza()
customer1.order()
customer2 = Pizza()
customer2.order()