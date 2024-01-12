# A class creates a template for objects that dont exist in premade form for python.
# This Class creats an exception that does not exist in pyhton
class LengthError(Exception):
    #Pass teel tell the code to go the next line
    pass
# This Class creats an exception that does not exist in pyhton
class SpecialCharacterError(Exception):
    #Pass teel tell the code to go the next line
    pass
# A definition or DEF creates a function for pyton to use later.
# This def creates 2 functions one to check for length errors and the other for special character errors 
def check_input(input_string):
    # The special character should not be in names
    special_characters = "~!@#$%^&*()_+=-`:\"';/[/[/}/{:;\"'</,>.|\\"
    # The max legth prevents overrun in name length
    max_length = 50  # Define a maximum length for the names
    # This line of code checks if the length of 'input_string' exceeds 'max_length'.
    # If the length of 'input_string' is greater than 'max_length', the condition becomes True.
    if len(input_string) > max_length:
        # The 'raise' keyword is used to throw an exception if a condition occurs. In this case, LengthError is raised when the input exceeds the maximum allowed length.
        raise LengthError(f"Input is too long. Maximum length is {max_length} characters.")
    # The 'for' Keyword is used to itterate in the input string from the user. 
    for character in input_string:
        #This if is only triggered in the event of special character being used in entry thats not allowed.
        if character in special_characters:
            # This raise condition is activated int event of invalid charter being tyoed in a name
            raise SpecialCharacterError(f"Special character '{character}' is not allowed.")
#This def creates a new file 
def create_new_file():
    ''' In this code, 'good_record.txt' is the name of the file to be opened. The 'r' argument means the file is opened in read mode.
   The as f part assigns the opened file to the variable f. Then, f.read() is used to read the entire content of the file, which is stored in the  '''
    with open('good_record.txt' , 'r' ) as f:
        #This prints the content of the file
        print(f.read())
# This allows the user to search for a keyword in a file        
def user_search(file_name, keyword):
    # Initialize a flag to track if any results were found
    found = False 
    # Open the file in read mode
    with open(file_name) as file:
         # Iterate over each line in the file, with line numbers starting at 1.
        for line_number, line in enumerate(file, start=1):
            # Check if the keyword is in the current line.
            if keyword in line:
                # If the keyword is found, print the line number and the line (stripped of leading/trailing whitespace).
                print(f'Keyword "{keyword}" found at line {line_number}: {line.strip()}')
                # Set the flag to True if a result is found
                found = True  
    # If no results were found (i.e., if the flag is still False), print a message indicating no results.           
    if not found:
        #This prints a this messag if no results are found
        print('Sorry, no results found')
 # The def main describes the main function of program 
def main():
    # The wile true loop allows a program to continue to run until a condition is met. In this case it is any answer than yes
    while True:
        # This try loop check the input from user for invalid characters
        try:
            # This function allows a user user to select yes or no in the answer 
            user_answer = input('Would you like to record some information? (Yes or No) ')
            # This call the definition earlier created to verify which special are not allowed. Also check to see if the maximum character limit is reach 
            check_input(user_answer)
        # The except allows the program to continue to if invalid characters are input
        except SpecialCharacterError as e: 
            # This print the character thats is invalid and tell the user the type of error that has occured
            print(e, 'You have entered an invalid Character')         
        # This if statment check make sure that "yes" or "no" are enterered 
        # The .lower method forces all characters are lower case so that if user Yes, yEs, yeS, YES or any combination of that it will still will work,.
        if user_answer.lower() == 'yes':
            # If the user answers 'yes', break the loop and continue with the rest of the program
            break
            # This message prints if no is enter 
        elif user_answer.lower() == 'no':
            print('Thank you for using my program')
            # This terminates the loop.
            exit()
            # This Else is triggered when when neither (Yes or No) is entered.
        else:
           # this prints when the esle sta is valid
           print('Invalid input. Please answer with either "yes" or "no".')

        try:
            # this tell the user what enter and how to enter numbers
            user_input_line1 = input('Write your first name here (use Roman numerals to indicate numbers): ')
            # This call the definition earlier created to verify which special are not allowed. Also check to see if the maximum character limit is reach
            check_input(user_input_line1)
            # This tell the user what they entered
            print('Your First Name is:', user_input_line1  )
        # The except allows the program to continue to if invalid characters are input   
        except SpecialCharacterError as e:
            print(e, 'You have entered an invalid Character')
            continue
        
        try:
            # This intiates user input to be used in the if statment 
            user_input_line2 = ('')
            # Asks the user if they have a middle name
            user_answer2 = input('Do you have a midle name? (Yes or NO)')
            # Checks the input from the user
            check_input(user_answer2)
            # If the user answers 'yes', it asks for the middle name
            if user_answer2.lower() == 'yes':
                # Prints this to user 
                user_input_line2 =input('Enter midle name here: ' )
                # checks the user input
                check_input(user_input_line2)
            
            elif user_answer2.lower() == 'no':
                print('Go to next line')
        except SpecialCharacterError as e:
            print(e, 'You have entered an invalid record')
            continue    
        try:
            user_input_line3 = input('Write your last name here: (use Roman numerals to indicate numbers):')
            check_input(user_input_line3)
            print(user_input_line3)
        except SpecialCharacterError as e:
            print(e, 'You have entered an invalid record')
            continue

        user_input_line4 = input('Write your email here: ')
        print(user_input_line1 , user_input_line2 , user_input_line3, user_input_line4)
        with open('good_record.txt', 'a') as f:
            f.write(f'{user_input_line1} {user_input_line2} {user_input_line3} {user_input_line4}\n')
        create_new_file()
        user_answer3 = input('Do you want to search for a keyword in the file? (Yes or No) ')
        if user_answer3.lower() == 'yes':
            keyword = input('Enter the keyword to search for: ')
            user_search('good_record.txt', keyword)
        else:
            print('Got to next line')



if __name__ == "__main__":
    main()
