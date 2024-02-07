import json

with open("qna.json",'r') as file:
    cont = file.read() #string

cont_list = json.loads(cont) #list

print(cont_list)

for ques in cont_list:
    print(ques["question_text"])
    for index, op in enumerate(ques["options"]):
        print(index + 1, "-",op)

    user_ans = int(input("Select a single option number: "))
    ques["user_resp"] = user_ans

print(cont_list)