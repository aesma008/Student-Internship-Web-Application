from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='/profile_pics/default_profile_picture.jpg')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who posts the review
    title = models.CharField(max_length=255)  # Title of the review
    company_name = models.CharField(max_length=255)  # Company name
    description = models.TextField()  # Description of the internship
    overall_experience = models.TextField()  # Overall experience of the internship
    skills_required = models.TextField()  # Skills required for the internship
    skills_learned = models.TextField()  # Skills learned during the internship
    duration = models.CharField(max_length=50)  # Duration of the internship
    compensation = models.CharField(max_length=100)  # Compensation details
    location = models.CharField(max_length=255)  # Location of the internship
    rating = models.PositiveIntegerField()  # Rating (e.g., 1-5)
    opinion = models.TextField()  # Opinion text
    date_posted = models.DateTimeField(auto_now_add=True)  # Timestamp of when the review was posted
    
    def __str__(self):
        return f"{self.company_name} - {self.user.username}"
