/* ============================================
   STUDENT GRADE MANAGEMENT SYSTEM
   ============================================ */


/* ============================================
   DATA
   ============================================ */

let students = JSON.parse(
    localStorage.getItem("students")
) || [];


/* ============================================
   SUBJECTS
   ============================================ */

const subjects = [
    "Programming",
    "Database",
    "Mathematics",
    "Networking",
    "Web Development"
];


/* ============================================
   DOM ELEMENTS
   ============================================ */

const form = document.getElementById("studentForm");

const studentCards =
    document.getElementById("studentCards");

const searchInput =
    document.getElementById("searchInput");

const modal =
    document.getElementById("studentModal");

const modalContent =
    document.getElementById("modalContent");

const toast =
    document.getElementById("toast");


/* ============================================
   PYTHON FUNCTION EQUIVALENTS
   ============================================ */


/*
    Python:

    def get_letter_grade(average):
*/

function getLetterGrade(average) {

    if (average >= 90) {
        return "A";
    }

    else if (average >= 80) {
        return "B";
    }

    else if (average >= 70) {
        return "C";
    }

    else if (average >= 60) {
        return "D";
    }

    else {
        return "F";
    }
}


/*
    Python:

    def get_status(average, attendance):
*/

function getStatus(average, attendance) {

    if (
        average >= 75 &&
        attendance >= 80
    ) {
        return "PASSED";
    }

    else if (
        average < 75 ||
        attendance < 80
    ) {
        return "FAILED";
    }
}


/*
    Python:

    def get_performance(average):
*/

function getPerformance(average) {

    if (average >= 95) {
        return "Outstanding";
    }

    else if (average >= 90) {
        return "Excellent";
    }

    else if (average >= 85) {
        return "Very Good";
    }

    else if (average >= 80) {
        return "Good";
    }

    else if (average >= 75) {
        return "Satisfactory";
    }

    else if (average >= 60) {
        return "Needs Improvement";
    }

    else {
        return "Poor";
    }
}


/* ============================================
   VALIDATION
   ============================================ */

function validateGrade(value) {

    return (
        !isNaN(value) &&
        value >= 0 &&
        value <= 100
    );
}


function validateAttendance(value) {

    return (
        !isNaN(value) &&
        value >= 0 &&
        value <= 100
    );
}


/* ============================================
   ACADEMIC WARNING
   ============================================ */

function getAcademicWarning(
    average,
    attendance
) {

    if (
        average < 75 &&
        attendance < 80
    ) {

        return {
            warning: true,
            message:
                "Student has both low grades and low attendance."
        };
    }


    else if (average < 75) {

        return {
            warning: true,
            message:
                "Student needs to improve academic performance."
        };
    }


    else if (attendance < 80) {

        return {
            warning: true,
            message:
                "Student needs to improve class attendance."
        };
    }


    return {
        warning: false,
        message: "No academic warning."
    };
}


/* ============================================
   SUBJECT REMARK
   ============================================ */

function getSubjectRemark(grade) {

    if (grade >= 90) {
        return "Excellent";
    }

    else if (grade >= 75) {
        return "Passed";
    }

    else {
        return "Needs Improvement";
    }
}


/* ============================================
   NAME FORMATTER
   ============================================ */

function formatName(name) {

    return name
        .trim()
        .toLowerCase()
        .replace(/\b\w/g, char =>
            char.toUpperCase()
        );
}


/* ============================================
   ADD STUDENT
   ============================================ */

