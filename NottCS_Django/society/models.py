from django.db import models
# from django.contrib.postgres.fields import JSONField


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    organizing_club = models.ForeignKey(
        'Club', on_delete=models.PROTECT, null=True)
    organizing_chairman = models.ForeignKey(
        'Member', on_delete=models.PROTECT, null=True)
    fees = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    STATUS_CHOICES = ((0, 'Pending'),
                      (1, 'Started'),
                      (3, 'Ended'),
                      (4, 'Cancelled'),)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    image = models.ImageField(upload_to='media/Event/',
                              default='/media/Default/noImage.png')
    venue = models.CharField(max_length=200)
    additional_info = models.TextField(blank=True)
    # addtional_info = JSONField()

    class Meta:
        ordering = ('status',)

    def __str__(self):
        return self.title


class EventTime(models.Model):
    event = models.ForeignKey('Event', on_delete=models.PROTECT, null=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    class Meta:
        ordering = ('start_time',)

    def __str__(self):
        return str(self.event) + "(" + str(self.start_time.date()) + ")"


class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='media/Club/',
                             default='/media/Default/noImage.png')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.ForeignKey('azureAD_auth.AzureADUser',
                             on_delete=models.PROTECT, null=True)
    club = models.ForeignKey('Club', on_delete=models.PROTECT, null=True)
    position = models.CharField(max_length=50, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = ((0, 'Pending'), (1, 'Approved'), (2, 'Cancelled'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return "{}".format(self.user)


class Participant(models.Model):
    user = models.ForeignKey('azureAD_auth.AzureADUser',
                             on_delete=models.PROTECT)
    event = models.ForeignKey('Event', on_delete=models.PROTECT)
    additional_file = models.FileField(upload_to='media/etc/', blank=True)
    additional_info = models.TextField(blank=True)
    STATUS_CHOICES = ((0, 'Pending'), (1, 'Approved'), (2, 'Cancelled'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        unique_together = ('user', 'event',)

    def __str__(self):
        return str(self.event) + ":" + str(self.user)


class Attendance(models.Model):
    participant = models.ForeignKey(
        'Participant', on_delete=models.PROTECT, null=True)
    event_time = models.ForeignKey(
        'EventTime', on_delete=models.PROTECT, null=True)

    ATTENDANCE_CHOICE = ((0, 'Absent'), (1, 'Present'))
    attendance = models.IntegerField(choices=ATTENDANCE_CHOICE, default=0)
    feedback = models.TextField(blank=True, default="")

    def __str__(self):
        return str(self.participant) + ":" + str(self.event_time)
