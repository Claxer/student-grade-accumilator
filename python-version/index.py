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
    # Logical AND operator
    if average >= 75 and attendance >= 80:
        return "PASSED"

    # Logical OR operator
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
        grade = float(input(f"Enter grade in {subject} (0-100): "))

        # Range checking
        if 0 <= grade <= 100:
            return grade
        else:
            print("Invalid grade!")
            print("Grade must be between 0 and 100.\n")


# FUNCTION: Validate Attendance
def get_valid_attendance():
    while True:
        attendance = float(input("Enter attendance percentage (0-100): "))

        if 0 <= attendance <= 100:
            return attendance
        else:
            print("Invalid attendance percentage!\n")


# ============================================================
# NEW FEATURE FUNCTIONS
# ============================================================

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


# MAIN PROGRAM

print("=" * 65)
print("     STUDENT GRADE MANAGEMENT AND PERFORMANCE ANALYZER")
print("=" * 65)


# Ask number of students
while True:
    number_of_students = int(
        input("\nHow many students do you want to process? ")
    )

    if number_of_students > 0:
        break

    print("Number of students must be greater than zero.")


# ============================================================
# CLASS STATISTICS VARIABLES
# ============================================================

total_class_average = 0

passed_students = 0
failed_students = 0

highest_average = 0
lowest_average = 101

highest_student = ""
lowest_student = ""

excellent_students = 0


# ============================================================
# NEW FEATURE: ADDITIONAL CLASS STATISTICS
# ============================================================

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


# NEW FEATURE: Subject totals
programming_total = 0
database_total = 0
mathematics_total = 0
networking_total = 0
web_development_total = 0


# NEW FEATURE:
# Store information about every student
student_records = []


# ============================================================
# FOR LOOP - PROCESS MULTIPLE STUDENTS
# ============================================================

