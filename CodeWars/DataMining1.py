class Datamining:

    def __init__(self, train_set):
        x_mean = sum([x[0] for x in train_set]) / len(train_set)
        y_mean = sum([x[1] for x in train_set]) / len(train_set)
        numerator = 0
        denominator = 0
        for i in range(len(train_set)):
            numerator += (train_set[i][0] - x_mean) * (train_set[i][1] - y_mean)
            denominator += (train_set[i][0] - x_mean) ** 2
        self.slope = numerator / denominator
        self.intercept = y_mean - self.slope * x_mean

    def predict(self, x):
        return self.slope * x + self.intercept


example_train_set = [(0, 1), (2, 2), (4, 3), (9, 8), (3, 5)]

dm = Datamining(example_train_set)
