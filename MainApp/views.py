from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

author = {
    "Имя": "Павел",
    "Отчество": "Борисович",
    "Фамилия": "Кузнецов",
    "телефон": "+7-926-925-50-37",
    "email": "toyottobb@gmail.com",
}


def home(request):
    text = """
    <h1>"Изучаем django"</h1
    <strong>Автор</strong>: <i>Кузнецов П.Б.</i>
    """
    return HttpResponse(text)


def about (request):
    text = f"""
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author["Фамилия"]}</b><br>
    телефон: <b>{author["телефон"]}</b><br>
    email: <b>{author["email"]}</b><br>
    """
    return HttpResponse(text)
      
        
       
       
       