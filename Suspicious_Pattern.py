# This code is for suspicious patterns
import re  # for patterns
import os  # for file handling
import pandas as pd
from datetime import datetime

'''
The difference between malicious indicators and suspicious patterns is 
that malicious indicator is looking for a word while suspicious patterns is a pattern

In python the re module is used when it comes to patterns

There are different suspicious patterns in cybersecurity these could be things like:
   - Unusual login times, unlisted software, malicious software, hijacking software, APT activities
   - Repeated login attempts from unknown IPs, deletion or modifications to a system 
   - Unusual spikes in traffic

def unusual_login_times ():
    print("This fucntion detects unusual logins")
#if the user logins in between the hours from 8pm - 5am it needs to be flagged.

def traffic_spikes():
    print("This fucntion detects unusal traffic spikes")

def repeated_logins():
    print("This function flags for too many repated logins at a time")

What are some suspicious patterns that would appear in a file? 
    - IP addresses, suspicious URLs, embedded email address, Base64 encoded string

Is doing the file format right for this type of thing? 

REGEX Tool in python for suspicious patterns (re module)
    - Used to search, match, validate, extract or modify text based on specific patterns
    - Allows you to define specific patterns using special characters 

    - You can quickly extract emails, phone numbers, etc..
    - Validate user inputs
    - Replace or reformat stringd

'''


# have a file use re to get IP addresses and then compare the addresses you get with
# known bad IPs

# read the file
# find IP addresses
# store them in a list/ dictionary and print
# Compare that with a stored "bad IP addresses"
# if there is a match "suspicious" if not "fine"


# pcap and log files


##########################################################################
### THE GOAL OF THIS CODE IS FOR THE CODE TO ANALYZE A LOG FILE,
### SEE IF THERE IS ANY SUSPICIOUS IPS, REPEATED LOGIN ATTEMPTS,
### AND UNUSAL LOGIN ATTEMPTS
#########################################################################


def main():
    print("SUSPICIOUS PATTERN TOOL")
    print("This tool tells the user whether the inputted log file has any suspicious ips," \
          "and frequent & unusual login attempts")
    print("an unusual login attempt is a user loging into the system at an unusual time")

    # I want the user to enter a file
    # Once the file is entered the coding begins

    file = input("Enter a filename: ")
    if not os.path.exists(file):  # making sure the file exists
        print("Error")
        return
    extension = os.path.splitext(file)[1].lower()  # grabbing the extension
    if extension == ".csv" or extension == ".txt":
        df = pd.read_csv(file)
    elif extension == ".xlsx":
        df = pd.read_excel(file)
    else:
        print("The file you are entering is not supported. Please try again!")
        return

    sus_ips(df)
    unusual_login(df)
    frequent_logins(df)


# The file has been read
# extract the content and use the content to do the suspicious pattern code

# checking for malicious IPs

def sus_ips(df):
    with open('bad_IPs.txt', 'r') as file:
        bad_ips = []
        for line in file:
            if line.strip():
                bad_ips.append(line.strip())

    # create a space for the ip addresses so I can use them
    match = False
    for index, row in df.iterrows():
        ip = row["IP Address"]

        if ip in bad_ips:
            print(f"Malicious IP found. The malicious IPS detected is {ip}")
            match = True
    if not match:
        print("No malicious IP found")

        # checking if login time is outside normal hours


def unusual_login(df):
    match = False
    # Timestamp format is YYYY - MM - DD HH:MM:SS
    # MAIN IDEA
    # if time is between 6pm to 6am
    # print unusual login time please check on user
    # else
    # print there has been no unusual login attempts

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])  # converting the timestamp to datetime
    for index, row in df.iterrows():  # getting just the hour for the if loop
        hour = row["Timestamp"].hour
        event_type = row["Event Type"]

        if (hour > 18 or hour < 6) and event_type == "LOGIN":
            print("###########################################################################")
            print(f"Unusual login detected from user {row['Username']} at {row['Timestamp']}")
            print("Check the user")
            match = True
    if not match:
        print("No unusal login activity detected")

def frequent_logins(df):
    match = False
    #looking for event_type = Login and username appears > 2 and Timestamp is really close to each other
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    logins = df[df["Event Type"] == "LOGIN"]
    login_count  = logins["Username"].value_counts()


    threshold = pd.Timedelta(minutes=2)

    for user, count in login_count.items():
        user_logins = logins[logins["Username"] == user].sort_values("Timestamp").copy()
        user_logins["time_diff"] = user_logins["Timestamp"].diff()

        first = user_logins["Timestamp"].min()
        last = user_logins["Timestamp"].max()

        if count > 2 and user_logins["time_diff"].min() < threshold:
            print("#################################")
            print(f"Alert: Frequent login attempts from the user {user}, They logged in {count} times "
                  f"Login times are: {first} to {last}")
            print()
            match = True
    if not match:
        print("There are no frequent logins today")

main()

