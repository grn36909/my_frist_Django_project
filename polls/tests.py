from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from .models import Question

'''
运行: python manage.py test polls
参考: http://www.liujiangblog.com/course/django/91
'''

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        '''
        在将来发布的投票应该返回 False
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        '''
        只要是超过1天的投票，返回 False
        '''
        time =  timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        '''
        最近1天的投票，返回 True
        '''
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
