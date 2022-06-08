# Generated by Django 3.2.12 on 2022-06-08 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('high', 'high'), ('middle', 'middle'), ('low', 'low')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_skill', models.ManyToManyField(through='skills.Knowledge', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='knowledge',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_knowledge', to='skills.skill'),
        ),
        migrations.AddField(
            model_name='knowledge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_knowledge', to=settings.AUTH_USER_MODEL),
        ),
    ]
