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


def start_new_thread(request, pk):
    thread_category = ThreadCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.AddThread(request.POST)

        if form.is_valid():

            new_thread = Thread(name=form.cleaned_data['name'],
                                creator=request.user,
                                thread_category=thread_category)

            new_thread.save()

            first_comment = ThreadComment(thread=new_thread,
                                          poster=request.user,
                                          text_content=form.cleaned_data['first_comment'])
            first_comment.save()

            return redirect('threads:thread', pk=new_thread.pk)

        else:
            # TODO add error page
            print('error creating thread - need to have page here')


    elif request.method == 'GET':
        form = forms.AddThread()
        return render(request, 'threads/start_new_thread.html', context={'thread_category': thread_category,
                                                                         'form': form})