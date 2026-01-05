def find_status(num):
    if num >= 85:
        return "Distinction"
    elif num >= 50:
        return "Pass"
    else:
        return "Fail"
        

def find_avg(numbers):
    total = 0
    size = len(numbers)
    
    for number in numbers:
        total += number
    
    return total / size


def Analyse(records):
    answer = {}
    
    for record in records:
        name = record[0]
        marks = record[1]
        
        average = find_avg(marks)
        status = find_status(average)
        
        answer[name] = {
            "average": round(average, 2),
            "status": status
        }
    
    return answer


students = [
    ("Ajay", [78, 85, 90]),
    ("Kumar", [65, 70, 60]),
    ("Rahul", [88, 92, 95])
]

result = Analyse(students)
print(result)