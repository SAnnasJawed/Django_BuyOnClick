# Generated by Django 3.2.5 on 2021-09-14 05:13

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
                ('product_Name', models.CharField(max_length=50)),
                ('product_Price', models.IntegerField(default=0)),
                ('product_Description', models.CharField(default='', max_length=200)),
                ('product_Image', models.ImageField(upload_to='media/store/')),
            ],
        ),
    ]