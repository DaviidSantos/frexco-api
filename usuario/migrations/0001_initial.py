# Generated by Django 4.1.3 on 2022-11-14 16:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=8)),
                ('dataDeNascimento', models.DateField()),
            ],
        ),
    ]