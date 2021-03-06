# Generated by Django 4.0.3 on 2022-04-08 15:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('key', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('session_id', models.UUIDField(db_index=True, editable=False, unique=True)),
                ('category', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('data', models.JSONField()),
                ('timestamp', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.application')),
            ],
        ),
    ]
