from rest_framework import serializers
from models import QuestionFaq, AnswerFaq
import json


def create_faq_tree(questions):

    tree_list = []

    for question in questions:
        answers = AnswerFaq.objects.filter(question=question)

        answers_list = []
        for answer in answers:
            answers_list.append({
                'photo': "/media/%s" % answer.account.photo,
                'name': answer.account.get_full_name(),
                'date': "%s" % answer.date,
                'text': answer.answer
            })

        tree_list.append({
            'id': question.id,
            'title': question.title,
            'date': "%s" % question.date,
            'text': question.question,
            'answers': answers_list
        })

    tree = json.dumps(tree_list)

    return tree
