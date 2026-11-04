import json
import os


class Student:
    """Represents a student. Demonstrates encapsulation and polymorphism."""

    def __init__(self, roll_no, name, marks):
        self._roll_no = str(roll_no).strip()
        self._name = str(name).strip()
        self.marks = marks

        if not self._roll_no:
            raise ValueError("Roll number cannot be empty.")
        if not self._name:
            raise ValueError("Name cannot be empty.")

    @property
    def roll_no(self):
        return self._roll_no

    @property
    def name(self):
        return self._name

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        value = float(value)
        if not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100.")
        self._marks = value

    def calculate_grade(self):
        """Grade rule for a regular student."""
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        elif self.marks >= 50:
            return "E"
        return "F"

    def student_type(self):
        return "Regular"

    def to_dict(self):
        return {
            "type": self.student_type(),
            "roll_no": self.roll_no,
            "name": self.name,
            "marks": self.marks
        }


class GraduateStudent(Student):
    """Graduate student with a different grade rule. Demonstrates inheritance."""

    def calculate_grade(self):
        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 55:
            return "C"
        return "F"

    def student_type(self):
        return "Graduate"


class StudentManager:
    """Manages student records and saves them in a JSON file."""

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load_records()

    def load_records(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                records = json.load(file)

            for record in records:
                student_class = (
                    GraduateStudent
                    if record.get("type") == "Graduate"
                    else Student
                )
                student = student_class(
                    record["roll_no"], record["name"], record["marks"]
                )
                self.students[student.roll_no] = student
        except (json.JSONDecodeError, KeyError, ValueError):
            print("Warning: Could not load records. Starting with an empty list.")

    def save_records(self):
        records = [student.to_dict() for student in self.students.values()]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

    def add_student(self, student):
        if student.roll_no in self.students:
            raise ValueError("A student with this roll number already exists.")
        self.students[student.roll_no] = student
        self.save_records()

    def display_students(self):
        if not self.students:
            print("\nNo student records found.")
            return

        print("\n{:<12} {:<22} {:<12} {:<10} {:<10}".format(
            "Roll No.", "Name", "Type", "Marks", "Grade"
        ))
        print("-" * 70)

        for student in self.students.values():
            print("{:<12} {:<22} {:<12} {:<10.2f} {:<10}".format(
                student.roll_no,
                student.name,
                student.student_type(),
                student.marks,
                student.calculate_grade()
            ))

    def search_student(self, roll_no):
        return self.students.get(str(roll_no).strip())

    def update_marks(self, roll_no, new_marks):
        student = self.search_student(roll_no)
        if student is None:
            return False

        student.marks = new_marks
        self.save_records()
        return True

    def delete_student(self, roll_no):
        roll_no = str(roll_no).strip()
        if roll_no not in self.students:
            return False

        del self.students[roll_no]
        self.save_records()
        return True


def get_marks():
    try:
        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return None
        return marks
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    manager = StudentManager()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Update student marks")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            roll_no = input("Enter roll number: ").strip()
            name = input("Enter student name: ").strip()
            marks = get_marks()

            if marks is None:
                continue

            student_type = input(
                "Student type (R = Regular, G = Graduate): "
            ).strip().upper()

            try:
                if student_type == "G":
                    student = GraduateStudent(roll_no, name, marks)
                elif student_type == "R":
                    student = Student(roll_no, name, marks)
                else:
                    print("Invalid student type.")
                    continue

                manager.add_student(student)
                print("Student added successfully!")
            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            roll_no = input("Enter roll number to search: ")
            student = manager.search_student(roll_no)

            if student:
                print("\nStudent found:")
                print("Roll Number:", student.roll_no)
                print("Name:", student.name)
                print("Type:", student.student_type())
                print("Marks:", student.marks)
                print("Grade:", student.calculate_grade())
            else:
                print("Student not found.")

        elif choice == "4":
            roll_no = input("Enter roll number: ")
            new_marks = get_marks()

            if new_marks is None:
                continue

            try:
                if manager.update_marks(roll_no, new_marks):
                    print("Marks updated successfully!")
                else:
                    print("Student not found.")
            except ValueError as error:
                print("Error:", error)

        elif choice == "5":
            roll_no = input("Enter roll number to delete: ")
            if manager.delete_student(roll_no):
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        elif choice == "6":
            print("Thank you for using the Student Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
