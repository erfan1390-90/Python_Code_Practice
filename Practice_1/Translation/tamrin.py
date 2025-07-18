import os
def  write_add(english,persian):
        with open("database_translation.txt","a") as f:
            f.write(f"{english}\n{persian}\n")
            f.close        
def write_in_database(new):
    new_persian = input(f"Enter translation for: '{new}':")
    with open("database_translation.txt","a") as f:
        f.write(f"{new}\n{new_persian}\n")
    
    with open("database_translation.txt","r") as f:
        big_text = f.read()
    return big_text
def write_persian_in_database(new):
    new_persian = input(f"Enter translation for: '{new}':")
    with open("database_translation.txt","a") as f:
        f.write(f"{new_persian}\n{new}\n")
    
    with open("database_translation.txt","r") as f:
        big_text = f.read()
    return big_text

def read_from_database():
    print("loading...")
    with open("database_translation.txt", "r") as f:
        big_text = f.read()
    parts = big_text.strip().split("\n")
    
    words = []
    
    for i in range(0 , len(parts)-1, 2):
        my_dict = {"English":parts[i], "Persian":parts[i+1]}
        words.append(my_dict)
    return words
    
        
def english_to_persian(user_string,words):
    #i am teacher
    user_words = user_string.split(" ")
    output_text = ""
    
    for user_word in user_words:
        for word in words:
            if word["English"] == user_word:
                output_text+=word["Persian"]+ ' '
                break
        else:
            output_text+=user_word+ ' '
            output_text= write_in_database(user_word)
    return output_text.strip().split("\n")       
    
def persian_to_english(user_string, words):
    user_words = user_string.split(" ")
    output_text = ""

    for user_word in user_words:
        for word in words:
            if word["Persian"] == user_word:
                output_text += word["English"] + ' '
                break
        else:
            output_text += user_word + ' '
            output_text=write_persian_in_database(user_word)  

    return output_text.strip().split("\n")
def search_persian_from_database(user_string,words):
    user_words = user_string.split(" ")
    output_text = ""
    
    for user_word in user_words:
        for word in words:
            if word["Persian"] == user_word :
                output_text+="true"+" "
                break
        else:
            output_text+="false"+" "
    print(user_words)
    return output_text.strip().split("\n")       
    

def search_from_database(user_string,words):
    user_words = user_string.split(" ")
    output_text = ""
    
    for user_word in user_words:
        for word in words:
            if word["English"] == user_word :
                output_text+="true"+" "
                break
        else:
            output_text+="false"+" "
    print(user_words)
    return output_text.strip().split("\n")       
def remove_persian_from_database(user_string, words):
    user_words = user_string.split(" ")
    output_text = ""

    for user_word in user_words:
        for word in words:
            if word["Persian"] == user_word:
                words.remove(word)
                print(f"Removed: {user_word}")
                break
        else:
            output_text += "not found" + ' '

   
    with open("database_translation.txt", "w") as f:
        for word in words:
            f.write(f"{word['English']}\n{word['Persian']}\n")

    return output_text.strip().split("\n")   

def remove_from_database(user_string, words):
    user_words = user_string.split(" ")
    output_text = ""

    for user_word in user_words:
        for word in words:
            if word["English"] == user_word:
                words.remove(word)
                print(f"Removed: {user_word}")
                break
        else:
            output_text += "not found" + ' '

   
    with open("database_translation.txt", "w") as f:
        for word in words:
            f.write(f"{word['English']}\n{word['Persian']}\n")

    return output_text.strip().split("\n")



print("Welcome dear user,please enter your text:")

options="""
1 = English to Persian
2 = Persian to English
3 = Search from Database
4 = Write in Dtabase
5 = Remove from Dtabase
"""
print(options)

d = input("Enter your choice:")
if d=="1"or d=="2" :

    user_string = input("Enter your string:")
elif d=="4":
    persian=input("Enter your string(Persian):")
    english=input("Enter Translation(English):")
words = read_from_database()

if d=="1":
    result = english_to_persian(user_string, words)
    print(result)
elif d=="2":
    result = persian_to_english(user_string, words)
    print(result)
elif d=="3":
    print("""
1 = English 
2 = Persian 
    """)
    e = input("Enter your choice:")
    user_string = input("Enter your string:")
    if e=="1":
        result = search_from_database(user_string,words)
        print(result)
    elif e=="2":
        result = search_persian_from_database(user_string,words)
        print(result)
elif d=="4":
    result =write_add(english,persian) 
    print(result)
elif d=="5":
    print("""
1 = English 
2 = Persian 
    """)
    e = input("Enter your choice:")
    user_string = input("Enter your string:")
    if e=="1":
        result = remove_from_database(user_string, words)
        print(result)
    elif e=="2":
        result = remove_persian_from_database(user_string, words)
        print(result)
else:
    print("not found")