# Generated by Django 3.0.5 on 2020-04-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_pace_of_losing_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('M', 'Man'), ('W', 'Woman')], default='M', max_length=1),
        ),
    ]