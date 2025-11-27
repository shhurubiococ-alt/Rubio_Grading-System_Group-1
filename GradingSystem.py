subjects = [
    "ITE 366",
    "ITE 260",
    "GEN 001",
    "GEN 006",
    "GEN 002",
    "NST 021",
    "MAT 152",
    "PED 030"
]

students = []

while True:
    print("\n--- Grading System ---")
    print("1. Add Student Grades")
    print("2. View All Grades")
    print("3. Delete Student Grades")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID (e.g., 2324-0000): ")

        
        duplicate = any(
            s["name"].lower() == student_name.lower() and s["id"].lower() == student_id.lower()
            for s in students
        )

        if duplicate:
            print("❌ A student with the same name and ID already exists.")
            continue  
        student_grades = []

        print(f"\nEnter grades for {student_name}:")
        for subject in subjects:
            while True:
                try:
                    grade = float(input(f"{subject}: "))
                    if 0 <= grade <= 100:
                        if grade >= 90:
                            eq = 1.0
                        elif grade >= 80:
                            eq = 1.5
                        elif grade >= 70:
                            eq = 2.0
                        elif grade >= 60:
                            eq = 2.5
                        elif grade >= 50:
                            eq = 3.0
                        else:
                            eq = 4.0
                        student_grades.append([subject, grade, eq])
                        break
                    else:
                        print("⚠ Grade must be between 0 and 100.")
                except:
                    print("❌ Invalid input. Enter a number.")

        
        students.append({
            "name": student_name,
            "id": student_id,
            "grades": student_grades
        })
        print("✅ Student grades added!")

    elif choice == "2":
        if not students:
            print("⚠ No student records available.")
        else:
            print("\n--- All Student Records ---")
            for student in students:
                print(f"\n📌 Student ID: {student['id']}")
                print(f"👤 Name: {student['name']}")
                total = 0
                for record in student["grades"]:
                    subject = record[0]
                    grade = record[1]
                    eq = record[2]
                    print(f"{subject} - {grade} | Equivalent Grade: {eq}")
                    total += grade

                percentage = total / len(student["grades"])
                print(f"Total Percentage: {percentage:.2f}%")

                if percentage >= 90:
                    general = 1.0
                elif percentage >= 80:
                    general = 1.5
                elif percentage >= 70:
                    general = 2.0
                elif percentage >= 60:
                    general = 2.5
                elif percentage >= 50:
                    general = 3.0
                else:
                    general = 4.0

                print(f"General Grade: {general}")

    elif choice == "3":
        if not students:
            print("⚠ No student records to delete.")
        else:
            name_to_delete = input("Enter the student name to delete: ")
            id_to_delete = input("Enter the student ID to delete: ")
            found = False
            for student in students:
                if student["name"].lower() == name_to_delete.lower() and student["id"].lower() == id_to_delete.lower():
                    students.remove(student)
                    print(f"🗑 Record for {name_to_delete} (ID: {id_to_delete}) deleted.")
                    found = True
                    break
            if not found:
                print("❌ Student not found.")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter 1 to 4.")
