FullNamevariable = "Denys Zakharov" # імя користувача записане у базі данних
InputName = input("Input your name :") # змінна ініціалізована індефікаційними данними користувача  
InputName1 = [] # масив для кінцевого форматування 
# Якщо користувач написав своє призвище та імя разом але є змога вичислити по базі для перевідки
# Маємо прибрати дефіз
# Для цього збираємо конструктор 
# перша частина із имені користувача шо він ввів ДО того моменту де в базі є пробіл + сам символ пробілу + ПОЧИНАЮЧИ З пробілу і до кінця
InputName1 =InputName.strip().title()[0:FullNamevariable.strip().find(' ')]+ ' '+ InputName[FullNamevariable.find(' '):len(InputName)+1]

print(InputName1.title())

if (InputName1.title() == FullNamevariable):
    print("True")
else:
    print("False")
