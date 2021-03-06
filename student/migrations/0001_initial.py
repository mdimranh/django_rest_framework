# Generated by Django 3.2.9 on 2021-12-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=17)),
                ('profile', models.ImageField(upload_to='stu_img')),
                ('department', models.CharField(max_length=200)),
                ('term', models.IntegerField()),
                ('level', models.IntegerField()),
                ('student_id', models.CharField(max_length=50)),
                ('admission', models.DateTimeField()),
            ],
        ),
    ]
