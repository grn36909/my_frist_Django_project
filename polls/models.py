#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'GRN31'

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)                    # 问题的文本描述
    pub_date = models.DateTimeField('date published')                   # 发布时间

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 外键关系: 每一个 Choice 关联到一个对应的 Question
    choice_text = models.CharField(max_length=200)                      # 选项的文本描述
    votes = models.IntegerField(default=0)                              # 投票数

    def __str__(self):
        return self.choice_text
