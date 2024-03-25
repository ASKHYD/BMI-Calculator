def save_bmi_record(height, weight, bmi, category):
    with open('bmi_records.txt', 'a') as file:
        file.write(f"{height},{weight},{bmi},{category}\n")

def load_bmi_records():
    records = []
    with open('bmi_records.txt', 'r') as file:
        for line in file:
            record = line.strip().split(',')
            records.append({
                'height': float(record[0]),
                'weight': float(record[1]),
                'bmi': float(record[2]),
                'category': record[3]
            })
    return records
