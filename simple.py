class SimpleClass:
    
    def print_simple(self):
        x = 1
        y =-1
        print(x+y)
        print("My name is Sushma")
        print(self.another_function())

    def another_function(self):
        return "I am learning Python"

simple = SimpleClass().print_simple()