for student_number in range(1, number_of_students + 1):

    print("\n" + "=" * 65)
    print(f"STUDENT #{student_number}")
    print("=" * 65)

    name = input("Enter student name: ").strip().title()

    # Subject Grades
    programming = get_valid_grade("Programming")
    database = get_valid_grade("Database")
    mathematics = get_valid_grade("Mathematics")
    networking = get_valid_grade("Networking")
    web_development = get_valid_grade("Web Development")

    # Attendance
    attendance = get_valid_attendance()

    # Calculate Average
    # Arithmetic Operators
    total_grade = (
        programming
        + database
        + mathematics
        + networking
        + web_development
    )

    average = total_grade / 5

    # Determine Grade and Status

    letter_grade = get_letter_grade(average)

    status = get_status(
        average,
        attendance
    )

    performance = get_performance(average)

    # Determine Scholarship Eligibility
    if average >= 90 and attendance >= 90:
        scholarship = "QUALIFIED"
    else:
        scholarship = "NOT QUALIFIED"

    # Determine Academic Warning
    academic_warning = False

    if average < 75 or attendance < 80:
        academic_warning = True

    # ========================================================
    # NEW FEATURE: HONOR STATUS
    # ========================================================

    honor_status = get_honor_status(
        average,
        attendance
    )

    # ========================================================
    # NEW FEATURE: GRADE POINT
    # ========================================================

    grade_point = get_grade_point(average)

    # ========================================================
    # NEW FEATURE: RISK LEVEL
    # ========================================================

    risk_level = get_risk_level(
        average,
        attendance
    )

    # Count Passed / Failed

    if status == "PASSED":
        passed_students += 1
    else:
        failed_students += 1

    # Count Excellent Students

    if average >= 90:
        excellent_students += 1

    # ========================================================
    # NEW FEATURE: COUNT HONOR STUDENTS
    # ========================================================

    if honor_status == "WITH HONORS":
        honors_students += 1

    elif honor_status == "WITH HIGH HONORS":
        high_honors_students += 1

    elif honor_status == "WITH HIGHEST HONORS":
        highest_honors_students += 1

    # ========================================================
    # NEW FEATURE: COUNT AT-RISK STUDENTS
    # ========================================================

    if risk_level != "LOW RISK":
        at_risk_students += 1

    # ========================================================
    # NEW FEATURE: GRADE DISTRIBUTION
    # ========================================================

    if letter_grade == "A":
        grade_a_count += 1

    elif letter_grade == "B":
        grade_b_count += 1

    elif letter_grade == "C":
        grade_c_count += 1

    elif letter_grade == "D":
        grade_d_count += 1

    elif letter_grade == "F":
        grade_f_count += 1

    # Find Highest Student

    if average > highest_average:
        highest_average = average
        highest_student = name

    # Find Lowest Student

    if average < lowest_average:
        lowest_average = average
        lowest_student = name

    # Add average to class total
    total_class_average += average

    # ========================================================
    # NEW FEATURE: ATTENDANCE STATISTICS
    # ========================================================

    total_class_attendance += attendance

    if attendance > highest_attendance:
        highest_attendance = attendance
        highest_attendance_student = name

    # ========================================================
    # NEW FEATURE: SUBJECT TOTALS
    # ========================================================

    programming_total += programming
    database_total += database
    mathematics_total += mathematics
    networking_total += networking
    web_development_total += web_development

    # ========================================================
    # NEW FEATURE:
    # SAVE STUDENT INFORMATION
    # ========================================================

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
        "risk": risk_level
    })

    # ========================================================
    # INDIVIDUAL STUDENT REPORT
    # ========================================================

    print("\n" + "-" * 65)
    print("STUDENT PERFORMANCE REPORT")
    print("-" * 65)

    print(f"Student Name       : {name}")

    print("\nSUBJECT GRADES")

    print(f"Programming        : {programming:.2f}")
    print(f"Database           : {database:.2f}")
    print(f"Mathematics        : {mathematics:.2f}")
    print(f"Networking         : {networking:.2f}")
    print(f"Web Development    : {web_development:.2f}")

    print("-" * 65)

    print(f"Average            : {average:.2f}")
    print(f"Letter Grade       : {letter_grade}")
    print(f"Performance        : {performance}")
    print(f"Attendance         : {attendance:.2f}%")
    print(f"Academic Status    : {status}")
    print(f"Scholarship        : {scholarship}")

    # ========================================================
    # NEW FEATURE: EXTRA STUDENT INFORMATION
    # ========================================================

    print(f"Grade Point        : {grade_point:.2f}")
    print(f"Honor Status       : {honor_status}")
    print(f"Risk Level         : {risk_level}")

    # Nested Selection

    if academic_warning:

        print("\nACADEMIC WARNING:")

        if average < 75 and attendance < 80:
            print(
                "Student has both low grades "
                "and low attendance."
            )

        elif average < 75:
            print(
                "Student needs to improve "
                "academic performance."
            )

        elif attendance < 80:
            print(
                "Student needs to improve "
                "class attendance."
            )

    else:
        print("\nNo academic warning.")

    # ========================================================
    # Subject Analysis
    # ========================================================

    print("\nSUBJECT PERFORMANCE ANALYSIS")

    subject_names = [
        "Programming",
        "Database",
        "Mathematics",
        "Networking",
        "Web Development"
    ]

    subject_grades = [
        programming,
        database,
        mathematics,
        networking,
        web_development
    ]

    # Nested for loop

    for i in range(len(subject_names)):

        if subject_grades[i] >= 90:
            remark = "Excellent"

        elif subject_grades[i] >= 75:
            remark = "Passed"

        else:
            remark = "Needs Improvement"

        print(
            f"{subject_names[i]:20} "
            f"{subject_grades[i]:6.2f} "
            f"{remark}"
        )


# ============================================================
# CLASS SUMMARY
# ============================================================

class_average = (
    total_class_average / number_of_students
)

pass_percentage = (
    passed_students / number_of_students
) * 100

fail_percentage = (
    failed_students / number_of_students
) * 100


# ============================================================
# NEW FEATURE: CLASS ATTENDANCE AVERAGE
# ============================================================

class_attendance_average = (
    total_class_attendance / number_of_students
)


# ============================================================
# NEW FEATURE: SUBJECT CLASS AVERAGES
# ============================================================

programming_average = (
    programming_total / number_of_students
)

database_average = (
    database_total / number_of_students
)

mathematics_average = (
    mathematics_total / number_of_students
)

networking_average = (
    networking_total / number_of_students
)

