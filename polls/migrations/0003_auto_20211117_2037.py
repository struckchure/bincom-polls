# Generated by Django 3.2.9 on 2021-11-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_pollunit_user_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollunit',
            name='date_entered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='pollunit',
            name='entered_by_user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pollunit',
            name='polling_unit_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pollunit',
            name='user_ip_address',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
