from django.views.generic import ListView

from .models import Tweet


class TweetListView(ListView):
    model = Tweet
    template_name = "homepage.html"
    paginate_by = 100
    ordering = "-pk"
