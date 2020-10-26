from django.shortcuts import render, redirect
from threads.models import ThreadCategory, Thread, ThreadComment
from threads import forms


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


def thread_view(request, pk):
    thread = Thread.objects.get(pk=int(pk))
    if request.method == 'GET':
        form = forms.AddComment(auto_id=False)



        comments = ThreadComment.objects.filter(thread=thread.pk)

        return render(request, 'threads/thread.html', context={'thread': thread,
                                                               'comments': comments,
                                                               'form': form})
    elif request.method == 'POST':
        form = forms.AddComment(request.POST)

        if form.is_valid():
            thread_comment = ThreadComment(thread=thread,
                                           poster=request.user,
                                           text_content=form.cleaned_data['text_content'])

            thread_comment.save()

        return redirect('threads:thread', pk=pk)
