from time import *

paragraphs = [
    "Scolding is something common in student life. Being a naughty boy, I am always scolded by my parents. But one day I was severely scolded by my English teacher. She infect teaches well. But that day, I could not resist the temptation that an adventure of Nancy Drew offered. While she was teaching, I was completely engrossed in reading that book. Nancy Drew was caught in the trap laid by some smugglers and it was then when I felt a light tap on my bent head.", 
    "The teacher had caught me red handed. She scolded me then and there and insulted me in front of the whole class. I was embarrassed. My cheeks burned being guilty conscious. When the class was over, I went to the teacher to apologize. When she saw that I had realized my mistake, she cooled down and then told me in a very kind manner how disheartening it was when she found any student not paying attention. I was genuinely sorry and promised to myself never to commit such a mistake again.",
    "Studying is the main source of knowledge. Books are indeed never failing friends of man. For a mature mind, reading is the greatest source of pleasure and solace to distressed minds. The study of good books ennobles us and broadens our outlook. Therefore, the habit of reading should be cultivated. A student should never confine himself to his schoolbooks only.",
    "They also inspire us to face the hardships of life courageously. Nowadays there are innumerable books and time is scarce. So we should read only the best and the greatest among them. With the help of books we shall be able to make our thinking mature and our life more meaningful and worthwhile."
    ]




def user_result(name,user_input,para,st,et):
    error = 0
    for i in range(len(para)):
        try:
            if user_input[i] != para[i]:
                error += 1 
        except:
            error += 1
    return error

def typing_test(name,para):
    import random
    test_para = random.choice(para)
    print("*****Test Paragraph*****")
    print(test_para)
    start_time = time()
    user_input = input("*****Type the above Paragraph*****\n")
    end_time = time()
    result = user_result(name,user_input,test_para,start_time,end_time)
    return result

def show_leaderboard():
    pass

def main():
    # Take the input
    user_name = input("Enter your name: ")
    print("1.Start Typing Test 2.Show Leaderboard 3.Exit ")
    user_choice = input("Choose you option (1/2/3): ")
    
    if user_choice == "1":
        score = typing_test(user_name,paragraphs)
        print(score)
    elif user_choice == "2":
        show_leaderboard()
    elif user_choice == "3":
        print("Thank you for using the app!!")
    else:
        print("Invalid input")     
        
main()
