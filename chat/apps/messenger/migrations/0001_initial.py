# Generated by Django 3.0.8 on 2020-07-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_author', models.CharField(max_length=20, verbose_name='автор')),
                ('message_text', models.TextField(verbose_name='сообщение')),
                ('message_time', models.DateTimeField(verbose_name='время отправки')),
            ],
        ),
    ]