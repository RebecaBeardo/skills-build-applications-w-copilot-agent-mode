from django.db import IntegrityError
from django.test import TestCase

from .models import Team, UserProfile


class UserProfileTests(TestCase):
    def test_email_must_be_unique(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        UserProfile.objects.create(
            name='Hero One',
            email='hero@example.com',
            hero_alias='Hero1',
            team=team,
        )

        with self.assertRaises(IntegrityError):
            UserProfile.objects.create(
                name='Hero Two',
                email='hero@example.com',
                hero_alias='Hero2',
                team=team,
            )
