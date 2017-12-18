from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


# Create your models here.

# 投稿を保存するテーブル
class Post(models.Model):
  author = models.ForeignKey('auth.User') # Userテーブルを外部参照
  title = models.CharField(max_length = 32)
  text = models.TextField()
  created_date = models.DateTimeField(default = timezone.now)
  published_date = models.DateTimeField(blank = True, null =True)

  def publish(self): # 投稿更新
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

  def get_absolute_url(self): # 詳細のurlを返す
    return reverse('post:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
  post = models.ForeignKey(Post, related_name = 'comments')
  author = models.CharField(max_length = 200)
  text = models.TextField()
  created_date = models.DateTimeField(default = timezone.now)
  approved_comment = models.BooleanField(default = False)

  def approve(self):
    self.approved_comment = True
    self.save()

  def approved(self):
    return self.comments.filter(approved_comment = True)

  def __str__(self):
    return self.text


class UserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, email, password, **extra_fields):
    """
    Create and save a User with the given email, and password.
    """
    if not email:
      raise ValueError('The given email must be set')

    email = self.normaliza_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password = None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_supperuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_supperuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_supperuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Supperuser must have is_staff=True')
    if extra_fields.get('is_supperuser') is not True:
      raise ValueError('Supperuser must have is_supperuser=True')

    return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(
    _('email address'),
    unique = True,
    error_messages = {'unique': _("A user with that email already exists.")},
  )
  first_name = models.CharField(_('first name'), max_length = 30, blanck = True)
  last_name = models.CharField(_('last name'), max_length = 150, blank = True)

  is_staff = models.BooleanField(
    _('staff status'),
    default = False,
    help_text = _('Designates whether the user can log into this admin site.')
  )
  is_active = models.BooleanField(
    _('active'),
    default = True,
    help_text = _(
      'Designates whether this user should be treated as active.'
      'Unselect this instead of deleting accounts.'
      ),
  )
  date_joined = models.DateTimeField(_('date joined'), default = timezone.now)
  objects = UserManager()

  EMAIL_FIELD = 'email'
  USErNAME_FIELD = 'email'
  REQUIRED_FIELD = []

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')

  def get_full_name(self):
    """Return the first_name plus the last_name, with a space in between."""
    full_name = '%s %s' % (self.first_name, self.last_name)
    return full_name.strip()

  def get_short_name(self):
    """Return the short name for the user."""
    return self.first_name

  def email_user(self, subject, message, from_email = None, **kwargs)
    """Send an email to this user."""
    send_mail(subject, message, from_email, [self.email], **kwargs)

