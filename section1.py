print("hello world")
myname="ahmed"
age =16
faculty ="Fci"
print("name is :"+myname)
print("age is :"+str(age))
print("faculty is: "+faculty)


degree= 90

if degree<50 :
    print("fail")
elif degree>50 and degree<75:
    print("pass by good")
elif degree>75 and degree<85:
    print("pass by very good")
else:
    print("pass by Excellence")

courses=["big data","DDS","DSS","security"]
print(courses[-1])
print(courses[1:3])
print(courses[:3])

courses.append("social IS")
courses.insert(2,"e-commerce")
print(courses[:])
del courses[2]
print(courses[:])
courses.append("social IS")
courses.append("social IS")
courses.append("social IS")
print(courses[:])

for course in courses:
    print(course)
    
newarr= []
for course in courses:
    if len(course) > 4:
        newarr.append(course)
        
print(newarr[:])
#Nested loops
course_pair=[]
for course_1 in courses:
    for course_2 in courses:
        course_pair.append((course_1,course_2))

print(course_pair)

#tuples

coll=("ahmed","ali",16)
print(coll)

#Unpacking
name1,name2,ag=coll;
print(ag)

doc_course={'ahmed':'bigdata','ali':'DSS','mohamed':'GIS',}

print(doc_course['ahmed'])

doc_course['tarek']='data mining'
print('tarek' in doc_course)

doc_course['ali']='DDS'
del doc_course['ahmed']
print(doc_course)

for key in doc_course:
    value = doc_course[key]
    print('student',key, 'is taking', value)

for key, value in doc_course.items():
    print('student',key, 'is taking', value)
#Dictionaries as records
subject = ('ahmed', 'it', '500')
doc_name, subj, numofstud = subject
print(doc_name, 'teatch',subj ,'with', numofstud,'students')
#List of tuples
doc__course = [
    ('ahmed','bigdata'),
    ('ali','DSS'),
    ('mohamed','GIS'),
]
print(doc__course[0])
print(doc__course[0][1])

# List of dictionaries
dic_doc_course = []
for doc_name, subject in doc__course:
    record = {
        'name': doc_name,
        'subject': subject,
    }
    dic_doc_course.append(record)

print(dic_doc_course)
print(dic_doc_course[1]['name'])

