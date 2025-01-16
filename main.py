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