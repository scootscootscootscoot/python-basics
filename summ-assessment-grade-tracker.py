## FUNCTION SPACE

def calculate_letter_grade(score):  ##function that calculates grade given the user input for score using if statements
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def print_student_summary(name, score, letter_grade): ##Function to output student name, score, and letter grade which we will define in main function
   
    print(f"Student: {name}")
    print(f"Score: {score}")
    print(f"Letter Grade: {letter_grade}")
    print("-" * 25)

def main(): ##this is the main function that rins the program and contains the while loop that allows user to input multiple grades
    
    students = [] ## This is the list that the data collected will be input to 
    

    ## Display welcome message and instructions to enter info or Q to quit
    print("Welcome to the Student Grade Tracker!")
    print("Enter student information (press 'q' for name to quit)")
    print("=" * 50)
    
    # While loop to allow multiple entries and run the functions we call until user quits
    while True:
        # First input prompt for student name, stores as variable "name". Strip function added to remove spaces and prevent errors
        name = input("\nEnter student's name (or 'q' to quit): ").strip()
        
        # Check if user wants to quit. Lower function included to allow user to press q or Q
        if name.lower() == 'q':
            break
        
        # String manipulation - capitalize the name properly using "title" function which caps the first character of each word EX: "scott cahill" -->> "Scott Cahill"
        name = name.title()
        
        # Input validation for score, make sure 0-100
        while True:
            try:
                # prompt user for score, store as var "score_input" and convert string input to float "score"
                score_input = input(f"Enter {name}'s score (0-100): ").strip()
                score = float(score_input)
                
                # Validate score range to make sure within a gradable range for our calculator function
                if 0 <= score <= 100:
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError: ## this is to ensure someone doesnt enter a string for the score input or some other value that wouldnt be appropriate
                print("Please enter a valid number.")
        
        # Calculate letter grade using function calculate_letter_grade and the score float the user provided
        letter_grade = calculate_letter_grade(score)
        
        # Store student record we collected "student_record" as a dictionary in the list
        student_record = {
            'name': name,
            'score': score,
            'letter_grade': letter_grade
        }
        students.append(student_record)
        
        print(f"\nAdded: {name} - Score: {score} - Grade: {letter_grade}") ##Prints the data weve collected and the grade a line below the input lines
    
    # Check if any students were entered prior to q, if not return and display goodbye message
    if not students:
        print("\nNo students were entered. Goodbye!")
        return
    
    # Display all student information using for loop
    print("\n" + "=" * 50)
    print("FINAL STUDENT GRADE SUMMARY")
    print("=" * 50)
    
    # For loop to print all students' information using out "print_student_summary" function
    for student in students:
        print_student_summary(student['name'], student['score'], student['letter_grade'])
    
    # Calculate and display class statistics using different variables
    total_students = len(students) ## This returns the number of items in our students list so we can show an accurate total student 

    ## this calculates the average grade by using sum funtion to add up all scores then dividing by the total student number we grabbed earlier
    total_score = sum(student['score'] for student in students)
    average_score = total_score / total_students
    average_grade = calculate_letter_grade(average_score) ## we call our calculation function to find the letter grade based on the average score we just got
    
    ##This prints the class statistics we just calculated below the summary of each student
    print(f"Class Statistics:")
    print(f"Total Students: {total_students}")
    print(f"Class Average: {average_score:.2f} ({average_grade})")
    print("=" * 50)
    
    # Write data to grades.txt file using file I/O
    try: ##error handling portion in case a txt file cant be created
        with open('grades.txt', 'w') as file: ##opens a txt file with write priveleges 
            file.write("STUDENT GRADE REPORT\n")
            file.write("=" * 50 + "\n")
            
        
            # Write each student's name, score, and letter grade to the txt file using for loop to run all students
            for student in students:
                file.write(f"Name: {student['name']}\n")
                file.write(f"Score: {student['score']}\n")
                file.write(f"Letter Grade: {student['letter_grade']}\n")
                file.write("-" * 25 + "\n")
            
            # Write class statistics after each student record written
            file.write(f"\nCLASS STATISTICS\n")
            file.write(f"Total Students: {total_students}\n")
            file.write(f"Class Average: {average_score:.2f} ({average_grade})\n")
        
        print(f"\nGrade report successfully saved to 'grades.txt'!") ##Message to indicate the report has been generated successfully
        
    except IOError:
        print("\nError: Could not save data to file.")

# Run the main function that runs our program
if __name__ == "__main__":
    main()