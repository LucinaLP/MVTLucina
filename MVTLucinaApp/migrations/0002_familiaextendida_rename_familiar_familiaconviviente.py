# Generated by Django 4.0.5 on 2022-06-16 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVTLucinaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaExtendida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('parentezco', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Familiar',
            new_name='FamiliaConviviente',
        ),
    ]
