# Generated by Django 3.1.1 on 2023-08-17 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Student')], default=1, max_length=1)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', main_app.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=20)),
                ('alternate_phone_no', models.CharField(max_length=20)),
                ('designation', models.CharField(choices=[('Assistant', 'Assistant'), ('Teacher', 'Teacher'), ('Faculty', 'Faculty')], max_length=100)),
                ('mon_sal', models.IntegerField(blank=True, null=True)),
                ('year_sal', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(default='', max_length=255)),
                ('subject_expertise', models.CharField(default='', max_length=100)),
                ('entitled_el', models.IntegerField(default=0)),
                ('form_copy', models.FileField(default='forms/default.png', upload_to='forms/')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('work_time_start', models.TimeField(blank=True, null=True)),
                ('work_time_end', models.TimeField(blank=True, null=True)),
                ('work_day_from', models.DateField(blank=True, null=True)),
                ('work_day_to', models.DateField(blank=True, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.BooleanField(default=False)),
                ('phone_no', models.CharField(max_length=20)),
                ('alternate_phone_no', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('handed', models.CharField(choices=[('Right', 'Right'), ('Left', 'Left'), ('Both', 'Both')], max_length=10)),
                ('admission_form_copy', models.FileField(default='admission_forms/default.png', upload_to='admission_forms/')),
                ('school_name', models.CharField(default='School Name', max_length=100)),
                ('date_of_birth', models.DateField(default='2000-01-01')),
                ('date_of_admission', models.DateField(default='2000-01-01')),
                ('batch_time', models.TimeField(default='00:00:00')),
                ('father_name', models.CharField(default='Father Name', max_length=100)),
                ('father_occupation', models.CharField(default='Father Occupation', max_length=100)),
                ('mother_name', models.CharField(default='Mother Name', max_length=100)),
                ('mother_occupation', models.CharField(default='Mother Occupation', max_length=100)),
                ('addmission_form_fees_paid', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.board')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.grade')),
                ('stream', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.stream')),
            ],
        ),
        migrations.CreateModel(
            name='StaffNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='staff_notes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shared_with', models.ManyToManyField(to='main_app.Staff')),
                ('uploaded_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='notes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('board', models.ManyToManyField(blank=True, to='main_app.Board')),
                ('grade', models.ManyToManyField(blank=True, to='main_app.Grade')),
                ('stream', models.ManyToManyField(blank=True, to='main_app.Stream')),
                ('uploaded_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('board', models.ManyToManyField(blank=True, to='main_app.Board')),
                ('grade', models.ManyToManyField(blank=True, to='main_app.Grade')),
                ('shared_with_staff', models.ManyToManyField(blank=True, to='main_app.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
