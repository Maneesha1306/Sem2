students = {
"Subbu": 85,
"Hasly": 72,
"Shruthi": 90,
"Madhangi": 68,
"Dharshini": 95,
"Kiruthiga": 78}
# 1. Sort students by marks in ascending order
ascending_marks = dict(sorted(students.items(), key=lambda item: item[1]))
print("Ascending order by marks:", ascending_marks)
# 2. Sort students by marks in descending order
descending_marks = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))
print("Descending order by marks:", descending_marks)
# 3. Find the top 3 students with the highest marks
top_3_students = dict(sorted(students.items(), key=lambda item: item[1], reverse=True)[:3])
print("Top 3 students:", top_3_students)
# 4. Sort students by name alphabetically
alphabetical_order = dict(sorted(students.items(), key=lambda item: item[0]))
print("Alphabetical order by name:", alphabetical_order)
players = [
("Messi", 30),
("Ronaldo", 28),
("Neymar", 25),
("Mbappe", 35),
("Lewandowski", 40),
("Kane", 22)]
# 1. Sort players by goals scored in ascending order
ascending_goals = sorted(players, key=lambda item: item[1])
print("Ascending order by goals:", ascending_goals)
# 2. Sort players by goals scored in descending order
descending_goals = sorted(players, key=lambda item: item[1], reverse=True)
print("Descending order by goals:", descending_goals)
# 3. Find the top 3 goal scorers
top_3_scorers = sorted(players, key=lambda item: item[1], reverse=True)[:3]
print("Top 3 goal scorers:", top_3_scorers)
# 4. Sort players by their names alphabetically
alphabetical_order = sorted(players, key=lambda item: item[0])
print("Alphabetical order by name:", alphabetical_order)
# 5. Find employees earning more than $5000
employees = {
"John": 4500,
"Emma": 5200,
"Ria": 4800,
"Vijay": 5300,
"Ebi": 6000}
high_earning_employees = {k:v for k,v in employees.items() if v > 5000}
print("Employees earning more than $5000:", high_earning_employees)