web_development_average = (
    web_development_total / number_of_students
)


# ============================================================
# ORIGINAL CLASS SUMMARY
# ============================================================

print("\n\n" + "=" * 65)
print("                    CLASS SUMMARY")
print("=" * 65)

print(f"Total Students       : {number_of_students}")

print(
    f"Passed Students      : "
    f"{passed_students}"
)

print(
    f"Failed Students      : "
    f"{failed_students}"
)

print(
    f"Pass Percentage      : "
    f"{pass_percentage:.2f}%"
)

print(
    f"Failure Percentage   : "
    f"{fail_percentage:.2f}%"
)

print(
    f"Excellent Students   : "
    f"{excellent_students}"
)

print(
    f"Class Average        : "
    f"{class_average:.2f}"
)

print(
    f"Highest Average      : "
    f"{highest_average:.2f}"
)

print(
    f"Top Student          : "
    f"{highest_student}"
)

print(
    f"Lowest Average       : "
    f"{lowest_average:.2f}"
)

print(
    f"Lowest Student       : "
    f"{lowest_student}"
)


# ============================================================
# NEW FEATURE: ATTENDANCE SUMMARY
# ============================================================

print("\n" + "-" * 65)
print("                    ATTENDANCE SUMMARY")
print("-" * 65)

print(
    f"Class Attendance Avg : "
    f"{class_attendance_average:.2f}%"
)

print(
    f"Best Attendance      : "
    f"{highest_attendance:.2f}%"
)

print(
    f"Best Attendance By   : "
    f"{highest_attendance_student}"
)


# ============================================================
# NEW FEATURE: HONOR SUMMARY
# ============================================================

print("\n" + "-" * 65)
print("                     HONOR SUMMARY")
print("-" * 65)

print(
    f"With Honors          : "
    f"{honors_students}"
)

print(
    f"With High Honors     : "
    f"{high_honors_students}"
)

print(
    f"With Highest Honors  : "
    f"{highest_honors_students}"
)


# ============================================================
# NEW FEATURE: RISK SUMMARY
# ============================================================

print("\n" + "-" * 65)
print("                     RISK SUMMARY")
print("-" * 65)

print(
    f"Students At Risk     : "
    f"{at_risk_students}"
)


# ============================================================
# NEW FEATURE: GRADE DISTRIBUTION
# ============================================================

print("\n" + "-" * 65)
print("                    GRADE DISTRIBUTION")
print("-" * 65)

print(f"A Grades             : {grade_a_count}")
print(f"B Grades             : {grade_b_count}")
print(f"C Grades             : {grade_c_count}")
print(f"D Grades             : {grade_d_count}")
print(f"F Grades             : {grade_f_count}")


# ============================================================
# NEW FEATURE: SUBJECT CLASS PERFORMANCE
# ============================================================

print("\n" + "-" * 65)
print("              SUBJECT CLASS PERFORMANCE")
print("-" * 65)

subject_class_averages = {
    "Programming": programming_average,
    "Database": database_average,
    "Mathematics": mathematics_average,
    "Networking": networking_average,
    "Web Development": web_development_average
}

for subject, subject_average in subject_class_averages.items():

    if subject_average >= 90:
        remark = "Excellent"

    elif subject_average >= 85:
        remark = "Very Good"

    elif subject_average >= 80:
        remark = "Good"

    elif subject_average >= 75:
        remark = "Satisfactory"

    else:
        remark = "Needs Improvement"

    print(
        f"{subject:20} "
        f"{subject_average:6.2f} "
        f"{remark}"
    )


# ============================================================
# NEW FEATURE: BEST AND MOST DIFFICULT SUBJECT
# ============================================================

best_subject = max(
    subject_class_averages,
    key=subject_class_averages.get
)

difficult_subject = min(
    subject_class_averages,
    key=subject_class_averages.get
)

print("\n" + "-" * 65)
print("                  SUBJECT ANALYSIS")
print("-" * 65)

print(
    f"Best Performing Subject : "
    f"{best_subject}"
)

print(
    f"Highest Subject Average : "
    f"{subject_class_averages[best_subject]:.2f}"
)

print(
    f"Most Difficult Subject  : "
    f"{difficult_subject}"
)

