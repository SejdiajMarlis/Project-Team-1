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