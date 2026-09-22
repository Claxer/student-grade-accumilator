# 🎓 Student Grade Management and Performance Analyzer

A beginner-friendly **Student Grade Management and Performance Analyzer** that manages and analyzes student academic performance. The program accepts grades and attendance, calculates averages, determines letter grades and academic status, and provides detailed performance reports.

The project started as a **Python console-based application** and was later expanded into a **web-based application using HTML, CSS, and JavaScript**.

## 📌 Features

* 👨‍🎓 Process multiple students
* 📚 Record grades for:

  * Programming
  * Database
  * Mathematics
  * Networking
  * Web Development
* 📊 Calculate student averages
* 🏆 Determine letter grades from A to F
* ✅ Determine academic status
* 📈 Analyze student performance
* 🎓 Check scholarship eligibility
* ⚠️ Identify students who need academic warnings
* 📋 Analyze individual subject performance
* 🏫 Generate an overall class summary
* 🥇 Find the highest and lowest-performing students
* 📊 Calculate class average, pass percentage, and failure percentage

### 🆕 New Python Version Features

* 🏅 Determine honor eligibility
* 🏆 Identify students with Honors
* 🥇 Identify students with High Honors
* 👑 Identify students with Highest Honors
* 📚 Calculate an equivalent grade point
* ⚠️ Determine student academic risk level
* 🚨 Identify students who are at risk
* 📊 Track grade distribution from A to F
* 🏆 Rank students based on their average
* 🥇 Display the Top 3 students
* 📋 Store individual student records for class analysis
* 📅 Calculate the class attendance average
* 🏅 Find the student with the highest attendance
* 📚 Calculate the average grade for every subject
* ⭐ Identify the best-performing subject
* 📉 Identify the most difficult subject based on class average
* 📝 Display an honor students list
* 🚨 Display an at-risk students list
* 💡 Generate an overall class recommendation
* 📊 Provide additional class performance statistics
* 🔎 Search for a student by name
* 👁️ Display detailed information for a selected student
* 📋 View all processed students
* 📚 Identify subjects that are below the passing grade
* 👨‍🏫 Identify the highest-performing student in each subject
* 📊 Calculate the class median average
* 📈 Calculate the difference between the highest and lowest averages
* 🎓 Determine scholarship levels
* 📅 Determine individual attendance status
* 📝 Export student and class information to a text report
* 🛠️ Use an interactive Additional Tools menu
* 🔐 Improve input validation for grades, attendance, number of students, and names
* ❌ Handle invalid numeric input without crashing the program

### 🌐 Web Version Features

* 💻 Interactive web-based dashboard
* 👨‍🎓 Add and manage student records
* 📝 Add student grades and attendance
* 📊 Automatic average calculation
* 🏆 Automatic letter grade calculation
* ✅ Automatic academic status detection
* 📈 Automatic performance level detection
* 🎓 Automatic scholarship eligibility checking
* ⚠️ Automatic academic warning detection
* 🔎 Search student records
* 👁️ View detailed student information
* 🗑️ Delete student records
* 📋 Generate individual student performance reports
* 📊 Display class statistics on the dashboard
* 🥇 Display highest-performing student
* 📉 Display lowest-performing student
* 💾 Save student records using browser LocalStorage
* 📱 Responsive web interface
* 🪟 Student details modal
* 🔔 Interactive notifications and user feedback

## 🆕 Additional Python Tools

The Python version now includes an **Additional Tools** menu that appears after the main class analysis.

The menu provides several options:

```text
1. Search Student
2. View All Students
3. View Students Needing Improvement
4. View Subject Leaders
5. Show Class Median
6. Export Report
7. Exit
```

### 🔎 Search Student

The program allows the user to search for a student by name.

The search displays:

* Student name
* Average
* Letter grade
* Performance
* Attendance
* Attendance status
* Academic status
* Scholarship status
* Scholarship level
* Honor status
* Grade point
* Academic risk
* Class rank
* Subject grades
* Subjects below the passing grade

### 📋 View All Students

The program can display all students currently stored in the system.

Each student includes:

* Student number
* Name
* Average
* Letter grade
* Academic status

### 🚨 Students Needing Improvement

The program checks every student for subjects below the passing grade.

It also checks the student's overall academic risk.

This makes it easier to identify students who may need additional academic support.

### 👨‍🏫 Subject Leaders

The program identifies the student with the highest grade in each subject.

The subjects include:

* Programming
* Database
* Mathematics
* Networking
* Web Development

### 📊 Class Median

The program now calculates the **median class average**.

The median is calculated by arranging the student averages from lowest to highest and finding the middle value.

The program displays both:

* Class median
* Class mean average

This provides another way to analyze the overall performance of the class.

### 📈 Class Average Range

The program calculates the difference between the highest and lowest student averages.