form.addEventListener("submit", function (event) {

    event.preventDefault();


    const name =
        formatName(
            document.getElementById(
                "studentName"
            ).value
        );


    const programming =
        Number(
            document.getElementById(
                "programming"
            ).value
        );


    const database =
        Number(
            document.getElementById(
                "database"
            ).value
        );


    const mathematics =
        Number(
            document.getElementById(
                "mathematics"
            ).value
        );


    const networking =
        Number(
            document.getElementById(
                "networking"
            ).value
        );


    const webDevelopment =
        Number(
            document.getElementById(
                "webDevelopment"
            ).value
        );


    const attendance =
        Number(
            document.getElementById(
                "attendance"
            ).value
        );


    /* VALIDATION */

    const grades = [
        programming,
        database,
        mathematics,
        networking,
        webDevelopment
    ];


    if (!name) {

        showToast(
            "Please enter a student name."
        );

        return;
    }


    if (
        grades.some(
            grade => !validateGrade(grade)
        )
    ) {

        showToast(
            "Grades must be between 0 and 100."
        );

        return;
    }


    if (
        !validateAttendance(attendance)
    ) {

        showToast(
            "Attendance must be between 0 and 100."
        );

        return;
    }


    /* CALCULATE AVERAGE */

    const totalGrade =
        grades.reduce(
            (total, grade) =>
                total + grade,
            0
        );


    const average =
        totalGrade / 5;


    /* DETERMINE RESULTS */

    const letterGrade =
        getLetterGrade(average);


    const status =
        getStatus(
            average,
            attendance
        );


    const performance =
        getPerformance(average);


    /* SCHOLARSHIP */

    const scholarship =
        average >= 90 &&
        attendance >= 90
            ? "QUALIFIED"
            : "NOT QUALIFIED";


    /* WARNING */

    const warning =
        getAcademicWarning(
            average,
            attendance
        );


    /* CREATE STUDENT OBJECT */

    const student = {

        id: Date.now(),

        name,

        grades: {

            Programming:
                programming,

            Database:
                database,

            Mathematics:
                mathematics,

            Networking:
                networking,

            "Web Development":
                webDevelopment

        },

        attendance,

        totalGrade,

        average,

        letterGrade,

        status,

        performance,

        scholarship,

        academicWarning:
            warning.warning,

        warningMessage:
            warning.message

    };


    /* ADD STUDENT */

    students.push(student);


    saveStudents();

    updateDashboard();

    renderStudents();

    renderReports();


    form.reset();


    showToast(
        `${name} was successfully added.`
    );


    /* SCROLL TO STUDENTS */

    setTimeout(() => {

        document
            .getElementById("students")
            .scrollIntoView({
                behavior: "smooth"
            });

    }, 300);

});


/* ============================================
   SAVE DATA
   ============================================ */

function saveStudents() {

    localStorage.setItem(
        "students",
        JSON.stringify(students)
    );
}


/* ============================================
   DASHBOARD
   ============================================ */

