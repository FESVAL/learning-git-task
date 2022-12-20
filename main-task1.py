my_dict = {
    "пекарня": ["хлеб", "булочки", "пончик"],
    "овощной": ["морковь", "петрушка", "рукола"]
    }
my_dict={key.capitalize():[x.capitalize() for x in value] 
    for key,value in my_dict.items()}


