def calculate_medication(weight):
    if 10 <= weight <= 20:
        return 0.5, 1  
    elif 30 <= weight <= 40:
        return 1, 2  
    elif weight > 45:
        return 3, 2  
    else:
        return "არასათანადო წონა"


weight = float(input("შეიყვანეთ თქვენი წონა (კილოგრამებში): "))
tablets, times_per_day = calculate_medication(weight)

if tablets == "არასათანადო წონა":
    print("გთხოვთ, შეიყვანეთ სწორი წონა.")
else:
    print(f"თქვენ უნდა დალიოთ {tablets} ტაბლეტი(ები) {times_per_day} -ჯერ დღეში.")