function updateDashboard() {

    const total =
        students.length;


    const passed =
        students.filter(
            student =>
                student.status === "PASSED"
        ).length;


    const failed =
        students.filter(
            student =>
                student.status === "FAILED"
        ).length;


    const excellent =
        students.filter(
            student =>
                student.average >= 90
        ).length;


    const classAverage =
        total > 0

            ? students.reduce(
                (sum, student) =>
                    sum + student.average,
                0
            ) / total

            : 0;


    const passPercentage =
        total > 0
            ? (passed / total) * 100
            : 0;


    const failPercentage =
        total > 0
            ? (failed / total) * 100
            : 0;


    /* HIGHEST */

    const highest =
        students.length

            ? students.reduce(
                (a, b) =>
                    a.average > b.average
                        ? a
                        : b
            )

            : null;


    /* LOWEST */

    const lowest =
        students.length

            ? students.reduce(
                (a, b) =>
                    a.average < b.average
                        ? a
                        : b
            )

            : null;


    /* UPDATE STAT CARDS */

    document.getElementById(
        "totalStudents"
    ).textContent = total;


    document.getElementById(
        "passedStudents"
    ).textContent = passed;


    document.getElementById(
        "failedStudents"
    ).textContent = failed;


    document.getElementById(
        "classAverage"
    ).textContent =
        classAverage.toFixed(2);


    /* PASS RATE */

    document.getElementById(
        "passPercentage"
    ).textContent =
        `${passPercentage.toFixed(0)}%`;


    document.getElementById(
        "passedPercentText"
    ).textContent =
        `${passPercentage.toFixed(0)}%`;


    document.getElementById(
        "failedPercentText"
    ).textContent =
        `${failPercentage.toFixed(0)}%`;


    document.getElementById(
        "passedProgress"
    ).style.width =
        `${passPercentage}%`;


    document.getElementById(
        "failedProgress"
    ).style.width =
        `${failPercentage}%`;


    /* CIRCLE */

    const circle =
        document.getElementById(
            "passCircle"
        );


    circle.style.background =
        `conic-gradient(
            var(--primary)
            ${passPercentage * 3.6}deg,
            #edf0f6
            ${passPercentage * 3.6}deg
        )`;


    /* OVERALL PERFORMANCE */

    let overall =
        "No Data";


    if (total > 0) {

        if (classAverage >= 90) {
            overall =
                "Excellent Class Performance";
        }

        else if (classAverage >= 80) {
            overall =
                "Very Good Class Performance";
        }

        else if (classAverage >= 75) {
            overall =
                "Satisfactory Class Performance";
        }

        else {
            overall =
                "Class Performance Needs Improvement";
        }
    }


    document.getElementById(
        "overallPerformance"
    ).textContent = overall;


    /* SUMMARY */

    document.getElementById(
        "excellentStudents"
    ).textContent = excellent;


    document.getElementById(
        "highestAverage"
    ).textContent =
        highest
            ? highest.average.toFixed(2)
            : "0.00";


    document.getElementById(
        "topStudent"
    ).textContent =
        highest
            ? highest.name
            : "—";


    document.getElementById(
        "lowestAverage"
    ).textContent =
        lowest
            ? lowest.average.toFixed(2)
            : "0.00";


    document.getElementById(
        "lowestStudent"
    ).textContent =
        lowest
            ? lowest.name
            : "—";


    document.getElementById(
        "failurePercentage"
    ).textContent =
        `${failPercentage.toFixed(0)}%`;


    renderTopStudent(highest);
}


/* ============================================
   TOP STUDENT
   ============================================ */

function renderTopStudent(student) {

    const container =
        document.getElementById(
            "topStudentContainer"
        );


    if (!student) {

        container.innerHTML = `
            <div class="empty-state">
                No student data available.
            </div>
        `;

        return;
    }


    container.innerHTML = `

        <div class="top-student">

            <div class="student-avatar">
                ${getInitials(student.name)}
            </div>

            <div class="top-student-info">

                <h3>
                    ${escapeHTML(student.name)}
                </h3>

                <span>
                    ${student.performance}
                </span>

            </div>

            <div class="top-score">

                <strong>
                    ${student.average.toFixed(2)}
                </strong>

                <span>
                    Average
                </span>

            </div>

        </div>
    `;
}


/* ============================================
   RENDER STUDENTS
   ============================================ */

function renderStudents(
    searchTerm = ""
) {

    const filtered =
        students.filter(student =>
            student.name
                .toLowerCase()
                .includes(
                    searchTerm
                        .toLowerCase()
                )
        );


    if (filtered.length === 0) {

        studentCards.innerHTML = `

            <div class="empty-students">

                <div class="empty-icon">
                    ♙
                </div>

                <h3>
                    ${
                        students.length === 0
                            ? "No Students Added"
                            : "No Students Found"
                    }
                </h3>

                <p>
                    ${
                        students.length === 0
                            ? "Add a student to start analyzing class performance."
                            : "Try searching for another student."
                    }
                </p>

                ${
                    students.length === 0
                        ? `
                            <button
                                class="primary-btn"
                                onclick="scrollToAddStudent()"
                            >
                                Add First Student
                            </button>
                        `
                        : ""
                }

            </div>
        `;

        return;
    }


    studentCards.innerHTML =
        filtered.map(
            student =>
                createStudentCard(student)
        ).join("");
}


/* ============================================
   STUDENT CARD
   ============================================ */

