# Count the White Space in a String

def countSpace1(Str):
    count = 0
    for stern in Str:
        if stern == " ":
            count += 1
    return count


def countSpace2(Str2):
    return Str2.count(" ")


a = input("Enter the String : ")
print("Count Space Using Hard Code Method       : ", countSpace1(a))
print("Count Space Using in the function Method : ", countSpace2(a))
