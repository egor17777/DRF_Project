# Generated by Django 4.0 on 2022-09-09 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='user'),
            preserve_default=False,
        ),
    ]