from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question detail',     {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]                    # 显示候选项(至少3个)
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 选择显示的列
    list_filter = ['pub_date']                  # 增加过滤面板
    search_fields = ['question_text']           # 增加搜索面板


admin.site.register(Question, QuestionAdmin)
