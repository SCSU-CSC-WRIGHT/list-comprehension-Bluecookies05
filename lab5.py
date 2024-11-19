## ============= grade calculator lab 1 ================
def lab_1():
    num = int(input("Enter number of scores: "))
    scores = []

    for i in range(num):
        score = int(input("Enter the score: "))
        scores.append(score)

    print("Scores:", scores)
    avg = sum(scores) / len(scores)

    if avg >= 90:
        print("A")
    elif avg >= 80:
        print("B")
    elif avg >= 70:
        print("C")
    elif avg >= 60:
        print("D")
    else:
        print("F")


lab_1()
## ============= Even and odd number counter lab 2 ==================

def lab_2():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]  

    even_count = 0
    odd_count = 0
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
            even_numbers.append(num)
        else:
            odd_count += 1
            odd_numbers.append(num)

    print("Here are the even numbers:", even_numbers)
    print("Here are the odd numbers:", odd_numbers)
    print("Even numbers count:", even_count)
    print("Odd numbers count:", odd_count)


lab_2()
## ============ Unique list merger lab 3 =========================

def merge_remove_duplicates():
    list1 =input(" enter numbers that ARE SEPERATE BY SPACE!!: ")
    list2= input(" enter numbers that ARE SEPERATE BY SPACE!!: ")
    ComList=list1+list2

    list1=ComList.split(",")
    unique_input = [] 

    for num in ComList:
        if num not in unique_input:
         unique_input.append(num)

    print(unique_input)
    

# anything that is a set would auto check for duplicates 



merge_remove_duplicates()

