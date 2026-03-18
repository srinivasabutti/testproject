from flask import Flask,render_template

app = Flask(__name__)


@app.route('/home/')
def Home_View():
    return render_template('home.html')

@app.route('/courses/')
def Courses_View():
    return render_template('courses.html')

@app.route('/students/')
def Students_View():
    return render_template('students.html')


if __name__ == '__main__':
    app.run()
