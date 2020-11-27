"""
Author: Sanam Jena
CWID:10454295
Date: 26 November 2020
Objective: In this assignment we will work on flask & Jinja2
"""

from flask import Flask, render_template
import sqlite3
from typing import Dict

DataBase: str = r'.\Homework11.db'

app = Flask(__name__)


@app.route('/student_summary/')
def student_summary() -> str:
    query: str = """select s.name, s.cwid, g.Course, g.Grade,i.name from students
    s join grades as g on s.cwid = g.StudentCWID join instructors i on
    i.cwid = g.InstructorCWID order by s.name"""

    db: sqlite3.Connection = sqlite3.connect(DataBase)

    data: Dict[str,
               str] = [{'name': name,
                        'cwid': cwid,
                        'course': course,
                        'grade': grade,
                        'instructor': instructor} for cwid,
                       name,
                       course,
                       grade,
                       instructor in db.execute(query)]

    db.close()
    return render_template(
        'student.html',
        title="Stevens Repository",
        table_title=" Stevens Institute of Technology",
        students=data)


if __name__ == '__main__':
    app.run(debug=True)
