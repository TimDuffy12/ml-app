"""
Simple GUI that launches jupyter notebooks about ML
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import subprocess
import os
import webbrowser  



#For the data screen
import csv
from functools import partial


class MachineLearningPortal(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        ## Define all the images for the new buttons,
        ## From a quick search this seems harder than it is worth as a grade
        """
        Linear_Regression_Image="Images/Linear_Regression"
        Logistic_Regression_Image="Images/Logistic_Regression"
        Bayesian_Classification_Image="Images/Bayesian_Classification"
        Decision_Tree_Image="Images/Decision_Tree"
        Random_Forest_Image="Images/Random_Forest"
        Cluster_Analysis_Image="Images/Cluster_Analysis"
        Fuzzy_Data_Matching_Image="Images/Fuzzy_Data_Matching"
        Multi-Layer_Neural_Networks_Image="Images/Multi-Layer_Neural_Networks"
        Optimization_with_Linear_Programming_Image="Images/Optimization_with_Linear_Programming"
        Massively_Parallel_Programming_with_Spark_Image="Images/Massively_Parallel_Programming_with_Spark"
        """

        self.startJupyterNotebook(self)

        main_box = toga.Box()
        scroll_box = toga.Box(children=[], style=Pack(direction=COLUMN, padding=10, flex=1, text_align=CENTER))

        
        group1Title = toga.Label('Linear Regression')
        def b1callback(button):
            self.openNotebook(self, "Regressions with charts.ipynb")
            pass
        button1 = toga.Button('Regression With Charts', style=Pack(height=20, padding=13), on_press=b1callback)
        def b2callback(button):
            self.openNotebook(self, "Non Linear Regression.ipynb")
            pass
        button2 = toga.Button('Non-Linear Regression', style=Pack(height=20, padding=13), on_press=b2callback)
        scroll_box.add(group1Title, button1, button2)

        group2Title = toga.Label('Classification')
        def b3callback(button):
            self.openNotebook(self, "Logistic Regression.ipynb")
            pass
        button3 = toga.Button('Logistic Regression', style=Pack(height=20, padding=13), on_press=b3callback)
        def b4callback(button):
            self.openNotebook(self, "Decision Tree Random Forest.ipynb")
            pass
        button4 = toga.Button('Decision Tree and Random Forest', style=Pack(height=20, padding=13), on_press=b4callback)
        def b5callback(button):
            self.openNotebook(self, "Naive Bayes.ipynb")
            pass
        button5 = toga.Button('Bayesian Classification', style=Pack(height=20, padding=13), on_press=b5callback)
        scroll_box.add(group2Title, button3, button4, button5)

        group3Title = toga.Label('K-Means Clustering')
        def b6callback(button):
            self.openNotebook(self, "K-Mean-Clustering-Final-WithLib.ipynb")
            pass
        button6 = toga.Button('Cluster Analysis', style=Pack(height=20, padding=13), on_press=b6callback)
        scroll_box.add(group3Title, button6)


        group4Title = toga.Label('Linear Programming Optimization')
        def b7callback(button):
            self.openNotebook(self, "Linear Programming.ipynb")
            pass
        button7 = toga.Button('Optimization with Linear Programming', style=Pack(height=20, padding=13), on_press=b7callback)
        scroll_box.add( group4Title, button7)


        group5Title = toga.Label('Fuzzy Matching of Data')
        def b8callback(button):
            self.openNotebook(self, "Fuzzy Matching of data.ipynb")
            pass
        button8 = toga.Button('Fuzzy Data Matching', style=Pack(height=20, padding=13), on_press=b8callback)
        scroll_box.add(group5Title, button8)
        

        group6Title = toga.Label('Neural Networking:')
        def b9callback(button):
            self.openNotebook(self, "Neural Network1.ipynb")
            pass
        button9 = toga.Button('Neural Networks 1', style=Pack(height=20, padding=13), on_press=b9callback)
        def b15callback(button):
            self.openNotebook(self, "Neural Network2.ipynb")
            pass
        button15 = toga.Button('Neural Networks 2', style=Pack(height=20, padding=13), on_press=b15callback)
        def b16callback(button):
            self.openNotebook(self, "Neural Network 3.ipynb")
            pass
        button16 = toga.Button('Neural Networks 3', style=Pack(height=20, padding=13), on_press=b16callback)
        scroll_box.add(group6Title, button9, button15, button16)


        group7Title = toga.Label('Spark')
        def b10callback(button):
            self.openNotebook(self, "Using Spark.ipynb")
            pass
        button10 = toga.Button('Massively Parallel Programming with Spark', style=Pack(height=20, padding=13), on_press=b10callback)
        scroll_box.add(group7Title, button10)

        group8Title = toga.Label('Extra')
        openJupyterButton = toga.Button('Turn on Jupyter', style=Pack(height=20, padding=13), on_press=self.startJupyterNotebook)
        closeJupyterButton = toga.Button('Close on Jupyter', style=Pack(height=20, padding=13), on_press=self.closeJupyterNotebook)
        scroll_box.add(group8Title, openJupyterButton, closeJupyterButton)

        scroll_view = toga.ScrollContainer(content=scroll_box, style=Pack(padding=10))
        main_box.add(scroll_view)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    #Functions for when any button is pressed
    def changeTextFile(self, widget, fileName):
        print("Changing the file to ", fileName)
        with open("currentDataSet.txt", 'w') as filetowrite:
            filetowrite.write(fileName)
            filetowrite.close()


    def startJupyterNotebook(self, widget):
        subprocess.Popen('jupyter notebook --no-browser', shell=True)


    def closeJupyterNotebook(self, widget):
        subprocess.Popen('jupyter notebook stop', shell=True)

    def openNotebook(self, widget, fileName):
        fullPath = "/ExampleNotebooks/" +  fileName
        fullPath = fullPath.replace(" ","%20")
        fullPath = fullPath.replace("\\","/")


        fullPath = "http://localhost:8888/notebooks" + fullPath


        webbrowser.open(fullPath, new=0, autoraise=True)

def main():
    return MachineLearningPortal()
