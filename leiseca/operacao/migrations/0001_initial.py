# Generated by Django 2.0.7 on 2018-07-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Efetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_servico', models.DateTimeField(verbose_name='date published')),
                ('chefe_civil', models.CharField(max_length=30)),
                ('chefe_militar', models.CharField(max_length=30)),
                ('segov_registro_um', models.CharField(max_length=30)),
                ('segov_registro_dois', models.CharField(max_length=30)),
                ('segov_filmagem', models.CharField(max_length=30)),
            ],
        ),
    ]
