from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tweet


# Create your views here.

# class TweetListView(ListView):
#     model = Tweet
#     queryset = Tweet.objects.all()
#     template_name = 'tweets/tweet_list.html'

def tweet_list(request):
    object_list = Tweet.objects.all()
    context = {
        'object_list': object_list
    }

    return render(request, 'tweets/tweet_list.html', context)