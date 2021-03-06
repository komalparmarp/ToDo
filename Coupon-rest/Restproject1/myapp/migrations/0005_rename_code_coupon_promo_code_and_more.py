# Generated by Django 4.0.1 on 2022-01-25 08:01

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_coupon_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='code',
            new_name='promo_code',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start_date',
            field=models.DateTimeField(validators=[myapp.models.Coupon.start_date]),
        ),
    ]
