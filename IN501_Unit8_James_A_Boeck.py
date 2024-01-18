# A class creates a template for objects that don't exist in premade form for Python.
# This Class creates an exception that does not exist in Python.
class LengthError(Exception):
    # Pass tells the code to go to the next line.
    pass
# This Class creates an exception that does not exist in Python.
class SpecialCharacterError(Exception):
    # Pass tells the code to go to the next line.
    pass
# A definition or DEF creates a function for Python to use later.
# This def creates two functions: one to check for length errors and the other for special character errors 
def check_input(input_string): # Creates a function called check_Input
    # The special character should not be in the names. 
    special_characters = "~!@#$%^&*()_+=-`:\"';/[/[/}/{:;\"'</,>.|\\"
    #The max length prevents overrun in name length
    max_length = 50  # Define a maximum length for the names
    # If the length of the input string is greater than the maximum length, raise a LengthError.
    if len(input_string) > max_length:
        # The raise provides the function to except the error 
        raise LengthError(f"Input is too long. Maximum length is {max_length} characters.")
    # For each character in the input string
    for character in input_string:
        # If the character is a special character, raise a SpecialCharacterError
        if character in special_characters:
            # Tell the user type of error trhat has occured
            raise SpecialCharacterError(f"Special character '{character}' is not allowed.")
#This def creates a new file
def create_new_file():
    ''' In this code, 'good_record.txt' is the file's name to be opened. The 'r' argument means the file is opened in read mode.
        The as f part assigns the opened file to the variable f. Then, f.read() is used to read the entire content of the file, 
        which is stored in the fille called (good_record_.txt) '''
    with open('good_record.txt' , 'r' ) as f:
        #This prints the content of the file
        print(f.read())
# This allows the user to search for a keyword in a file.
def user_search(file_name, keyword):
    # Initialize a flag to track if any results were found
    found = False 
    # Open the file in read mode
    with open(file_name) as file:
        # Iterates over each line in the file, with line numbers starting at 1.
        for line_number, line in enumerate(file, start=1):
            # Check if the keyword is in the current line.
            if keyword in line:
                # If the keyword is found, print the line number and the line (stripped of leading/trailing whitespace).
                print(f'Keyword "{keyword}" found at line {line_number}: {line.strip()}')
                # Set the flag to True if a result is found
                found = True 
    # If no results were found (i.e. if the flag is still False), print a message indicating no results.            
    if not found:
        #This prints this message if no results are found
        print('Sorry, no results found')
