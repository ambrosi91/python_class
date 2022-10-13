#importing existing json module
import json
import requests

# reading json file from current directory
with open("data.json", "r") as data_file:
    data = json.load(data_file)

# Get class value for json object
print (data["class"])

# Get school value for json object
print (data["school"])

# Get location value for json object
print (data["location"])

# Get instructors value for json object
print (data["instructors"])

# Get 1 instructor value for json object
print (data["instructors"][0]["instructor1"]["name"])
INSTRUCTOR1_NAME = data["instructors"][0]["instructor1"]["name"]
INSTRUCTOR1_LASTNAME = data["instructors"][0]["instructor1"]["lastname"]

# write instructor information to a file
with open("instructor1_data", "w")as target_file:
    target_file.write(INSTRUCTOR1_NAME + " " + INSTRUCTOR1_LASTNAME)


# Get 2 instructor value for json object
print (data["instructors"][1]["instructor2"]["name"])
INSTRUCTOR2_NAME = data["instructors"][1]["instructor2"]["name"]
INSTRUCTOR2_LASTNAME = data["instructors"][1]["instructor2"]["lastname"]

# write instructor information to a file
with open("instructor2_data", "w")as target_file:
    target_file.write(INSTRUCTOR2_NAME + " " + INSTRUCTOR2_LASTNAME)



# Get 3 instructor value for json object
print (data["instructors"][2]["instructor3"]["name"])
INSTRUCTOR3_NAME = data["instructors"][2]["instructor3"]["name"]
INSTRUCTOR3_LASTNAME = data["instructors"][2]["instructor3"]["lastname"]

# write instructor information to a file
with open("instructor3_data", "w")as target_file:
    target_file.write(INSTRUCTOR3_NAME + " " + INSTRUCTOR3_LASTNAME)        
    
target_file.close()    
# for i in data:
#     print(i)      
    