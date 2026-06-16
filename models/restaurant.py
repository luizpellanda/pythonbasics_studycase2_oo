# The idea is to reproduce the previous class - The restaurant - but utilizing objects

class Restaurant:

    restaurants = [] # list onde os restaurantes estarao guardados

    # importante - nao precisa ser SELF, pode ser literalmente qualquer merda - por convencao se utiliza o self
    def __init__(self, name, category): # Esse eh o constructor - name and category sao os parametros
        self.name = name # sera o nome passado no parametro
        self.category = category # mesma ideia, passada no parametro
        self._active = False # o _ eh para informar que esse atributo nao deve ser mexido
        Restaurant.restaurants.append(self) # todo restaurante ao ser criado sera colocado diretamente dentro da lista


    def __str__(self): # metodo nativo do python (sempre eh com __) - chama de dunder methods
        return f"{self.name} | {self.category}"
    
    def list_restaurants(): #metodo criado pelo desenvolvdor, nao nativo
        print(f'{'\nRestaurant Name'.ljust(25)} | {'Restaurant Category'.ljust(25)} | {'Restaurant Status'.ljust(25)}\n')
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name.ljust(25)} | {restaurant.category.ljust(25)} | {restaurant.active.ljust(25)}')

    @property
    def active(self):
        return '✅ Active' if self._active else '❌ Not Active'

restaurant_pizza = Restaurant('Pizza Express', 'Italian')
restaurant_sushi = Restaurant('MyBox', 'Japanese')

Restaurant.list_restaurants()

