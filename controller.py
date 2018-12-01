class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_listener(lambda value: self.change_value(value))

    def change_value(self, value):
        fahrenheit = self.model.calc_fahrenheit(value)
        celsius = self.model.calc_celsius(value)
        self.view.set_values(celsius, fahrenheit)

    def start(self):
        self.change_value(0)
        self.view.show()