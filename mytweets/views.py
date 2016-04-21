from django.views.generic import ListView

from pinax.types.periods import get_period

from .models import Tweet


class TweetListView(ListView):
    model = Tweet
    template_name = "homepage.html"
    paginate_by = 100
    ordering = "-pk"

    def get_queryset(self):
        queryset = super(TweetListView, self).get_queryset()
        period = self.request.GET.get("period")
        if period:
            queryset = queryset.filter(
                timestamp__range=get_period(period).get_start_end()
            )
        return queryset
