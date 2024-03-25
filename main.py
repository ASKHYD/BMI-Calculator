from bmi_utils import calculate_bmi, categorize_bmi
from data_handler import save_bmi_record, load_bmi_records

def main():
    height = float(input("Enter your height in centimeters: "))
    weight = float(input("Enter your weight in kilograms: "))

    bmi = calculate_bmi(height, weight)
    category = categorize_bmi(bmi)

    print(f"Your BMI is: {bmi}")
    print(f"You are in the '{category}' category.")

    save_option = input("Do you want to save this record? (yes/no): ").lower()
    if save_option == 'yes':
        save_bmi_record(height, weight, bmi, category)
        print("Record saved successfully.")

    load_option = input("Do you want to load previous records? (yes/no): ").lower()
    if load_option == 'yes':
        records = load_bmi_records()
        print("\nPrevious BMI Records:")
        for record in records:
            print(f"Height: {record['height']} cm, Weight: {record['weight']} kg, BMI: {record['bmi']}, Category: {record['category']}")

if __name__ == "__main__":
    main()
