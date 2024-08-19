class Analysis:
    def __init__(self, df):
        self.df = df

    def calculate_statistics(self, group_by, metrics):
        stats = self.df.groupby(group_by).agg(metrics).reset_index()
        return stats