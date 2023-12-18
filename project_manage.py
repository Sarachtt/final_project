import csv
import sys
from datetime import date
from database import Table,DB,CSVReader

project_list_header = ["Project_id","Project_name","advisor", "id","role","status"]
member_pending_header=["inveter","member_id","date"]
advisor_pending_header = ["invitor","advisor_id","date"]
today = date.today
all_role =['student','member','lead','faculty','advisor']

def initializing():
    db = DB()

    persons_csv = CSVReader('persons.csv')
    read_persons = persons_csv.read_csv()
    persons_table = Table('persons', read_persons)
    db.insert(persons_table)

    login_csv = CSVReader('login.csv')
    read_login = login_csv.read_csv()
    login_table = Table('login', read_login)
    db.insert(login_table)

    project_csv =CSVReader('project_list.csv')
    read_project = project_csv.read_csv()
    project_table = Table('project', read_project)
    db.insert(project_table)

    member_pending_csv = CSVReader('member_pending_list')
    read_member = member_pending_csv.read_csv()
    member_table = Table('members', read_member)
    db.insert(member_table)

    advisor_pending_csv = CSVReader('advisor_pending_list')
    read_advisor = advisor_pending_csv.read_csv()
    advisor_table = Table('advisor', read_advisor)
    db.insert(advisor_table)
    return db

def login():
    name = input("Enter your name: ")
    password = input("Enter your password : ")
    db = initializing()
    login_check = db.search("login")

    for login in login_check.table:
        if name == login["username"] and password == login["password"]:
            print(f"Welcome {login['username']}")
            print(f"Role : {login['role']}")
            return [login["ID"], login["role"]]
        else:
            print("Your username or password is wrong please try again.")
            return None

class project_table:
    def __init__(self,Title):
        db = initializing()
        project_check = db.search('project')
        a = set()
        for i in project_check.table:
            a.add(i["Project_name"])

        self.project_id = str((len(a))+1)
        self.Title = Title
        self.status = "Pending"
        self.advisor = "none"

    def create_project(self,id):
        input = [[self.project_id,self.Title,self.advisor,id,"lead",self.status]]
        with open ("project_list.csv","a") as project:
            projectupdate = csv.writer(project)
            projectupdate.writerows(input)
    
    def add_member(self,name):
        input = [[self.project_id,self.Title,self.advisor,name,"member",self.status]]
        with open ("project_list.csv","a") as project:
            projectupdate = csv.writer(project)
            projectupdate.writerows(input)

    def remove_member(self,name):
        pass

class student:
    def __init__(self,uid):
        self.id =uid[0]
    
    def choice(self):
        db = initializing()
        project_check = db.search('project')
        for i in project_check.table:
            if self.id not in i["id"]:
                print("You doesn't have project yet.")
                while True:
                    print("1.Create Project")
                    print("2.Create a project")
                    print("3.Logout")
                    choice = input("Enter :")
                    if choice == "1":
                        title = input("Enter Title: ")
                        project = project_table(title)
                        project.create_project(self.id)
                        break
                    elif choice == "2":
                        self.response_request()
                        break
                    elif choice == "3":
                        exit()
                        break
                    else:
                        print("Please try again")
            else:
                if project_check["role"] == "lead":
                    a = lead(self.id)
                    while True:
                        response = a.menu()
                        if response == "1":
                            a.see_status()
                            break
                        elif response =="2":
                            a.invite_member()
                            break
                        elif response =="3":
                            a.advisor_invite()
                            break
                        elif response =="4":
                            exit()
                            break
                        else:
                            print("Please try again")
                elif project_check["role"] == "member":
                    b = member(self.id)
                    while True:
                        response = b.menu()
                        if response == "1":
                            b.see_status()
                            break
                        elif response == "2":
                            exit()
                            break
                        else:
                            print("Please try again")
    
    def response_request(self):
        db = initializing()
        member_check = db.search('members')
        for i in member_check.table:
            if self.id == i['member_id']:
                print(f"your have request from : {i['inviter']}")
    
