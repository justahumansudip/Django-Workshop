# class Robot:
#     new_var ="this is token"
   
# robto = Robot()    
# print(robto.new_var)

# #constructor

# class Fruit:
#     def __init__(self,name:str,price:int):
#         self.name = name
#         self.price = price
        
#     def __str__(self) -> str:
#         return f"this fruit is {self.name} and price is {self.price}" 
    
#     def getFruitValue(self):
#         return f"this fruit is {self.name} and price is {self.price}"
  
        
        
# fruit = Fruit("apple",500)
# fruit1 =Fruit("apple",200)

# print(fruit1)
# #inheritance
# class Music:
#     def PlayMusic(self):
#         return "Music has been played"

# class Guitar(Music):    
#     def GuitarPlay(self):
#         return "JHing JHing"
    
    
# guitar = Guitar()
# print(guitar.PlayMusic())
# print(guitar.GuitarPlay())
 
#static method
class StaticExample:
    @staticmethod #annotations
    def guitarPlay(self):
        return "Jhing"
print(StaticExample.guitarPlay())
           