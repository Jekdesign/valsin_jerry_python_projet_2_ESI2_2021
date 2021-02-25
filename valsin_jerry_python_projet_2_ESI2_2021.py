
class Pizza:
    def __init__(self, name, price, ingredient, vegetarian):
        self.name = name
        self.price = price
        self.ingredient = ingredient
        self.vegetarian = vegetarian

    def order(self):
        print('Preparing %s' % self.name)
        print('Baking %s' % self.name)
        print('Cutting %s' % self.name)
        print('Boxing %s' % self.name)

    def displayPizza(self):
        if self.vegetarian == True:
            veggie = "VEGETARIAN"
        else:
            veggie = "NON VEGETARIAN"
        print("PIZZA %s : price %s - %s " %
              (self.name, self.price, veggie))
        for i in self.ingredient:
            print(i)


class CustomPizza(Pizza):
    def __init__(self, name, price, ingredient, vegetarian):
        Pizza.__init__(self, name, price, ingredient, vegetarian)

    def requestIngredients(self):
        nb = 1
        while nb == 1:
            addIngredient = input(
                'Add ingredients to personalise your pizza (ENTER to finish) : ')
            if addIngredient == "":
                nb = 0
                self.displayPizza()
                return
            else:
                self.ingredient = self.ingredient + [addIngredient]
                self.price += 1.2


pizzaHawai = Pizza("Hawai", 9.5, ["tomates", "ananas", "oignons"], False)
pizzaHawai.displayPizza()
pizzaHawai.order()
print("-----------------------------------------")
pizzaSeasons = Pizza(
    "4 saisons", 11, ["oeuf", "emmental", "tomates", "jambon", "olives"], False)
pizzaSeasons.displayPizza()
pizzaSeasons.order()
print("----------------------------------------")
pizzaVeggie = Pizza(
    "Veggie", 7.8, ["champignons", "tomates", "oignon", "poivrons"], True)
pizzaVeggie.displayPizza()
pizzaVeggie.order()
print("----------------------------------------")
pizzaPerso1 = CustomPizza("Perso 1", 7, [], False)
pizzaPerso1.requestIngredients()
