class HussainCanteent:
    items = ['1. Tea', '2. Coffee', '3. Poha', '4. Full Unlimited Food']
    cost = [10, 20, 10, 9999]
    stock = [100, 100, 30, 10]
    def order(self):
        print(HussainCanteent.items)
        food = int(input())
        if food == 0:
            print("Thank You!")
            return
        count = int(input())
        if count == 0:
            print("Thank You!")
            return
        if HussainCanteent.stock[food - 1] < count:
            print("We are having only ", HussainCanteent.stock[food - 1])
            return
        else:
            print("Certainly")
        price = count * HussainCanteent.cost[food - 1]
        print("The total cost - ",price)
        HussainCanteent.stock[food - 1] -= count
print("Welcome!")
HussainCanteent.order(self=None)
