# Generated by Django 5.1 on 2024-10-17 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_ticket_booked_time_ticket_ticket_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='booked_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 17, 55, 26, 701491, tzinfo=datetime.timezone.utc)),
        ),
    ]
