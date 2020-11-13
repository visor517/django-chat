from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import Message

def index(request):
    latest_messages_list = Message.objects.order_by('message_time')
    return render(request, 'messenger/page.html', {'latest_messages_list': latest_messages_list})

def leave_message(request):
    new_message = Message(message_author=request.POST['name'], message_text=request.POST['text'], message_time=timezone.now())
    new_message.save()
    return HttpResponseRedirect(reverse('messenger:index'))