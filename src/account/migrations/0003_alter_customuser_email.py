# Generated by Django 4.2.2 on 2023-06-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]