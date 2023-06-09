import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QSize, pyqtSignal


class ClickableLabel(QLabel):
    clicked = pyqtSignal(int, int)

    def __init__(self, row, col, parent=None):
        super().__init__(parent)
        self.row = row
        self.col = col

    def mousePressEvent(self, event):
        self.clicked.emit(self.row, self.col)


class MeshWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tic Tac Toe game')
        self.setGeometry(100, 100, 400, 400)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)  # Remove spacing between cells
        self.setLayout(grid_layout)

        self.labels = []
        self.turn = "X"
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        for row in range(3):
            for col in range(3):
                label = ClickableLabel(row, col)
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(
                    "border: 1px solid black; font-size: 36px; font-weight: bold; background-color: white;")
                label.setFixedSize(QSize(133, 133))  # Adjust size of cells
                label.clicked.connect(self.label_clicked)
                grid_layout.addWidget(label, row, col)
                self.labels.append(label)

        self.show()

    def label_clicked(self, row, col):
        label = self.labels[row * 3 + col]
        if label.text() == "":
            label.setText(self.turn)
            self.board[row][col] = self.turn

            if self.check_winner():
                QMessageBox.information(self, "Game Over", f"The End! '{self.turn}' wins!")
                self.reset_game()
            else:
                self.toggle_turn()

    def check_winner(self):
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],  # Top row
            [(1, 0), (1, 1), (1, 2)],  # Middle row
            [(2, 0), (2, 1), (2, 2)],  # Bottom row
            [(0, 0), (1, 0), (2, 0)],  # Left column
            [(0, 1), (1, 1), (2, 1)],  # Middle column
            [(0, 2), (1, 2), (2, 2)],  # Right column
            [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
            [(0, 2), (1, 1), (2, 0)]   # Diagonal from top-right to bottom-left
        ]

        for combination in winning_combinations:
            symbols = [self.board[row][col] for row, col in combination]
            if symbols.count('X') == 3 or symbols.count('O') == 3:
                return True

        return False

    def toggle_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def reset_game(self):
        for label in self.labels:
            label.setText("")
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.turn = "X"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MeshWindow()
    sys.exit(app.exec_())
