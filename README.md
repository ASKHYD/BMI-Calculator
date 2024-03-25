
BMI Calculator Project Description
The BMI Calculator project is a simple yet effective tool developed in Python for calculating the Body Mass Index (BMI) based on user input. BMI is a widely used metric to assess whether a person has a healthy weight relative to their height. This project aims to provide users with a quick and convenient way to calculate their BMI and determine their weight category (Underweight, Normal Weight, Overweight, or Obese).

Functionalities
BMI Calculation: The calculator takes the user's height (in centimeters) and weight (in kilograms) as input and calculates the BMI using the formula BMI = weight / (height^2).

BMI Categorization: After calculating the BMI, the program categorizes the result into different weight categories based on standard BMI ranges. These categories include Underweight (BMI < 18.5), Normal Weight (18.5 <= BMI < 25), Overweight (25 <= BMI < 30), and Obese (BMI >= 30).

Data Handling: The project includes functionality to save BMI records to a text file (bmi_records.txt) and load previous records from the file. This allows users to keep track of their BMI history and monitor changes over time.

How to Use
Clone Repository: Clone or download the repository to your local machine.

Python Installation: Make sure you have Python installed on your machine.

Run the Program: Execute main.py using a Python interpreter.

Input Height and Weight: Follow the on-screen instructions to enter your height (in centimeters) and weight (in kilograms).

View BMI Result: The program will calculate your BMI and display the result along with your weight category.

Save/Load Records: Optionally, you can choose to save the BMI record or load previous records from the text file.

Project Structure
The project is organized into multiple files for modularity and maintainability:

main.py: Contains the main program logic for the BMI Calculator, including user input and interaction.
bmi_utils.py: Includes functions for BMI calculation (calculate_bmi) and categorization (categorize_bmi).
data_handler.py: Manages saving (save_bmi_record) and loading (load_bmi_records) of BMI records to/from a text file.
bmi_records.txt: Text file used to store BMI records.
