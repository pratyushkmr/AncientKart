# Generated by Django 3.0.2 on 2020-02-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200222_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['price']},
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('V', 'Vintage'), ('A', 'Antique')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'Indian'), ('I', 'International')], max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
