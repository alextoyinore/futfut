from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

gender_choices = (('M', 'Male'), ('F', 'Female'), ('R', 'Rather Not Say'))

class FutUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=gender_choices, default='R')
    tag_line = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    profile_img = models.URLField(null=True, blank=True)
    profile_banner = models.URLField(null=True, blank=True)
    date_joined = models.DateField(auto_now=True, auto_now_add=False)
    phone = models.CharField(max_length=11, null=True, blank=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['date_joined']


class Geo(models.Model):
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=False)
    lon = models.DecimalField(max_digits=8, decimal_places=6, null=False)

    def __str__(self):
        return f'${str(self.lat), str(self.long)}'

    class Meta:
        unique_together = ('lat', 'lon')


class Address(models.Model):
    user = models.ForeignKey('FutUser', on_delete=models.CASCADE)
    country = models.CharField(max_length=100, default='Nigeria', null=True)
    state = models.CharField(max_length=100, default='Lagos', null=True)
    city = models.CharField(max_length=100, default='Agege', null=True)
    street = models.CharField(max_length=100, null=True)
    street_no = models.SmallIntegerField(null=True)
    zip_code = models.CharField(max_length=10, null=True)
    geo = models.ForeignKey('Geo', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.geo
        
class Base(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    user = models.ForeignKey('FutUser', on_delete=models.PROTECT, null=False)
    description = models.TextField(max_length=500)
    base_img = models.URLField(null=True)
    base_banner = models.URLField(null=True)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['date']

class BaseMember(models.Model):
    user = models.ForeignKey('FutUser', on_delete=models.CASCADE)
    base = models.ForeignKey('Base', on_delete=models.PROTECT)
    date_joined = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.username

'''
@Post: Post table
'''

class Post(models.Model):
    text = models.CharField(max_length=222, null=True)
    image = models.URLField(null=True)
    video = models.URLField(null=True)
    poll = models.BooleanField(default=False)
    parent = models.ManyToManyField('self', symmetrical=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey('FutUser', on_delete=models.PROTECT, null=False)
    base = models.ForeignKey('Base', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text
    class Meta:
        ordering = ['-date']
        unique_together = ('text', 'user')

'''
@PollPostOption: Each option of a poll will be added to this table. In the frontend,
this table will be queried and filtered by post_id. options will be queried as collection
 and filtered post_id and displayed together to create poll options
'''

class PollPostOption(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    option = models.CharField(max_length=200)

    def __str__(self):
        return self.option

'''
@PollPostResponse: A user can enter one pick one option from the frontend it will be 
added to this table. The total votes for this option will be the count of the query
filtered by the selection field. One user can put one selection
'''

class PollPostResponse(models.Model):
    selection = models.ForeignKey('PollPostOption', on_delete=models.CASCADE)
    voter = models.ForeignKey('FutUser', on_delete=models.CASCADE, verbose_name='voter')

    def __str__(self):
        return self.selection

    class Meta:
        unique_together = ('selection', 'voter')

'''
@QuestionPost: Table for holding posts of type question
'''

class QuestionPost(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    question = models.CharField(max_length=222)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ('post__date',)

'''
@QuestionPostResponse: Users response to question posts are entered as uniquely in this table
'''

class QuestionPostResponse(models.Model):
    user = models.ForeignKey('FutUser', on_delete=models.CASCADE)
    question_post = models.ForeignKey('QuestionPost', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_post.question
    

'''
@Like: A user can enter one post_id into this table. The total likes on a post
will be the count of post_id queried from this table
'''

class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT, null=False)
    user = models.ForeignKey('FutUser', on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.id
    class Meta:
        unique_together = ('post', 'user')


'''
@View: A user can enter one post_id into this table. The total views on a post
will be the count of post_id queried from this table. Also views by IP Address will be collated.
In the frontend, TrueView is a feature that returns views by IP Address. It is the count of 
query filtered by ip_address for a particular post
'''

class View(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT, null=False)
    ip_address = models.GenericIPAddressField(null=True)
    user = models.ForeignKey('FutUser', on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.id
    class Meta:
        unique_together = ('post', 'user')

'''
@Bookmark: Operates similarly to @Like
'''

class Bookmark(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT, null=False)
    user = models.ForeignKey('FutUser', on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.id
    class Meta:
        ordering = ['date']
        unique_together = ('post', 'user')

'''
@Republish: A user may add record of a post to this table only once
'''

class Republish(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT, null=False)
    user = models.ForeignKey('FutUser', on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post.id
    class Meta:
        unique_together = ('post', 'user')

'''
@Follow: A user may add another user's id to this table. both ids are unique for
a particular combination. Total follows for a users is the count of a queryall
on this table
'''

class Follow(models.Model):
    follower = models.ForeignKey('FutUser', on_delete=models.PROTECT, null=False, related_name='follower')
    followed = models.ForeignKey('FutUser', on_delete=models.PROTECT, null=False, related_name='followed')
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.follower.username
    class Meta:
        unique_together = ('follower', 'followed')

'''
@Message: this works a simple messaging feature that works on database rather than
socket
'''

class Message(models.Model):
    title = models.CharField(max_length=100)
    msg_sender = models.ForeignKey('FutUser', on_delete=models.PROTECT, related_name='sender')
    msg_receiver = models.ForeignKey('FutUser', on_delete=models.PROTECT, related_name='receiver')
    image = models.URLField()
    video = models.URLField()
    text = models.CharField(max_length=222)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['date']

'''
@Notification: Only admins may send notifications to users and notifications on behalf
of users
'''

class Notification(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    sender = models.ForeignKey('FutUser', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
