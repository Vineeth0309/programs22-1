class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getprice(self):
        return self.price
    def __str__(self):
        return self.name + ' : ' + str(self.getprice())
def buildmenu(names, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], costs[i]))
    return menu
names = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Apple', 'Donut', 'Cake']
costs = [250, 150, 180, 70, 65, 55, 120, 350]
Foods = buildmenu(names, costs)
n = 1
for el in Foods:
    print(n, '. ', el)
    n = n + 1
