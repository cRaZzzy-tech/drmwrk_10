from django.core import management
from django.shortcuts import render

from .models import Users, Posts, Address, Company

def main(request):
    if request.POST:
        management.call_command('add_users')
        management.call_command('add_posts')

    # pagePosts = Posts.objects.all()                            #default 20.91 ms (105 queries including 102 similar and 102 duplicates )
    pagePosts = Posts.objects.select_related('user').all()       # default 1.74 ms (3 queries )
    users = Users.objects.all().order_by('name').values('id', 'name')
    return render(request, 'first/main.html', context={'posts': pagePosts, 'users': users})

#ajax
def ajax_filter(request):
    print('ajax_filter')
    if request.GET['clear'] == 'false':
        posts = Posts.objects.filter(user = Users.objects.get(id=request.GET['user']))
    else:
        posts = Posts.objects.all()
    return render(request, 'first/ajax_filter.html', {'posts': posts})

