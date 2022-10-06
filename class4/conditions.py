



# NUMBER1 = 10
# NUMBER2 = 7

# # if NUMBER1 is NUMBER2:
# #     print("They're equal")
# # else:
# #     print("They're not equal")    


# if NUMBER1 is not NUMBER2:
#     print("They're not equal")
# else:
#     print("They're  equal")    

# HIDDEN_FRUIT = "kiwi"

# FRUIT_LIST1 = ["apple","pear","banana"]
# FRUIT_LIST2 = ("mango","melon","kiwi")
# FRUIT_LIST3 = {"pear","apricot","cherry"}


# if HIDDEN_FRUIT in FRUIT_LIST1:
#     print("Hidden fruit is in List1")
# elif HIDDEN_FRUIT in FRUIT_LIST2:
#     print("Hidden fruit is in List2")
# elif HIDDEN_FRUIT in FRUIT_LIST3:
#     print("Hidden fruit is in List3")        
# else:
#     print("Hidden fruit is not found")


# while True:
#     try:
#         RESPONSE =int(input("where were you born? 'example year': "))
#         if RESPONSE >= 2000 and RESPONSE <= 2022:
#             print("You were born in 21 century")
#         elif RESPONSE >= 1900 and RESPONSE <= 1999:
#             print("You were born in 20th century") 
#         elif RESPONSE >= 1899 or RESPONSE <= 1898:
#             print("You should not be runnig this")        
#         else:
#             print("Please give me a number")
#         break        

#     except TypeError:
#         print("Did you provide digits e.g 1")
ANSWER = "no"
while ANSWER != "yes":
    ANSWER = input("Are you crazy? ")
    if ANSWER == "yes":
        print("I knew that")   