#создай приложение для запоминания информации
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from random import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('MemoryCard')

#создаем layouts
main_layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

AnsGroup = QGroupBox("Результат теста")
result_label = QLabel("правильно/неправильно")
right_answer_label = QLabel("Правильный ответ")
statistic_label = QLabel("Здесь будет статистика")
layout7 = QVBoxLayout()
layout7.addWidget(result_label)
layout7.addWidget(right_answer_label, alignment=Qt.AlignHCenter)
layout7.addWidget(statistic_label)
AnsGroup.setLayout(layout7)
AnsGroup.hide()

RadioGroup = QGroupBox("Варианты ответов")
layout4 = QHBoxLayout()
layout5 = QVBoxLayout()
layout6 = QVBoxLayout()

question_label = QLabel("Здесь будет вопрос")
r_btn1 = QRadioButton("Первый вариант")
r_btn2 = QRadioButton("Второй вариант")
r_btn3 = QRadioButton("Третий вариант")
r_btn4 = QRadioButton("Четвертый вариант")

RadioG = QButtonGroup()
RadioG.addButton(r_btn1)
RadioG.addButton(r_btn2)
RadioG.addButton(r_btn3)
RadioG.addButton(r_btn4)


btn_OK = QPushButton("Ответить")

#насаживаем виджеты на лейауты

layout5.addWidget(r_btn1)
layout5.addWidget(r_btn2)
layout6.addWidget(r_btn3)
layout6.addWidget(r_btn4)

layout4.addLayout(layout5)
layout4.addLayout(layout6)

RadioGroup.setLayout(layout4)

layout1.addWidget(question_label, alignment=Qt.AlignHCenter)
layout2.addWidget(RadioGroup)
layout2.addWidget(AnsGroup)
layout3.addWidget(btn_OK)

main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
main_layout.addLayout(layout3)

main_win.setLayout(main_layout)


answers = [r_btn1, r_btn2, r_btn3, r_btn4]

question_list = []

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list.append(Question("Когда начинается школа?", '1 сентября', 'никогда', 'не хочу говорить об этом', '1 января'))
question_list.append(Question("Вопрос2?", '1', '123', 'не хочу говорить об этом', '1 января'))
question_list.append(Question("Вопрос3", '1', '2', 'не хочу говорить об этом', '1 января'))
question_list.append(Question("Вопрос4", '1', '23', 'не хочу говорить об этом', '1 января'))
question_list.append(Question("Вопрос5", '1', '1234', 'не хочу говорить об этом', '1 января'))


main_win.count_right = 0
main_win.count_all = 1


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_label.setText(q.question)
    right_answer_label.setText(q.right_answer)

ask(Question("Когда начинается школа?", '1 сентября', 'никогда', 'не хочу говорить об этом', '1 января'))

def check_answer():
    if answers[0].isChecked():
        result_label.setText("Правильно")
        main_win.count_right += 1
    else:
        result_label.setText("Неправильно")
    btn_OK.setText("Следующий вопрос")
    statistic_label.setText("Статистика правильных ответов в % " + str(round(main_win.count_right/main_win.count_all * 100, 2)))

    RadioGroup.hide()
    AnsGroup.show()

def show_question():
    main_win.count_all += 1
    x = randint(0, len(question_list)-1)
    q1 = question_list[x]
    ask(q1)
    AnsGroup.hide()
    RadioGroup.show()
    btn_OK.setText("Ответить")
    RadioG.setExclusive(False)    
    r_btn1.setChecked(False)
    r_btn2.setChecked(False)
    r_btn3.setChecked(False)
    r_btn4.setChecked(False)
    RadioG.setExclusive(True)
    print("Статистика в % правильных ответов", main_win.count_right/main_win.count_all * 100)

def start_test():
    if btn_OK.text().lower() == "ответить":
        check_answer()
    else:
        show_question()
    

btn_OK.clicked.connect(start_test)

main_win.show()
app.exec_()
