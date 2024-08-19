from models.analysis import Analysis

class PerformanceAnalysis(Analysis):
    def calculate_performance_correlation(self):
        correlacion = self.df[['years_with_company', 'performance_score']].corr().iloc[0, 1]
        print(f'Correlación entre years_with_company y performance_score: {correlacion}')

    def calculate_salary_correlation(self):
        correlacion = self.df[['salary', 'performance_score']].corr().iloc[0, 1]
        print(f'Correlación entre salary y performance_score: {correlacion}')

    def plot_salary_vs_performance(self):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x='salary', y='performance_score', hue='department', palette='viridis')
        plt.title('Salary vs. Performance Score')
        plt.xlabel('Salary')
        plt.ylabel('Performance Score')
        plt.legend(title='Departamento')
        plt.show()

    def plot_years_vs_performance(self):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x='years_with_company', y='performance_score', hue='department', palette='viridis')
        plt.title('Years with Company vs. Performance Score')
        plt.xlabel('Years with Company')
        plt.ylabel('Performance Score')
        plt.legend(title='Departamento')
        plt.show()

