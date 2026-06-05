from abc import ABC , abstractmethod

class MLModel(ABC):

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class LinearRegrassionModel(MLModel):

    def train(self):
        print("Training LinearRegrassionModel")

    def predict(self):
        print("Predict LinearRegrassionModel")

class DecisionTreeModel(MLModel):

    def train(self):
        print("Training DecisionTreeModel")

    def predict(self):
        print("Predict DecisionTreeModel")

l = LinearRegrassionModel()
d = DecisionTreeModel()

l.train()
l.predict()

d.train()
d.predict()
