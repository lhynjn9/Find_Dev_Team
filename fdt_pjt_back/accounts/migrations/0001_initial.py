# Generated by Django 3.2.12 on 2022-06-12 06:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sex', models.CharField(choices=[('male', '남'), ('female', '여')], max_length=10)),
                ('region', models.CharField(choices=[('seoul', '서울'), ('daejeon', '대전'), ('kwang', '광주'), ('bu', '부울경'), ('gu', '구미')], max_length=30)),
                ('position', models.CharField(choices=[('back', '백엔드'), ('front', '프론트엔드')], max_length=30)),
                ('major', models.CharField(choices=[('yes', '전공'), ('no', '비전공')], max_length=30)),
                ('group', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('img', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('intro', models.CharField(blank=True, max_length=200, null=True)),
                ('kakao_chat', models.CharField(blank=True, max_length=50, null=True)),
                ('github_url', models.CharField(blank=True, max_length=200, null=True)),
                ('portfolio_url', models.CharField(blank=True, max_length=200, null=True)),
                ('strength', models.CharField(blank=True, max_length=50, null=True)),
                ('bookmarking', models.ManyToManyField(blank=True, related_name='bookmarked_users', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
