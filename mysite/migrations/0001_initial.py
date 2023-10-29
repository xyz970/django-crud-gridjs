# Generated by Django 4.2.6 on 2023-10-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=50)),
                ('published_date', models.DateField()),
                ('author', models.CharField(max_length=50)),
                ('cover', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
    ]