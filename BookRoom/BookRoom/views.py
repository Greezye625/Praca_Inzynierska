from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from threads.models import Thread, ThreadComment

@csrf_exempt
def search_view(request):

    searched_phrase = request.GET['search']

    users_found = get_user_model().objects.filter(username__contains=searched_phrase)

    threads_found = Thread.objects.filter(name__contains=searched_phrase).exclude(thread_category__name__in=['Buy', 'Sell', "Exchange"])

    transactions_found = Thread.objects.filter(name__contains=searched_phrase, thread_category__name__in=['Buy', 'Sell', "Exchange"])

    thread_comments_found = ThreadComment.objects.filter(text_content__contains=searched_phrase)




    return render(request, 'searchpage.html', context={'users_found': users_found,
                                                       'threads_found': threads_found,
                                                       'thread_comments_found': thread_comments_found,
                                                       'transactions_found': transactions_found})

