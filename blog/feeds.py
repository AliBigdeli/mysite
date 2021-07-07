from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class LatestEntriesFeed(Feed):
    title = "blog newest posts"
    link = "/rss/feed"
    description = "best blog ever"

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
