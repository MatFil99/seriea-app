# Generated by Django 4.2.5 on 2023-10-21 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("footballstats", "0005_rename_stadium_id_club_stadium_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="match",
            name="guest_team",
        ),
        migrations.RemoveField(
            model_name="match",
            name="home_team",
        ),
        migrations.RemoveField(
            model_name="match",
            name="season",
        ),
        migrations.RemoveField(
            model_name="matchaction",
            name="match_player_id",
        ),
        migrations.RemoveField(
            model_name="matchplayer",
            name="match_id",
        ),
        migrations.RemoveField(
            model_name="matchplayer",
            name="player_id",
        ),
        migrations.RemoveField(
            model_name="playerclubofseason",
            name="club",
        ),
        migrations.RemoveField(
            model_name="playerclubofseason",
            name="player",
        ),
        migrations.RemoveField(
            model_name="playerclubofseason",
            name="season",
        ),
        migrations.DeleteModel(
            name="Club",
        ),
        migrations.DeleteModel(
            name="Match",
        ),
        migrations.DeleteModel(
            name="MatchAction",
        ),
        migrations.DeleteModel(
            name="MatchPlayer",
        ),
        migrations.DeleteModel(
            name="Player",
        ),
        migrations.DeleteModel(
            name="PlayerClubOfSeason",
        ),
        migrations.DeleteModel(
            name="Season",
        ),
        migrations.DeleteModel(
            name="Stadium",
        ),
    ]
