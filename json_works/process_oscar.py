from json import load

file_path ="json_works\\oscar-best-picture-award-winners.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr)

#print(len(data))


movie_title =[m.get("name")for m in data]

#print(movie_title)

title_release_year=[(m.get("name"),m.get("released_year"))for m in data]

#print(title_release_year)

before_2000_movies= [m.get("name")for m in data if m.get("released_year")<2000]

#print(before_2000_movies)

runtime_greater = [m.get("name")for m in data if m.get("duration")>"150 min"]

#print(runtime_greater)

#director_name = [d.get("name")for d in data if d.get("directors").startswith("S")]

#print(director_name)

runtime_lessthan = [r.get("name")for r in data if r.get("duration")<"90 min"]

#print(runtime_lessthan)

total_oscar_winning = [m.get("oscar")for m in data]

#print(total_oscar_winning)









