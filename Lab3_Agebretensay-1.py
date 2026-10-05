"""
    Project Name: Word Count
    Author:Adhanet Gebretensay
    Purpose:an OOP program that processes files, handle exeptions, and counts word frequnceses.
    Starter Code:pathlib and string.
    Date:10/04/2026

"""
from pathlib import Path
import string

class WordAnalyzer:
    
    def __init__(self,filepath):
        self.__filepath = Path(filepath)
        self.__frequncies = {}
    
    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError(f"The file does not exist. Please try again.")
            punctuation_table = str.maketrans('','', string.punctuation)

            with self.__filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(punctuation_table)
                    words = line.split()

                    for word in words:
                        self.__frequncies[word] = self.__frequncies.get(word, 0) + 1
            return True
        except FileNotFoundError:
            print(f"Error: The file is not found")
            return False

    def print_report(self):
        words = self.__frequncies.keys()
        sorted_words = sorted(words)

        for word in sorted_words:
            count = self.__frequncies[word]
            print(f"{word:<25} :: {count}")

def main():
    files = {
        '1':Path("moby_dick_ch1.txt"),
        '2':Path('frankenstein_ch1.txt'),
        '3':Path('alice_in_wonderland_ch1.txt'),
        '4':Path('pride_and_prejudice_ch1.txt')
    }

    menu = {
        "1" : "Moby Dick (Chapter 1)",
        "2" : "Frankenstein (Chapter 1)",
        "3" : "Alice in Wonderland (Chapter 1)",
        "4" : "Pride and Prejudice (Chapter 1)"

    }

    while True:
        print("--- Word Analyzer ---")
        print("Please select a file to analyze")

        for key, value in menu.items():
            print (f"{key}. {value}")
        print("5. Exit\n")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in files:

            selected_file_path = files[choice]
            analyzer = WordAnalyzer(selected_file_path)
            success = analyzer.process_file()

            if success:
                analyzer.print_report()

            input("Press Enter to return to the menu... \n")
        else:
            print("\nInvalid Choice. Please select from 1-5.\n")
            input("Press Enter to return to the menu...\n")
if __name__ == "__main__":
    main()
        


        






    
            