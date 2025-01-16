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
        # Map severity levels to logical expressions
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

        # Get severity level from 1-10
        while True:
            try:
                severity_level = float(input("Enter Severity Level (1-10, where 1 is least severe and 10 is most severe): ").strip())
                if 1 <= severity_level <= 10:
                    break
                print("Please enter a number between 1 and 10")
            except ValueError:
                print("Please enter a valid number")
            
        # Determine logical expression based on severity level
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
# Determine logical expression based on severity level
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
            sorted_patients = algorithm.sort(patients_list.copy())  # Create a copy for sorting
            end_time = time.time()

            print(f"Sorting completed in {end_time - start_time:.6f} seconds.")
            print("\nSorted Patients:")
            for patient in sorted_patients:
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}, Severity: {patient.severity_level}, Logical Expression: {patient.logical_expr}")