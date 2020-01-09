import os
import time
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import *
from dotenv import load_dotenv,set_key
from app.models import *
from app.routes import *

# load_dotenv(dotenv_path='./env/flask_setting.env')
# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def test():
    teacherAccount = TypeAccount('Teacher')
    studentAccount = TypeAccount('Student')

    db.session.add_all([teacherAccount, studentAccount])

    user1 = User('eric', '123', 'Eric Camplin', 'eric@gmail.com')
    user2 = User('david', '345', 'David J.Malan', 'david@gmail.com')
    user3 = User('jordan', '654', 'Jordan Hayashi', 'jordan@gmail.com')
    user4 = User('jordan', '654', 'Jordan Hayashi', 'jordan@gmail.com')

    teacherAccount.users.append(user1)
    teacherAccount.users.append(user2)
    teacherAccount.users.append(user3)

    course1 = Course("Introduction to Artificial Intelligence", "A high-level overview of AI to learn how Machine Learning provides the foundation for AI, and how you can leverage cognitive services in your apps", 400)
    course2 = Course("Logic and Computational Thinking", 'Understanding how a computer "thinks" is one of the first steps to becoming an excellent computer programmer. A foundation in logic is crucial in developing this understanding. Mastering logic is more than learning a set of rules.', 220)
    course3 = Course("Introduction to Python", 'Focus on Python data structures, and work with string, list, and range sequences. Discover the power of list iteration, and learn about string and list methods. From there, get the details on file input and output--open files, read them, add to them, close them, and more.', 220)
    course4 = Course("Strategic Management", 'Learn how a manager or CEO develops a business strategy, including analyzing the market and creating competitive advantage.', 440)
    course5 = Course("Corporate Finance", 'Business organizations are constantly engaged in financial decision-making related to financial planning, investments, capital purchases, etc. The right financial decisions play a critical role in maximizing an organization’s business value.',600)
    course6 = Course("Marketing Management", 'Learn how to effectively apply marketing management theories and practices, including the marketing mix, through real-world business scenarios. According to world-renowned management consultant, Peter Drucker, "Marketing is the only distinguishing and unique function of business…There is only one valid definition of business purpose and that is to create a customer.”', 300)
    course7 = Course('Understanding Political Concepts', 'This course offers an exciting journey through political science concepts. Understand key concepts like party, bureaucracy, andconstitution by using new methods developed for scholars and students; including the innovative "Hyperpolitics" tool.',500)
    course8 = Course('Introduction to Sociology', 'This course is designed to look critically and analytically through different sociological perspectives, including the functionalist, interactionist, conflict and feminist, to help us realize the extent to which society guides our thoughts and actions. The course material provides a fresh, new look at societies and cultures—more objective, full of inquiry and analysis, striving towards social justice and change. Sociology urges us to draw connections between public issues and personal problems, to see the strange as familiar and the familiar as strange, and to examine biography in a historical and social context.',700)
    course9 = Course('Global Politics', 'The course explores global order and local disorders to explain why International Studies in the West are moving towards a planetary approach to World politics. Thinking globally helps explain new links between changes in the natural environment (demographics and climate) and changes in governing Institutions.',500)
    course10 = Course('Human Rights Defenders','Human rights defenders are people who have the courage to stand up against injustice. In this online course, you will follow their stories, learn how they mitigate risks and explore the creative ways they use to speak up. You will find out what drives them to take action, witness what defenders can achieve and discover how you can use your voice to defend your rights and those of others.',800)
    db.session.add_all([user1, user2, user3, course1, course2])

    teacherCourse1 = TeacherCourse()
    teacherCourse1.course = course1
    user1.courses.append(teacherCourse1)

    teacherCourse2 = TeacherCourse()
    # teacherCourse2.course = course1
    teacherCourse2.course = course2
    user2.courses.append(teacherCourse2)
    db.session.commit()
    teacherCourse2.course = course1
    user2.courses.append(teacherCourse2)
    db.session.commit()
    topic = ["Computer Science","Business", "Social Sciences", 'Humanities',"Information Technology"]

    tp1 = Topic(topic[0])
    tp1.coursers.append(course1)
    tp1.coursers.append(course2)
    tp1.coursers.append(course3)
    db.session.add(tp1)


    tp2 = Topic(topic[1])
    tp2.coursers.append(course4)
    tp2.coursers.append(course5)
    tp2.coursers.append(course6)

    tp3 = Topic(topic[2])
    tp3.coursers.append(course7)
    tp3.coursers.append(course8)
    tp3.coursers.append(course9)

    tp4 = Topic(topic[3])
    tp4.coursers.append(course10)


    tp5 = Topic(topic[4])
    tp6 = Topic(topic[5])

    db.session.add_all([tp1, tp2, tp3, tp4, tp5, tp6])
    db.session.commit()


    # for tp in topic:
    #     t = Topic(tp)
    #     t.coursers.append(course1)
    #     db.session.add(t)
    #     db.session.commit()

@manager.command
def migrate():
    """
    Creates database. Use only in first time
    """
    time.sleep(15)
    db.drop_all()
    db.create_all()

    test()

    db.session.commit()
    print("Done1")


@manager.command
def build():
    app.run(host='0.0.0.0', port=8081)

if __name__ == '__main__':
    manager.run()
    #app.run(host='0.0.0.0', port=8081)