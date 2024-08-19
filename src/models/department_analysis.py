import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from db.db_connection import connect_to_db
from models.analysis import Analysis

class DepartmentAnalysis(Analysis):
    def __init__(self, df):
        super().__init__(df)
        self.__departamento_stats = None

    def calculate_department_statistics(self):
        metrics = {
            'performance_score': ['mean', 'median', 'std'],
            'salary': ['mean', 'median', 'std'],
            'employee_id': 'count'
        }
        self.__departamento_stats = self.calculate_statistics('department', metrics)
        self.__departamento_stats.columns = ['department',
                                             'performance_score_mean', 'performance_score_median', 'performance_score_std',
                                             'salary_mean', 'salary_median', 'salary_std',
                                             'total_employees']
        print(self.__departamento_stats)

    def plot_performance_histogram(self):
        departments = self.df['department'].unique()
        plt.figure(figsize=(6, 8))

        for department in departments:
            subset = self.df[self.df['department'] == department]
            plt.hist(subset['performance_score'], alpha=0.5, label=department)

        plt.title('Histograma del performance_score por departamento')
        plt.xlabel('Performance Score')
        plt.ylabel('Frecuencia')
        plt.legend(title='Departamento')
        plt.show()

