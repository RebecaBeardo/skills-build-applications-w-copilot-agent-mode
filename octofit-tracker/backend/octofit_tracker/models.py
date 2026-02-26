from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=20)
    motto = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    hero_alias = models.CharField(max_length=120)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.hero_alias


class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=120)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    performed_at = models.DateTimeField()

    class Meta:
        db_table = 'activities'


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']


class Workout(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=150)
    description = models.TextField()
    intensity = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'
