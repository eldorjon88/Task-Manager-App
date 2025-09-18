from database import engine, metadata
from models import users, tasks
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

metadata.create_all(engine)


def register_user(session):
    username = input("Username: ")
    fullname = input("Fullname: ")

    stmt = insert(users).values(username=username, fullname=fullname)
    session.execute(stmt)
    session.commit()
    print("Foydalanuvchi qo'shildi.")


def list_users(session):
    stmt = select(users)
    result = session.execute(stmt).fetchall()
    if not result:
        print("Foydalanuvchilar yo'q.")
    else:
        for row in result:
            print(row)


def update_user(session):
    user_id = int(input("User ID: "))
    new_username = input("Yangi username: ")
    new_fullname = input("Yangi fullname: ")

    stmt = (
        update(users)
        .where(users.c.id == user_id)
        .values(username=new_username, fullname=new_fullname)
    )
    session.execute(stmt)
    session.commit()
    print("Foydalanuvchi yangilandi.")


def delete_user(session):
    user_id = int(input("User ID: "))
    stmt = delete(users).where(users.c.id == user_id)
    session.execute(stmt)
    session.commit()
    print("Foydalanuvchi o'chirildi.")


def create_task(session):
    user_id = int(input("User ID: "))
    name = input("Task nomi: ")
    description = input("Task tavsifi: ")

    stmt = insert(tasks).values(name=name, description=description, user_id=user_id)
    session.execute(stmt)
    session.commit()
    print("Task qo'shildi.")


def list_tasks(session):
    stmt = select(tasks)
    result = session.execute(stmt).fetchall()
    if not result:
        print("Tasklar yo'q.")
    else:
        for row in result:
            print(row)


def update_task(session):
    task_id = int(input("Task ID: "))
    new_name = input("Yangi nom: ")
    new_desc = input("Yangi tavsif: ")

    stmt = (
        update(tasks)
        .where(tasks.c.id == task_id)
        .values(name=new_name, description=new_desc)
    )
    session.execute(stmt)
    session.commit()
    print("Task yangilandi.")


def delete_task(session):
    task_id = int(input("Task ID: "))
    stmt = delete(tasks).where(tasks.c.id == task_id)
    session.execute(stmt)
    session.commit()
    print("Task o'chirildi.")


def main():
    with Session(engine) as session:
        while True:
            print("\n--- MENU ---")
            print("1. Foydalanuvchi qo'shish")
            print("2. Foydalanuvchilarni ko'rish")
            print("3. Foydalanuvchi yangilash")
            print("4. Foydalanuvchi o'chirish")
            print("5. Task qo'shish")
            print("6. Tasklarni ko'rish")
            print("7. Task yangilash")
            print("8. Task o'chirish")
            print("0. Chiqish")

            choice = input("Tanlang: ")

            if choice == "1":
                register_user(session)
            elif choice == "2":
                list_users(session)
            elif choice == "3":
                update_user(session)
            elif choice == "4":
                delete_user(session)
            elif choice == "5":
                create_task(session)
            elif choice == "6":
                list_tasks(session)
            elif choice == "7":
                update_task(session)
            elif choice == "8":
                delete_task(session)
            elif choice == "0":
                print("Dastur tugadi.")
                break
            else:
                print("Noto'g'ri tanlov.")


if __name__ == "__main__":
    main()

