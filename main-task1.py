my_dict = {
    "пекарня": ["хлеб", "булочки", "пончик"],
    "овощной": ["морковь", "петрушка", "рукола"]
    }

my_dict={key.capitalize():[x.capitalize() for x in value] 
  for key,value in my_dict.items()}
  
for key in my_dict.keys():
  print("Иду в ", key, ",","покупаю тут такие товары:", my_dict[key], ".")

num=sum(len(value) for value in my_dict.values()) 
print("Всего покупаю",num, "товаров")
my_dict["сырный"]= ["бри", "камамбер","голландский"]
print (my_dict)

print('Hello, Volodymyr! Happy New Year!')