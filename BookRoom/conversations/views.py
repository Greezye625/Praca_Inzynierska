from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.db.models import Q
from conversations import forms
from conversations.models import Conversation, Message


def start_new_conversation_from_profile(request, recipent_pk):
    recipent = get_user_model().objects.get(pk=recipent_pk)

    if request.method == 'POST':
        form = forms.StartNewConversationFromProfile(request.POST)

        if form.is_valid():
            new_conversation = Conversation(subject=form.cleaned_data['subject'],
                                            initiator=request.user,
                                            recipent=recipent)
            new_conversation.save()

            first_message = Message(conversation=new_conversation,
                                    sender=request.user,
                                    receiver=recipent,
                                    content=form.cleaned_data['message'])
            first_message.save()

            return redirect('conversations:conversation_page', conversation_pk=new_conversation.pk)

        else:
            # TODO add error page
            print('error creating conversation - need to have page here')


    elif request.method == 'GET':
        form = forms.StartNewConversationFromProfile()
        return render(request, 'conversations/start_new_conversation.html', context={'recipent': recipent,
                                                                                     'form': form})


def conversation_view(request, conversation_pk):
    conversation = Conversation.objects.get(pk=conversation_pk)

    if request.method == 'POST':
        user = request.user
        addressee = conversation.recipent if conversation.initiator == user else conversation.initiator
        form = forms.ReplyToConversation(request.POST)

        if form.is_valid():
            reply = Message(conversation=conversation,
                            sender=user,
                            receiver=addressee,
                            content=form.cleaned_data['message'])

            reply.save()
            return redirect('conversations:conversation_page', conversation_pk=conversation_pk)

        else:
            # TODO add error page
            print('error replying - need to have page here')


    elif request.method == 'GET':
        form = forms.ReplyToConversation()
        messages = Message.objects.filter(conversation=conversation)
        return render(request, 'conversations/conversation_page.html', context={'conversation': conversation,
                                                                                'messages': messages,
                                                                                'form': form})


def conversations_panel(request):
    user = request.user
    conversations = Conversation.objects.filter(Q(initiator=user) |
                                                Q(recipent=user))

    if request.method == "POST":
        pass
    elif request.method == 'GET':
        return render(request, 'conversations/conversations_panel.html', context={'conversations': conversations})
