# Generated by Django 4.2.4 on 2023-08-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='reservation_slot',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='menu_item_description',
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
    ]
