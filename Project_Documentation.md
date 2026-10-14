# Student Performance Analytics System
**EWB Courses — Python with AI Internship**

- **Student Name:** Gattu Shiva Chandra
- **College:** Balaji Institute of Technology and Science
- **Project:** Student Performance Analytics System
- **Technologies:** Python, NumPy, Pandas
- **Submission deadline in assignment:** 15 October 2026

## 1. Objective

To build a Python data-analysis system that reads student marks and attendance from a CSV file, calculates total and average marks, assigns grades, identifies pass/fail status and analyzes individual, class-level and subject-level performance.

## 2. Technologies Used

- **Python:** Functions, loops, conditions and program logic.
- **NumPy:** Numerical calculations on the subject-mark array.
- **Pandas:** CSV loading, DataFrame processing and summary statistics.
- **CSV:** Storage format for the student dataset.
- **Visual Studio Code:** Development environment.

## 3. Dataset Description

The project uses a fictional sample dataset containing 20 student records with eight original columns: Student_ID, Name, Department, Python, Mathematics, Statistics, Computer_Fundamentals and Attendance. Each subject mark is out of 100, and attendance is represented as a percentage.

## 4. Implementation

### 4.1 Load and inspect data
Pandas reads `students.csv` into a DataFrame. The program displays the student records, number of records, number and names of columns, data types, non-null counts and numerical summary.

### 4.2 Calculate total and average marks
The program selects the four subject columns and converts them into a NumPy array. NumPy calculates each student's total and average marks. The resulting values are stored in `Total_Marks` and `Average_Marks`.

### 4.3 Assign grades
The project uses these grade boundaries:

| Average marks | Grade |
|---|---|
| 90–100 | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| 50–59.99 | E |
| Below 50 | F |

These boundaries are defined for this project because the assignment does not specify a grading scale.

### 4.4 Identify pass/fail status
A student passes if every subject mark is at least 40. If any subject mark is below 40, the student is classified as Fail. This passing rule is defined for this project.

### 4.5 Analyze class and subject performance
The program identifies the students with the highest and lowest average marks, calculates the overall class average, calculates the average for each subject, and identifies the strongest and weakest subject by average.

### 4.6 Identify top performers and class statistics
The program sorts students by average marks and displays the top three. It also counts passed and failed students and calculates their percentages.

## 5. Key Features

- CSV data loading and dataset inspection.
- Total and average marks using NumPy.
- Reusable functions and loops.
- Grade assignment and pass/fail classification.
- Highest, lowest and overall class average analysis.
- Subject-wise average analysis.
- Top-three student identification.
- Pass/fail counts and percentages.

## 6. Output and Screenshots

The terminal output displays the dataset, individual student totals and averages, grades, pass/fail status, highest and lowest performers, subject averages, top three students and pass/fail statistics.

**Add the captured output images here** or upload them to a `screenshots/` folder in the GitHub repository:
1. Student records and dataset summary.
2. Student results and class/subject analysis.
3. Top performers and pass/fail statistics.

## 7. Final Outcome

The system applies Python, NumPy and Pandas to a structured student dataset and provides student-level results alongside class-level and subject-level summaries.

For the included sample data and the rules defined above, expected results are:

| Metric | Result |
|---|---|
| Total students | 20 |
| Original dataset columns | 8 |
| Highest performer | Sneha Rao — 92.50 |
| Lowest performer | Mahesh Babu — 36.25 |
| Overall class average | 68.96 |
| Best-performing subject | Computer Fundamentals — 70.60 |
| Lowest-performing subject | Python — 67.65 |
| Passed students | 14 |
| Failed students | 6 |
| Pass percentage | 70.00% |
| Fail percentage | 30.00% |

## 8. Challenges and Learning

During development, the program initially encountered an environment issue because different Python interpreters were used. NumPy and Pandas were installed and verified with the interpreter used to run the project.

This project helped practice Python variables, data types, functions, loops, conditions, CSV processing, NumPy arrays, Pandas DataFrames, numerical summaries, sorting and data analysis.

## 9. GitHub Repository

https://github.com/shivachandra77/student-performance-analytics

The repository should include `main.py`, `students.csv`, `README.md`, this documentation and the final screenshots. The Word report with embedded images can also be uploaded if required by the trainer.

## 10. Conclusion

The Student Performance Analytics System demonstrates how Python, NumPy and Pandas can be used to process student marks and produce understandable academic performance summaries without advanced machine learning.
