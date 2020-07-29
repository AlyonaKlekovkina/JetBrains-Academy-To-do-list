# stage 3
from datetime import datetime, date, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='task')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

while True:
    users_input = input("\n1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add task\n0) Exit\n")
    all_tasks = session.query(Task).order_by(Task.deadline).all()
    the_day = datetime.today().date()
    today = datetime.today()
    current_day = today.day
    current_month = today.strftime('%b')
    today_tasks = session.query(Task).filter(Task.deadline == the_day).all()
    last_day = the_day + timedelta(days=6)
    week_tasks = session.query(Task).filter(Task.deadline.between(the_day, last_day)).order_by(Task.deadline).all()

    if users_input == '1':
        if not today_tasks:
            print("\nToday ", current_day, " ", current_month, ":\nNothing to do!\n", sep="")
        else:
            for today_task in today_tasks:
                print(today_task.id, ". ", today_task.task, ". ", today_task.deadline.strftime("%-d %b"), sep="")
        continue
    elif users_input == '2':
        first_day = datetime.today().date()
        first_day_task = session.query(Task).filter(Task.deadline == first_day).all()
        if not first_day_task:
            print("\n", first_day.strftime("%A %-d %b"), ":\nNothing to do!", sep="")
        else:
            print("\n", first_day.strftime("%A %-d %b"), ":", sep="")
            i = 1
            for task in first_day_task:
                print(i, ". ", task.task, sep="")
        second_day = the_day + timedelta(days=1)
        second_day_task = session.query(Task).filter(Task.deadline == second_day).all()
        if not second_day_task:
            print("\n", second_day.strftime("%A %-d %b"), ":\nNothing to do!", sep="")
        else:
            print("\n", second_day.strftime("%A %-d %b"), ":", sep="")
            i = 1
            for task in second_day_task:
                print(i, ". ", task.task, sep="")
        third_day = the_day + timedelta(days=2)
        third_day_task = session.query(Task).filter(Task.deadline == third_day).all()
        if not third_day_task:
            print("\n", third_day.strftime("%A %-d %b"), ":\nNothing to do!", sep="")
        else:
            print("\n", third_day.strftime("%A %-d %b"), ":", sep="")
            i = 1
            for task in third_day_task:
                print(i, ". ", task.task, sep="")
        forth_day = the_day + timedelta(days=3)
        forth_day_task = session.query(Task).filter(Task.deadline == forth_day).all()
        if not forth_day_task:
            print("\n", forth_day.strftime("%A %-d %b"), ":\nNothing to do!", sep="")
        else:
            print("\n", forth_day.strftime("%A %-d %b"), ":", sep="")
            i = 1
            for task in forth_day_task:
                print(i, ". ", task.task, sep="")
        fifth_day = the_day + timedelta(days=4)
        fifth_day_task = session.query(Task).filter(Task.deadline == fifth_day).all()
        if not fifth_day_task:
            print("\n", fifth_day.strftime("%A %-d %b"), ":\nNothing to do!", sep="")
        else:
            print("\n", fifth_day.strftime("%A %-d %b"), ":", sep="")
            i = 1
            for task in fifth_day_task:
                print(i, ". ", task.task, sep="")
        six_day = the_day + timedelta(days=5)
        six_day_task = session.query(Task).filter(Task.deadline == six_day).all()
        if not six_day_task:
            print("\n", six_day.strftime("%A %-d %b"), ":\nNothing to do!", sep="")
        else:
            print("\n", six_day.strftime("%A %-d %b"), ":", sep="")
            i = 1
            for task in six_day_task:
                print(i, ". ", task.task, sep="")
        seventh_day = the_day + timedelta(days=6)
        seventh_day_task = session.query(Task).filter(Task.deadline == seventh_day).all()
        if not seventh_day_task:
            print("\n", seventh_day.strftime("%A %-d %b"), ":\nNothing to do!", sep="")
        else:
            print("\n", seventh_day.strftime("%A %-d %b"), ":", sep="")
            i = 1
            for task in seventh_day_task:
                print(i, ". ", task.task, sep="")
                i += 1
        continue
    elif users_input == '3':
        print("All tasks:")
        for all_task in all_tasks:
            print(all_task.id, ". ", all_task.task, ". ", all_task.deadline.strftime("%-d %b"), sep="")
        continue
    elif users_input == '4':
        task_entry = input("Enter task\n")
        date_entry = input('Enter deadline\n')
        deadline_year, current_month, current_day = map(int, date_entry.split('-'))
        date1 = date(deadline_year, current_month, current_day)
        new_task = Task(task=task_entry, deadline=date1)
        session.add(new_task)
        session.commit()
        print("The task has been added!")
        continue
    elif users_input == '0':
        print("Bye!")
        break
