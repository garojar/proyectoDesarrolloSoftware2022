# Generated by Django 4.0.4 on 2022-05-04 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petclub', '0004_delete_b'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={},
        ),
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petclub.person'),
        ),
    ]
