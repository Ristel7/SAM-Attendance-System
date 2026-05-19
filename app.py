from flask import Flask, render_template, request, redirect, session
import mysql.connector
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")

# MYSQL CONNECTION
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB"),
    port=os.getenv("MYSQL_PORT")
)

cursor = db.cursor(dictionary=True, buffered=True)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# LOGIN PAGE
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":

            session["teacher"] = username

            return redirect("/dashboard")

        else:
            return "Invalid Username or Password"

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    if "teacher" not in session:
        return redirect("/login")

    # total students
    cursor.execute("SELECT COUNT(*) AS total FROM students")
    total_students = cursor.fetchone()

    # all students
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # total present today
    cursor.execute(
        """
        SELECT COUNT(*) AS present_count
        FROM attendance
        WHERE attendance_date = CURDATE()
        AND status = 'Present'
        """
    )

    present_count = cursor.fetchone()

    # total absent today
    cursor.execute(
        """
        SELECT COUNT(*) AS absent_count
        FROM attendance
        WHERE attendance_date = CURDATE()
        AND status = 'Absent'
        """
    )

    absent_count = cursor.fetchone()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        students=students,
        present_count=present_count,
        absent_count=absent_count
    )

# Students Page


@app.route("/students")
def students():
    return render_template("students.html")

# MARK ATTENDANCE


@app.route("/mark_attendance/<int:student_id>/<status>")
def mark_attendance(student_id, status):

    if "teacher" not in session:
        return redirect("/login")

    # check if attendance already exists today
    check_query = """
    SELECT * FROM attendance
    WHERE student_id = %s
    AND attendance_date = CURDATE()
    """

    cursor.execute(check_query, (student_id,))

    existing = cursor.fetchone()

    # if attendance already exists update it
    if existing:

        update_query = """
        UPDATE attendance
        SET status = %s
        WHERE student_id = %s
        AND attendance_date = CURDATE()
        """

        cursor.execute(update_query, (status, student_id))

    else:

        insert_query = """
        INSERT INTO attendance
        (student_id, attendance_date, status)
        VALUES(%s, CURDATE(), %s)
        """

        cursor.execute(insert_query, (student_id, status))

    db.commit()

    return redirect("/dashboard#attendance-section")


# ADD STUDENT
@app.route("/add_student", methods=["POST"])
def add_student():

    roll_no = request.form["roll_no"]
    name = request.form["name"]

    query = """
    INSERT INTO students
    (roll_no, name)
    VALUES(%s, %s)
    """

    values = (roll_no, name)

    cursor.execute(query, values)

    db.commit()

    return redirect("/dashboard")


# DELETE STUDENT
@app.route("/delete_student/<int:id>")
def delete_student(id):

    # delete attendance first
    attendance_query = """
    DELETE FROM attendance
    WHERE student_id = %s
    """
    cursor.execute(attendance_query, (id,))

    # now delete student
    student_query = """
    DELETE FROM students
    WHERE id = %s
    """
    cursor.execute(student_query, (id,))
    db.commit()
    return redirect("/dashboard#attendance-section")


# LOGOUT
@app.route("/logout")
def logout():

    session.pop("teacher", None)

    return redirect("/login")

# Report Page


@app.route('/reports')
def reports():

    cursor = db.cursor(dictionary=True)

    # =========================
    # TOTAL STUDENTS

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM students
    """)

    total_students = cursor.fetchone()['total']

    # =========================
    # PRESENT TODAY
    # =========================

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM attendance
        WHERE status = 'Present'
        AND attendance_date = CURDATE()
    """)

    present_today = cursor.fetchone()['total']

    # =========================
    # ABSENT TODAY
    # =========================

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM attendance
        WHERE status = 'Absent'
        AND attendance_date = CURDATE()
    """)

    absent_today = cursor.fetchone()['total']

    # =========================
    # ATTENDANCE PERCENTAGE
    # =========================

    total_today = present_today + absent_today

    if total_today > 0:
        attendance_percentage = round(
            (present_today / total_today) * 100,
            2
        )
    else:
        attendance_percentage = 0

    # =========================
    # PIE CHART DATA
    # =========================

    cursor.execute("""
        SELECT status, COUNT(*) AS total
        FROM attendance
        GROUP BY status
    """)

    pie_data = cursor.fetchall()

    labels = [row['status'] for row in pie_data]

    values = [row['total'] for row in pie_data]

    # =========================
    # MONTHLY LINE CHART
    # =========================

    cursor.execute("""
        SELECT
            MONTH(attendance_date) AS month,
            COUNT(*) AS total
        FROM attendance
        WHERE status = 'Present'
        GROUP BY MONTH(attendance_date)
        ORDER BY MONTH(attendance_date)
    """)

    line_data = cursor.fetchall()

    month_labels = [
        f"Month {row['month']}"
        for row in line_data
    ]

    month_values = [
        row['total']
        for row in line_data
    ]

    # =========================
    # SEND TO HTML
    # =========================

    return render_template(

        'reports.html',

        total_students=total_students,

        present_today=present_today,

        absent_today=absent_today,

        attendance_percentage=attendance_percentage,

        labels=labels,

        values=values,

        month_labels=month_labels,

        month_values=month_values
    )


if __name__ == "__main__":
    app.run(debug=True)
