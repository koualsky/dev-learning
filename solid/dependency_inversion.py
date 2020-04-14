"""
Klasa 'Task' jest ogółem, jest ważniejsza i nie może wiedzieć nic o klasach niższych, szczegółowych, więc musi mieć metody zaimplementowane za pomocą interfejsu
klasa 'Process' jest szczegółem

Jak o tym myśleć? Napisać klasę Task, która za pomocą agregacji pobiera obiekt do dalszej obróbki... Ale, żeby mieć jakiegoś hinta,
to dodać sobie klasę abstrakcyjną i zrobić to tak: process: ProcessInterface w konstruktorze Task'a.
Bo dzięki temu też, mamy pewność, że przekazana klasa, implementująca interfejs, będzie miała metodę send...
I będziemy mogli robić to elastycznie, bez modyfikacji klasy Task i podejmowania ryzyka zepsucia czegoś.

Więcej: moje notki i: https://naukapython.pl/zasady-solid-w-pythonie-dla-poczatkujacych-dependency-inversion-principle/
"""


from abc import ABC, abstractmethod


class ProcessInterface(ABC):
    @abstractmethod
    def send(self, txt):
        pass


class Process(ProcessInterface):
    def send(self, txt):
        print(f'Message in Process: {txt}')


class Task:
    def __init__(self, process: ProcessInterface):
        self.process = process

    def send_something_to_process(self, txt):
        self.process.send(f'Message from Task: {txt}')


process = Process()
task = Task(process)
task.send_something_to_process('hello')