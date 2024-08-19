from models.department_analysis import DepartmentAnalysis
from models.performance_analysis import PerformanceAnalysis
from db.db_connection import connect_to_db
import pandas as pd

if __name__ == "__main__":
    results = connect_to_db()
    df = pd.DataFrame(results)

    department_analysis = DepartmentAnalysis(df)
    department_analysis.calculate_department_statistics()
    department_analysis.plot_performance_histogram()

    performance_analysis = PerformanceAnalysis(df)
    performance_analysis.calculate_performance_correlation()
    performance_analysis.calculate_salary_correlation()
    performance_analysis.plot_years_vs_performance()
    performance_analysis.plot_salary_vs_performance()