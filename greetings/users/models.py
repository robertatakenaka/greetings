from datetime import datetime
from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    year = datetime.now().isoformat()
    default_date1 = year[0:10]
    year = year[:4]
    year = str(int(year) - 30)
    default_date2 = year+'-07-01'

    name = models.CharField('Apelido', blank=True, max_length=255)
    photo = models.ImageField('Foto', blank=True, default='./photo.png')
    birthday = models.DateField('Data de nascimento', blank=True, default=default_date2)
    anniversary = models.DateField('Data de admissão', blank=True, default=default_date1)

    def __str__(self):
        return self.username

    def birthday_day(self):
        return self.birthday.isoformat()[6:]

    def anniversary_day(self):
        return self.anniversary.isoformat()[6:]

    def years(self):
        current = datetime.now().isoformat()[:4]
        d = self.anniversary.isoformat()[:4]
        return int(current) - int(d)

    def display_years(self):
        return str(self.years())

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
