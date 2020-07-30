# stage 3
from datetime import datetime, date, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


def show_today_tasks():
    day = datetime.today().date()
    today_tasks = session.query(Task).filter(Task.deadline == day).all()
    if not today_tasks:
        print("\nToday ", day.strftime("%-d %b"), ":\nNothing to do!\n", sep="")
    else:
        for today_task in today_tasks:
            print(today_task.id, ". ", today_task.task, ". ", today_task.deadline.strftime("%-d %b"), sep="")


def show_weeks_tasks():
    the_day = datetime.today().date()
    for day in range(7):
        needed_day = the_day + timedelta(days=day)
        needed_day_task = session.query(Task).filter(Task.deadline == needed_day).all()
        if not needed_day_task:
            print("\n", needed_day.strftime("%A %d %b"), ":\nNothing to do!", sep="")
        else:
            print("\n", needed_day.strftime("%A %d %b"), sep="")
            i = 1
            for task in needed_day_task:
                print(i, ". ", task.task, sep="")
                i += 1


def show_all_tasks():
    print("All tasks:")
    all_tasks = session.query(Task).order_by(Task.deadline).all()
    for task in all_tasks:
        print(task.id, ". ", task.task, ". ", task.deadline.strftime("%-d %b"), sep="")


def show_missed_tasks():
    print("Missed tasks:")
    day = datetime.today().date()
    missed_tasks = session.query(Task).filter(Task.deadline < day).all()
    if not missed_tasks:
        print("Nothing is missed!")
    else:
        for missed in missed_tasks:
            print(missed.id, ". ", missed.task, ". ", missed.deadline.strftime("%-d %b"), sep="")


def add_task():
    task_entry = input("Enter task\n")
    date_entry = input('Enter deadline\n')
    deadline_year, current_month, current_day = map(int, date_entry.split('-'))
    date1 = date(deadline_year, current_month, current_day)
    new_task = Task(task=task_entry, deadline=date1)
    session.add(new_task)
    session.commit()
    print("The task has been added!")


def delete_task():
    all_tasks = session.query(Task).order_by(Task.deadline).all()
    if not all_tasks:
        print("Nothing to delete")
    else:
        print("Chose the number of the task you want to delete:")
        show_all_tasks()

    to_delete = int(input())
    for to_be_deleted in all_tasks:
        if to_delete == to_be_deleted.id:
            session.query(Task).filter(Task.id == to_be_deleted.id).delete()
            session.commit()
            print("The task has been deleted!")


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
    users_input = input("\n1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit\n")
    if users_input == '1':
        show_today_tasks()
        continue
    elif users_input == '2':
        show_weeks_tasks()
        continue
    elif users_input == '3':
        show_all_tasks()
        continue
    elif users_input == '4':
        show_missed_tasks()
        continue
    elif users_input == '5':
        add_task()
        continue
    elif users_input == '6':
        delete_task()
        continue
    elif users_input == '0':
        print("Bye!")
        break
