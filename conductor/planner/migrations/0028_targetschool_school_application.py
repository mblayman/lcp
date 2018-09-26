# Generated by Django 2.0.6 on 2018-09-25 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("planner", "0027_schoolapplication")]

    operations = [
        migrations.AddField(
            model_name="targetschool",
            name="school_application",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="planner.SchoolApplication",
            ),
        )
    ]