```text
Average Range = Highest Average - Lowest Average
```

This helps show how spread out the student performance is.

### 📝 Export Report

The Python version can create a text report named:

```text
student_report.txt
```

The exported report contains:

* Total students
* Class average
* Class attendance
* Student names
* Student averages
* Letter grades
* Academic status
* Attendance
* Honor status
* Academic risk level

The report is automatically created in the same folder where the Python program is running.

## 🛠️ Concepts Used

This project demonstrates basic Python programming concepts, including:

* Functions
* `if`, `elif`, and `else` statements
* `for` loops
* `while` loops
* Nested loops
* Logical operators (`and`, `or`)
* Arithmetic operators
* Input validation
* Exception handling
* Variables and data types
* Lists
* Dictionaries
* Lists of dictionaries
* String formatting
* Sorting
* `max()` and `min()` functions
* Lambda functions
* `enumerate()`
* `sum()`
* List comprehensions
* Basic statistics and calculations
* Searching records
* File writing
* Record management
* Storing and processing multiple records

### 🌐 Web Development Concepts Used

The web version also demonstrates:

* HTML5
* CSS3
* JavaScript
* Arrays and objects
* DOM manipulation
* Event handling
* Form handling
* LocalStorage
* Responsive web design
* Modal interfaces
* Search and filtering
* Dynamic content updates

## ⚙️ How It Works

### 🐍 Python Version

1. The user enters the number of students to process.
2. The program asks for each student's name.
3. Grades for five subjects are entered.
4. The student's attendance percentage is entered.
5. The program validates the entered information.
6. The program calculates the student's average.
7. It determines the:

   * Letter grade
   * Academic status
   * Performance level
   * Scholarship eligibility
   * Scholarship level
   * Academic warning
   * Honor eligibility
   * Grade point
   * Academic risk level
   * Attendance status
8. A detailed student performance report is displayed.
9. The student's subject grades are analyzed.
10. Subjects below the passing grade are identified.
11. The student's information is stored in a list of dictionaries.
12. The next student is processed until all students have been entered.
13. After processing all students, a class summary is generated.
14. The program calculates the average performance of every subject.
15. The program identifies the best-performing and most difficult subjects.
16. Students are ranked from highest to lowest average.
17. The Top 3 students are displayed.
18. At-risk students and honor students are displayed.
19. Grade distribution and attendance statistics are calculated.
20. The class median is calculated.
21. The difference between the highest and lowest averages is calculated.
22. Students with subjects needing improvement are identified.
23. The program identifies the highest-performing student for each subject.
24. An overall class recommendation is generated.
25. The user can access the Additional Tools menu.
26. The user can search students, view records, check improvement areas, view subject leaders, calculate the median, or export a report.

### 🌐 Web Version

1. The user opens the web application.
2. Student information is entered through the student form.
3. Grades and attendance are entered.
4. The system validates the entered information.
5. JavaScript automatically calculates the student's average.
6. The system determines the:

   * Letter grade
   * Academic status
   * Performance level
   * Scholarship eligibility
   * Academic warning
7. The student record is added to the dashboard.
8. Class statistics are automatically updated.
9. Students can be searched and their details can be viewed.
10. Student records can be deleted from the dashboard.
11. Student information is saved using browser LocalStorage.

## 📊 Grading System

|  Average | Letter Grade |
| -------: | :----------: |
|   90–100 |       A      |
|    80–89 |       B      |
|    70–79 |       C      |
|    60–69 |       D      |
| Below 60 |       F      |

## 📈 Performance Levels

|  Average | Performance       |
| -------: | :---------------- |
|   95–100 | Outstanding       |
|    90–94 | Excellent         |
|    85–89 | Very Good         |
|    80–84 | Good              |
|    75–79 | Satisfactory      |
|    60–74 | Needs Improvement |
| Below 60 | Poor              |

## ✅ Academic Status

A student is considered **PASSED** when:

* Average is **75 or higher**
* Attendance is **80% or higher**

Otherwise, the student is marked **FAILED**.

## 🎓 Scholarship Eligibility

The original scholarship check considers a student qualified when:

* Average is **90 or higher**
* Attendance is **90% or higher**

The expanded Python version also provides additional scholarship levels.

| Requirement                     | Scholarship Level   |
| :------------------------------ | :------------------ |
| Average 95+ and Attendance 95%+ | Full Scholarship    |
| Average 90+ and Attendance 90%+ | Scholarship         |
| Average 85+ and Attendance 85%+ | Partial Scholarship |
| Does not meet requirements      | Not Eligible        |

## 🏅 Honor Eligibility

The Python version includes an additional honor classification system.

| Requirement                     | Honor Status        |
| :------------------------------ | :------------------ |
| Average 85+ and Attendance 85%+ | With Honors         |
| Average 90+ and Attendance 90%+ | With High Honors    |
| Average 95+ and Attendance 90%+ | With Highest Honors |
| Does not meet requirements      | No Honor            |

