import requests
import json
from pprint import pprint


def getCourses(firstApi):
    response=requests.get(courses_url)
    json_data=response.json()
    coursesData=json_data["availableCourses"]
    count=0
    coursesIdList=[]
    for index in coursesData:
        print count,index["name"],index["id"]
        coursesIdList.append(index["id"])
        
        count=count+1
    return coursesIdList
courses_url="http://saral.navgurukul.org/api/courses"
coursesIdList=getCourses(courses_url)

user_input=input("enter your Id:")
user_Id=coursesIdList[user_input]

def getExercises(secondApi):   
    response1=requests.get(secondApi)
    json_data1=response1.json()
    exercisesData=json_data1["data"]
    count=0
    slug_list=[]
    exercisesIdData=[]
    for index in exercisesData:
        print count,index["name"],index["id"] ,index["slug"]
        exercisesIdData.append(index["id"]) 
        childExercisesdata=index["childExercises"]
        count1 = 0   
        for index1 in childExercisesdata:
            print "\t","\t",count1, index1["name"],index1["id"]  
            count1=count1+1
        count=count+1          
    return exercisesIdData              
exercises_url= "http://saral.navgurukul.org/api/courses/"+str(user_Id)+"/exercises"
exercisesIdData=getExercises(exercises_url)


slug_list=[]
def getSlug(user_input):
    exercises_url= "http://saral.navgurukul.org/api/courses/"+str(user_Id)+"/exercises"
    response1=requests.get(exercises_url)
    json_data1=response1.json()
    exercisesData=json_data1["data"]
    for index in exercisesData:
        count=0
        parent_slug=exercisesIdData[user_input]
        if parent_slug==index["id"]:
            print count,index["name"]
            slug_list.append(index["slug"]) 
            childExercisesdata=index["childExercises"]
            count1=count+1  
            for index1 in childExercisesdata:
                print count1, index1["name"]
                slug_list.append(index1["slug"])  
                count1=count1+1  
        count=count+1        
    return slug_list   
slug_input=input("Enter your slug number:")
slug_list=getSlug(slug_input)


user_input1=input("enter your Exercise Id:")
Exercises_Id=slug_list[user_input1]
# print Exercises_Id

def getContant(thirdApi):
    response2=requests.get(thirdApi)
    json_data2=response2.json()
    contantData=json_data2["content"]
    print contantData    

contant_url="http://saral.navgurukul.org/api/courses/"+str(user_Id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(Exercises_Id)
getContant(contant_url)