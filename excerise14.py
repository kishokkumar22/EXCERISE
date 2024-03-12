# Ranking System in Python using list and user definer function
def ranking(marks):
    total = sum(marks)
    avg = total / len(marks)
    print("Total marks : ", total)
    print("Average     : ", avg)
    for mark in marks:
        if mark <= 35:
            return "We are sorry about that your are Failed in the Examination. Better luck Next time."

    return "Congratulations you are Passed in the Examination. Keep Rocking"


list1 = ["Tamil", "English", "Maths", "Science", "Social Science"]
list2 = []
for i in list1:
    a = int(input(f"Enter the {i} mark : "))
    list2.append(a)

print(ranking(list2))
