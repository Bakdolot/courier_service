# Generated by Django 4.0.1 on 2022-01-15 09:05

import account.managers
import account.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_2gis_maps.fields
import django_2gis_maps.mixins


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
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(error_messages={'unique': 'A user with that phone number already exists.'}, help_text='Required. 9 digits in format: 996*********** without "+".', max_length=15, unique=True, validators=[account.validators.PhoneValidator], verbose_name='user phone number')),
                ('email', models.CharField(max_length=30, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('patronymic', models.CharField(max_length=30, verbose_name='patronymic')),
                ('points', models.PositiveIntegerField(default=0, verbose_name='user bonus points')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', account.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django_2gis_maps.fields.AddressField(max_length=100, verbose_name='name')),
                ('geolocation', django_2gis_maps.fields.GeoLocationField(verbose_name='geolocation')),
            ],
            bases=(django_2gis_maps.mixins.DoubleGisMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(verbose_name='sum')),
                ('payment_type', models.PositiveSmallIntegerField(choices=[(1, 'credit'), (2, 'debit')], verbose_name='payment type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(verbose_name='sum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django_2gis_maps.fields.AddressField(max_length=100, verbose_name='name')),
                ('geolocation', django_2gis_maps.fields.GeoLocationField(verbose_name='geolocation')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.region', verbose_name='region')),
            ],
            bases=(django_2gis_maps.mixins.DoubleGisMixin, models.Model),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.city', verbose_name='city'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.region', verbose_name='region'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
