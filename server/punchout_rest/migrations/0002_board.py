# Generated by Django 4.1.6 on 2023-02-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punchout_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('b', 'Built-in'), ('u', 'User defined')], max_length=1)),
            ],
        ),
    ]