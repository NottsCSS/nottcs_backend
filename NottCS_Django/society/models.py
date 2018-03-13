from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_desp = models.CharField(max_length=1000)
    event_start = models.DateTimeField(null=True,blank=True)
    event_end = models.DateTimeField(null=True ,blank=True)
    
    created_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    organizing_club = models.ForeignKey('Club', on_delete=models.PROTECT, null=True)
    organizing_chairman = models.ForeignKey('Member', on_delete=models.PROTECT, null=True)
    
    STATUS_CHOICES = (('PD', 'Pendding'),
    ('ST', 'Started'),
    ('ED', 'Ended'),
    ('CC', 'Cenceled'),)
    status = models.CharField(max_length=2, choices = STATUS_CHOICES , default = 'PD')
    
    image = models.ImageField(upload_to='media/Event/' , default='/default/noImage.png')
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    event_venue = models.CharField(max_length=200)
    
    class Meta:
        ordering = ('status','event_start')
        
    def __str__(self):
        return self.event_title

class Club(models.Model):
    club_name = models.CharField(max_length=200)
    club_desp = models.CharField(max_length=200)
    club_icon = models.ImageField(upload_to='media/Club/', default='/default/noImage.png')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('club_name',)
        
    def __str__(self):
        return self.club_name

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

class Participant(models.Model):
    user = models.CharField(max_length=50, null=False)
    #uses event_id as placeholder as the design of attendance table is not finalised
    event_id = models.CharField(max_length=50, null=False, default='None')
    
    ABSENT = 'ABSENT'
    PRESENT = 'PRESENT'
    ATTENDANCE_CHOICE = (
        (ABSENT, 'Absent'),
        (PRESENT, 'Present')
    ) 
    attendance = models.CharField(max_length=10, choices=ATTENDANCE_CHOICE, default=ABSENT)
    
    additional_info = models.TextField(blank=True)
    feedback = models.TextField(blank=True)
    
    def __str__(self):
        return self.user