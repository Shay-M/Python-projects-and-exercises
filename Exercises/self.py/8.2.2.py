def sort(args):
    return args[-1]


def sort_prices(list_of_tuples):
    print(sorted(list_of_tuples, key=sort))
    pass


products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)

#
# כתבו פונקציה שנקראת sort_prices המוגדרת כך:
#
# def sort_prices(list_of_tuples):
# הפונקציה מקבלת רשימה של טאפלים שבכל אחד פריט ומחירו.
# הפונקציה מחזירה רשימה של טאפלים ממוינים על פי מחיר הפריטים שבהם מהגדול לקטן.
#
# הגדירו את רשימת הטאפלים שהפונקציה מקבלת בהתאם לצורה הבאה:
#
# [('item', 'price'), ('item', 'price'), ('item', 'price')]
# שימו לב כי כל האיברים הם מטיפוס מחרוזת ומחיר כתוב כמספר שאינו שלם.
