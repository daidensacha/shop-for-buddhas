from .models import Post


def posts(request):
    """ Create context processor for the archive posts by year/ month """
    return {
        'all_posts': Post.objects.order_by('posted_at')
    }
