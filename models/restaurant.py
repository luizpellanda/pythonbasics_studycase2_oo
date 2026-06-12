# The idea is to reproduce the previous class - The restaurant - but utilizing objects

class Restaurant:

    restaurants = [] # list onde os restaurantes estarao guardados

    # importante - nao precisa ser SELF, pode ser literalmente qualquer merda - por convencao se utiliza o self
    def __init__(self, name, category): # Esse eh o constructor - name and category sao os parametros
        self.name = name # sera o nome passado no parametro
        self.category = category # mesma ideia, passada no parametro
        self.active = False
        Restaurant.restaurants.append(self) # todo restaurante ao ser criado sera colocado diretamente dentro da lista


    def __str__(self): # metodo nativo do python (sempre eh com __) - chama de dunder methods
        return f"{self.name} | {self.category}"
    
    def list_restaurants(): #metodo criado pelo desenvolvdor, nao nativo
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name} | {restaurant.category} | {restaurant.active}')

restaurant_pizza = Restaurant('Pizza Express', 'Italian')
restaurant_sushi = Restaurant('MyBox', 'Japanese')

Restaurant.list_restaurants()

