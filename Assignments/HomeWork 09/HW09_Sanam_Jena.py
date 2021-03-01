"""
Author: Sanam Jena
CWID:10454295
Date: 13 December 2020
Objective: In this assignment we will work on student & instructor repository
"""

from typing import Dict, List, DefaultDict, Set
from collections import defaultdict
from HW08_Sanam_Jena import file_reader
from prettytable import PrettyTable
import os


class Student:
    """In this class, we will be creating an instance of a student.
    """
    field_name: List[str] = ["Cwid", "Name", "Courses"]

    def __init__(
            self,
            cwid: str,
            name: str,
            major: str
    ) -> None:
        """In this method, we will be initializing all the fields related to a student.

        Args:
            cwid (str)
            name (str)
            major (str)
            required (List[str])
            electives (List[str])
        """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = DefaultDict(int)

    def add_course(self, course: str, grade: str) -> None:
        """In this method, we will add course based on type (Required/Elective).

        Args:
            type (str): Course type (Required / Elective)
            course (str)
        """
        self._courses[course] = grade

    def info(self) -> List[str]:
        """In this function, we will be returning the outputs.
        """
        return [self._cwid, self._name, sorted(self._courses.keys())]


class Instructor:
    """In this class, we will be creating an instance of an instructor.
    """
    field_name: List[str] = ["Cwid", "Name",
                             "Department", "Course", "Students"]

    def __init__(self, cwid: str, name: str, dept: str) -> None:
        """In this method, we will be initializing all the fields related to an
        Instructor.

        Args:
            cwid (str)
            name (str)
            dept (str)
        """
        self._cwid: str = cwid
        self._name: str = name
        self._dept: str = dept
        self._setcourse: Set = set()
        self._courses: DefaultDict[str, int] = defaultdict(int)

    def inst_courses_add(self, course: str) -> None:
        """In this method, we will add course name and number of students enrolled.

        Args:
            course (str): [description]
        """
        self._setcourse.add(course)
        self._courses[course] += 1

    def info(self) -> List[str]:
        """In this function, we will be returning the outputs.
        """
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, count]


class Repository:
    """In this class, we will be creating a repository of student
    and instructor in an University
    """

    def __init__(self, path: str) -> None:
        """In this method, we will be initializing all the fields related to
        Repository.

        Args:
            path (str): path loaction of university
        """
        self._path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._read_students()
        self._read_instructors()
        self._read_grades()
        self.student_pretty_table()
        self.instructor_pretty_table()

    def _read_students(self) -> None:
        """
        In this method, we will be reading each student and creating
        instances of each student as soon as it is read.
        """
        try:
            for cwid, name, major in file_reader(os.path.join(
                    self._path, "students.txt"), fields=3, sep='\t', header=False):
                if cwid in self._students:
                    raise KeyError("Student with CWID is already in the file")
                self._students[cwid] = Student(
                    cwid, name, major)
        except FileNotFoundError:
            print(f"Cannot open file at {self._path}")
        except ValueError:
            print("Missing field")

    def _read_instructors(self) -> None:
        """
        In this method, we will be reading each student and creating
        instances of each instructor as soon as it is read.
        """
        try:
            for cwid, name, dept in file_reader(os.path.join(
                    self._path, "instructors.txt"), fields=3, sep='\t', header=False):
                if cwid in self._instructors:
                    raise KeyError(
                        "Instructor with CWID is already in the file")
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except (FileNotFoundError, ValueError) as e:
            print(f"Cannot open file at {self._path}")
        except ValueError:
            print("Missing field")

    def _read_grades(self) -> None:
        """
        In this method, we will be reading the grades of each student.
        """
        try:
            for stud_cwid, course, grade, prof_cwid in file_reader(
                    os.path.join(self._path, "grades.txt"), fields=4, sep='\t', header=False):
                if stud_cwid in self._students:
                    # handle the key error if a new student
                    s: Student = self._students[stud_cwid]
                    s.add_course(course=course, grade=grade)

                else:
                    raise KeyError(f"No such Student with {stud_cwid}")
                if prof_cwid in self._instructors:
                    # handle the key error if a new instructor
                    p: Instructor = self._instructors[prof_cwid]
                    p.inst_courses_add(course)
                else:
                    raise KeyError(f"No such Student with {prof_cwid}")

        except FileNotFoundError:
            print(f"Cannot open file at {self._path}")
        except ValueError:
            print("Wrong input")

    def student_pretty_table(self) -> PrettyTable:
        """
        In this function, we will be creating pretty table for Student
        """
        pt: PrettyTable = PrettyTable()
        pt.field_names = Student.field_name
        for s in self._students.values():
            pt.add_row(s.info())
        print("\nStudent Summary")
        print(pt)
        return pt

    def instructor_pretty_table(self) -> PrettyTable:
        """
        In this function, we will be creating pretty table for Instructor
        """
        pt: PrettyTable = PrettyTable(field_names=Instructor.field_name)
        for instructor in self._instructors.values():
            for row in instructor.info():
                pt.add_row(row)
        print("\nInstructor Summary")
        print(pt)
        return pt


def main():
    stevens: Repository = Repository(
        "C:\\Users\\sanam\\Documents\\Desk\\SSW 810 B\\Assignments\\HomeWork 09")


if __name__ == '__main__':
    main()
