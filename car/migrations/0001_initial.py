# Generated by Django 5.0.4 on 2024-04-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.UUIDField(auto_created=True, default='745fb1e0-bbbb-40e3-be1f-58eb4ebc5efd', editable=False, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('car_year', models.IntegerField()),
                ('color', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=1024)),
                ('motor_detail', models.CharField(max_length=1024)),
                ('fuel', models.CharField(choices=[('GASOLINE', 'Gasoline'), ('ALCHOHOL', 'Alcool'), ('DIESEL', 'Diesel')], max_length=10)),
                ('kilometers', models.DecimalField(decimal_places=2, max_digits=10)),
                ('version', models.CharField(max_length=24)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('model', models.CharField(default='new', max_length=20)),
                ('car_type', models.CharField(choices=[('AUTOMATIC', 'Automatico'), ('MANUAL', 'Manual')], max_length=10)),
                ('situation', models.CharField(default='new', max_length=10)),
                ('photo_car', models.ImageField(blank=True, upload_to='photos/')),
            ],
        ),
    ]
