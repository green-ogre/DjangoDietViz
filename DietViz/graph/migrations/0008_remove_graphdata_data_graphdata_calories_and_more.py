# Generated by Django 4.1.3 on 2023-09-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0007_alter_graphdata_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphdata',
            name='data',
        ),
        migrations.AddField(
            model_name='graphdata',
            name='calories',
            field=models.CharField(default='', max_length=365),
        ),
        migrations.AddField(
            model_name='graphdata',
            name='protein',
            field=models.CharField(default='', max_length=365),
        ),
        migrations.AddField(
            model_name='graphdata',
            name='weight',
            field=models.CharField(default='', max_length=365),
        ),
    ]
