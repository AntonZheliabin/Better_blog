from datetime import datetime
from django.shortcuts import render, redirect
from .models import Publication, Message, CommentsPublication


def publications(request):
    publications_objects = Publication.objects.all().order_by('-date')
    publications_last = Publication.objects.order_by('date').reverse()[:10]
    comments_publication_objects = CommentsPublication.objects.all().order_by('-id')
    if request.method == 'POST':
        comment_name = request.POST.get('comment_name', '')
        comment_text = request.POST.get('comment_text', '')

        if not comment_name or not comment_text:
            return render(request, 'publications.html', context={
                'error': 'Есть пустое поле',
                'publications': publications_objects,
                'publications_last': publications_last,
                'comments': comments_publication_objects
            })
        comment = CommentsPublication(comment_name=comment_name, comment_text=comment_text)
        comment.save()
    return render(request, 'publications.html', context={
        'publications': publications_objects,
        'publications_last': publications_last,
        'comments': comments_publication_objects,
    })


def contacts(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        user_phone = request.POST.get('user_phone', '')
        user_text = request.POST.get('user_text', '')

        message = Message(user_name=user_name, user_phone=user_phone, user_text=user_text)
        message.save()

    return render(request, 'contacts.html', context={
        'email': 'wdqd@affew.com',
        'phone': '4567890',
        'server_time': datetime.now(),
    })




def publication(request, number):
    try:
        publication = Publication.objects.get(id=number)
    except Publication.DoesNotExist:
        return redirect('/publications')
    return render(request, 'publication.html', context={
        'publication': publication
    })



def user_message(request):
    messages = Message.objects.all().order_by('-id')
    return render(request, 'user_message.html', context={
        'messages': messages
    })
