ingredient = []


class Pizza:
    def __init__(self, name, price, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredient = []
        self.vegetarian = vegetarian

    def order(self):
        print('Preparing %s' % self.name)
        print('Baking %s' % self.name)
        print('Cutting %s' % self.name)
        print('Boxing %s' % self.name)

    def displayPizza(self):
        print("PIZZA %s : price %s - vegetarian %s " %
              (self.name, self.price, self.vegetarian))

    # def showIngredients():
    #     print("")


class CustomPizza(Pizza):
    def __init__(self, name, price, vegetarian):
        Pizza.__init__(self, name, price, vegetarian)

    # def requestIngredient(self):

        # def calculPrice(self):


pizzaHawai = Pizza("Hawai", 9.5, ["tomates", "ananas", "oignons"])
pizzaHawai.displayPizza()
pizzaHawai.order()
print("-----------------------------------------")
pizzaSeasons = Pizza(
    "4 saisons", 11, ["oeuf", "emmental", "tomates", "jambon", "olives"])
pizzaSeasons.displayPizza()
pizzaSeasons.order()
print("----------------------------------------")
pizzaVeggie = Pizza(
    "Veggie", 7.8, ["champignons", "tomates", "oignon", "poivrons"])
pizzaVeggie.displayPizza()
pizzaVeggie.order()
print("----------------------------------------")
pizzaPerso1 = Pizza(
    "Perso 1", 10.5, ["fromage", "jambon", "boeuf"])
pizzaPerso1.displayPizza()
pizzaPerso1.order()
print("----------------------------------------")
pizzaPerso2 = Pizza(
    "Perso 2", 10.5, ["oignons", "champignon"])
pizzaPerso2.displayPizza()
pizzaPerso2.order()
