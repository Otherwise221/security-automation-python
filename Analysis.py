import os #the os module is for simple keyword removal
import hashlib


words = open('Keywords.txt','r')
r_words = words.read()

def main():
    while True:
        print("TOOL")
        print("*****************************")
        #what are the options for this tool
        prompt = input("What would you like to do today:" \
        "\n A) Scan a file for malicious indicators" \
        "\n B) Turn a file into a hash" \
        "\n C) Suspicious Patterns" \
        "\n D) Behavioural Signatures" \
        "\n E) Add a keyword to the keyword List" \
        "\n F) Delete words for the keyword list" \
        "\n G) Compare a file to an existing hash (analyzing)"
        "\n Z) Quit" \
        "\n Enter choice : ").strip().upper()

        #based on what the user picks do the following
        if prompt == 'A':
            print("Scanning file for malicious indicators....")
            filename = input("Enter the file you want to scan or press enter for default file: \n")
            result = malicious_indicators(filename if filename else 'file.txt')
            print_result(result)
            print()
        elif prompt == 'B':
            file = input("Enter a file: ")
            if not os.path.exists(file):
                print("File not found...try again")
            else: 
                file_hash = hash_maker(file)
                print(f"Hash: {file_hash}")

                with open("hashLibrary.txt", "a") as f:
                    f.write(file_hash + "\n")
                print("File saved in hash library")
           
            print("...")
        elif prompt == 'C':
            print("g")
        elif prompt == 'D':
            print("g")
        elif prompt == 'E':
            add_keywords_to_file()
            print("...")
        elif prompt == 'F':
            print("kk")
        elif prompt == 'G':
            input_1 = input("Filename: ")
            if not os.path.exists(input_1):
                print("Not found...")
            else:
                hash_analyzer(input_1)
            print("..")
        elif prompt == 'Z':
            print("Program Done...")
            print("Thanks!!")
            break
        else:
            print("I don't understand???? Please try again")

#scanning a file for malicious indicators
#the goal is to take a file and scan it for any malicious indicator keywords
#the malicious indicator keywords are located in the keywords.txt
#prompt == A
#we want to be able to use any file or the default file.txt 

#the keywords
def loading_keywords(filepath='Keywords.txt'):
    #reading the keywords from the file
    try:
        with open(filepath, 'r') as f:
            keywords = []
            for line in f:
                if line.strip():
                    keywords.append(line.strip().lower())
        return keywords
    except FileNotFoundError:
        print("Error")
        return []

#checking for malicious indicators

def malicious_indicators (scan_filepath='file.txt'):
    #to scan for indicators we have to get the keywords first
    keywords = loading_keywords()
    if not keywords:
        print("There are no keyword indicators. Try the adding a keyword")
        return
    # scanning the keywords for indicators
    try: 
        with open(scan_filepath, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error the file is not found")
        return
    result = [] #empty list to store the matches

    for line_no, line in enumerate(lines, start=1):
        line_lower = line.lower()
        for keyword in keywords:
            if keyword in line_lower:
                result.append((line_no, keyword, line.strip()))
    
    # if result: 
    #     print("Indicators found...")
    # else:
    #     print("No malicious indicators found...")
    return result

#Prompt == E
#Adding a keyword to the malicious indicator list

def print_result(result):
    for res in result:
        print("In line " + str(res[0]) + ": the malicious indicator " + str(res[1]) + " was found")

def add_keywords_to_file ():
    while True:
        word = input("What keyword: ").strip().lower() # asking for an indicator keyword

        if not word:
            print("No word entered...Try Again...")
            continue
        
        #to avoid enetering the same word twice we need to check for duplicates
        duplicates  = loading_keywords()
        if word in duplicates:
            print("The indicator you are trying to enter already exists...")
        else:
            with open('Keywords.txt', 'a') as file: #open the keyword file to append to it
                file.write(word + '\n') #append the input word into the file
        print("New keyword added successfully")

        ask = input("Add another word: "
                    "\nYes or No: ").strip().lower()
        
        if ask != "yes": 
            break
     

# Prompt B === analyzing file hashes

#hashlib , hmac (creates hashes)

# process:
    # File is entered --> processed --> hash analyzed
# A file is entered, a hash for the file is geenrated, the hash generated is stored in a file
# another file is then hashed and compared to the hashes stored in the hash library

#hash analysis
def hash_maker(file):
    print("File --> Hash Maker")
    algorithm = hashlib.sha256()
    with open(file, "rb") as f:  #rb is read binary
        while data := f.read(8192):
            algorithm.update(data)
    return algorithm.hexdigest()

#enter the file, turn that into a hash and compare with hash stored in hash library   
def hash_analyzer(input_1):
    print("Analyzeerrrr")
    output = hash_maker(input_1)
    print(f"The hash of the given file is {output}")
    #if the output of the hash is the same as what is stored in the file? 
    with open("hashLibrary.txt", "r") as f:
        storedHashes = []
        for line in f:
            line = line.strip()
            if line:
                storedHashes.append(line)
    if output in storedHashes:
        print("Match Found")
    else:
        print("No match found")


#prompt == F -- deleting keywords in the keyword file
#this function targets the key words file and deletes keywords or all the keywords in the file

def delete_keywords():
    prompt_1 = input("What would you like to delete?" \
    "\n A) A specific keyword" \
    "\n B) All the keywords in the file").strip().lower()

    if prompt_1 == 'A':
        print("Deleting keyword {prompt_1} from file....")
        # [CODE TO DELETE A SPECIFIC KEYWORD FROM A FILE]

        print("Deleting all the keywords")
            #[CODE TO DELETE ALL THE KEYWORDS FROM THE FILE]
        print("All the keywords have been deleted")
        return
    else: 
        print ("Error! Wrong input, Please try again")
        return
    

main()

# TO DO LIST  3/06/2026

# COMPELTE DELETE KEYWORD function
# Suspicious Pattern stuff
# Make / Update journal
