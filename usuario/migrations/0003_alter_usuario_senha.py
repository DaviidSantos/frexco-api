# Generated by Django 4.1.3 on 2022-11-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
