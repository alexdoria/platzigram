# from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

posts = [
    {
        'name': 'The Great Mountains of Kiwaloo',
        'user': 'Alex Doria',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1002/600/600'
    },
    {
        'name': 'High temperature states in Mexico',
        'user': 'Dulce Ojeda',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1053/600/600'
    },
    {
        'name': 'I have been busy but never felt better',
        'user': 'Alex Doria',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1003/600/600'
    },
    {
        'name': 'A Very Sad Story',
        'user': 'Mr John McLovin',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1021/600/600'
    }

]


@login_required(login_url="login")
def list_posts(request):
    """List existing posts"""
    return render(request, 'posts/feed.html', {'posts': posts})
