# Generated by Django 3.2.8 on 2021-11-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='name',
            field=models.CharField(default=0, max_length=64, unique=True, verbose_name='название'),
            preserve_default=False,
        ),
    ]