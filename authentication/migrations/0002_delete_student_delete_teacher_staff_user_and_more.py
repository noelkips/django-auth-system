# Generated by Django 4.1.7 on 2023-02-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authentication.useraccount',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authentication.useraccount',),
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='student',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='teacher',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='type',
            field=models.CharField(choices=[('USER', 'user'), ('STAFF', 'staff'), ('ADMIN', 'admin')], default='ADMIN', max_length=20),
        ),
    ]
