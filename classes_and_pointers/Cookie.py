class Cookie:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return self.color
    def get_Color(self):
        return self.color
    def set_Color(self, color):
        self.color = color

# Create a green cookie
cookie_one = Cookie('green')
# Create a blue cookie
cookie_two = Cookie('blue')

print(f"Cookie one is {cookie_one.get_Color()}")
print(f"Cookie two is {cookie_two.get_Color()}")

cookie_one.set_Color('red')
print(f"Cookie one is {cookie_one.get_Color()}")
print(f"Cookie two is {cookie_two.get_Color()}")


