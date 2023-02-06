#Tuple Methods
numbers = (65, 78, 498, 198, 594, 903, 287, 695, 578, 392, 186, 762, 824)
sorted_t = sorted(numbers)
print(sorted_t) 

numerals = (38, 17, 48, 10, 54, 93, 25, 61, 52, 23, 86, 76, 16)
print(max(numerals)) 
print(min(numerals)) 

n = [18, 29, 36, 43, 51]
t = tuple(n)
print(t) 

name = "SheilaOjukwu"
t = tuple(name)
print(t) 

Cars = ('Ford', 'Toyota', 'BMW', 'Lexus', 'Volkswagon')
Footwares = ('Sandals', 'Slippers', 'Stockings', 'Shoes', 'Sneakers', 'Slides')
Things = Cars + Footwares
print(Things) 

Food = ('Noodles', 'Meat', 'Cereal', 'Beans', 'Abacha', 'Eba')
print('Abacha' in Food) 
print('Rice' not in Food) 
