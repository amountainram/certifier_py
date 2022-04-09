from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
    }
]

def config():
    answers = prompt(questions)