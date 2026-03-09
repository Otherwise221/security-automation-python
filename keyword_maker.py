#this program adds keywords to the keyword.txt file as more keywords are found

file = 'Keywords.txt'

def add_keyword_to_file():
    while True:
        word = input("What keyword: ") # asking for an indicator keyword
    
        with open('Keywords.txt', 'a') as file: #open the keyword file to append to it
            file.write(word + '\n') #append the input word into the file
        print("New keyword added successfully")

        ask = input("Add another word: "
                    "\nYes or No: ").lower()
        
        if ask != "yes": 
            break

        
    with open('Keywords.txt', 'r') as file: # read the keyword file
        content = file.read()
        print("\nCurrent KEYWORDS:")
        print(content) 


add_keyword_to_file()



#what if i want to delete keywords from the file or delete all the keywords in the file

def delete_keywords_in_file():
    print("")







