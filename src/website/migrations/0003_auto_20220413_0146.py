# Generated by Django 3.1.2 on 2022-04-12 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_scanimage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanimage',
            name='user',
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sessions',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='scanimage',
            name='session',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.session'),
        ),
    ]
