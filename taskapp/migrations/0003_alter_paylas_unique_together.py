# Generated by Django 3.2.9 on 2021-11-15 07:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskapp', '0002_alter_fayl_muellif'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='paylas',
            unique_together={('kimle', 'fayl')},
        ),
    ]
