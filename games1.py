import random
num1 = random.randint(1,20)
num2 = 0
c = 0

while num2 != 'exit':
    num2 = input("taxminiy son tanlang 1 - 20 gacha, tugatish uchun 'exit' deb yozing: ")
  
    if num2 == "exit":
        print("Xayr 😊")
        break
    
    num2 = int(num2)
  
    c += 1
  
    if num2 < num1:
        print("siz kichkroq son kiritdingiz")
    
  
    elif num2 > num1:
        print("siz katta son kiritdingiz")
    else:
        print("To'g'ri!")
        print("Siz", c, "martta uringshda topdingiz!\n")
    

