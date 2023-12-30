# Generated by Django 3.2.23 on 2023-12-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Code', models.CharField(max_length=255)),
                ('Diagnosis_Code', models.IntegerField()),
                ('Full_Code', models.CharField(max_length=255)),
                ('Abbreviated_Description', models.CharField(max_length=255)),
                ('Full_Description', models.CharField(max_length=255)),
                ('Category_Title', models.CharField(max_length=255)),
            ],
        ),
    ]