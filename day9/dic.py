
dic = {"city":"London",
       "country": "United Kingdom",
       "continent":"Europe"
}

for key in dic:
    print(key)
    print(dic[key])

# student score dic
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}


for student in student_scores:
  score = student_scores[student]
  if score>90:
    student_grades[student] = "Outstanding"
  elif score>80:
    student_grades[student] = "Exceeds Expectations"
  elif score>70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    
print(student_grades)

# travel_log
travel_log = [
  {"country":"france",
   "cities_visited": ["paris","lille","bordeaux","lyon"],
   "total": 12
  },
  {
   "country":"united kingdom", 
   "cities_visited":["london","manchester","birmingham","oxford"],
   "total":11
  }
]

def add_new_country(country,cities,times):
  new_country = {}
  new_country["country"] = country
  new_country["cities_visited"] = cities
  new_country["total"]=times

  travel_log.append(new_country)
  
# each key can have only one value
add_new_country("Russia",["moscow","saint petersburg"],2)
print(travel_log)


# dict ={}
 
# for i in range (0,4):
#     l = input("name: ")
#     o = input("no. : ")
#     dict[l] = o
#     print(dict)