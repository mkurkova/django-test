from django.contrib import admin
from .models import Project, Task

# Register your models here.
## admin.site.register(Project)

#Inline класс для модели Task 
class TaskInLine(admin.TabularInline):
    model = Task
    extra = 0 #не будут отображаться пустые формы для новых задач
    fields = ('name', 'description', 'assignee', 'status', 'created_at', 'updated_at') #поля, которые хотим отредактировать
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True #позволяет удалять задач прямо из проекта
    show_change_link = True

#Класс администратора для модели Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at') #определяет, какие поля модели будут отображаться
    search_fields = ('name', 'description') #позволяет создать поисковую строку для фильтрации списка объекта
    ordering = ('created_at',) #позволяет определить порядок сортировки
    date_hierarchy = 'created_at' #позволяет добавить навигацию по датам

    #Подключение inline для Task
    inlines = [TaskInLine]


#Класс администратора для модели Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assignee', 'status', 'created_at', 'updated_at') 
    list_filter = ('status', 'assignee', 'project') #добавляет фильтр сбоку
    search_fields = ('name', 'description') 
    list_editable = ('status', 'assignee') #указывает поля, которые можно будет редактировать
    readonly_fields = ('created_at', 'updated_at') #доступны только для чтения
