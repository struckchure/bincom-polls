# Generated by Django 3.2.9 on 2021-11-19 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga_id', models.PositiveBigIntegerField()),
                ('lga_name', models.CharField(max_length=50)),
                ('state_id', models.PositiveBigIntegerField()),
                ('lga_description', models.TextField(blank=True)),
                ('entered_by_user', models.CharField(max_length=50, null=True)),
                ('date_entered', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_id', models.PositiveBigIntegerField()),
                ('ward_id', models.PositiveBigIntegerField()),
                ('uniquewardid', models.PositiveBigIntegerField()),
                ('polling_unit_number', models.CharField(blank=True, max_length=50)),
                ('polling_unit_name', models.CharField(blank=True, max_length=50)),
                ('polling_unit_description', models.TextField(blank=True, null=True)),
                ('lat', models.CharField(blank=True, max_length=255)),
                ('long', models.CharField(blank=True, max_length=255)),
                ('entered_by_user', models.CharField(max_length=50, null=True)),
                ('date_entered', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=50, null=True)),
                ('lga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.lga')),
            ],
            options={
                'verbose_name': 'Poll unit',
                'verbose_name_plural': 'Poll unit',
            },
        ),
    ]
