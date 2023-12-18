import csv 
header = ["Project_id","Project_name","advisor", "id","role","status"]
lead = [["pj0","project_test","Superior Aum","Aum","lead","???"]]
mem_1=[["pj0","project_test","Superior Aum","aum_1","member","???"]]
mem_2=[["pj0","project_test","Superior Aum","aum_2","member","???"]]
member_pending_header=["inveter","member_id","date"]
advisor_pending_header = ["invitor","advisor_name","date"]
test_mem = [["Aum","sdsaad","11"]]

with open ("project_list.csv","w") as project:
    project_list = csv.writer(project)
    project_list.writerow(header)

with open ("member_pending_list","w") as member:
    member_pending = csv.writer(member)
    member_pending.writerow(member_pending_header)

    with open ("advisor_pending_list","w") as advisor:
        advisor_pending = csv.writer(advisor)
        advisor_pending.writerow(advisor_pending_header)






