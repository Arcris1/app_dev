class Fruits:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_info(self):
        print(f"The fruit is : {self.name}, color is : {self.color}") 

if __name__ == "__main__":
    fruits1 = Fruits("Apple", "Red")
    fruits1.display_info()
    
    fruits2 = Fruits("Banana", "Yellow")
    fruits2.name = "Blueberry"
    fruits2.color ="Blue"
    fruits2.display_info()
