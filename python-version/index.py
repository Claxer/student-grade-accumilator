# STUDENT GRADE MANAGEMENT AND PERFORMANCE ANALYZER

# FUNCTION: Determine Letter Grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# FUNCTION: Determine Academic Status
def get_status(average, attendance):
    if average >= 75 and attendance >= 80:
        return "PASSED"
    elif average < 75 or attendance < 80:
        return "FAILED"

# FUNCTION: Determine Performance Description
def get_performance(average):
    if average >= 95:
        return "Outstanding"
    elif average >= 90:
        return "Excellent"
    elif average >= 85:
        return "Very Good"
    elif average >= 80:
        return "Good"
    elif average >= 75:
        return "Satisfactory"
    elif average >= 60:
        return "Needs Improvement"
    else:
        return "Poor"

# FUNCTION: Validate Grade
def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter grade in {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Invalid grade! Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

# FUNCTION: Validate Attendance
def get_valid_attendance():
    while True:
        try:
            attendance = float(input("Enter attendance percentage (0-100): "))
            if 0 <= attendance <= 100:
                return attendance
            print("Invalid attendance percentage!")
        except ValueError:
            print("Please enter a valid number.")

# NEW FEATURE: Determine Honor Eligibility
def get_honor_status(average, attendance):
    if average >= 95 and attendance >= 90:
        return "WITH HIGHEST HONORS"
    elif average >= 90 and attendance >= 90:
        return "WITH HIGH HONORS"
    elif average >= 85 and attendance >= 85:
        return "WITH HONORS"
    else:
        return "NO HONOR"

# NEW FEATURE: Find Subject Remark
def get_subject_remark(grade):
    if grade >= 90:
        return "Excellent"
    elif grade >= 85:
        return "Very Good"
    elif grade >= 80:
        return "Good"
    elif grade >= 75:
        return "Passed"
    elif grade >= 60:
        return "Needs Improvement"
    else:
        return "Failed"

# NEW FEATURE: Get Grade Point
def get_grade_point(average):
    if average >= 95:
        return 1.00
    elif average >= 90:
        return 1.25
    elif average >= 85:
        return 1.50
    elif average >= 80:
        return 1.75
    elif average >= 75:
        return 2.00
    elif average >= 70:
        return 2.25
    elif average >= 65:
        return 2.50
    elif average >= 60:
        return 2.75
    else:
        return 5.00

# NEW FEATURE: Determine Risk Level
def get_risk_level(average, attendance):
    if average < 75 and attendance < 80:
        return "HIGH RISK"
    elif average < 75 or attendance < 80:
        return "MODERATE RISK"
    else:
        return "LOW RISK"

# NEW FEATURE: Attendance Status
def get_attendance_status(attendance):
    if attendance >= 95:
        return "Excellent"
    elif attendance >= 90:
        return "Very Good"
    elif attendance >= 80:
        return "Good"
    elif attendance >= 75:
        return "Needs Improvement"
    else:
        return "Critical"

# NEW FEATURE: Scholarship Level
def get_scholarship_level(average, attendance):
    if average >= 95 and attendance >= 95:
        return "FULL SCHOLARSHIP"
    elif average >= 90 and attendance >= 90:
        return "SCHOLARSHIP"
    elif average >= 85 and attendance >= 85:
        return "PARTIAL SCHOLARSHIP"
    else:
        return "NOT ELIGIBLE"

# NEW FEATURE: Calculate Median
def calculate_median(numbers):
    if not numbers:
        return 0
    values = sorted(numbers)
    middle = len(values) // 2
    if len(values) % 2 == 0:
        return (values[middle - 1] + values[middle]) / 2
    return values[middle]

# NEW FEATURE: Find Student
def find_student(records, search_name):
    for student in records:
        if search_name.lower() in student["name"].lower():
            return student
    return None

# NEW FEATURE: Get Failed Subjects
def get_failed_subjects(subjects):
    failed = []
    for subject, grade in subjects.items():
        if grade < 75:
            failed.append(subject)
    return failed

# NEW FEATURE: Get Student Rank
def get_student_rank(records, name):
    ranking = sorted(records, key=lambda student: student["average"], reverse=True)
    for rank, student in enumerate(ranking, start=1):
        if student["name"] == name:
            return rank
    return 0

# NEW FEATURE: Display Student Details
def display_student_details(student, records):
    print("\n" + "=" * 65)
    print("                    STUDENT DETAILS")
    print("=" * 65)
    print(f"Name              : {student['name']}")
    print(f"Average           : {student['average']:.2f}")
    print(f"Letter Grade      : {student['letter_grade']}")
    print(f"Performance       : {student['performance']}")
    print(f"Attendance        : {student['attendance']:.2f}%")
    print(f"Attendance Status : {student['attendance_status']}")
    print(f"Academic Status   : {student['status']}")
    print(f"Scholarship       : {student['scholarship']}")
    print(f"Scholarship Level : {student['scholarship_level']}")
    print(f"Honor Status      : {student['honor']}")
    print(f"Grade Point       : {student['grade_point']:.2f}")
    print(f"Risk Level        : {student['risk']}")
    print(f"Class Rank        : {get_student_rank(records, student['name'])}")
    failed = get_failed_subjects(student["subjects"])
    print("\nSUBJECTS")
    for subject, grade in student["subjects"].items():
        print(f"{subject:20} {grade:6.2f} - {get_subject_remark(grade)}")
    if failed:
        print("\nSubjects Below Passing: " + ", ".join(failed))
    else:
        print("\nAll subjects are passing.")

# NEW FEATURE: Export Report
def export_report(records, class_average, attendance_average):
    try:
        with open("student_report.txt", "w", encoding="utf-8") as file:
            file.write("STUDENT GRADE MANAGEMENT AND PERFORMANCE ANALYZER\n")
            file.write("=" * 65 + "\n")
            file.write(f"Total Students: {len(records)}\n")
            file.write(f"Class Average: {class_average:.2f}\n")
            file.write(f"Class Attendance: {attendance_average:.2f}%\n\n")
            for number, student in enumerate(records, start=1):
                file.write(f"STUDENT #{number}: {student['name']}\n")
                file.write(f"Average: {student['average']:.2f}\n")
                file.write(f"Grade: {student['letter_grade']}\n")
                file.write(f"Status: {student['status']}\n")
                file.write(f"Attendance: {student['attendance']:.2f}%\n")
                file.write(f"Honor: {student['honor']}\n")
                file.write(f"Risk: {student['risk']}\n")
                file.write("-" * 65 + "\n")
        print("\nReport saved as student_report.txt")
    except OSError:
        print("\nUnable to save the report.")

# NEW FEATURE: Additional Tools Menu
def additional_tools(records, subject_class_averages, class_average, attendance_average):
    while True:
        print("\n" + "=" * 65)
        print("                    ADDITIONAL TOOLS")
        print("=" * 65)
        print("1. Search Student")
        print("2. View All Students")
        print("3. View Students Needing Improvement")
        print("4. View Subject Leaders")
        print("5. Show Class Median")
        print("6. Export Report")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            search = input("Enter student name to search: ").strip()
            student = find_student(records, search)
            if student:
                display_student_details(student, records)
            else:
                print("Student not found.")
        elif choice == "2":
            print("\nALL STUDENTS")
            print("-" * 65)
            for number, student in enumerate(records, start=1):
                print(f"{number}. {student['name']:20} Average: {student['average']:.2f} "
                      f"Grade: {student['letter_grade']} Status: {student['status']}")
        elif choice == "3":
            print("\nSTUDENTS NEEDING IMPROVEMENT")
            print("-" * 65)
            found = False
            for student in records:
                failed = get_failed_subjects(student["subjects"])
                if failed or student["risk"] != "LOW RISK":
                    found = True
                    print(f"{student['name']:20} Average: {student['average']:.2f} "
                          f"Risk: {student['risk']}")
                    if failed:
                        print("  Subjects: " + ", ".join(failed))
            if not found:
                print("No students currently need improvement.")
        elif choice == "4":
            print("\nSUBJECT LEADERS")
            print("-" * 65)
            for subject in subject_class_averages:
                best = max(records, key=lambda student: student["subjects"][subject])
                print(f"{subject:20} {best['name']:20} "
                      f"{best['subjects'][subject]:.2f}")
        elif choice == "5":
            averages = [student["average"] for student in records]
            median = calculate_median(averages)
            print(f"\nClass Median Average: {median:.2f}")
            print(f"Class Mean Average  : {class_average:.2f}")
            print(f"Class Attendance    : {attendance_average:.2f}%")
        elif choice == "6":
            export_report(records, class_average, attendance_average)
        elif choice == "7":
            print("\nThank you for using the Student Grade Management System!")
            break
        else:
            print("Invalid option. Please choose 1-7.")

# MAIN PROGRAM
print("=" * 65)
print("     STUDENT GRADE MANAGEMENT AND PERFORMANCE ANALYZER")
print("=" * 65)

# Ask number of students
while True:
    try:
        number_of_students = int(input("\nHow many students do you want to process? "))
        if number_of_students > 0:
            break
        print("Number of students must be greater than zero.")
    except ValueError:
        print("Please enter a whole number.")

# CLASS STATISTICS VARIABLES
total_class_average = 0
passed_students = 0
failed_students = 0
highest_average = 0
lowest_average = 101
highest_student = ""
lowest_student = ""
excellent_students = 0
total_class_attendance = 0
highest_attendance = 0
highest_attendance_student = ""
honors_students = 0
high_honors_students = 0
highest_honors_students = 0
at_risk_students = 0
grade_a_count = 0
grade_b_count = 0
grade_c_count = 0
grade_d_count = 0
grade_f_count = 0
programming_total = 0
database_total = 0
mathematics_total = 0
networking_total = 0
web_development_total = 0
student_records = []

# FOR LOOP - PROCESS MULTIPLE STUDENTS
for student_number in range(1, number_of_students + 1):
    print("\n" + "=" * 65)
    print(f"STUDENT #{student_number}")
    print("=" * 65)

    name = input("Enter student name: ").strip().title()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip().title()

    programming = get_valid_grade("Programming")
    database = get_valid_grade("Database")
    mathematics = get_valid_grade("Mathematics")
    networking = get_valid_grade("Networking")
    web_development = get_valid_grade("Web Development")
    attendance = get_valid_attendance()

    total_grade = programming + database + mathematics + networking + web_development
    average = total_grade / 5
    letter_grade = get_letter_grade(average)
    status = get_status(average, attendance)
    performance = get_performance(average)

    if average >= 90 and attendance >= 90:
        scholarship = "QUALIFIED"
    else:
        scholarship = "NOT QUALIFIED"

    academic_warning = average < 75 or attendance < 80
    honor_status = get_honor_status(average, attendance)
    grade_point = get_grade_point(average)
    risk_level = get_risk_level(average, attendance)
    attendance_status = get_attendance_status(attendance)
    scholarship_level = get_scholarship_level(average, attendance)

    subjects = {
        "Programming": programming,
        "Database": database,
        "Mathematics": mathematics,
        "Networking": networking,
        "Web Development": web_development
    }

    if status == "PASSED":
        passed_students += 1
    else:
        failed_students += 1

    if average >= 90:
        excellent_students += 1

    if honor_status == "WITH HONORS":
        honors_students += 1
    elif honor_status == "WITH HIGH HONORS":
        high_honors_students += 1
    elif honor_status == "WITH HIGHEST HONORS":
        highest_honors_students += 1

    if risk_level != "LOW RISK":
        at_risk_students += 1

    if letter_grade == "A":
        grade_a_count += 1
    elif letter_grade == "B":
        grade_b_count += 1
    elif letter_grade == "C":
        grade_c_count += 1
    elif letter_grade == "D":
        grade_d_count += 1
    else:
        grade_f_count += 1

    if average > highest_average:
        highest_average = average
        highest_student = name

    if average < lowest_average:
        lowest_average = average
        lowest_student = name

    total_class_average += average
    total_class_attendance += attendance

    if attendance > highest_attendance:
        highest_attendance = attendance
        highest_attendance_student = name

    programming_total += programming
    database_total += database
    mathematics_total += mathematics
    networking_total += networking
    web_development_total += web_development

    student_records.append({
        "name": name,
        "average": average,
        "attendance": attendance,
        "letter_grade": letter_grade,
        "status": status,
        "performance": performance,
        "scholarship": scholarship,
        "honor": honor_status,
        "grade_point": grade_point,
        "risk": risk_level,
        "attendance_status": attendance_status,
        "scholarship_level": scholarship_level,
        "subjects": subjects
    })

    # INDIVIDUAL STUDENT REPORT
    print("\n" + "-" * 65)
    print("STUDENT PERFORMANCE REPORT")
    print("-" * 65)
    print(f"Student Name       : {name}")
    print("\nSUBJECT GRADES")
    for subject, grade in subjects.items():
        print(f"{subject:20} : {grade:.2f} ({get_subject_remark(grade)})")
    print("-" * 65)
    print(f"Average            : {average:.2f}")
    print(f"Letter Grade       : {letter_grade}")
    print(f"Performance        : {performance}")
    print(f"Attendance         : {attendance:.2f}%")
    print(f"Attendance Status  : {attendance_status}")
    print(f"Academic Status    : {status}")
    print(f"Scholarship        : {scholarship}")
    print(f"Scholarship Level  : {scholarship_level}")
    print(f"Grade Point        : {grade_point:.2f}")
    print(f"Honor Status       : {honor_status}")
    print(f"Risk Level         : {risk_level}")

    if academic_warning:
        print("\nACADEMIC WARNING:")
        if average < 75 and attendance < 80:
            print("Student has both low grades and low attendance.")
        elif average < 75:
            print("Student needs to improve academic performance.")
        elif attendance < 80:
            print("Student needs to improve class attendance.")
    else:
        print("\nNo academic warning.")

    print("\nSUBJECT PERFORMANCE ANALYSIS")
    for subject, grade in subjects.items():
        print(f"{subject:20} {grade:6.2f} {get_subject_remark(grade)}")

# CLASS SUMMARY
class_average = total_class_average / number_of_students
pass_percentage = passed_students / number_of_students * 100
fail_percentage = failed_students / number_of_students * 100
class_attendance_average = total_class_attendance / number_of_students

programming_average = programming_total / number_of_students
database_average = database_total / number_of_students
mathematics_average = mathematics_total / number_of_students
networking_average = networking_total / number_of_students
web_development_average = web_development_total / number_of_students

print("\n\n" + "=" * 65)
print("                    CLASS SUMMARY")
print("=" * 65)
print(f"Total Students       : {number_of_students}")
print(f"Passed Students      : {passed_students}")
print(f"Failed Students      : {failed_students}")
print(f"Pass Percentage      : {pass_percentage:.2f}%")
print(f"Failure Percentage   : {fail_percentage:.2f}%")
print(f"Excellent Students   : {excellent_students}")
print(f"Class Average        : {class_average:.2f}")
print(f"Highest Average      : {highest_average:.2f}")
print(f"Top Student          : {highest_student}")
print(f"Lowest Average       : {lowest_average:.2f}")
print(f"Lowest Student       : {lowest_student}")

print("\n" + "-" * 65)
print("                    ATTENDANCE SUMMARY")
print("-" * 65)
print(f"Class Attendance Avg : {class_attendance_average:.2f}%")
print(f"Best Attendance      : {highest_attendance:.2f}%")
print(f"Best Attendance By   : {highest_attendance_student}")

print("\n" + "-" * 65)
print("                     HONOR SUMMARY")
print("-" * 65)
print(f"With Honors          : {honors_students}")
print(f"With High Honors     : {high_honors_students}")
print(f"With Highest Honors  : {highest_honors_students}")

print("\n" + "-" * 65)
print("                     RISK SUMMARY")
print("-" * 65)
print(f"Students At Risk     : {at_risk_students}")

print("\n" + "-" * 65)
print("                    GRADE DISTRIBUTION")
print("-" * 65)
print(f"A Grades             : {grade_a_count}")
print(f"B Grades             : {grade_b_count}")
print(f"C Grades             : {grade_c_count}")
print(f"D Grades             : {grade_d_count}")
print(f"F Grades             : {grade_f_count}")

subject_class_averages = {
    "Programming": programming_average,
    "Database": database_average,
    "Mathematics": mathematics_average,
    "Networking": networking_average,
    "Web Development": web_development_average
}

print("\n" + "-" * 65)
print("              SUBJECT CLASS PERFORMANCE")
print("-" * 65)
for subject, subject_average in subject_class_averages.items():
    print(f"{subject:20} {subject_average:6.2f} {get_performance(subject_average)}")

best_subject = max(subject_class_averages, key=subject_class_averages.get)
difficult_subject = min(subject_class_averages, key=subject_class_averages.get)

print("\n" + "-" * 65)
print("                  SUBJECT ANALYSIS")
print("-" * 65)
print(f"Best Performing Subject : {best_subject}")
print(f"Highest Subject Average : {subject_class_averages[best_subject]:.2f}")
print(f"Most Difficult Subject  : {difficult_subject}")
print(f"Lowest Subject Average  : {subject_class_averages[difficult_subject]:.2f}")

student_ranking = sorted(student_records, key=lambda student: student["average"], reverse=True)

print("\n" + "=" * 65)
print("                     STUDENT RANKING")
print("=" * 65)
for rank, student in enumerate(student_ranking, start=1):
    print(f"{rank:2}. {student['name']:20} Average: {student['average']:6.2f} "
          f"Grade: {student['letter_grade']} Status: {student['status']}")

print("\n" + "-" * 65)
print("                       TOP 3 STUDENTS")
print("-" * 65)
for rank, student in enumerate(student_ranking[:3], start=1):
    print(f"{rank}. {student['name']} - {student['average']:.2f}")

print("\n" + "-" * 65)
print("                     AT-RISK STUDENTS")
print("-" * 65)
risk_found = False
for student in student_records:
    if student["risk"] != "LOW RISK":
        risk_found = True
        print(f"{student['name']:20} Average: {student['average']:.2f} "
              f"Attendance: {student['attendance']:.2f}% Risk: {student['risk']}")
if not risk_found:
    print("No students are currently at risk.")

print("\n" + "-" * 65)
print("                      HONOR STUDENTS")
print("-" * 65)
honor_found = False
for student in student_records:
    if student["honor"] != "NO HONOR":
        honor_found = True
        print(f"{student['name']:20} {student['average']:.2f} - {student['honor']}")
if not honor_found:
    print("No students qualified for honors.")

print("\nOVERALL CLASS PERFORMANCE:")
if class_average >= 90:
    print("Excellent Class Performance")
elif class_average >= 80:
    print("Very Good Class Performance")
elif class_average >= 75:
    print("Satisfactory Class Performance")
else:
    print("Class Performance Needs Improvement")

print("\n" + "-" * 65)
print("                  CLASS RECOMMENDATION")
print("-" * 65)
if class_average >= 90 and class_attendance_average >= 90:
    print("The class is performing excellently academically and has strong attendance.")
elif class_average >= 75 and class_attendance_average >= 80:
    print("The class is performing satisfactorily. Students should continue maintaining their grades and attendance.")
elif class_average < 75 and class_attendance_average < 80:
    print("The class needs significant improvement in both academic performance and attendance.")
elif class_average < 75:
    print("The class should focus on improving academic performance.")
else:
    print("The class should focus on improving attendance.")

# NEW FEATURE: MEDIAN AND CLASS RANGE
all_averages = [student["average"] for student in student_records]
median_average = calculate_median(all_averages)
average_range = highest_average - lowest_average
print("\n" + "-" * 65)
print("                ADDITIONAL CLASS STATISTICS")
print("-" * 65)
print(f"Class Median Average : {median_average:.2f}")
print(f"Highest-Lowest Range : {average_range:.2f}")
print(f"Scholarship Students : {sum(1 for s in student_records if s['scholarship_level'] != 'NOT ELIGIBLE')}")

# NEW FEATURE: STUDENTS WITH FAILED SUBJECTS
print("\n" + "-" * 65)
print("                 SUBJECT IMPROVEMENT LIST")
print("-" * 65)
improvement_found = False
for student in student_records:
    failed = get_failed_subjects(student["subjects"])
    if failed:
        improvement_found = True
        print(f"{student['name']:20}: {', '.join(failed)}")
if not improvement_found:
    print("No students have subjects below 75.")

print("\n" + "=" * 65)
print("                    PROGRAM STATISTICS")
print("=" * 65)
print(f"Students Processed   : {number_of_students}")
print(f"Students Passed      : {passed_students}")
print(f"Students Failed      : {failed_students}")
print(f"Students At Risk     : {at_risk_students}")
print(f"Honor Students       : {honors_students + high_honors_students + highest_honors_students}")
print(f"Class Average        : {class_average:.2f}")
print(f"Class Attendance     : {class_attendance_average:.2f}%")

# NEW FEATURE: ADDITIONAL TOOLS
additional_tools(student_records, subject_class_averages, class_average, class_attendance_average)

print("\n" + "=" * 65)
print("               END OF PROGRAM")
print("=" * 65)