class lead:
    def __init__(self,id):
        self.id = id

    def menu(self):
        print("Menu:")
        print("1.See your project status")
        print("2.Send out requests to find members")
        print("3.Send out requests to find advisor")
        print("4.Logout")
        response = input("Enter : ") 
        return response

    def invite_member(self):
        db = initializing()
        id_check = db.search('persons')
        response = input("Enter the student's id you want to invite: ")
        for i in id_check.table:
            if response not in i['ID'] and i['type'] != "student":
                print("Can't find student id please try again.")
            else:
                input = [[self.id,response,today]]
                with open ("member_pending_list","a") as member:
                    member_pending = csv.writer(member)
                    member_pending.writerows(input)
                    print("request sent")
        
    def advisor_invite(self,):
        response = input("Enter the advisor's id you want to invite: ")
        input = [[self.id,response,today]]
        with open ("advisor_pending_list","a") as advisor:
            advisor_pending = csv.writer(advisor)
            advisor_pending.writerows(input)

    def see_status(self):
        print("Your project status: ")
        db = initializing()
        project_check = db.search('project')
        for id in project_check.table:
            if self.id == id["id"]:
                print(f"Your project status : {id['status']}")

class member :
    def __init__(self,uid):
        self.id = uid
    
    def menu(self):
        print("Menu:")
        print("1.See your project status")
        print("2.Logout")    
        response = input("Enter: ")
        return response    
    
    def see_status(self):
        db = initializing()
        project_check = db.search('project')
        for i in project_check.table:
            if self.id == i['id']:
                print("Your project status: ")
                print(f"Your project status : {i['status']}")

class admin:
    def __init__(self,id):
        self.id = id

    def menu(self):
        print("Menu:")
        print("1.Add user")
        print("2.Logout")
        response = input("Enter")
        return response

    def add_user(self):
        print("Do you want to add user")
        print("1.Yes")
        print("2.No")
        response = input("Enter: ")
        if response == "1":
            id = input("Enter ID:")
            username = input('Enter username: ')
            password = input('Enter password: ')
            while True:
                role = input('Enter role : ')
                if role not in all_role:
                    print("Your role doesn't exist,please try again")
                else:
                    break
            input = [[id,username,password,role]]
            with open ("login.csv","a") as login:
                add_user = csv.writer(login)
                add_user.writerows(input)
        else :
            print("Please try again")

class facility:
    def __init__(self,id):
        self.id = id
    
    def menu(self):
        print("Menu: ")
        print("1.See request")
        print("2.Logout")
        response = input("Enter: ")
        if response == "1":
            print("Your request:")
            db = initializing()
            advisor_check = db.search('advisor_pending_list')
            for i in advisor_check.table:
                if self.id == i['advisor_id']:
                    print(f"You have request form : {i['invitor']} date: {i['date']}")
            return response
        elif response =="2":
            return response


def exit():
    print("Saving")
    person = open('persons.csv', 'w')
    person_writer = csv.writer(person)
    person_writer.writerow(['ID','first','last','type'])
    for dic in DB.search('person').table:
        person_writer.writerow(dic.values())
    person.close()

    login = open('login.csv', 'w')
    login_writer = csv.writer(login)
    login_writer.writerow(['ID','username','password','role'])
    for dic in DB.search('login').table:
        login_writer.writerow(dic.values())
    login.close()

    project = open('project_list.csv', 'w')
    project_writer = csv.writer(project)
    project_writer.writerow(['Project_id','Project_name','advisor','id','role','status'])
    for _project in DB.search('project').table:
        project_writer.writerow(_project.save())
    project.close()

    member_save = open('member_pending.csv', 'w')
    member_writer = csv.writer(member_save)
    member_writer.writerow(['inveter','member_id','date'])
    for _member in DB.search('members').table:
        project_writer.writerow(_member.save())
    member_save.close()

    advisor_save = open('advisor_pending.csv', 'w')
    advisor_writer = csv.writer(advisor_save)
    advisor_writer.writerow(['invitor','advisor_name','date'])
    for _advisor in DB.search('advisor').table:
        advisor_writer.writerow(_advisor.save())
    advisor_save.close()

    print("Saving complete")
    sys.exit()

initializing()
val = login()
if val[1] == "student":
    a = student(val[0])
    a.choice()
elif val[1] =="admin":
    b = admin(val[0])
    admin_res = b.menu
    if admin_res =="1":
        b.add_user()
    elif admin_res == "2":
        exit()
elif val[1] =="faculty":
    c = facility(val[0])
    faci_res = c.menu()
    if faci_res =="2":
        exit()






