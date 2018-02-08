from django.db import models

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