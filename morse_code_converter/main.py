import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Morse code dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

class MorseConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Input field
        self.input_label = QLabel('Enter text:')
        self.input_field = QLineEdit()

        # Output field
        self.output_label = QLabel('Morse code:')
        self.output_field = QLabel()
        self.output_field.setStyleSheet('font-size: 16pt')

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.input_field)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_field)
        self.setLayout(vbox)

        # Set style sheet to customize appearance
        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
            QLineEdit, QLabel#output_field {
                font-size: 24px;
                padding: 5px;
                border: 1px solid gray;
                border-radius: 5px;
            }
        """)

        # Connect signal to slot
        self.input_field.textChanged.connect(self.convert)

        # Button to switch conversion direction
        self.btn_switch = QPushButton('Switch direction')
        self.btn_switch.clicked.connect(self.switch_direction)
        vbox.addWidget(self.btn_switch)

        self.direction = 'normal_to_morse'

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Morse Converter')
        self.show()

    def convert(self):
        text = self.input_field.text().upper()
        if self.direction == 'normal_to_morse':
            self.output_field.setText(self.normal_to_morse(text))
        else:
            self.output_field.setText(self.morse_to_normal(text))

    def normal_to_morse(self, text):
        morse = ''
        for char in text:
            if char == ' ':
                morse += ' '
            elif char in MORSE_CODE_DICT:
                morse += MORSE_CODE_DICT[char] + ' '
            else:
                morse += char + ' '
        return morse

    def morse_to_normal(self, text):
        normal = ''
        MORSE_CODE_REVERSE = {v: k for k, v in MORSE_CODE_DICT.items()}
        words = text.split(' / ')
        for word in words:
            chars = word.split(' ')
            for char in chars:
                if char in MORSE_CODE_REVERSE:
                    normal += MORSE_CODE_REVERSE[char]
                else:
                    normal += char
            normal += ' '
        return normal.rstrip()

    def switch_direction(self):
        if self.direction == 'normal_to_morse':
            self.direction = 'morse_to_normal'
            self.input_label.setText('Enter morse code:')
            self.output_label.setText('Normal text:')
        else:
            self.direction = 'normal_to_morse'
            self.input_label.setText('Enter text:')
            self.output_label.setText('Morse code:')
        self.input_field.setText('')
        self.output_field.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = MorseConverter()
    sys.exit(app.exec_())