# The def main describes the main function of the program
def main():
    # The while true loop allows a program to run until a condition is met. In this case, it is any answer than yes
    while True:
        # This try loop checks the input from the user for invalid character
        try:
            # This function allows a user to select yes or no in the answer
            user_answer = input('Would you like to record some information? (Yes or No) ')
            # This calls the definition earlier created to verify which specials are not allowed. Also, check to see if the maximum character limit is reach 
            check_input(user_answer)
            # The .lower method forces all characters to be lowercase so that if the user Yes, yes, YES, or any combination of that, it will still work
            if user_answer.lower() == 'yes':
                #The try stament is an error handling function in Python.
                try:
                    # This tells the user what to enter and how to enter numbers
                    print('use Roman numerals to indicate numbers')
                    # Tells the user to enter their firt name. 
                    user_input_line1 = input('Enter your first name here: ')
                    # This calls the definition earlier created to verify which specials are not allowed. Also calls the definition of max character allowed   
                    check_input(user_input_line1)
                    # Tells the user what they entered 
                    print('Your First Name is:', user_input_line1  )
                # This calls the special charters definition earlier in the program an allows the program to continue    
                except SpecialCharacterError as e:
                    # Prints if an invalid Character was entered 
                    print(e, 'You have entered an invalid Character')
                    # Tells the program go to the next line 
                    continue
                # Checks to see if the maximum character limit is reach
                except LengthError as e:
                   # This is only tirggered if more than 50 characters are entered then Print the error message to tell the user the etere to many characters 
                   print(e)
                   # Tells the program go to the next line 
                   continue
                #The try stament is an error handling function in Python. 
                try:
                    # Tells the user to enter their middle name. If yes is selectd also acts as vailidation 
                    user_answer2 = input('Do you have a middle name? (Yes or NO)')
                    # This calls the definition earlier created to verify which specials are not allowed. Also calls the definition of max character allowed.
                    check_input(user_answer2)
                    # This intilializes user_inpu_line2 outside of the if stement so it will function properly
                    user_input_line2 = ('')
                    # The .lower method forces all characters to be lowercase so that if the user Yes, yes, YES, or any combination of that, it will still work.
                    if user_answer2.lower() == 'yes': # The 'if' stament checks to see the stament 'yes' is true.
                        # Tells the user to enter their Middle name.
                        user_input_line2 =input('Enter middle your name here: ' )
                        # This calls the definition earlier created to verify which specials are not allowed.  Also calls the definition of max character allowed.
                        check_input(user_input_line2)
                        # This line is triggered when No is entered in the validation block
                    elif user_answer2.lower() == 'no':
                        # Tell the user what the program is doing
                        print('Go to next line')
                # This calls the special charters definition earlier in the program an allows the program to continue         
                except SpecialCharacterError as e:
                    # Prints if an invalid Character was entered 
                    print(e, 'You have entered an invalid Character')
                    # Tells the program go to the next line 
                    continue
                # Checks to see if the maximum character limit is reach
                except LengthError as e:
                   # This is only tirggered if more than 50 characters are entered then Print the error message to tell the user the etere to many characters 
                   print(e, 'You hav entered to many characters ' )
                   # Tells the program go to the next line 
                   continue
                #The try stament is an error handling function in Python. 
                try:
                    # Tells the user to enter their Last name.
                    user_input_line3 = input('Write your last name here: ')
                    # This calls the definition earlier created to verify which specials are not allowed. Also calls the definition of max character allowed
                    check_input(user_input_line3)
                    # Tells  the user what they entered
                    print(user_input_line3)
                # This calls the special charters definition earlier in the program an allows the program to continue 
                except SpecialCharacterError as e:
                    # Is trigerred if an invalid Character was entered 
                    print(e, 'You have entered an invalid Character')
                    # Tells the program go to the next line 
                    continue
                # Checks to see if the maximum character limit is reach
                except LengthError as e:
                   # This is only tirggered if more than 50 characters are entered then Print the error message to tell the user the etere to many characters 
                   print(e, 'You hav entered to many characters ' )
                   # Tells the program go to the next line 
                   continue
                #The try stament is an error handling function in Python. 
                try: 
                    # Tells the user to enter their Email.
                    user_input_line4 = input('Write your email here: ')
                    # Print all data that was enterd  
                    print(user_input_line1 , user_input_line2 , user_input_line3, user_input_line4)
                    # The 'with' statement is a precursor to an operation in Python.
                    # The 'open' fuction opens the file
                    # The 'a' is function that allows python to append the data entered in the file called 'good_record.txt'
                    # The 'f' Creates standard named variable to allow it to be used i ht next line of code
                    with open('good_record.txt', 'a') as f:
                        # The 'f' variable is uses to write the data entered into the program 
                        f.write(f'{user_input_line1} {user_input_line2} {user_input_line3} {user_input_line4}\n')
                  # Checks to see if the maximum character limit is reach
                except LengthError as e:
                   # This is only tirggered if more than 50 characters are entered then Print the error message to tell the user the etere to many characters 
                   print(e, 'You have entered to many characters ' )
                   # Tells the program go to the next line 
                   continue 
                # Uses the function defined earlier 
                create_new_file()
                # Crates a validation step for the 'search' function.
                user_answer5 = input('Do you want to search for a keyword in the file? (Yes or No) ')
                # The if stament checks to see if the user is yes
                if user_answer5.lower() == 'yes':
                    #tells the use what to do 
                    print('Only enter one word in the search fuction')
                    # This tells the user to enter the key word 
                    keyword = input('Enter the keyword to search for: ')
                    # Usese the definiton 'Search' to find the keyword entered 
                    user_search('good_record.txt', keyword)
                # The else is trigger if anything besides yes is entered    
                else:
                    # tell the user what the program is doing
                    print('You will now go back the begining of the program')
            # The .lower method forces all characters to be lowercase so that if the user Yes, yes, YES, or any combination of that, it will still works.   
            # The 'elif' stament check to see if the answer is no from the variable 'user_answer'.
            elif user_answer.lower() == 'no':
                # Tell thes user this message if they chose no
                print('Thank you for using my program')
                # Ends the loops
                break
            # this else is trigered if 'Yes' or 'No' is not entered in the variable user_answer
            else:
                # Is printed if the else stement is triggered 
                print('Invalid input. Please answer with either "yes" or "no".')
        #This calls the special charters definition earlier in the program an allows the program to continue                
        except SpecialCharacterError as e:
            # is dispaled if the error is excuted
            print(e, 'You have entered an invalid Character')
            # Tells the program go to the next line 
            continue
        # Checks to see if the maximum character limit is reach
        except LengthError as e:
                   # This is only tirggered if more than 50 characters are entered then Print the error message to tell the user the etere to many characters        
                   print(e, 'You hav entered to many characters ' )
                   # Tells the program go to the next line 
                   continue
# If this script is run directly (instead of being imported), it calls the function 'main()'      
if __name__ == "__main__":
    main()