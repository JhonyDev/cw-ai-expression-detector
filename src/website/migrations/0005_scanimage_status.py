# Generated by Django 3.1.2 on 2022-03-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20220309_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanimage',
            name='status',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
