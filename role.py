def project_status():
    pass

def Modify_project():
    pass

class member:
    print("1.See project status")
    print("2.Modify project")
    print("3.exit")
    while True:
        choice = input("input : ")
        if choice == 1:
            project_status()
        elif choice == 2:
            Modify_project()
        elif choice == 3:
            break

class lead:
    print("1.See project status")
    print("2.Modify project")
    print("3.sent requests member")
    print("4.sent requests advisor")
    print("5.exit")
    while True:
        choice = input("input : ")
        if choice == 1:
            project_status()
        elif choice == 2:
            Modify_project()
        elif choice == 4:
            pass
        elif choice == 5:
            break

class student:
    



