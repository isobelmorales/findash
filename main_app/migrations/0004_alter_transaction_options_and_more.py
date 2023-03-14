# Generated by Django 4.1.7 on 2023-03-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_account'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='name',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='actual',
        ),
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('N', 'None'), ('A', 'Asset'), ('L', 'Liability')], default='N', max_length=1),
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='category',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ManyToManyField(to='main_app.account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ManyToManyField(to='main_app.budget'),
        ),
    ]
