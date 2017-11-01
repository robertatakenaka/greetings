from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


@python_2_unicode_compatible
class CommemorativeDate(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    photo = models.ImageField(_('Photo'))
    date = models.DateField(_('Date'))


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(_('Photo'))


@python_2_unicode_compatible
class Person(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    birthday = models.DateField(_('Birthday date'))
    anniversary = models.DateField(_('Anniversary date'))
