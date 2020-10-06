"""
Simple GUI that launches jupyter notebooks about ML
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class MachineLearningPortal(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        button1 = toga.Button('Linear Regression', style=Pack(height=20, padding=13))
        button2 = toga.Button('Logistic Regression', style=Pack(height=20, padding=13))
        button3 = toga.Button('Bayesian Classification', style=Pack(height=20, padding=13))
        button4 = toga.Button('Decision Tree', style=Pack(height=20, padding=13))
        button5 = toga.Button('Random Forest', style=Pack(height=20, padding=13))
        button6 = toga.Button('Cluster Analysis', style=Pack(height=20, padding=13))
        button7 = toga.Button('Fuzzy Data Matching', style=Pack(height=20, padding=13))
        button8 = toga.Button('Multi-Layer Neural Networks', style=Pack(height=20, padding=13))
        button9 = toga.Button('Optimization with Linear Programming', style=Pack(height=20, padding=13))
        button10 = toga.Button('Massively Parallel Programming with Spark', style=Pack(height=20, padding=13))

        main_box.add(button1, button2, button3, button4, button5)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return MachineLearningPortal()
