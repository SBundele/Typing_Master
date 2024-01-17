from time import *
import json

paragraphs = [
    "Scolding is something common in student life. Being a naughty boy, I am always scolded by my parents. But one day I was severely scolded by my English teacher.", 
    "The teacher had caught me red handed. She scolded me then and there and insulted me in front of the whole class. I was embarrassed. My cheeks burned being guilty conscious.",
    "Studying is the main source of knowledge. Books are indeed never failing friends of man. For a mature mind, reading is the greatest source of pleasure and solace to distressed minds.",
    "They also inspire us to face the hardships of life courageously. Nowadays there are innumerable books and time is scarce. So we should read only the best and the greatest among them."
    ]

# Leaderboard functions
def maintain_leaderboard(speed,accuracy,name,data,json_file = "leaderboard.json"):
    if name not in data:
        data[name] = [speed,accuracy]
    else:
        exist = round(data[name][1]/data[name][0],4)
        new = round(accuracy/speed,4)
        if exist < new:
            data[name][0] = speed
            data[name][1] = accuracy
    
    with open(json_file,"w") as file:
        json.dump(data,file,indent=2)
    
    show_leaderboard(data)
       
def show_leaderboard(data):
    print()
    print("----Leaderboard----")
    for user in data:
        print(f"Username: {user}, speed: {data[user][0]} WPA, accuracy: {data[user][1]}%")
    print()
    print("Thankyou for using the app!!\nWish you Best of Luck!!")

# Speed and Accuracy calculation function
def inputLength(user_inp):
    arr = user_inp.split(" ")
    return len(arr)

def calculate_time(st_time,ed_time,user_inp,accuracy):
    time_delay = ed_time - st_time
    time_r = round(time_delay,2)
    # minute conversion
    minute_conversion = round(time_r/60)
    # length calculation
    length = inputLength(user_inp)
    # WPA calculation
    try:
        speed = round(length/minute_conversion)
    # result
    except:
        speed = round(length/(time_r/60),2)
    print(f"Typing Speed: {speed} WPA(Words Per Minute) \nAccuracy: {accuracy}%")
     
    return speed,accuracy

def user_result(user_input,para,st,et):
    correct_word = 0
    arr = para.split(" ")
    arr1 = user_input.split(" ")
    original_length = len(arr)
    
    for i in range(len(arr)):
        try:
            if arr[i] == arr1[i]:
                correct_word += 1
        except:
            continue
        
    accuracy = round((correct_word/original_length)*100)
    
    return calculate_time(st,et,user_input,accuracy)

def typing_test(para):
    import random
    test_para = random.choice(para)
    print("*****Test Paragraph*****")
    print()
    print(test_para)
    print()
    start_time = time()
    user_input = input("*****Type the above Paragraph*****\n Enter: ")
    end_time = time()
    print()
    speed,accuracy = user_result(user_input,test_para,start_time,end_time)
    
    return speed,accuracy

def existing_user(status,data):
    name = input("Enter your username: ")
    print()
    if status == 'y':
        while True:
            if name not in data:
                print("Invalid username")
                name = input("Enter your username: ")
            else:
                return name
    else:
        while True:
            if name in data:
                print("name already exists")
                name = input("Enter your username: ")
            else:
                return name

def main(data):
    # Take the input
    status = input("Have you given the test before ? (y/n): ")
    user_name = existing_user(status,data)
    print()
    print("1.Start Typing Test 2.Show Leaderboard 3.Exit ")
    user_choice = input("Choose you option (1/2/3): ")
    
    if user_choice == "1":
        speed,accuracy = typing_test(paragraphs)
        maintain_leaderboard(speed,accuracy,user_name,data)
    elif user_choice == "2":
        show_leaderboard(data)
    elif user_choice == "3":
        print()
        print("Thank you for using the app!!")
        print()
    else:
        print("Invalid input")   
        print()  
        
file = open("leaderboard.json","r")
data = json.load(file) 
    
main(data)
