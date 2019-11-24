from server.app import db

class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    title = db.Column(db.String(250), unique=True, nullable=False)
    content = db.Column(db.String(250), nullable=False)
    answer = db.Column(db.String(250), nullable=False)
    grade = db.Column(db.Float)

    def __init__(self, section_id, title, content, answer, grade):
        self.section_id = section_id
        self.title = title
        self.content = content
        self.answer = answer
        self.grade = grade

class StudentQuiz(db.Model):
    __tablename__ = 'student_quiz'
    student_id = db.Column(db.Integer, db.ForeignKey('student_course.id'), primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), primary_key=True)
    answer = db.Column(db.String(250), nullable=False)
    grade = db.Column(db.Float)

    def __init__(self, student_id, quiz_id, answer):
        self.student_id = student_id
        self.quiz_id = quiz_id
        self.answer = answer
