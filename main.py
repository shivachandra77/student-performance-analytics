import numpy as np
import pandas as pd


def load_student_data(file_name):
    """Load student records from a CSV file."""
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        print("Error: CSV file not found.")
        print("Make sure students.csv is in the project folder.")
        return None


def display_basic_information(students):
    """Display student records and dataset information."""
    print("\n===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====")
    print("\n===== STUDENT RECORDS =====")
    print(students.to_string(index=False))

    print("\n===== DATASET INFORMATION =====")
    print("Total number of students:", len(students))
    print("Total number of columns:", len(students.columns))

    print("\nColumn names:")
    for column in students.columns:
        print("-", column)

    print("\n===== DATA TYPES AND MISSING VALUES =====")
    students.info()

    print("\n===== NUMERICAL SUMMARY =====")
    print(students.describe())


def calculate_student_results(students):
    """Calculate total and average marks for every student."""
    subject_columns = [
        "Python",
        "Mathematics",
        "Statistics",
        "Computer_Fundamentals",
    ]
    marks = students[subject_columns].to_numpy()
    students["Total_Marks"] = np.sum(marks, axis=1)
    students["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)
    return students


def assign_grade(average):
    """Assign a grade based on average marks."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    return "F"


def check_pass_fail(student, subject_columns):
    """Pass if every subject mark is at least 40."""
    for subject in subject_columns:
        if student[subject] < 40:
            return "Fail"
    return "Pass"


def analyze_grades_and_results(students):
    """Add grades and pass/fail results to the DataFrame."""
    subject_columns = [
        "Python",
        "Mathematics",
        "Statistics",
        "Computer_Fundamentals",
    ]
    students["Grade"] = students["Average_Marks"].apply(assign_grade)
    students["Result"] = students.apply(
        check_pass_fail, axis=1, subject_columns=subject_columns
    )
    return students


def display_student_results(students):
    """Display marks, grades and pass/fail status."""
    print("\n===== STUDENT PERFORMANCE RESULTS =====")
    columns = [
        "Student_ID", "Name", "Total_Marks",
        "Average_Marks", "Grade", "Result"
    ]
    print(students[columns].to_string(index=False))


def analyze_class_performance(students):
    """Find highest, lowest and overall class average."""
    highest = students.loc[students["Average_Marks"].idxmax()]
    lowest = students.loc[students["Average_Marks"].idxmin()]
    class_average = students["Average_Marks"].mean()

    print("\n===== OVERALL CLASS PERFORMANCE =====")
    print("Highest-performing student:", highest["Name"], f'({highest["Student_ID"]})')
    print(f'Highest average: {highest["Average_Marks"]:.2f}/100')
    print("Lowest-performing student:", lowest["Name"], f'({lowest["Student_ID"]})')
    print(f'Lowest average: {lowest["Average_Marks"]:.2f}/100')
    print(f"Overall class average: {class_average:.2f}/100")


def analyze_subject_performance(students):
    """Calculate subject averages and identify best and worst subjects."""
    subject_columns = [
        "Python",
        "Mathematics",
        "Statistics",
        "Computer_Fundamentals",
    ]
    averages = students[subject_columns].mean()

    print("\n===== SUBJECT-WISE PERFORMANCE =====")
    for subject, average in averages.items():
        print(f"{subject}: {average:.2f}/100")

    highest_subject = averages.idxmax()
    lowest_subject = averages.idxmin()
    print("\nBest-performing subject:", highest_subject)
    print(f"Highest subject average: {averages[highest_subject]:.2f}/100")
    print("\nLowest-performing subject:", lowest_subject)
    print(f"Lowest subject average: {averages[lowest_subject]:.2f}/100")


def identify_top_performers(students):
    """Display the three highest-performing students."""
    top_students = students.sort_values(
        by="Average_Marks", ascending=False
    ).head(3)
    print("\n===== TOP 3 PERFORMING STUDENTS =====")
    columns = ["Student_ID", "Name", "Average_Marks", "Grade", "Result"]
    print(top_students[columns].to_string(index=False))


def display_pass_fail_statistics(students):
    """Count passed and failed students and calculate percentages."""
    passed = (students["Result"] == "Pass").sum()
    failed = (students["Result"] == "Fail").sum()
    total = len(students)
    pass_percentage = passed / total * 100 if total else 0
    fail_percentage = failed / total * 100 if total else 0

    print("\n===== PASS/FAIL STATISTICS =====")
    print("Total students:", total)
    print("Students passed:", passed)
    print("Students failed:", failed)
    print(f"Pass percentage: {pass_percentage:.2f}%")
    print(f"Fail percentage: {fail_percentage:.2f}%")


def main():
    students = load_student_data("students.csv")
    if students is None:
        return
    if students.empty:
        print("The dataset is empty. Please add student records.")
        return

    display_basic_information(students)
    students = calculate_student_results(students)
    students = analyze_grades_and_results(students)
    display_student_results(students)
    analyze_class_performance(students)
    analyze_subject_performance(students)
    identify_top_performers(students)
    display_pass_fail_statistics(students)


if __name__ == "__main__":
    main()
