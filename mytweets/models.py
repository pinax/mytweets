import datetime

from django.db import models


def format_date(date_str):
    if date_str:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z")


class Tweet(models.Model):
    tweet_id = models.IntegerField()
    in_reply_to_status_id = models.IntegerField(null=True, blank=True)
    in_reply_to_user_id = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField()
    source = models.TextField()
    text = models.TextField()
    retweeted_status_id = models.IntegerField(null=True, blank=True)
    retweeted_status_user_id = models.IntegerField(null=True, blank=True)
    retweeted_status_timestamp = models.DateTimeField(null=True, blank=True)
    expanded_urls = models.TextField(blank=True)

    @classmethod
    def import_archive(cls, csv_data):
        """
        Expects a DictReader (`csv_data`) from a Twitter archive.

        >>> import csv
        >>> from mytweets.models import Tweet
        >>> reader = csv.DictReader(open("../tweets.csv", "r"))
        >>> Tweet.import_archive(reader)
        """
        for tweet in reversed(list(csv_data)):
            cls.objects.create(
                tweet_id=tweet["tweet_id"],
                in_reply_to_status_id=tweet["in_reply_to_status_id"] or None,
                in_reply_to_user_id=tweet["in_reply_to_user_id"] or None,
                timestamp=format_date(tweet["timestamp"]),
                source=tweet["source"],
                text=tweet["text"],
                retweeted_status_id=tweet["retweeted_status_id"] or None,
                retweeted_status_user_id=tweet["retweeted_status_user_id"] or None,
                retweeted_status_timestamp=format_date(tweet["retweeted_status_timestamp"]),
                expanded_urls=tweet["expanded_urls"]
            )
