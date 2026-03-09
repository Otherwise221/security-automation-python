# This script scans a file for specific keywords and flags any that match.
#the key words are malicious indicators

#this script is a file analysis

#Import the file or get the file

#read through the file for keywords

#what are the keywords

#the keywords can also be a large file of words that are indicators

prompt = input("What would you like to do today? " \
"\n A) Scan a file for a malicious indicator" \
"\n B) Analyze file hashes" \
"\n C) Suspicious Patterns" \
"\n D) Behavioural Signatures" \
"\n E) Do you want to add a keyword to file: \n")

words = open('Keywords.txt','r')
r_words = words.read()
#print(r_words)

#file = open('file.txt','r')

with open('file.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
#print(lines)

def malicious_checker(r_words, lines):
    keywords = r_words.lower().split(',')
    result = []

    for line in lines:
        line_lower = line.lower()
        for keyword in keywords:
            if keyword in line_lower:
                result.append(keyword)
    #if the words in file match the words in keywords
    if result:
        print("Malicious indicator found")
        print(result)
    #print the word
    #if not
    else:
    #print nothing
        print("No malicious words found")

malicious_checker(r_words, lines)






#hashlib -- generating hashes
#option E add a keyword to file

#do you want to do a paper or how do you want the poster to look like
# look at the wagner awards


#how to make the code more sophisticated. 
    #how can I  make it so i can add keywords which are malicious indicators to the keywords file
    #how can I make it so that any file will be ran against the keywords file

    #Developing automated malware detection tool using Python to scan files for malicious indicators, analyzing file hashes, suspicious patterns, and behavioral signatures to identify threats.
	#Building file analysis automation that parses directory structures, extracts metadata, and flags suspicious executables based on threat intelligence indicators.
	#Implementing security assessment workflows that streamline malware triage processes, reducing manual analysis time and improving consistency of threat detection.

# create powershell workflows to stamdardize scanning across enterprise ****
# build python scripts to parse logs and categorize threats automatically