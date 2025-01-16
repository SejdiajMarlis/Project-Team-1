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
