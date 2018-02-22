from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_desp = models.CharField(max_length=1000)
    event_start = models.DateTimeField(null=True,blank=True)
    event_end = models.DateTimeField(null=True ,blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    #organizing_club = models.ForeignKey('Club', on_delete=models.PROTECT,)
    organizing_chairman = models.ForeignKey('Member', on_delete=models.PROTECT,)
    
    STATUS_CHOICES = (('PD', 'Pendding'),
    ('ST', 'Started'),
    ('ED', 'Ended'),
    ('CC', 'Cenceled'),)
    status = models.CharField(max_length=2, choices = STATUS_CHOICES , default = 'PD')
    
    image = models.ImageField(upload_to='media/Event/' , default='http://mattislist.com/marketingapp/postimage/noimageavailable.png')
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    event_venue = models.CharField(max_length=200)
    
    class Meta:
        ordering = ('status','event_start')
        
    def __str__(self):
        return self.event_title
    
class Member(models.Model):
    """This class represents the Member model."""
    user = models.CharField(max_length=50, blank=False, unique=True)
    """user = models.ForeignKey('enter foreign key here', on_delete=models.CASCADE)"""
    club = models.CharField(max_length=50, blank=False, unique=True)
    """club = models.ForeignKey('enter foreign key here', on_delete=models.CASCADE)"""
    status = models.CharField(max_length=50, blank=False, unique=True)
    position = models.CharField(max_length=50, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.user)