# Generated by Django 4.1.3 on 2022-12-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='abcd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]