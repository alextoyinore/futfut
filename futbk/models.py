from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class FutUser(AbstractUser):
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Male'), 
            ('F', 'Female'), 
            ('', 'Rather Not Say')
        ), null=True
    )
    profile_img = models.CharField(max_length=1000, null=True)
    profile_banner = models.CharField(max_length=1000, null=True)
    date_joined = models.DateField(auto_now=True, auto_now_add=False)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Geo(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=4, null=False)
    long = models.DecimalField(max_digits=10, decimal_places=4, null=False)

    def __str__(self):
        return str(self.lat, self.long)

class Address(models.Model):
    country = models.CharField(max_length=100, default='Nigeria', null=False)
    state = models.CharField(max_length=100, default='Lagos', null=False)
    street = models.CharField(max_length=100, null=True)
    street_no = models.SmallIntegerField(null=True)
    zip_code = models.CharField(max_length=10, null=True)
    geo = models.ForeignKey(Geo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.country

class Base(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    user = models.ForeignKey(FutUser, on_delete=models.PROTECT)
    description = models.TextField(max_length=500)
    base_img = models.CharField(max_length=1000)
    base_banner = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']

class Post(models.Model):
    text = models.TextField(max_length=300, null=True)
    image = models.CharField(max_length=1000, null=True)
    video = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(FutUser, on_delete=models.PROTECT, null=False)
    base = models.ForeignKey(Base, on_delete=models.PROTECT)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['date']
        unique_together = ('text', 'user')

class Reply(models.Model):
    text = models.TextField(max_length=300, null=True)
    image = models.CharField(max_length=1000, null=True)
    video = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(FutUser, on_delete=models.PROTECT, null=False)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'Replies'
        ordering = ['date']
        unique_together = ('text', 'user')

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(FutUser, on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.id

    class Meta:
        unique_together = ('post', 'user')
    
class View(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(FutUser, on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.id

    class Meta:
        unique_together = ('post', 'user')

class Bookmark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(FutUser, on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.id

    class Meta:
        ordering = ['date']
        unique_together = ('post', 'user')

class Republish(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(FutUser, on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.id

    class Meta:
        db_table = 'Republishes'
        unique_together = ('post', 'user')

class Follow(models.Model):
    follower = models.ForeignKey(FutUser, on_delete=models.PROTECT, null=False, related_name='follower')
    followed = models.ForeignKey(FutUser, on_delete=models.PROTECT, null=False, related_name='followed')
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.follower.username

    class Meta:
        unique_together = ('follower', 'followed')

class BaseMember(models.Model):
    user = models.ForeignKey(FutUser, on_delete=models.CASCADE)
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    date_joined = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    title = models.CharField(max_length=100)
    msg_sender = models.ForeignKey(FutUser, on_delete=models.PROTECT, related_name='sender')
    msg_reciever = models.ForeignKey(FutUser, on_delete=models.PROTECT, related_name='reciever')
    image = models.CharField(max_length=1000)
    video = models.CharField(max_length=1000)
    text = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date']

class Notification(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    sender = models.ForeignKey(FutUser, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

