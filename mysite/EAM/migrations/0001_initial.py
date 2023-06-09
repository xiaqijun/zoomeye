# Generated by Django 4.1.3 on 2022-11-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30)),
                ('region', models.CharField(blank=True, max_length=30, null=True)),
                ('area', models.CharField(blank=True, max_length=30, null=True)),
                ('asset', models.CharField(blank=True, max_length=30, null=True)),
                ('product_name', models.CharField(blank=True, max_length=30, null=True)),
                ('system_classification', models.CharField(blank=True, max_length=30, null=True)),
                ('system_grading', models.CharField(blank=True, max_length=30, null=True)),
                ('administrator', models.CharField(blank=True, max_length=30, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
