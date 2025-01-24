from django.db import models
from users.models import User


# Create your models here.
class Gym(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_gyms")

    def __str__(self):
        return self.name


class Entrance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    subscription = models.ForeignKey(
        "Subscription", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.user.email} entered {self.gym.name} at {self.timestamp}"


class GroupWorkout(models.Model):
    name = models.CharField(max_length=100)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="group_workouts"
    )
    participants = models.ManyToManyField(User, related_name="workouts")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class PersonalTrainingSession(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="personal_training_sessions"
    )
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="personal_training_sessions_as_client",
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Personal training session with {self.trainer.email} and {self.client.email} at {self.gym.name}"


class SubscriptionType(models.Model):
    name = models.CharField(max_length=100)
    validity_days = models.IntegerField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name="subscriptions")
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.email} - {self.subscription_type.name} at {self.gym.name}"


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    activation_time = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.email} - {self.subscription.subscription_type.name} (Active: {self.active})"
