def reportCard(student_name, age):
    print("Name of Student:", student_name)
    print("Age of Student:", age)
    
    max_paper_marks = int(input("Enter the maximum marks a paper can have: "))
    total_marks = 0
    subjects = ["Data Structure", "DBMS", "Python", "Java", "Maths"]
    
    for subject in subjects:
        marks = int(input(f"Enter Marks of {subject}: "))

        
        while marks > max_paper_marks:
            print(f"Entered marks ({marks}) cannot exceed the maximum marks ({max_paper_marks}).")
            marks = int(input(f"Enter Marks of {subject}: "))

        if((marks*100)/max_paper_marks < 40):
            print(f"{student_name} , You have failed in {subject} You have to appear for re-Exam")
        total_marks += marks
        
    
    print("Total Marks is", total_marks)
    percent = (total_marks * 100) / (len(subjects) * max_paper_marks)
    print("Your Percent is:", percent)
    
    if percent < 40:
        print("Fail")
        print("\n")
    elif 40 <= percent < 60:
        print("Average")
        print("\n")
    elif 60 <= percent < 80:
        print("Great")
        print("\n")
    else:
        print("Distinction")
        print("\n")

reportCard("Aditya", 20)
