# Generated by Django 3.1.1 on 2020-09-08 11:24

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_member', models.BooleanField(default=False, verbose_name='member status')),
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
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_description', models.TextField(max_length=1000)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('logo', models.ImageField(default='images/club_pic/logo/art.png', upload_to='images/club_pic/logo')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPresident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=300)),
                ('message', models.TextField(max_length=1000)),
                ('club', models.CharField(max_length=200)),
                ('sent_by', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('event_description', models.TextField(max_length=1000)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/club_pic/gallery')),
            ],
        ),
        migrations.CreateModel(
            name='MemberApplicationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('interest_reason', models.CharField(max_length=200)),
                ('resume', models.ImageField(blank=True, null=True, upload_to='images/resume')),
                ('email', models.EmailField(max_length=254)),
                ('club_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.club')),
            ],
        ),
        migrations.CreateModel(
            name='UserStaffs',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='club.user')),
                ('club_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='club.club')),
            ],
        ),
        migrations.CreateModel(
            name='UserMembers',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='club.user')),
                ('club_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.club')),
            ],
        ),
    ]
