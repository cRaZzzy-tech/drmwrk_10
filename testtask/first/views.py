from django.shortcuts import render, get_object_or_404

from .models import Users, Posts, Address, Company

from pip._vendor import requests

def main(request):
    if request.POST:
        print('read')
        users = requests.get('http://jsonplaceholder.typicode.com/users')
        if users.status_code == 200:
            dict = users.json()
            for line in dict:
                try:
                    Users.objects.get(sec_id=line['id'])
                except:
                    addr = Address.objects.create(
                        street= line['address']['street'],
                        suite = line['address']['suite'],
                        city = line['address']['city'],
                        zipcode = line['address']['zipcode'],
                        geo_lat = line['address']['geo']['lat'],
                        geo_lng = line['address']['geo']['lng'],
                    )
                    com = Company.objects.create(
                        name = line['company']['name'],
                        catchPhrase = line['company']['catchPhrase'],
                        bs = line['company']['bs'],
                    )
                    Users.objects.create(
                        sec_id = line['id'],
                        name = line['name'],
                        username = line['username'],
                        email = line['email'],
                        address = addr,
                        phone = line['phone'],
                        website = line['website'],
                        company = com
                    )

        posts = requests.get('http://jsonplaceholder.typicode.com/posts')
        if posts.status_code == 200:
            dict = posts.json()
            for line in dict:
                try:
                    Posts.objects.get(sec_id=line['id'])
                except:
                    Posts.objects.create(
                        sec_id = line['id'],
                        user = Users.objects.get(sec_id=line['userId']),
                        title = line['title'],
                        body = line['body'],
                    )
    pagePosts = Posts.objects.all()
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

