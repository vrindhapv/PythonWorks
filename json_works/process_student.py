from json import load 

file_path = "json_works\\student.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr)

for st in data:

    print(st.get("name"),st.get("gender"))

st_course= [s.get("name")for s in data if s.get("course")=="software testing"]

print(st_course)