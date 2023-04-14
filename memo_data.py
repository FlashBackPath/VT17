from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle


new_quest_templ = 'Нове запитання'
new_answer_templ = 'Нова відповідь'

text_wrong = 'Неправильно'
text_correct = 'Правильно'

class Question():
    # клас, який представляє собою питання. Заповніть пропуски, щоб init працював коректно
    ____ __init__(____, question=new_quest_templ, answer=new_answer_templ,
                       wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        # створіть властивості для всіх аргументів
        ____.____ = question # питання
        ____.____ = answer # правильна відповідь
        ____.____ = wrong_answer1 # невірна відповідь №1
        ____.____ = wrong_answer2 # невірна відповідь №2
        ____.____ = wrong_answer3 # невірна відповідь №3
        ____.____ = ____ # чи продовжувати задавати це питання. Булева змінна. За замовчуванням - True
        ____.____ = 0 # скільки задавали це питання
        ____.____ = 0 # скільки правильно відповідали на це питання
    def got_right(self):
        # метод, який реалізує правильну відповідь. Додає одиничку до кількості спроб та к-сті правильних відповідей
        ____.____ += 1
        ____.____ += 1
    def got_wrong(____):
        # метод, який реалізує неправильну відповідь. Додає одиничку до к-сті спроб
        ____.____ += 1

class QuestionView():
    # дозволяє співставити питання та віджети, на яких це питання треба показати. Суть класу в тому, щоб реалізувати швидку підстановку питання до віджетів
    def ____(____, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # конструктор отримує і запам'ятовує об'єкт із даними та віджети, що відповідають полям анкети
        # створіть властивості для всіх аргументів
        ____.frm_model = ____
        ____.question = ____
        ____.answer = ____
        ____.wrong_answer1 = ____
        ____.wrong_answer2 = ____
        ____.wrong_answer3 = ____
    def change(____, ____):
        ''' обновление данных, уже связанных с интерфейсом '''
        self.frm_model = frm_model
    def show(self):
        # Цей метод звертається до кожного віджету та підставляє туди відповідну частину запитання.
        # В останню комірку(після frm_model.) не вписуйте нічого. Ми заповнимо це на уроці
        ____.question.setText(____.frm_model.____)
        ____.answer.setText(____.frm_model.____)
        ____.wrong_answer1.setText(____.frm_model.____)
        ____.wrong_answer2.setText(____.frm_model.____)
        ____.wrong_answer3.setText(____.frm_model.____)

