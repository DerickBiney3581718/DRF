# Generated by Django 4.0.10 on 2023-07-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='content')),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15, verbose_name='price')),
            ],
        ),
    ]
