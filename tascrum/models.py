from django.db import models
from Auth.models import User
import uuid
from django.core.exceptions import ValidationError



class Member(models.Model):

    occupations_choice = (
    ('Student','Student'),
    ('Employee','Employee'),
    ('Project Manager','Project Manager'),
    ('Other','Other'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='users',null=False)\
    
    occupations = models.CharField(max_length=255,null=False,choices=occupations_choice)
    bio = models.TextField(null=True)
    profimage = models.ImageField(upload_to='Member/Profile',null=True,default='default_profile.png')
    birthdate = models.DateField(null=True)



class Workspace(models.Model):
    
    workspace_choice = (
    ('operations','operations'),
    ('education','education'),
    ('human resources','human resources'),
    ('small business','small business'),
    ('sales crm','sales crm'),
    ('engineering','engineering'),
    ('marketing','marketing'),
    ('Other','Other'),
    )
    
    name = models.CharField(max_length=255,null=True)
    type = models.CharField(max_length=20,choices=workspace_choice)
    description = models.TextField(null=True)
    members = models.ManyToManyField(Member, through='MemberWorkspaceRole', related_name='wmembers')
    backgroundimage = models.ImageField(upload_to='images/',default='default_profile.png')

class MemberWorkspaceRole(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='mrole')
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE,related_name='wrole')
    role = models.CharField(max_length=50)


class Board(models.Model):
    title = models.CharField(max_length=255,null=False)
    workspace = models.ForeignKey(Workspace,on_delete=models.CASCADE,related_name='wboard')
    members = models.ManyToManyField(Member, through='MemberBoardRole',related_name='bmembers')
    has_star = models.BooleanField(default=False)
    invitation_link = models.CharField(max_length=255, default=uuid.uuid4, unique=True)
    backgroundimage = models.ImageField(upload_to='images/',default='default_profile.png')
    lastseen = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        if not self.invitation_link:
            self.invitation_link = str(uuid.uuid4())
        super(Board, self).save(*args, **kwargs)

class MemberBoardRole(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='bmember')
    board = models.ForeignKey(Board, on_delete=models.CASCADE,related_name='brole')
    role = models.CharField(max_length=50,default='member')


class Meeting(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='Mmember')
    board = models.ForeignKey(Board,on_delete=models.CASCADE,related_name='mboard')
    title = models.CharField(max_length=255,null=False,default='meeting')
    time = models.DateTimeField(null=False)

    class Meta:
        ordering = ['time']
        # unique_together = ('board', 'time',)


class List(models.Model):
    title = models.CharField(max_length=255,null=False)
    board = models.ForeignKey(Board,on_delete=models.CASCADE,related_name='lboard')

class Lable(models.Model):
    color = models.CharField(max_length=30, null=False)
    title = models.CharField(max_length=30, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='boardl')

class Card(models.Model):
    title = models.CharField(max_length=255,null=False)
    list = models.ForeignKey(List,on_delete=models.CASCADE,related_name='clist')
    members = models.ManyToManyField(Member, through='MemberCardRole',related_name='cmembers')
    startdate = models.DateTimeField(null=True)
    duedate = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    storypoint = models.IntegerField(default=0)
    setestimate = models.IntegerField(default=0)
    reminder_choice =(
    ('At time of due date','At time of due date'),
    ('1 Day before','1 Day before'),
    ('2 Day before','2 Day before'),
    ('3 Day before','3 Day before'),
    ('5 Days before','5 Days before'),
    ('None','None'),
    ) 
    reminder = models.CharField(max_length=30,choices=reminder_choice , default='1 Day before')
    order = models.IntegerField(null=True,auto_created=True)
    labels = models.ManyToManyField(Lable, through='CardLabel', related_name='clabel')
    comment = models.CharField(max_length=255,null=True)
    status_choice = (
    ('Done','Done'),
    ('overdue','overdue'),
    ('pending','pending'),
    ('failed','failed'),
    )
    status = models.CharField(max_length=8,choices=status_choice,default='pending')

    class Meta:
        ordering = ('order',)
        # unique_together = ('list', 'order',)
    
    def save(self, *args, **kwargs):
        if self.startdate and self.duedate and self.startdate <= self.duedate:
            raise ValidationError("Due date must be after start date.")
            
        if not self.order:
            max_order_in_list = Card.objects.filter(list=self.list).aggregate(models.Max('order'))['order__max']
            if max_order_in_list is not None:
                self.order = max_order_in_list + 1
            else:
                self.order = 1
        super().save(*args, **kwargs)


class CardLabel(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='cardl')
    label = models.ForeignKey(Lable, on_delete=models.CASCADE, related_name='labelc')
    class Meta:
        unique_together = ('card', 'label')
        ordering = ['label']

class Checklist(models.Model):
    title = models.CharField(max_length=60, null=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='chcard')

class Item(models.Model):
    content = models.CharField(max_length=255, null=True)
    checked = models.BooleanField(default=False)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='ichecklist')

class MemberCardRole(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='cmember')
    card = models.ForeignKey(Card, on_delete=models.CASCADE,related_name='crole')
    role = models.CharField(max_length=50,default='member')
    class Meta:
        ordering = ['member']
    
class BurndownChart(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='burndown_charts')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='burndown_charts')
    date = models.DateField(null=False)
    done = models.FloatField(default=0)
    estimate = models.FloatField(default=0)

class Question(models.Model):
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class Survey(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, through='SurveyQuestion',related_name='survey')

class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Chatbot(models.Model):
    request_message = models.CharField(max_length=500)
     
