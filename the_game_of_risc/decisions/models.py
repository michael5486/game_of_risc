from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_guesses = models.PositiveSmallIntegerField()
    num_correct_guesses = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{}".format(self.user)

class Adjudication(models.Model):
    digest = models.CharField(max_length=200)
    outcome = models.BooleanField()

    def __str__(self):
        return self.digest

class Decision(models.Model):
    adjudication_id = models.ForeignKey(Adjudication, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User)
    answer = models.BooleanField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.id)


