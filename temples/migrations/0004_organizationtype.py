# Generated by Django 5.0.3 on 2024-03-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("temples", "0003_alter_event_organizer"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganizationType",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        help_text="The type of the organization.", max_length=50
                    ),
                ),
            ],
        ),
    ]