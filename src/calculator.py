#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
calculator.py

Une application de calculatrice simple utilisant PyQt6 et 
important la logique métier depuis src/utils.py.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# Importation des fonctions de calcul depuis le module utils
try:
    import utils as utils
except ImportError:
    print("Erreur: Impossible de trouver le module 'src/utils.py'.")
    print("Assurez-vous que le fichier utils.py se trouve dans un dossier 'src' "
          "au même niveau que calculator.py.")
    sys.exit(1)


class Calculator(QWidget):
    """
    Classe principale de la calculatrice.
    """
    def __init__(self):
        super().__init__()

        # --- Variables d'état ---
        # La chaîne de caractères du nombre en cours de saisie
        self.current_operand = ""
        # Le premier nombre stocké après qu'une opération est pressée
        self.stored_operand = None
        # La fonction d'opération en attente (ex: utils.add)
        self.pending_operation = None

        self.initUI()
        self.on_clear_click() # Initialiser l'affichage

    def initUI(self):
        """Initialise l'interface utilisateur (GUI)."""
        self.setWindowTitle("Calculatrice")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(5) # Espacement entre les widgets

        # --- Affichage (Display) ---
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", 24))
        self.display.setMinimumHeight(60)
        self.display.setStyleSheet("background-color: #000000; border: 1px solid #ccc;")
        # Ajout à la grille: (widget, row, col, rowspan, colspan)
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        # --- Dictionnaire des boutons ---
        # (texte, row, col, rowspan, colspan)
        buttons = {
            'C': (1, 0, 1, 1), '%': (1, 1, 1, 1), 'DEL': (1, 2, 1, 1), '/': (1, 3, 1, 1),
            '7': (2, 0, 1, 1), '8': (2, 1, 1, 1), '9': (2, 2, 1, 1), '*': (2, 3, 1, 1),
            '4': (3, 0, 1, 1), '5': (3, 1, 1, 1), '6': (3, 2, 1, 1), '-': (3, 3, 1, 1),
            '1': (4, 0, 1, 1), '2': (4, 1, 1, 1), '3': (4, 2, 1, 1), '+': (4, 3, 1, 1),
            '0': (5, 0, 1, 2), '.': (5, 2, 1, 1), '=': (5, 3, 1, 1),
        }

        # Styles CSS pour les boutons
        style_sheet = """
            QPushButton {
                font-size: 18px;
                font-weight: bold;
                padding: 15px 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: #fafafa;
                color: #333; /* <-- CORRECTION ICI */
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
            QPushButton[data-op="op"] {
                background-color: #f0ad4e;
                color: white;
            }
            QPushButton[data-op="op"]:pressed {
                background-color: #ec971f;
            }
            QPushButton[data-op="eq"] {
                background-color: #5cb85c;
                color: white;
            }
            QPushButton[data-op="eq"]:pressed {
                background-color: #449d44;
            }
            QPushButton[data-op="clear"] {
                background-color: #d9534f;
                color: white;
            }
            QPushButton[data-op="clear"]:pressed {
                background-color: #c9302c;
            }
        """
        self.setStyleSheet(style_sheet)

        # --- Création et connexion des boutons ---
        for text, pos in buttons.items():
            button = QPushButton(text)
            
            # Appliquer les styles CSS personnalisés
            if text in ['+', '-', '*', '/']:
                button.setProperty("data-op", "op")
            elif text == '=':
                button.setProperty("data-op", "eq")
            elif text in ['C', 'DEL']:
                button.setProperty("data-op", "clear")

            # Connexion des signaux (clics) aux slots (méthodes)
            if text.isdigit():
                button.clicked.connect(self.on_digit_click)
            elif text == '.':
                button.clicked.connect(self.on_dot_click)
            elif text in ['+', '-', '*', '/']:
                button.clicked.connect(self.on_operation_click)
            elif text == '=':
                button.clicked.connect(self.on_equals_click)
            elif text == 'C':
                button.clicked.connect(self.on_clear_click)
            elif text == 'DEL':
                button.clicked.connect(self.on_delete_click)
            elif text == '%':
                # Note: % n'était pas demandé, mais est commun.
                # Nous le connectons à une opération pour l'exemple.
                # Si vous ne le voulez pas, supprimez-le du dict 'buttons'.
                pass 

            self.layout.addWidget(button, pos[0], pos[1], pos[2], pos[3])

    # --- Slots (Méthodes de gestion des événements) ---

    def on_digit_click(self):
        """Appelé lors du clic sur un chiffre."""
        button = self.sender()
        digit = button.text()
        
        # Si le résultat précédent est affiché, on commence un nouveau nombre
        if self.pending_operation is None and self.stored_operand is None and self.current_operand == self.display.text():
             # Cas spécial : après un '='
             pass
        
        self.current_operand += digit
        self.display.setText(self.current_operand)

    def on_dot_click(self):
        """Appelé lors du clic sur le point décimal."""
        if '.' not in self.current_operand:
            # Ajoute '0.' si on tape '.' en premier
            self.current_operand += '.' if self.current_operand else '0.'
            self.display.setText(self.current_operand)

    def on_delete_click(self):
        """Appelé lors du clic sur 'DEL' (retour arrière)."""
        if self.current_operand:
            self.current_operand = self.current_operand[:-1] # Enlève le dernier caractère
            self.display.setText(self.current_operand if self.current_operand else "0")

    def on_clear_click(self):
        """Réinitialise l'état de la calculatrice."""
        self.current_operand = ""
        self.stored_operand = None
        self.pending_operation = None
        self.display.setText("0")

    def on_operation_click(self):
        """Appelé lors du clic sur +, -, *, /."""
        button = self.sender()
        op_symbol = button.text()

        # S'il y a déjà une opération en attente, on la calcule d'abord
        # (Ex: 5 + 5 + ... )
        if self.pending_operation and self.current_operand:
            self.on_equals_click()

        try:
            # Stocker l'opérande actuel (ou le résultat précédent)
            # On utilise self.display.text() au cas où l'utilisateur
            # appuie sur une op juste après un '='
            current_value_str = self.current_operand if self.current_operand else self.display.text()
            self.stored_operand = float(current_value_str)
        except ValueError:
            self.display.setText("Erreur Format")
            self.on_clear_click()
            return

        # Assigner la fonction utilitaire correspondante
        if op_symbol == '+':
            self.pending_operation = utils.add
        elif op_symbol == '-':
            self.pending_operation = utils.subtract
        elif op_symbol == '*':
            self.pending_operation = utils.multiply
        elif op_symbol == '/':
            self.pending_operation = utils.divide

        # Réinitialiser l'opérande actuel pour la prochaine saisie
        self.current_operand = ""
        # L'affichage montre l'opérande stocké en attendant
        self.display.setText(self.format_result(self.stored_operand))


    def on_equals_click(self):
        """Appelé lors du clic sur '='. Effectue le calcul final."""
        
        # On ne peut calculer que si on a :
        # 1. Un opérande stocké (ex: 5)
        # 2. Une opération en attente (ex: +)
        # 3. Un nouvel opérande en cours (ex: 3)
        if not self.pending_operation or not self.current_operand:
            return

        try:
            operand2 = float(self.current_operand)

            # Appel de la fonction stockée (add, subtract, etc.)
            resultat = self.pending_operation(self.stored_operand, operand2)

            result_str = self.format_result(resultat)
            self.display.setText(result_str)
            
            # Le résultat devient le nouvel "opérande courant"
            # mais pas encore "stocké"
            self.current_operand = result_str


        except ZeroDivisionError:
            self.display.setText("Erreur: Div 0")
        except (ValueError, TypeError) as e:
            # Capture l'erreur de utils.multiply ou un mauvais format
            self.display.setText(f"Erreur: {e}")
        finally:
            # Réinitialise l'état d'opération après le calcul
            self.stored_operand = None
            self.pending_operation = None

    def format_result(self, number):
        """Formate le résultat pour enlever le '.0' si c'est un entier."""
        if number == int(number):
            return str(int(number))
        else:
            # Limiter à un nombre raisonnable de décimales pour l'affichage
            return f"{number:.10g}"


def main():
    """Fonction principale pour lancer l'application."""
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()