def calculate_bmi(height, weight):
    # Convert height from centimeters to meters
    height_meters = height / 100

    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
