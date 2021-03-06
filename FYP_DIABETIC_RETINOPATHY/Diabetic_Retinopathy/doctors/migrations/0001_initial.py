# Generated by Django 2.2.1 on 2019-11-25 08:59

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_type', models.CharField(max_length=30)),
                ('mc_number', models.CharField(max_length=10)),
                ('doctor_address', models.CharField(max_length=100)),
                ('doctor_contact', models.CharField(max_length=20)),
                ('image', models.ImageField(default='default.jpg', upload_to='doctor-profiles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=10)),
                ('identity_number', models.CharField(max_length=15)),
                ('patient_address', models.CharField(max_length=50)),
                ('diagnosis_id', models.CharField(max_length=10)),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
