# Generated by Django 4.1.3 on 2022-11-11 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_alter_departure_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Город прибытия')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours', to='tours.destination', verbose_name='Город прибытия'),
        ),
    ]