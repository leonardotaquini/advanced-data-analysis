import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from db.db_connection import connect_to_db


def main():
    results = connect_to_db()
    df = pd.DataFrame(results)
    
    # Calculo las siguientes estadísticas para cada departamento:
    departamento_stats = df.groupby('department').agg({
        'performance_score': ['mean', 'median', 'std'],
        'salary': ['mean', 'median', 'std'],
        'employee_id': 'count' 
    }).reset_index()

    # Renombro las columnas
    departamento_stats.columns = ['department', 
                                  'performance_score_mean', 'performance_score_median', 'performance_score_std',
                                  'salary_mean', 'salary_median', 'salary_std',
                                  'total_employees']

    print(departamento_stats)

    # Cálculo de correlación entre years_with_company y performance_score
    correlacion_years_performance = df[['years_with_company', 'performance_score']].corr().iloc[0,1]
    print()
    print(f'Correlación entre years_with_company y performance_score: {correlacion_years_performance}')

    # Cálculo de correlación entre salary y performance_score
    correlacion_salary_performance = df[['salary', 'performance_score']].corr().iloc[0,1]
    print()
    print(f'Correlación entre salary y performance_score: {correlacion_salary_performance}')
    
    # Histograma del performance_score para cada departamento
    departments = df['department'].unique()
    plt.figure(figsize=(6, 8))

    for department in departments:
        subset = df[df['department'] == department]
        plt.hist(subset['performance_score'], alpha=0.5, label=department)

    plt.title('Histograma del performance_score por departamento')
    plt.xlabel('Performance Score')
    plt.ylabel('Frecuencia')
    plt.legend(title='Departamento')
    plt.show()

    # Gráfico de dispersion de years_with_company - performance_score
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='years_with_company', y='performance_score', hue='department', palette='viridis')
    plt.title('Years with Company vs. Performance Score')
    plt.xlabel('Years with Company')
    plt.ylabel('Performance Score')
    plt.legend(title='Departamento')
    plt.show()

    # Gráfico de dispersion de salary - performance_score
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='salary', y='performance_score', hue='department', palette='viridis')
    plt.title('Salary vs. Performance Score')
    plt.xlabel('Salary')
    plt.ylabel('Performance Score')
    plt.legend(title='Departamento')
    plt.show()


if __name__ == "__main__":
    main()