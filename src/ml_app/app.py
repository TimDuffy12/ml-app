"""
Simple GUI that launches jupyter notebooks about ML
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import subprocess


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


        scroll_box = toga.Box(children=[], style=Pack(direction=COLUMN, padding=10, flex=1))

        scroll_box.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)

        scroll_box.add(openJupyterButton, closeJupyterButton)

        scroll_view = toga.ScrollContainer(content=scroll_box, style=Pack(padding=10))



        main_box.add(scroll_view)
        #main_box.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)


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
