from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QTextEdit,QLineEdit,QListWidget,QPushButton,QInputDialog
import json

app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Умные заметки')
main_win.resize(1000,800)
main_win.show()

def show_note():
    name=list2.selectedItems()[0].text()
    for note in notes:
        if name==note[0]:
            texte.setText(note[1])
            list1.clear()
            list1.addItems(note[2])
            break

def add_button():
    note_name,ok=QInputDialog.getText(main_win,'Добавить заметку','Название заметки') 
    if ok and note_name !='':
        note=[note_name,'',[]]
        notes.append(note)
        list2.addItem(note[0])
        name=str(len(notes)-1)+'.txt'
        with open(name,'w',encoding='utf-8') as file:
            file.write(note[0]+'\n')
def del_button():
    if list2.selectedItems():
        name=list2.selectedItems()[0].text()
        del notes[name]
        list1.clear()
        texte.clear()
        list2.clear()
        list2.addItems(notes)
def save_button():  
    name=list2.selectedItems()[0].text() 
    if list2.selectedItems():
        text=texte.toPlainText()
        for note in notes:
            if name==note[0]:
                note[1]=text
        
def add_tag():
    if list2.selectedItems():
        name=list2.selectedItems()[0].text()
        tag=line.text()
        if tag!='':
            for note in notes:
                if name==note[0]:
                    if not tag in note[2]:
                        note[2].append(tag)
                list1.addItem(tag)
                line.clear()
def del_tag():
    if list2.selectedItems():
        if list1.selectedItems():
            name=list2.selectedItems()[0].text()
            tag=list1.selectedItems()[0].text()
            for note in notes:
                if name==note[0]:
                    note[2].remove(tag)
            list1.clear()
            for note in notes:
                if name==note[0]:
                    list1.addItems(note[2])
def search_tag():
    name=list2.selectedItems()[0].text()
    text=line.text()
    if button6.text()=='Искать по тегу' and text:
        for note in notes:
            if name==note[0]:
                if text in note[2]:
                    list2.clear()
                    texte.clear()
                    list1.clear()
                    list2.addItem(note)
                    button6.setText('Сбросить поиск')
    elif button6.text()=='Сбросить поиск':
        line.clear()
        list2.clear()
        for note in notes:
            if name==note[0]:
                list2.addItem(note)
                button6.setText('Искать по тегу')

notes=[["заметка","важный текст", ["черновик", "мысли"]]]
num_name=0

while True:
    name=str(num_name)+'.txt'
    try:
        with open(name,'r',encoding='utf-8') as file:
            note=file.read()
            note=note.split('/')
            note[2]=note[2].split('#')
            notes.append(note)
            num_name+=1
    except IOError:
        break

button1=QPushButton('Создать заметку')
button2=QPushButton('Удалить заметку')
button3=QPushButton('Сохранить заметку')
button4=QPushButton('Добавить к заметке')
button5=QPushButton('Открепить от заметки')
button6=QPushButton('Искать по тегу')

button1.clicked.connect(add_button)
button2.clicked.connect(del_button)
button3.clicked.connect(save_button)
button4.clicked.connect(add_tag)
button5.clicked.connect(del_tag)
button6.clicked.connect(search_tag)

texte=QTextEdit()
line=QLineEdit()
line.setPlaceholderText('Введите тег...')
list1=QListWidget()
list2=QListWidget()
for note in notes:
    list2.addItem(note[0])
label1=QLabel('Список заметок')
label2=QLabel('Список тегов')

list2.itemClicked.connect(show_note)

hlayout=QHBoxLayout()
vlayout1=QVBoxLayout()
vlayout2=QVBoxLayout()
hlayout1=QHBoxLayout()
hlayout2=QHBoxLayout()

vlayout1.addWidget(texte)

hlayout1.addWidget(button1)
hlayout1.addWidget(button2)
hlayout2.addWidget(button4)
hlayout2.addWidget(button5)

vlayout2.addWidget(label1)
vlayout2.addWidget(list2)
vlayout2.addLayout(hlayout1)
vlayout2.addWidget(button3)
vlayout2.addWidget(label2)
vlayout2.addWidget(list1)
vlayout2.addWidget(line)
vlayout2.addLayout(hlayout2)
vlayout2.addWidget(button6)

hlayout.addLayout(vlayout1)
hlayout.addLayout(vlayout2)
main_win.setLayout(hlayout)

app.exec_()

#затем запрограммируй демо-версию функционала
