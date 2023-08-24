# Generated by Django 4.2.4 on 2023-08-24 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='rental_period',
            new_name='retal_period',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rental_price_per_day',
        ),
        migrations.AddField(
            model_name='book',
            name='retal_price_day',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='total_render',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo_author',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo_book',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('rented', 'rented'), ('sold', 'sold')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]