print(
    f"Lowest Subject Average  : "
    f"{subject_class_averages[difficult_subject]:.2f}"
)


# ============================================================
# NEW FEATURE: STUDENT RANKING
# ============================================================

student_ranking = sorted(
    student_records,
    key=lambda student: student["average"],
    reverse=True
)

print("\n" + "=" * 65)
print("                     STUDENT RANKING")
print("=" * 65)

for rank, student in enumerate(student_ranking, start=1):

    print(
        f"{rank:2}. "
        f"{student['name']:20} "
        f"Average: {student['average']:6.2f} "
        f"Grade: {student['letter_grade']} "
        f"Status: {student['status']}"
    )


# ============================================================
# NEW FEATURE: TOP 3 STUDENTS
# ============================================================

print("\n" + "-" * 65)
print("                       TOP 3 STUDENTS")
print("-" * 65)

top_three = student_ranking[:3]

for rank, student in enumerate(top_three, start=1):

    print(
        f"{rank}. {student['name']} "
        f"- {student['average']:.2f}"
    )


# ============================================================
# NEW FEATURE: AT-RISK STUDENTS
# ============================================================

print("\n" + "-" * 65)
print("                     AT-RISK STUDENTS")
print("-" * 65)

risk_found = False

for student in student_records:

    if student["risk"] != "LOW RISK":

        risk_found = True

        print(
            f"{student['name']:20} "
            f"Average: {student['average']:.2f} "
            f"Attendance: {student['attendance']:.2f}% "
            f"Risk: {student['risk']}"
        )

if not risk_found:
    print("No students are currently at risk.")


# ============================================================
# NEW FEATURE: HONOR STUDENTS LIST
# ============================================================

print("\n" + "-" * 65)
print("                      HONOR STUDENTS")
print("-" * 65)

honor_found = False

for student in student_records:

    if student["honor"] != "NO HONOR":

        honor_found = True

        print(
            f"{student['name']:20} "
            f"{student['average']:.2f} "
            f"- {student['honor']}"
        )

if not honor_found:
    print("No students qualified for honors.")


# ============================================================
# OVERALL CLASS PERFORMANCE
# ============================================================

print("\nOVERALL CLASS PERFORMANCE:")

if class_average >= 90:
    print("Excellent Class Performance")

elif class_average >= 80:
    print("Very Good Class Performance")

elif class_average >= 75:
    print("Satisfactory Class Performance")

else:
    print("Class Performance Needs Improvement")


# ============================================================
# NEW FEATURE: OVERALL CLASS RECOMMENDATION
# ============================================================

print("\n" + "-" * 65)
print("                  CLASS RECOMMENDATION")
print("-" * 65)

if class_average >= 90 and class_attendance_average >= 90:

    print(
        "The class is performing excellently "
        "academically and has strong attendance."
    )

elif class_average >= 75 and class_attendance_average >= 80:

    print(
        "The class is performing satisfactorily. "
        "Students should continue maintaining "
        "their grades and attendance."
    )

elif class_average < 75 and class_attendance_average < 80:

    print(
        "The class needs significant improvement "
        "in both academic performance and attendance."
    )

elif class_average < 75:

    print(
        "The class should focus on improving "
        "academic performance."
    )

else:

    print(
        "The class should focus on improving "
        "attendance."
    )


# ============================================================
# NEW FEATURE: PROGRAM STATISTICS
# ============================================================

print("\n" + "=" * 65)
print("                    PROGRAM STATISTICS")
print("=" * 65)

print(
    f"Students Processed   : "
    f"{number_of_students}"
)

print(
    f"Students Passed      : "
    f"{passed_students}"
)

print(
    f"Students Failed      : "
    f"{failed_students}"
)

print(
    f"Students At Risk     : "
    f"{at_risk_students}"
)

print(
    f"Honor Students       : "
    f"{honors_students + high_honors_students + highest_honors_students}"
)

print(
    f"Class Average        : "
    f"{class_average:.2f}"
)

print(
    f"Class Attendance     : "
    f"{class_attendance_average:.2f}%"
)


# ============================================================
# END OF PROGRAM
# ============================================================

print("\n" + "=" * 65)
print("               END OF PROGRAM")
print("=" * 65)
