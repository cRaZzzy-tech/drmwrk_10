import requests
from django.core.management.base import BaseCommand

from first.models import Users, Address, Company

class Command(BaseCommand):
    def handle(self, *args, **options):
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