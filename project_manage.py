# import database module
from database import Table,DB,CSVReader
# define a funcion called initializing

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

    return db
# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database


# define a funcion called login

def login():
    user = input("username : ")
    password = str(input("password : "))
    db = initializing()
    login_check = db.search("login")

    for login in login_check.table:
        if user == login["username"] and password == login["password"]:
            print(f"Welcome {login['username']}")
            print(f"Role : {login['role']}")
            return [login["ID"], login["role"]]
        else:
            print("Your username or password is wrong please try again.")
            return None

# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    pass

# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
def logged(role):
    



initializing()
val = login()


# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function


exit()
