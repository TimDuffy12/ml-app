"""
Simple GUI that launches jupyter notebooks about ML
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import subprocess
import os
from functools import partial

class MachineLearningPortal(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        openJupyterButton = toga.Button('Turn on Jupyter', style=Pack(height=20, padding=13), on_press=self.openJupyterNotebook)
        closeJupyterButton = toga.Button('Close on Jupyter', style=Pack(height=20, padding=13), on_press=self.closeJupyterNotebook)

        button1 = toga.Button('Linear Regression', style=Pack(height=20, padding=13), on_press=self.LinearRegression)
        button2 = toga.Button('Logistic Regression', style=Pack(height=20, padding=13), on_press=self.LogisticRegression)
        button3 = toga.Button('Bayesian Classification', style=Pack(height=20, padding=13), on_press=self.BayesianClassification)
        button4 = toga.Button('Decision Tree', style=Pack(height=20, padding=13), on_press=self.DecisionTree)
        button5 = toga.Button('Random Forest', style=Pack(height=20, padding=13), on_press=self.RandomForest)
        button6 = toga.Button('Cluster Analysis', style=Pack(height=20, padding=13), on_press=self.ClusterAnalysis)
        button7 = toga.Button('Fuzzy Data Matching', style=Pack(height=20, padding=13), on_press=self.FuzzyDataMatching)
        button8 = toga.Button('Multi-Layer Neural Networks', style=Pack(height=20, padding=13), on_press=self.MultiLayerNeuralNetworks)
        button9 = toga.Button('Optimization with Linear Programming', style=Pack(height=20, padding=13), on_press=self.OptimizationWithLinearProgramming)
        button10 = toga.Button('Massively Parallel Programming with Spark', style=Pack(height=20, padding=13), on_press=self.MassivelyParallelProgrammingWithSpark)
        button11 = toga.Button('Change Data Set', style=Pack(height=20, padding=13), on_press=self.changeDataset)
        scroll_box = toga.Box(children=[], style=Pack(direction=COLUMN, padding=10, flex=1))
        scroll_box.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
        scroll_box.add(openJupyterButton, closeJupyterButton)
        scroll_view = toga.ScrollContainer(content=scroll_box, style=Pack(padding=10))



        main_box.add(scroll_view)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def handle_dataset_selection(self, widget, data):
        #self.data = pd.read_csv(data)
        print(data)

    def changeDataset(self, widget):
        main_box = toga.Box(style=Pack(direction=COLUMN))
        #TODO: WE should make this a list of buttons
        dataFiles = [
            (i, i.split(".")[0].replace("_", " "))
            for i in os.listdir('./Data')
        ]

        self.left_container = toga.Box(style=Pack(direction=COLUMN, padding_top=50))

        for i in dataFiles:
            tmpbutton = toga.Button(i[1], style=Pack(width=100, height=25), on_press=partial(self.handle_dataset_selection,data=i[0]))
            self.left_container.add(tmpbutton)

        #TODO: we should change this is a datatable and have it show the data from the file selected
        right_content = toga.Box(
            style=Pack(direction=COLUMN, padding_top=50, flex= 5)
        )



        right_container = toga.ScrollContainer(horizontal=False)

        right_container.content = right_content

        split = toga.SplitContainer()

        split.content = [self.left_container, right_container]

        main_box.add(split)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    #Functions for when any button is pressed
    def LinearRegression(self, widget):
        print("Linear Regression button has been pressed")
    def LogisticRegression(self, widget):
        print("Logistic Regression button has been pressed")
    def BayesianClassification(self, widget):
        print("Bayesian Classification button has been pressed")
    def DecisionTree(self, widget):
        print("Decision Tree has been pressed")
    def RandomForest(self, widget):
        print("Random Forest button has been pressed")
    def ClusterAnalysis(self, widget):
        print("Cluster Analysis button has been pressed")
    def FuzzyDataMatching(self, widget):
        print("Fuzzy Data Matching button has been pressed")
    def MultiLayerNeuralNetworks(self, widget):
        print("Multi-Layer Neural Networks has been pressed")
    def OptimizationWithLinearProgramming(self, widget):
        print("Optimization with Linear Programming button has been pressed")
    def MassivelyParallelProgrammingWithSpark(self, widget):
        print("Massively Parallel Programming with Spark button has been pressed")

    def openJupyterNotebook(self, widget):
        subprocess.Popen('jupyter notebook --no-browser', shell=True)
    def closeJupyterNotebook(self, widget):
        subprocess.Popen('jupyter notebook stop', shell=True)

def main():
    return MachineLearningPortal()