function createStudentCard(student) {

    const statusClass =
        student.status === "PASSED"
            ? "status-passed"
            : "status-failed";


    return `

        <div class="student-card">

            <div class="student-card-header">

                <div class="card-avatar">
                    ${getInitials(student.name)}
                </div>

                <div>

                    <h3>
                        ${escapeHTML(student.name)}
                    </h3>

                    <p>
                        Grade ${student.letterGrade}
                        • ${student.performance}
                    </p>

                </div>


                <div class="card-actions">

                    <button
                        class="icon-btn"
                        onclick="viewStudent(${student.id})"
                        title="View"
                    >
                        👁
                    </button>

                    <button
                        class="icon-btn delete"
                        onclick="deleteStudent(${student.id})"
                        title="Delete"
                    >
                        ×
                    </button>

                </div>

            </div>


            <div class="card-stats">

                <div class="card-stat">

                    <span>
                        Average
                    </span>

                    <strong>
                        ${student.average.toFixed(2)}
                    </strong>

                </div>


                <div class="card-stat">

                    <span>
                        Grade
                    </span>

                    <strong>
                        ${student.letterGrade}
                    </strong>

                </div>


                <div class="card-stat">

                    <span>
                        Status
                    </span>

                    <span
                        class="status-badge ${statusClass}"
                    >
                        ${student.status}
                    </span>

                </div>

            </div>


            <div class="card-footer">

                <span class="attendance">
                    Attendance:
                    <strong>
                        ${student.attendance.toFixed(2)}%
                    </strong>
                </span>


                <span class="status-badge performance-badge">
                    ${student.scholarship}
                </span>

            </div>

        </div>
    `;
}


/* ============================================
   REPORTS
   ============================================ */

function renderReports() {

    const container =
        document.getElementById(
            "reportContainer"
        );


    if (students.length === 0) {

        container.innerHTML = `

            <div class="empty-state">
                Add students to generate performance reports.
            </div>
        `;

        return;
    }


    container.innerHTML =
        students.map(
            student =>
                createReport(student)
        ).join("");
}


function createReport(student) {

    const rows =
        Object.entries(
            student.grades
        )
        .map(
            ([subject, grade]) => {

                const remark =
                    getSubjectRemark(
                        grade
                    );


                let className =
                    "improve";


                if (
                    remark === "Excellent"
                ) {
                    className =
                        "excellent";
                }

                else if (
                    remark === "Passed"
                ) {
                    className =
                        "passed";
                }


                return `

                    <tr>

                        <td>
                            ${subject}
                        </td>

                        <td>
                            ${grade.toFixed(2)}
                        </td>

                        <td
                            class="remark ${className}"
                        >
                            ${remark}
                        </td>

                    </tr>
                `;
            }
        )
        .join("");


    return `

        <div class="report-card">

            <div class="report-header">

                <div>

                    <p class="eyebrow">
                        STUDENT REPORT
                    </p>

                    <h3>
                        ${escapeHTML(student.name)}
                    </h3>

                </div>

                <span class="status-badge ${
                    student.status === "PASSED"
                        ? "status-passed"
                        : "status-failed"
                }">
                    ${student.status}
                </span>

            </div>


            <table class="subject-table">

                <thead>

                    <tr>
                        <th>Subject</th>
                        <th>Grade</th>
                        <th>Remark</th>
                    </tr>

                </thead>

                <tbody>
                    ${rows}
                </tbody>

            </table>

        </div>
    `;
}


/* ============================================
   VIEW STUDENT
   ============================================ */