This allows the program to identify students who meet different academic achievement levels.

## 📚 Grade Point

The Python version converts the student's average into an equivalent grade point.

|  Average | Grade Point |
| -------: | :---------: |
|      95+ |     1.00    |
|    90–94 |     1.25    |
|    85–89 |     1.50    |
|    80–84 |     1.75    |
|    75–79 |     2.00    |
|    70–74 |     2.25    |
|    65–69 |     2.50    |
|    60–64 |     2.75    |
| Below 60 |     5.00    |

## ⚠️ Academic Warning

An academic warning is given when:

* The student's average is below **75**, or
* Attendance is below **80%**

The program also identifies whether the issue is related to grades, attendance, or both.

## 🚨 Academic Risk Level

The Python version also analyzes the student's overall academic risk.

| Condition                                 | Risk Level    |
| :---------------------------------------- | :------------ |
| Average 75+ and Attendance 80%+           | Low Risk      |
| Average below 75 OR Attendance below 80%  | Moderate Risk |
| Average below 75 AND Attendance below 80% | High Risk     |

This allows the program to quickly identify students who may need additional academic support.

## 📅 Attendance Status

The Python version now provides a separate description for attendance performance.

| Attendance | Status            |
| ---------: | :---------------- |
|    95–100% | Excellent         |
|     90–94% | Very Good         |
|     80–89% | Good              |
|     75–79% | Needs Improvement |
|  Below 75% | Critical          |

## 📊 Class Statistics

After all students have been processed, the program displays:

* Total number of students
* Number of passed students
* Number of failed students
* Pass percentage
* Failure percentage
* Number of excellent students
* Class average
* Class median
* Highest average
* Top student
* Lowest average
* Lowest-performing student
* Overall class performance
* Class attendance average
* Student with the highest attendance
* Number of students at risk
* Number of honor students
* Grade distribution
* Average range
* Number of scholarship students

The web version displays these statistics directly on the dashboard and automatically updates them when student records are added or deleted.

## 🏆 Student Ranking

The Python version stores the processed student records and sorts them according to their average.

The ranking displays:

* Student rank
* Student name
* Average
* Letter grade
* Academic status

The program also displays the **Top 3 students** separately for quick identification of the highest-performing students.

The student search tool can also display an individual student's current class rank.

## 🚨 At-Risk Students

The program provides a separate list of students who have either:

* An average below 75
* Attendance below 80%
* Both low academic performance and low attendance

This makes it easier to identify students who may require additional academic support.

## 🏅 Honor Students

The program also generates a separate list of students who qualify for:

* With Honors
* With High Honors
* With Highest Honors

This provides a quick overview of the students with strong academic performance.

## 📚 Subject Class Performance

The Python version calculates the **class average for every subject**.

The subjects analyzed are:

* Programming
* Database
* Mathematics
* Networking
* Web Development

The program then identifies:

* The best-performing subject
* The highest subject average
* The most difficult subject
* The lowest subject average

This allows the user to determine which subjects the class performs well in and which subjects may require additional attention.

## 👨‍🏫 Subject Leaders

The expanded Python version identifies the student with the highest grade in each subject.

For example:

```text
Programming         Jose Navoa            95.00
Database            Student 2             93.00
Mathematics         Student 3             97.00
Networking          Student 1             91.00
Web Development     Student 4             96.00
```

This provides another way to analyze individual subject performance.

## 📊 Grade Distribution

The program counts the number of students who received each letter grade:

* A
* B
* C
* D
* F

This provides a quick overview of the overall grade distribution of the class.

## 📅 Attendance Statistics

The Python version also analyzes class attendance.

It calculates:

* Class attendance average
* Highest attendance percentage
* Student with the highest attendance
* Individual attendance status

This allows attendance to be analyzed alongside academic performance.

## 📉 Failed Subject Analysis

The expanded version checks each student's individual subjects.

A subject is considered to need improvement when its grade is below **75**.

The program can display:

```text
Student Name        : Subjects Below Passing
Student 1           : Mathematics, Networking
Student 2           : Database
```

If no student has a subject below 75, the program displays that there are no subjects needing improvement.

## 📊 Median and Average Range

The Python version now provides additional statistical information.

### Class Median

The median represents the middle value of all student averages after they have been sorted.

### Average Range

The range is calculated using:

```text
Highest Average - Lowest Average
```

These statistics provide additional information about the distribution of student performance.

## 💡 Class Recommendation

After analyzing the class, the program provides a recommendation based on:

* Overall class average
* Overall attendance average
* Academic performance
* Attendance performance

The recommendation can indicate whether the class is performing excellently, satisfactorily, or needs improvement.

## 📝 Report Export

