students = {
      "Giannis": {"age": 40, "lessons": ["sql" ,"html"]},
      "Elena": {"age": 20, "lessons": ["css","php"]}
}


students["kostas"] = {"age":40, "lessons" :["react" ,"js"]}

for name, info in students.items():
      print(f"mathitis : {name}, ilikia : {info['age']}, mathimata : {','.join(info['lessons'])}")