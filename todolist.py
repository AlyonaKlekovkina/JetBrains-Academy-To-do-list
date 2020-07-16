# Write your code here
# stage 1
# print("Today:")
# print("1) Do yoga")
# print("2) Make breakfast")
# print("3) Learn basics of SQL")
# print("4) Learn what is ORM")

# stage 2
from datetime import datetime
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
    users_input = input("\n1) Today's tasks\n2) Add task\n0) Exit\n")
    tasks = session.query(Task).all()
    if users_input == '1':
        if not tasks:
            print("\nToday:\nNothing to do!\n")
        else:
            first_task = tasks[0]
            print("\nToday:\n", first_task.id, ". ", first_task.task, sep='')
        continue
    elif users_input == '2':
        new_task = Task(task=input("Enter task\n"),
                        deadline=datetime.today())
        session.add(new_task)
        session.commit()
        print("The task has been added!")
        continue
    elif users_input == '0':
        print("Bye!")
        break
