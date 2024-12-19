#Project topic - Hospital Patient Management System

import csv

# File name for the patient data CSV
file_name = "Hospital_Patient_Data.csv"

# Create a new patient record
def create_patient(patient_data):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(patient_data)
    print("Patient record added successfully.")

# Read all patient records
def read_patients():
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Update a patient record by PatientID
def update_patient(patient_id, updated_data):
    rows = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == patient_id:  # Assuming PatientID is the first column
                rows.append(updated_data)
            else:
                rows.append(row)
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Patient record updated successfully.")

# Delete a patient record by PatientID
def delete_patient(patient_id):
    rows = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != patient_id:  # Skip the row to be deleted
                rows.append(row)
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Patient record deleted successfully.")
# Main program loop

# Add a new patient
create_patient(["51", "Jane Doe", "30", "F", "Flu", "2024-12-04", "Rest and hydration"])

# Read all patients
read_patients()

# Update a patient's record
update_patient("51", ["51", "Jane Smith", "31", "F", "Hypertension", "2024-12-04", "Medication and lifestyle changes"])

# Delete a patient's record
delete_patient("51")
# Read all patients after deletion
read_patients()

create_patient(["52", "John Doe", "40", "M", "Pneumonia", "2024-12-05", "Antibiotics and rest"])
search_patient(4, "Pneumonia")  # Search by Diagnosis
# Search for patients based on a specific column and value
def search_patient(column_index, search_value):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        found = False
        print(f"Search Results for '{search_value}':")
        for row in reader:
            if row[column_index] == search_value:
                print(row)
                found = True
        if not found:
            print("No matching records found.")

# Example usage of the search_patient function
# Assuming columns: [PatientID, Name, Age, Gender, Diagnosis, Admission Date, Treatment]
# Search for patients with a specific diagnosis (e.g., "Pneumonia")
search_patient(4, "Pneumonia")
# Search for patients by age
def search_by_age(age):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        found = False
        print(f"Search Results for Age {age}:")
        for row in reader:
            if row[2] == age:  # Assuming Age is the 3rd column
                print(row)
                found = True
        if not found:
            print("No matching records found.")
