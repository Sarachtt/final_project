# Final project for 2023's 219114/115 Programming I
#List of files in this project:
-project_manage.py
  -initializing
    -to read all .csv files and insert them in a table
  -login
    Ask user to enter username/password and return ID and role
  -project_table(Class)
    -create project
    -add member to project
    -remove  member
  -student(Class)
    -Check user in project yet
      -if not
        -create project
        -see some request from prject lead
      -if in
        -lead
          -see status of project
          -invite memebr/advisor
        -member
          -see project status

  -lead(Class)
    -see status of project
    -invite memebr/advisor
  -member(Class)
    -see project status
  -admin(Class)
    -Manage the database 
  -facility(Class)
    -see a request from lead project
  -exit
    -convert the data and inset it back in to .csv files
All file that store data
-advisor_pending_list (store  invite pending from lead to advisor)
-login (store  username and password)
-member_pending_list (store invite pending from lead to student)
-persons
-project_list (store project data)

#How to compile and run project
1. Clone this repository in to your local repository
2. Change the persons.csv and login.csv to your data pool
3. Run the project_manage.py and Thats it! (Optional: if you have data for your student's projects too, then you can put them in projects.csv file)

|  Role   | Action                                                         | Method                  |  Class  | Completion<br/>Percentage |
|:-------:|----------------------------------------------------------------|-------------------------|:-------:|--------------------------:|
|  Admin  | Insert information                                             | add_user                |  Admin  |                      100% |
|  Admin  | Delete information                                             | -                       |  Admin  |                        0% |
| Student | Create project                                                 | create_project          | Student |                       70% |
| Student | See and Respond an invitation request(to be group member)      | invitation_detail       | Student |                       50% |
| Member  | See project info(your own group)                               | see_status              | Member  |                       80% |
|  Lead   | Send an invitation to other student                            | invite_member           |  Lead   |                       70% |
|  Lead   | Send an invitation to faculty                                  | advisor_invite          |  Lead   |                       70% |
|  Lead   | See project info(your own group)                               | see_status              |  Lead   |                       80% |
| Faculty | See and Respondan invitation request(to be an advisor)         | invitation_detail       | Faculty |                       50% |

#Missing features and bugs

-admin can't delete user from database
-student advisor can't accept request from lead
-no type checks at all

  
  
