import requests
from django.core.management.base import BaseCommand

from first.models import Posts, Users

class Command(BaseCommand):
    def handle(self, *args, **options):
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