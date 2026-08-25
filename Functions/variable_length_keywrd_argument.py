def student_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
student_details(name="Yuva", age=20, course="MCA", semseter=2)

def student(*subjects, **details):
    print("Subjects:")
    for subject in subjects:
        print("-",subject)
    print("\nStudent Details:")
    for key, value in details.items():
        print(f"{key}: {value}")
student("Maths", "Physics", "Chemistry", name="Yuva", age=20, course="MCA", semester=2)
