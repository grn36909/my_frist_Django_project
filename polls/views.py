#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'GRN31'

# from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from .models import Question, Choice
# from django.template import loader


def err_404(request):
    return HttpResponse("Oops! Page not find. Check url and retry. <br>%s" % request.path)


def hello(request):  # 显示欢迎信息
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):  # index.html
    # return HttpResponse("This is a index site of polls app.")
    # output = '<br>'.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    # return render(request, 'polls/index.html', context)  # 返回一个经过字典数据渲染过的模板封装而成的HttpResponse对象
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   # 最后5个Question
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}            # 模板变量和Python对象之间的映射关系
    return HttpResponse(template.render(context, request))


def detail(request, question_id):   # 描述
    # return HttpResponse("You'er looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)              # 对象不存在时弹出“404错误页面”
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):  # 结果
    # response = "You'er looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


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
