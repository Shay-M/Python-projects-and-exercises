# create dictionary
this_dict = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": '27.03.1970',
    "hobbies": ["Sing", "Compose", "Act"]
}
"""הדפיסו למסך את שם המשפחה של מריה.
הדפיסו למסך את החודש בו נולדה מריה.
הדפיסו למסך את מספר התחביבים שיש למריה.
הדפיסו למסך את התחביב האחרון ברשימת התחביבים של מריה.
הוסיפו את התחביב "Cooking" לסוף רשימת התחביבים.
הפכו את טיפוס תאריך הלידה לטאפל שכולל 3 מספרים (יום, חודש ושנה - משמאל לימין) והדפיסו אותו.
הוסיפו מפתח חדש בשם age אשר כולל את גילה של מריה והציגו אותו."""
inn = int(input("enter num for command: "))
while inn > 0:
    if inn == 1:
        print("last_name: ", this_dict["last_name"])
    elif inn == 2:
        print("birth_date", this_dict["birth_date"])
    elif inn == 3:
        print(len(this_dict["hobbies"]))
    elif inn == 4:
        print(this_dict["hobbies"][-1])
    elif inn == 5:
        print(this_dict["hobbies"].append("Cooking"))
    elif inn == 6:
        temp_tuple = tuple(this_dict["birth_date"].split("."))
        i = len(temp_tuple)
        while i > 0:
            print(temp_tuple[i - 1])
            i = i - 1
    elif inn == 7:
        temp_tuple = tuple(this_dict["birth_date"].split("."))
        this_dict.update({"age": 2020 - int(temp_tuple[2])})
        print("age", this_dict["age"])
    inn = int(input("enter: "))
