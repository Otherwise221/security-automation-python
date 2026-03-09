

'''
#enter a keyword
# the keyword is added into the file
#the program asks you do you want to add more words
#yes or no
#if yes, the program asks you to enter the keyword 
#if no, the program breaks
list = []
while:
    word = input("Enter a word: ")
    list.append(word)
    ask = input("Do you want to add more words: "
                "\n Yes or No")
    if ask == "Yes" or ask == "yes":
        word1 = input("Enter a word: ")
        list.append(word1)
    else:
        break




'''

# File Analysis Tool
# Scans files for malicious indicators and manages the keyword list

def load_keywords(filepath='Keywords.txt'):
    """Read keywords from file, one per line."""
    try:
        with open(filepath, 'r') as f:
            # Strip whitespace and filter out empty lines
            keywords = [line.strip().lower() for line in f if line.strip()]
        return keywords
    except FileNotFoundError:
        print(f"Warning: '{filepath}' not found. Starting with empty keyword list.")
        return []


def malicious_checker(scan_filepath='file.txt'):
    """Scan a file for malicious indicator keywords."""
    keywords = load_keywords()

    if not keywords:
        print("No keywords loaded. Please add keywords first (Option E).")
        return

    try:
        with open(scan_filepath, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: '{scan_filepath}' not found.")
        return

    result = []

    for line_num, line in enumerate(lines, start=1):
        line_lower = line.lower()
        for keyword in keywords:
            if keyword in line_lower:
                result.append((line_num, keyword, line.strip()))  # track line number too

    if result:
        print("\n[!] Malicious indicators found:")
        for line_num, keyword, line_text in result:
            print(f"  Line {line_num} | Keyword: '{keyword}' | Content: {line_text}")
    else:
        print("\n[✓] No malicious indicators found.")


def add_keyword():
    """Add new keywords to the Keywords.txt file."""
    while True:
        word = input("Enter keyword to add: ").strip().lower()

        if not word:
            print("No keyword entered, try again.")
            continue

        # Check if keyword already exists to avoid duplicates
        existing = load_keywords()
        if word in existing:
            print(f"'{word}' is already in the keyword list.")
        else:
            with open('Keywords.txt', 'a') as f:
                f.write(word + '\n')  # one keyword per line
            print(f"[✓] '{word}' added successfully.")

        ask = input("\nAdd another keyword? (yes/no): ").strip().lower()
        if ask != 'yes':
            break

    # Show current keyword list
    print("\nCurrent keywords:")
    keywords = load_keywords()
    for kw in keywords:
        print(f"  - {kw}")


def main():
    while True:
        print("\n=============================")
        print("   File Analysis Tool")
        print("=============================")
        prompt = input(
            "What would you like to do today?\n"
            "  A) Scan a file for malicious indicators\n"
            "  B) Analyze file hashes\n"
            "  C) Suspicious Patterns\n"
            "  D) Behavioural Signatures\n"
            "  E) Add a keyword to the keyword list\n"
            "  Q) Quit\n"
            "Enter choice: "
        ).strip().upper()

        if prompt == 'A':
            filename = input("Enter filename to scan (or press Enter for 'file.txt'): ").strip()
            malicious_checker(filename if filename else 'file.txt')

        elif prompt == 'B':
            print("Hash analysis coming soon...")

        elif prompt == 'C':
            print("Suspicious pattern analysis coming soon...")

        elif prompt == 'D':
            print("Behavioural signature analysis coming soon...")

        elif prompt == 'E':
            add_keyword()

        elif prompt == 'Q':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


main()