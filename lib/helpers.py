import feedparser
import requests


def fetch_feed(feed_url):
    """
    Use feedparser to fetch and parse an RSS feed
    """

    insights_feed = requests.get(feed_url)
    return feedparser.parse(insights_feed.text)


def format_post(post):
    """
    Format a feedparser post for printing
    """

    return (
        "Title: " + post['title'] + "\n" +
        "\n" +
        "Summary:\n" +
        post['summary']
    )
