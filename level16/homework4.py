def check_entrance():
  
    height = float(input("გთხოვთ ჩაწეროთ თქვენი სიმაღლე სანტიმეტრებში: "))
    weight = float(input("გთხოვთ ჩაწეროთ თქვენი წონა კილოგრამებში: "))
    
    if height >= 180 and 50 <= weight <= 90:
        print("თქვენ შეგიძლიათ შედგეთ ზოოპარკში!")
    else:
        print("თქვენ ვერ შეძლებთ ზოოპარკში შესვლას")