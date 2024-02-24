from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QMessageBox, QHBoxLayout, QVBoxLayout

app = QApplication([])
win = QWidget()


win.setWindowTitle('Роблакс')
win.resize(400, 200)

question = QLabel('В якому році сказали урааа роблакс?')
option1 = QRadioButton('1999')
option2 = QRadioButton('1939')
option3 = QRadioButton('1939 до н.е.')
option4 = QRadioButton('2020')

layout_main =QVBoxLayout()
layout_main.addWidget(question, alignment = Qt.AlignCenter )

layout_H1 = QHBoxLayout()
layout_H1.addWidget(option1, alignment=Qt.AlignCenter)
layout_H1.addWidget(option2, alignment=Qt.AlignCenter)

layout_H2 = QHBoxLayout()
layout_H2.addWidget(option3, alignment=Qt.AlignCenter)
layout_H2.addWidget(option4, alignment=Qt.AlignCenter)

layout_main.addLayout(layout_H1)
layout_main.addLayout(layout_H2)

win.setLayout(layout_main)

def show_win():
    win_win = QMessageBox()
    win_win.setText('Правильно! (введіть номер карточки щоб продовжити)')
    win_win.exec_()
def show_lose():
    lose_win = QMessageBox()
    lose_win.setText('З вашої карточки знято 1000$')
    lose_win.exec_()

option1.clicked.connect(show_lose)
option2.clicked.connect(show_lose)
option3.clicked.connect(show_lose)
option4.clicked.connect(show_win)
win.show()
app.exec_()