function viewStudent(id) {

    const student =
        students.find(
            student =>
                student.id === id
        );


    if (!student) return;


    const warning =
        student.academicWarning
            ? `
                <div class="warning-box">
                    <strong>
                        Academic Warning
                    </strong>

                    <p>
                        ${student.warningMessage}
                    </p>
                </div>
            `
            : "";


    modalContent.innerHTML = `

        <h2 class="modal-title">
            ${escapeHTML(student.name)}
        </h2>

        <p class="modal-subtitle">
            Student Performance Report
        </p>


        <div class="modal-grid">

            <div class="modal-stat">
                <span>Average</span>
                <strong>
                    ${student.average.toFixed(2)}
                </strong>
            </div>

            <div class="modal-stat">
                <span>Letter Grade</span>
                <strong>
                    ${student.letterGrade}
                </strong>
            </div>

            <div class="modal-stat">
                <span>Performance</span>
                <strong>
                    ${student.performance}
                </strong>
            </div>

            <div class="modal-stat">
                <span>Attendance</span>
                <strong>
                    ${student.attendance.toFixed(2)}%
                </strong>
            </div>

            <div class="modal-stat">
                <span>Academic Status</span>
                <strong>
                    ${student.status}
                </strong>
            </div>

            <div class="modal-stat">
                <span>Scholarship</span>
                <strong>
                    ${student.scholarship}
                </strong>
            </div>

        </div>


        <br>

        <p class="eyebrow">
            SUBJECT PERFORMANCE
        </p>

        <table class="subject-table">

            <thead>

                <tr>
                    <th>Subject</th>
                    <th>Grade</th>
                    <th>Remark</th>
                </tr>

            </thead>

            <tbody>

                ${
                    Object.entries(
                        student.grades
                    )
                    .map(
                        ([subject, grade]) => {

                            const remark =
                                getSubjectRemark(
                                    grade
                                );


                            return `
                                <tr>

                                    <td>
                                        ${subject}
                                    </td>

                                    <td>
                                        ${grade.toFixed(2)}
                                    </td>

                                    <td>
                                        ${remark}
                                    </td>

                                </tr>
                            `;
                        }
                    )
                    .join("")
                }

            </tbody>

        </table>


        ${warning}

    `;


    modal.classList.add("show");
}


/* ============================================
   DELETE STUDENT
   ============================================ */

function deleteStudent(id) {

    const student =
        students.find(
            student =>
                student.id === id
        );


    if (!student) return;


    const confirmed =
        confirm(
            `Delete ${student.name}'s record?`
        );


    if (!confirmed) return;


    students =
        students.filter(
            student =>
                student.id !== id
        );


    saveStudents();

    updateDashboard();

    renderStudents(
        searchInput.value
    );

    renderReports();


    showToast(
        `${student.name} was deleted.`
    );
}


/* ============================================
   SEARCH
   ============================================ */

searchInput.addEventListener(
    "input",
    function () {

        renderStudents(
            this.value
        );
    }
);


/* ============================================
   NAVIGATION BUTTONS
   ============================================ */

document
    .getElementById("headerAddBtn")
    .addEventListener(
        "click",
        scrollToAddStudent
    );


document
    .getElementById("emptyAddBtn")
    ?.addEventListener(
        "click",
        scrollToAddStudent
    );


function scrollToAddStudent() {

    document
        .getElementById("addStudent")
        .scrollIntoView({
            behavior: "smooth"
        });
}


/* ============================================
   MODAL
   ============================================ */

document
    .getElementById("modalClose")
    .addEventListener(
        "click",
        () => {

            modal.classList.remove(
                "show"
            );

        }
    );


modal.addEventListener(
    "click",
    function (event) {

        if (
            event.target === modal
        ) {

            modal.classList.remove(
                "show"
            );
        }
    }
);


/* ============================================
   TOAST
   ============================================ */

function showToast(message) {

    toast.textContent = message;

    toast.classList.add("show");


    setTimeout(() => {

        toast.classList.remove(
            "show"
        );

    }, 3000);
}


/* ============================================
   INITIALS
   ============================================ */

function getInitials(name) {

    return name
        .split(" ")
        .map(
            word =>
                word.charAt(0)
        )
        .slice(0, 2)
        .join("")
        .toUpperCase();
}


/* ============================================
   HTML SECURITY
   ============================================ */

function escapeHTML(value) {

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(
            /'/g,
            "&#039;"
        );
}


/* ============================================
   INITIAL LOAD
   ============================================ */

updateDashboard();

renderStudents();

renderReports();
