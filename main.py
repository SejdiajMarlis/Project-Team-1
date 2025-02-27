
#Project topic - Hospital Patient Management System
import csv
import pandas as pd
import time
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Patient(Person):
    def __init__(self, patient_id, name, age, condition, severity_level, logical_expr):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.condition = condition
        self.severity_level = severity_level  # Numeric field for primary sorting
        self.logical_expr = logical_expr     # Logical field for secondary sorting
        
class SortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, patients):
        pass
        
class BubbleSort(SortingAlgorithm):
    def sort(self, patients):
        n = len(patients)
        for i in range(n):
            for j in range(0, n-i-1):
                if patients[j].severity_level < patients[j+1].severity_level:
                    patients[j], patients[j+1] = patients[j+1], patients[j]
        return patients

class MergeSort(SortingAlgorithm):
    def sort(self, patients):
        if len(patients) > 1:
            mid = len(patients) // 2
            left_half = patients[:mid]
            right_half = patients[mid:]

            self.sort(left_half)
            self.sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i].severity_level >= right_half[j].severity_level:
                    patients[k] = left_half[i]
                    i += 1
                else:
                    patients[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                patients[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                patients[k] = right_half[j]
                j += 1
                k += 1
        return patients

class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
        self.severity_to_logic = {
            range(1, 4): "p and not q",     # Low severity (1-3)
            range(4, 7): "not p or q",      # Medium severity (4-6)
            range(7, 9): "p and (q or r)",  # High severity (7-8)
            range(9, 11): "p and r"         # Critical severity (9-10)
        }

    def add_patient(self):
        patient_id = input("Enter Patient ID: ").strip().lower()
        if patient_id in self.patients:
            print("Patient ID already exists. Use the edit option to modify patient details.")
            return
        name = input("Enter Patient Name: ").strip()
        age = int(input("Enter Patient Age: ").strip())
        condition = input("Enter Medical Condition/Disease (e.g., flu, broken arm, pneumonia): ").strip()

        while True:
            try:
                severity_level = float(input("Enter Severity Level (1-10, where 1 is least severe and 10 is most severe): ").strip())
                if 1 <= severity_level <= 10:
                    break
                print("Please enter a number between 1 and 10")
            except ValueError:
                print("Please enter a valid number")
            
        logical_expr = "p"  # default
        for severity_range, expr in self.severity_to_logic.items():
            if int(severity_level) in severity_range:
                logical_expr = expr
                break

        self.patients[patient_id] = Patient(patient_id, name, age, condition, severity_level, logical_expr)
        print(f"\nPatient added with {condition} severity classification")

    def edit_patient(self):
        patient_id = input("Enter Patient ID to edit: ").strip().lower()
        if patient_id not in self.patients:
            print("Patient ID not found.")
            return
        patient = self.patients[patient_id]
        print(f"Editing details for Patient ID: {patient_id}, Current details: Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}, Severity: {patient.severity_level}, Logical Expression: {patient.logical_expr}")

        name = input("Enter new Patient Name (leave blank to keep current): ").strip() or patient.name
        age = input("Enter new Patient Age (leave blank to keep current): ").strip()
        age = int(age) if age else patient.age
        condition = input("Enter new Medical Condition/Disease (e.g., flu, covid, pneumonia, leave blank to keep current): ").strip() or patient.condition

        while True:
            severity_input = input("Enter new Severity Level (1-10, where 1 is least severe and 10 is most severe, leave blank to keep current): ").strip() or str(patient.severity_level)
            if not severity_input:
                severity_level = patient.severity_level
                break
            try:
                severity_level = float(severity_input)
                if 1 <= severity_level <= 10:
                    break
                print("Please enter a number between 1 and 10")
            except ValueError:
                print("Please enter a valid number")

        logical_expr = "p"  # default
        for severity_range, expr in self.severity_to_logic.items():
            if int(severity_level) in severity_range:
                logical_expr = expr
                break
        self.patients[patient_id] = Patient(patient_id, name, age, condition, severity_level, logical_expr)
        print("Patient details updated successfully.")

    def display_patients(self):
        print("\nCurrent Patients in the System:")
        for patient in self.patients.values():
            print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}, Severity: {patient.severity_level}, Logical Expression: {patient.logical_expr}")

    def evaluate_logical_expr(self, expr):
        variables = {"p": True, "q": False, "r": True, "s": False}  # Example truth values
        try:
            return eval(expr, {}, variables)
        except Exception as e:
            print(f"Error in logical expression '{expr}': {e}")
            return False

    def sort_patients(self, algorithm):
        patients_list = list(self.patients.values())
        start_time = time.time()
        sorted_patients = algorithm.sort(patients_list.copy())
        end_time = time.time()
        print(f"Sorting completed in {end_time - start_time:.6f} seconds.")
        print("\nSorted Patients:")
        for patient in sorted_patients:
            print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}, Severity: {patient.severity_level}, Logical Expression: {patient.logical_expr}")

    def search_patient(self, patient_id):
        patient_id = patient_id.strip().lower()
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            print(f"Found Patient - ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}, Severity: {patient.severity_level}, Logical Expression: {patient.logical_expr}")
        else:
            print("Patient not found.")

    def load_from_csv(self, file_name):
        try:
            df = pd.read_csv(file_name)
            for _, row in df.iterrows():
                patient_id = row['PatientID'].strip().lower()
                severity_level = float(row['SeverityLevel'])
                logical_expr = "p"  # default
                for severity_range, expr in self.severity_to_logic.items():
                    if int(severity_level) in severity_range:
                        logical_expr = expr
                        break
                self.patients[patient_id] = Patient(
                    patient_id,
                    row['Name'].strip(),
                    int(row['Age']),
                    row['Condition'].strip(),
                    severity_level,
                    logical_expr
                )
            print("Patients loaded successfully from CSV.")
        except Exception as e:
            print(f"Error reading CSV: {e}")

    def save_to_csv(self, file_name):
        try:
            file_name = file_name or "hospital_patients.csv"
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['PatientID', 'Name', 'Age', 'Condition', 'SeverityLevel', 'LogicalExpression'])
                for patient in self.patients.values():
                    writer.writerow([patient.patient_id, patient.name, patient.age, patient.condition, patient.severity_level, patient.logical_expr])
            print(f"Patients saved successfully to {file_name}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")

def main():
    system = HospitalManagementSystem()
    bubble_sort = BubbleSort()
    merge_sort = MergeSort()
    while True:
        print("\n--- Hospital Patient Management System ---")
        print("1. Add Patient")
        print("2. Edit Patient")
        print("3. Display Patients")
        print("4. Sort Patients (Bubble Sort)")
        print("5. Sort Patients (Merge Sort)")
        print("6. Search Patient")
        print("7. Load Patients from CSV")
        print("8. Save Patients to CSV")
        print("9. Exit")
        choice = input("Enter your choice: ").strip().lower()
        if choice == '1':
            system.add_patient()
        elif choice == '2':
            system.edit_patient()
        elif choice == '3':
            system.display_patients()
        elif choice == '4':
            system.sort_patients(bubble_sort)
        elif choice == '5':
            system.sort_patients(merge_sort)
        elif choice == '6':
            patient_id = input("Enter Patient ID to search: ")
            system.search_patient(patient_id)
        elif choice == '7':
            file_name = input("Enter CSV file name to load: (Press Enter to use the default file): ").strip() or "hospital_patients.csv"
            system.load_from_csv(file_name)
        elif choice == '8':
            file_name = input("Press Enter to save to hospital_patients.csv or enter a different filename: ").strip()
            system.save_to_csv(file_name)
        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
