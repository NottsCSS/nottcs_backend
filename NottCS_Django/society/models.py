from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
  
    created_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    organizing_club = models.ForeignKey('Club', on_delete=models.PROTECT, null=True)
    organizing_chairman = models.ForeignKey('Member', on_delete=models.PROTECT, null=True)
    
    STATUS_CHOICES = (('PD', 'Pendding'),
    ('ST', 'Started'),
    ('ED', 'Ended'),
    ('CC', 'Cenceled'),)
    status = models.CharField(max_length=2, choices = STATUS_CHOICES , default = 'PD')
    
    image = models.ImageField(upload_to='media/Event/' , default='/media/Default/noImage.png')
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    venue = models.CharField(max_length=200)
    
    class Meta:
        ordering = ('status',)
        
    def __str__(self):
        return self.title

class EventTime(models.Model):
    event = models.ForeignKey('Event', on_delete=models.PROTECT, null=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    class Meta:
        ordering = ('start_time',)
        
    def __str__(self):
        return str(self.event) + "(" + str(self.start_time.date()) + ")"


class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='media/Club/', default='/media/Default/noImage.png')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

class Member(models.Model):
    """This class represents the Member model."""
    
    user = models.ForeignKey('azureAD_auth.AzureADUser', on_delete=models.PROTECT, null=True)
    club = models.ForeignKey('Club', on_delete=models.PROTECT, null=True)
    status = models.CharField(max_length=50, blank=False, unique=True)
    position = models.CharField(max_length=50, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.user)

class Participant(models.Model):
    user = models.ForeignKey('azureAD_auth.AzureADUser', on_delete=models.PROTECT, null=True)
    #uses event_id as placeholder as the design of attendance table is not finalised
    event = models.ForeignKey('Event', on_delete=models.PROTECT, null=True)
    
    additional_file = models.FileField(upload_to='media/etc/', null =True)
    additional_info = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.event) +":" + str(self.user)

class Attendance(models.Model):
    participant = models.ForeignKey('Participant', on_delete=models.PROTECT, null=True)
    #uses event_id as placeholder as the design of attendance table is not finalised
    event_time = models.ForeignKey('EventTime', on_delete=models.PROTECT, null=True)

    ABSENT = 'ABSENT'
    PRESENT = 'PRESENT'

    ATTENDANCE_CHOICE = (
        (ABSENT, 'Absent'),
        (PRESENT, 'Present')
    ) 
    attendance = models.CharField(max_length=10, choices=ATTENDANCE_CHOICE, default=ABSENT)
    feedback = models.TextField(blank=True, default="")
    def __str__(self):
        return str(self.participant) + ":" + str(self.event_time)
