# blog/views.py
from django.views.generic import ListView, DetailView # нове

from .models import Post, Likes

from django.shortcuts import redirect


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): # нове
    model = Post
    template_name = 'post_detail.html'

def get_request_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    print(ip)
    return ip

class AddLike(DetailView):
    def get(self, requst, pk):
        ip_client = get_request_ip(request=requst)
        if not ip_client:
           ip_client = "127.0.0.0"

        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f"/post/{pk}")
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f"/post/{pk}")
