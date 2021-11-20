from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=50, verbose_name='Улица')
    suite = models.CharField(max_length=50, verbose_name='Аппартамент')
    city = models.CharField(max_length=50, verbose_name='Город')
    zipcode = models.CharField(max_length=50, verbose_name='Почтовый индекс')
    geo_lat = models.CharField(max_length=8, verbose_name='Гео ширина')
    geo_lng = models.CharField(max_length=8, verbose_name='Гео долгота')

class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    catchPhrase = models.CharField(max_length=100, verbose_name='Краткое описание')
    bs = models.CharField(max_length=100, verbose_name='Сфера работы')

class Posts(models.Model):
    sec_id = models.IntegerField(unique=True, verbose_name='jsonId')
    user = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.CharField(max_length=1000, verbose_name='Пост')

class Users(models.Model):
    sec_id = models.IntegerField(unique=True, verbose_name='jsonId')
    name = models.CharField(max_length=50, verbose_name='Имя')
    username =  models.CharField(max_length=20, verbose_name='Пользователь')
    email = models.EmailField(verbose_name='E-mail')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, verbose_name='Адрес')
    phone = models.CharField(max_length=25, verbose_name='Телефон')
    website = models.CharField(max_length=25, verbose_name='Сайт')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Компания')

