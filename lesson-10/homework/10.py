##1
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✔ Completed" if self.completed else "❌ Incomplete"
        return f"{self.title} - {self.description} (Due: {self.due_date}) [{status}]"

#2
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if not task.completed:
                print(task)

##3
def main():
    todo = ToDoList()
    while True:
        print("\nToDo List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            desc = input("Task description: ")
            due = input("Due date: ")
            todo.add_task(Task(title, desc, due))
        elif choice == "2":
            todo.list_tasks()
            idx = int(input("Enter task number to mark complete: "))
            if 0 <= idx-1 < len(todo.tasks):
                todo.tasks[idx-1].mark_complete()
        elif choice == "3":
            todo.list_tasks()
        elif choice == "4":
            todo.list_incomplete_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option!")


#4
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nBy: {self.author}\n{self.content}\n"

#5
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for post in self.posts:
            print(post)

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post)

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, old_title, new_title, new_content):
        for post in self.posts:
            if post.title == old_title:
                post.title = new_title
                post.content = new_content

    def latest_posts(self, count=3):
        for post in self.posts[-count:]:
            print(post)

#6
def main():
    blog = Blog()
    while True:
        print("\nBlog Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == "2":
            blog.list_posts()
        elif choice == "3":
            author = input("Author name: ")
            blog.posts_by_author(author)
        elif choice == "4":
            title = input("Post title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            old_title = input("Title of post to edit: ")
            new_title = input("New title: ")
            new_content = input("New content: ")
            blog.edit_post(old_title, new_title, new_content)
        elif choice == "6":
            blog.latest_posts()
        elif choice == "7":
            break
        else:
            print("Invalid option!")

#7
class Account:
    def __init__(self, acc_num, holder, balance=0):
        self.acc_num = acc_num
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("❌ Insufficient funds!")
            return False

    def __str__(self):
        return f"Account {self.acc_num} | Holder: {self.holder} | Balance: {self.balance}"

#8
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_num] = acc

    def get_account(self, acc_num):
        return self.accounts.get(acc_num)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver:
            if sender.withdraw(amount):
                receiver.deposit(amount)

#9
def main():
    bank = Bank()
    while True:
        print("\nBank Menu:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Show Account Details")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            num = input("Account number: ")
            name = input("Account holder name: ")
            bank.add_account(Account(num, name))
        elif choice == "2":
            num = input("Enter account number: ")
            acc = bank.get_account(num)
            print(acc.balance if acc else "Account not found")
        elif choice == "3":
            num = input("Account number: ")
            amt = float(input("Amount: "))
            acc = bank.get_account(num)
            if acc:
                acc.deposit(amt)
        elif choice == "4":
            num = input("Account number: ")
            amt = float(input("Amount: "))
            acc = bank.get_account(num)
            if acc:
                acc.withdraw(amt)
        elif choice == "5":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amt = float(input("Amount: "))
            bank.transfer(from_acc, to_acc, amt)
        elif choice == "6":
            for acc in bank.accounts.values():
                print(acc)
        elif choice == "7":
            break
        else:
            print("Invalid option!")
