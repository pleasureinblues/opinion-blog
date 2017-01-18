from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.forms import ModelForm

from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
            return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.title

class Comment (models.Model):
    comment_body = models.TextField()
    commented_on = models.DateTimeField(db_index=True,auto_now=True)
    commenter = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return '%s' % self.comment_body

class Tag (models.Model):
    tag_title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    post = models.ManyToManyField(Post)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tag_title)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.tag_title


class UserProfile(models.Model):
    # This line is required.Links Userprofile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override th __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=75)
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __unicode__(self):
        return self.subject


LIKE_CHOICES = (
    ('YS', 'YES I LIKE'),
    ('NO', 'I DON\'T LIKE'),
    )

class Feedback(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=75)
    like_dislike = models.CharField(max_length=2, choices=LIKE_CHOICES)
    feedback_msg = models.TextField()

    def __unicode__(self):
        return self.name