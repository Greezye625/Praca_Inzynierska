from django.shortcuts import render
from threads.models import ThreadCategory, Thread


def homepage(request):
    if request.method == 'GET':
        thread_categories = ThreadCategory.objects.exclude(name__in=['Sell', 'Buy', 'Exchange'])
        market_categories = ThreadCategory.objects.filter(name__in=['Sell', 'Buy', 'Exchange'])

        return render(request, 'index.html', context={'thread_categories': thread_categories,
                                                      'market_categories': market_categories, })


def category(request, pk):
    if request.method == 'GET':
        thread_category = ThreadCategory.objects.get(pk=int(pk))

        threads_in_current_category = Thread.objects.filter(thread_category=int(pk))

        return render(request, 'threads/discussion_threads_category.html', context={'thread_category': thread_category,
                                                                                    'threads_in_current_category': threads_in_current_category, })
