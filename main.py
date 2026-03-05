from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:
                filtered_students.append(student)
        return filtered_students
    return data

@app.get('/stats')
async def get_stats():
    chicken_count = 0
    fish_count = 0
    vegetarian_count = 0
    css_count = 0
    csm_count = 0
    itm_count = 0
    its_count = 0
    for student in data:
        if student['pref'] == 'Chicken':
            chicken_count = chicken_count + 1
        elif student['pref'] == 'Fish':
            fish_count = fish_count + 1
        elif student['pref'] == 'Vegetarian':
            vegetarian_count = vegetarian_count + 1
        if student['programme'] == 'Computer Science (Special)':
            css_count = css_count + 1
        elif student['programme'] == 'Computer Science (Major)':
            csm_count = csm_count + 1
        elif student['programme'] == 'Information Technology (Major)':
            itm_count = itm_count + 1
        elif student['programme'] == 'Information Technology (Special)':
            its_count = its_count + 1
    return {
        'Chicken': chicken_count,
        'Computer Science (Major)': csm_count,
        'Computer Science (Special)': css_count,
        'Fish': fish_count,
        'Information Technology (Major)': itm_count,
        'Information Technology (Special)': its_count,
        'Vegetarian': vegetarian_count
    }

@app.get('/students/{id}')
async def get_student(id):
    for student in data:
        if student['id'] == id:
            return student
    return None

@app.get('/add/{a}/{b}')
async def add(a, b):
    return int(a) + int(b)

@app.get('/subtract/{a}/{b}')
async def subtract(a, b):
    return int(a) - int(b)

@app.get('/multiply/{a}/{b}')
async def multiply(a, b):
    return int(a) * int(b)

@app.get('/divide/{a}/{b}')
async def divide(a, b):
    return int(a) / int(b)
