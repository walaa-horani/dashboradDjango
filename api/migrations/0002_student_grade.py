# Generated by Django 5.0 on 2023-12-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
