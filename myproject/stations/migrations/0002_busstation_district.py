# Generated by Django 4.2.5 on 2023-09-20 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='busstation',
            name='district',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
