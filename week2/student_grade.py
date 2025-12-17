def get_grade(student_grades, student_name):
    try:
          print(student_grades[student_name])
          return student_grades[student_name]
    except KeyError:
            print("Student not found in the system")

student_grades = { "sara": 97,
                  "Wes": 89,
                  "Jossy": 100}

get_grade(student_grades, "saron"); 
