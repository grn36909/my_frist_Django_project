#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'GRN31'

# from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Question, Choice
# from django.template import loader


def err_404(request):
    return HttpResponse("Oops! Page not find. Check url and retry. <br>%s" % request.path)


def hello(request):  # 显示欢迎信息
    return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):  # index
    template_name = 'polls/index.html'                                  # 通过 template_name 属性指定模板名
    context_object_name = 'latest_question_list'                        # 通过 context_object_name 指定

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]               # 返回最近发布的5个投票


class DetailView(generic.DetailView):   # 描述
    model = Question                                                    # 通过 model 属性指定模型
    template_name = 'polls/detail.html'                                 # 通过 template_name 属性指定模板名


class ResultsView(generic.DetailView):  # 结果
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):     # 投票
    # return HttpResponse("You'er voting on question %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question': question,
                   'error_message': "You didn't select a choice.",
                  }
        return render(request, 'polls/detail.html', context)            # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交

# TODO: 这是一个 idea 测试
