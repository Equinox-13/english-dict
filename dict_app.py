import json
from difflib import get_close_matches
import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database")

cursor = con.cursor()

def execute_query(arg):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"%(arg))
    results = cursor.fetchall()
    return results

def check_close_match(arg):
    query = cursor.execute("SELECT Expression FROM Dictionary WHERE Expression like '%%%s%%'"%(arg))
    result = cursor.fetchall()
    row = [item[0] for item in result]
    if len(get_close_matches(arg,row,cutoff=0.8)) > 0:
        return True

def retrieve_close_match(arg):
    query = cursor.execute("SELECT Expression FROM Dictionary WHERE Expression like '%%%s%%'"%(arg))
    result = cursor.fetchall()
    row = [item[0] for item in result]
    close_match = get_close_matches(arg,row,cutoff=0.8)[0]
    return close_match



def fetch_meaning(word):
    word = word.lower()
    if execute_query(word):
        return execute_query(word)
    elif execute_query(word.title()):
        return execute_query(word.title())
    elif execute_query(word.upper()):
        return execute_query(word.upper())
    elif check_close_match(word):
        print("inside close_match")
        yn = input("Did you mean %s instead? Enter Y if Yes, or N if No:"%(retrieve_close_match(word)))
        if yn == "Y":
            return execute_query(retrieve_close_match(word))
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understood your input."
    else:
        return "The word doesn't exist. Please double check it."

word  = input("Enter a word:")
result = fetch_meaning(word)
if type(result) == list:
    for each in result:
        print(each[1])
else:
    print(result)