The Python version can export a basic class report to:

```text
student_report.txt
```

The exported file contains information about the class and each processed student.

Example:

```text
STUDENT GRADE MANAGEMENT AND PERFORMANCE ANALYZER
=================================================================
Total Students: 5
Class Average: 88.50
Class Attendance: 92.00%

STUDENT #1: Student Name
Average: 91.50
Grade: A
Status: PASSED
Attendance: 95.00%
Honor: WITH HIGH HONORS
Risk: LOW RISK
-----------------------------------------------------------------
```

This feature demonstrates basic Python file handling and allows the results to be saved outside the program.

## 💾 Student Record Management

The Python version stores each student as a dictionary inside a list.

Each student record can contain:

* Name
* Average
* Attendance
* Letter grade
* Academic status
* Performance
* Scholarship status
* Scholarship level
* Honor status
* Grade point
* Risk level
* Attendance status
* Subject grades

This allows the program to search, sort, rank, and analyze student records after they have been entered.

## 🛠️ Input Validation

The expanded Python version includes additional validation to prevent common input errors.

The program checks:

* Number of students
* Student name
* Subject grades
* Attendance percentage
* Numeric input

Grades and attendance must remain between **0 and 100**.

Invalid numeric input is handled without immediately crashing the program.

## 💻 Technologies Used

### Python Version

* Python 3.x
* Functions
* Conditional statements
* `for` loops
* `while` loops
* Lists
* Dictionaries
* Lists of dictionaries
* Sorting
* Lambda functions
* `max()` and `min()`
* `enumerate()`
* List comprehensions
* File handling
* Input validation
* Exception handling
* Basic statistics and calculations

### Web Version

* HTML5
* CSS3
* JavaScript
* LocalStorage
* Responsive Web Design

## 💾 Data Storage

The web version uses **LocalStorage** to save student records in the browser.

This allows student information to remain available even after refreshing the webpage.

The Python version stores student information in memory while the program is running. Student records are placed into a list of dictionaries so they can be searched, sorted, ranked, analyzed, and included in additional reports.

The Python version can also export selected class and student information to a text file using the `student_report.txt` file.

> Note: LocalStorage is used for this educational project and is not intended to replace a production database.

## 💻 Requirements

### Python Version

* Python 3.x
* No external libraries are required.

### Web Version

* Modern web browser
* No additional libraries or frameworks are required.

## 🚀 How to Run

### 🐍 Python Version

1. Install **Python 3** on your computer.
2. Clone this repository:

```bash
git clone https://github.com/yourusername/student-grade-management.git
```

3. Open the project folder.
4. Run the Python file:

```bash
python main.py
```

5. Follow the instructions displayed in the terminal.
6. After the class analysis is finished, use the **Additional Tools** menu if you want to search students, view records, analyze subjects, or export a report.

### 🌐 Web Version

1. Open the project folder.
2. Navigate to the web version folder.
3. Open `index.html` in a web browser.

You can also use **VS Code with Live Server** for easier development.

## 📁 Project Structure

```text
Student-Grade-Management/
│
├── README.md
│
├── web-version/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── python-version/
    └── index.py
```

The project contains two versions:

### Python Version

* Console-based student grade management system
* Focuses on Python programming logic and problem solving
* Performs student ranking and class analysis
* Provides academic risk and honor analysis
* Calculates subject performance statistics
* Calculates median and average range
* Provides student search and record viewing
* Identifies subjects needing improvement
* Identifies subject leaders
* Provides detailed student information
* Exports class results to a text file
* Provides an interactive Additional Tools menu

### Web Version

* Browser-based student grade management system
* Focuses on HTML, CSS, JavaScript, UI design, and interactivity
* Uses LocalStorage for student records
* Provides an interactive dashboard for managing students
* Provides search and student detail features
* Automatically updates class statistics

## 🎯 Purpose

This project was created as a beginner-level Python programming project to practice **programming logic, functions, conditional statements, loops, input validation, and basic data analysis**.

The project was later expanded into a web application to practice **HTML, CSS, JavaScript, DOM manipulation, form handling, LocalStorage, responsive design, and user interface development**.

The Python version has also been expanded to demonstrate more programming concepts such as:

* Lists of dictionaries
* Sorting
* Lambda functions
* `max()` and `min()`
* `enumerate()`
* List comprehensions
* Record management
* Student searching
* Ranking systems
* Academic risk analysis
* Honor classification
* Scholarship classification
* Attendance analysis
* Subject-level statistics
* Median calculation
* File handling
* Report generation
* Input validation
* Exception handling

The goal is to demonstrate how the same student grade management logic can be implemented in both a **Python console application** and an **interactive web application**.

## 👨‍💻 Author

**Jose Navoa**

First-Year Information Technology Student

## 📄 License

This project is for **educational and learning purposes**.
