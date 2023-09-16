# Generated by Django 4.0.4 on 2023-09-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(blank=True, max_length=100)),
                ('Date', models.DateField()),
                ('Completed', models.BooleanField(default=False)),
            ],
        ),
    ]