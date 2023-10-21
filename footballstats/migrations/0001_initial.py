# Generated by Django 4.2.5 on 2023-10-18 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Club",
            fields=[
                ("club_id", models.AutoField(primary_key=True, serialize=False)),
                ("club_name", models.CharField(max_length=100, null=True)),
                ("headquarter", models.CharField(max_length=100, null=True)),
                ("website", models.URLField(null=True)),
                ("president", models.CharField(max_length=150, null=True)),
                ("coach", models.CharField(max_length=150, null=True)),
                ("assistant_coach", models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                ("match_id", models.AutoField(primary_key=True, serialize=False)),
                ("referee", models.CharField(max_length=100, null=True)),
                ("date", models.DateField(null=True)),
                (
                    "guest_team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="guest_matches",
                        to="footballstats.club",
                    ),
                ),
                (
                    "home_team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_matches",
                        to="footballstats.club",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                ("player_id", models.AutoField(primary_key=True, serialize=False)),
                ("firstname", models.CharField(max_length=100, null=True)),
                ("surname", models.CharField(max_length=100, null=True)),
                ("role", models.CharField(max_length=50, null=True)),
                ("date_of_birth", models.DateField(null=True)),
                ("nationality", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SeasonPart",
            fields=[
                ("season_part_id", models.AutoField(primary_key=True, serialize=False)),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
                ("season_part", models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Stadium",
            fields=[
                ("stadium_id", models.AutoField(primary_key=True, serialize=False)),
                ("stadium_name", models.CharField(max_length=100, null=True)),
                ("capacity", models.PositiveIntegerField(null=True)),
                ("guest_sector_capacity", models.PositiveIntegerField(null=True)),
                ("year_of_construction", models.PositiveIntegerField(null=True)),
                ("city", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="MatchPlayer",
            fields=[
                (
                    "match_player_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "match",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="footballstats.match",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="footballstats.player",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MatchAction",
            fields=[
                (
                    "match_action_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("action", models.CharField(max_length=100, null=True)),
                (
                    "match_player",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="footballstats.matchplayer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="match",
            name="season_part",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="footballstats.seasonpart",
            ),
        ),
        migrations.AddField(
            model_name="club",
            name="stadium",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="footballstats.stadium",
            ),
        ),
    ]
