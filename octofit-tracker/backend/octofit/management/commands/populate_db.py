from django.core.management.base import BaseCommand
from octofit.models import User, Team, Activity, Leaderboard, Workout
import json

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        print('Command class loaded successfully')
        with open('octofit_tracker/test_data.json') as f:
            data = json.load(f)

        # Populate Users
        for user_data in data['users']:
            User.objects.create(**user_data)

        # Populate Teams
        for team_data in data['teams']:
            members = User.objects.filter(username__in=team_data.pop('members'))
            team = Team.objects.create(**team_data)
            # Convert User objects to dictionaries for ArrayField compatibility
            team.members = [{'username': member.username, 'email': member.email} for member in members]
            team.save()

        # Populate Activities
        for activity_data in data['activities']:
            user = User.objects.get(username=activity_data.pop('user'))
            Activity.objects.create(user=user, **activity_data)

        # Populate Leaderboard
        for leaderboard_data in data['leaderboard']:
            team = Team.objects.get(name=leaderboard_data.pop('team'))
            Leaderboard.objects.create(team=team, **leaderboard_data)

        # Populate Workouts
        for workout_data in data['workouts']:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
