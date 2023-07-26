from django.shortcuts import render
from django.http import HttpResponse
from . import chatbot_logic
from .chatbot_logic import extract_intent, skills

def index (request):
    return render(request,'chat/index.html')

def chat_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        intent, entities = extract_intent(text)
        skill = skills[intent]
        resp = skill(**entities)
        return render(request, 'chat/chat.html', {'response': resp})
    else:
        return render(request, 'chat/chat.html')