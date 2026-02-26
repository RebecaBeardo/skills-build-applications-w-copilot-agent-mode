from django.core.management.base import BaseCommand
from django.utils import timezone

from octofit_tracker.models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        Workout.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        team_marvel = Team.objects.create(
            name='Team Marvel',
            universe='Marvel',
            motto='Avengers Assemble',
        )
        team_dc = Team.objects.create(
            name='Team DC',
            universe='DC',
            motto='Justice For All',
        )

        users = [
            UserProfile.objects.create(
                name='Peter Parker',
                email='spiderman@octofit.com',
                hero_alias='Spider-Man',
                team=team_marvel,
            ),
            UserProfile.objects.create(
                name='Tony Stark',
                email='ironman@octofit.com',
                hero_alias='Iron Man',
                team=team_marvel,
            ),
            UserProfile.objects.create(
                name='Diana Prince',
                email='wonderwoman@octofit.com',
                hero_alias='Wonder Woman',
                team=team_dc,
            ),
            UserProfile.objects.create(
                name='Bruce Wayne',
                email='batman@octofit.com',
                hero_alias='Batman',
                team=team_dc,
            ),
        ]

        now = timezone.now()
        activity_templates = [
            ('Web Swinging Cardio', 45, 420),
            ('Armor HIIT', 30, 360),
            ('Lasso Strength Circuit', 40, 390),
            ('Night Patrol Run', 35, 340),
        ]

        for user, template in zip(users, activity_templates):
            activity_type, duration_minutes, calories_burned = template
            Activity.objects.create(
                user=user,
                activity_type=activity_type,
                duration_minutes=duration_minutes,
                calories_burned=calories_burned,
                performed_at=now,
            )

        leaderboard_scores = [980, 940, 920, 900]
        for rank, user in enumerate(users, start=1):
            LeaderboardEntry.objects.create(
                user=user,
                score=leaderboard_scores[rank - 1],
                rank=rank,
            )

        workout_templates = [
            ('Spider Agility Routine', 'Plyometrics and grip training', 'Medium'),
            ('Arc Reactor Endurance', 'Intervals and loaded carries', 'Hard'),
            ('Amazon Power Flow', 'Strength and mobility sequence', 'Medium'),
            ('Gotham Tactical Conditioning', 'Sprints and core stabilization', 'Hard'),
        ]

        for user, workout in zip(users, workout_templates):
            title, description, intensity = workout
            Workout.objects.create(
                user=user,
                title=title,
                description=description,
                intensity=intensity,
            )

        self.stdout.write(self.style.SUCCESS('octofit_db test data populated successfully.'))
