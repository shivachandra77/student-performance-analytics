# Student Performance Analytics System

**EWB Courses — Python with AI Internship**

## 1. Project Overview

The Student Performance Analytics System is a Python data-analysis project. It processes student marks using Python, NumPy and Pandas and produces individual results, class summaries and subject-wise analysis.

## 2. Objective

- Load student records from a CSV file into a Pandas DataFrame.
- Calculate total and average marks for each student.
- Assign grades according to a defined grading scale.
- Identify pass/fail students.
- Find the highest- and lowest-performing students.
- Calculate subject averages and identify the strongest and weakest subjects.
- Identify the top three students.
- Calculate pass/fail counts and percentages.

## 3. Technologies Used

- **Python** — functions, loops, conditions and program logic.
- **NumPy** — numerical calculations.
- **Pandas** — CSV loading, DataFrame operations and analysis.
- **CSV** — storage of the student sample dataset.

## 4. Dataset

The file `students.csv` contains 20 sample student records and eight original fields: Student_ID, Name, Department, Python, Mathematics, Statistics, Computer_Fundamentals and Attendance.

The four subject marks are out of 100. Attendance is expressed as a percentage. The dataset is fictional sample data.

## 5. Grading and Pass/Fail Rules

Grades are based on average marks:

| Average marks | Grade |
|---|---|
| 90–100 | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| 50–59.99 | E |
| Below 50 | F |

A student passes only if every subject mark is at least 40. These thresholds are defined for this project; the assignment PDF does not prescribe exact thresholds.

## 6. Features

- Read and display CSV data.
- Display dataset dimensions, column names, data types and numerical summaries.
- Calculate total and average marks for each student using NumPy.
- Assign grades and pass/fail results.
- Find the highest and lowest student averages and overall class average.
- Calculate subject-wise averages and identify highest/lowest subjects.
- Display the top three performers.
- Report pass/fail counts and percentages.

## 7. Project Structure

```text
student-performance-analytics/
├── main.py
├── students.csv
├── README.md
└── Project_Documentation.md
```

The Word report and screenshots can also be added to this repository. See the submission checklist below.

## 8. Requirements and Setup

Python 3.11 or later is recommended. Install dependencies in the Python environment you will use to run the project:

```bash
python -m pip install numpy pandas
```

If your computer has multiple Python installations, run the program using the interpreter where NumPy and Pandas are installed.

## 9. Run the Program

Keep `main.py` and `students.csv` in the same folder, then run:

```bash
python main.py
```

The program displays the original dataset, student results, overall class performance, subject averages, top three performers and pass/fail statistics.

## 10. Expected Results

For the current sample dataset and defined rules:

| Metric | Expected result |
|---|---:|
| Students | 20 |
| Original dataset columns | 8 |
| Highest-performing student | Sneha Rao |
| Highest average | 92.50 |
| Lowest-performing student | Mahesh Babu |
| Lowest average | 36.25 |
| Overall class average | 68.96 |
| Best-performing subject | Computer Fundamentals |
| Best subject average | 70.60 |
| Lowest-performing subject | Python |
| Lowest subject average | 67.65 |
| Passed | 14 |
| Failed | 6 |
| Pass percentage | 70.00% |
| Fail percentage | 30.00% |

## 11. Concepts Demonstrated

Python variables, data types, loops, conditions, functions, NumPy numerical operations, Pandas DataFrames, CSV processing, sorting and descriptive analysis.

## 12. Limitations

- The project uses fictional sample data rather than a live college database.
- Grades and pass/fail outcomes depend on the thresholds defined above.
- This is a basic data-analysis project; it does not require advanced machine learning.

## 13. Submission Checklist

- [x] Python source file uploaded.
- [x] CSV dataset uploaded.
- [x] README added.
- [ ] Add the completed Word project documentation.
- [ ] Add output screenshots.
- [ ] Verify that all files are visible in the public repository.
- [ ] Submit the repository URL through the EWB Google Form.

## 14. Repository

https://github.com/shivachandra77/student-performance-analytics
