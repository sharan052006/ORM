# Generated by Django 5.1.2 on 2024-10-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankLoan',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('Account_No', models.IntegerField(primary_key='Account_No', serialize=False)),
                ('Phone_Number', models.IntegerField()),
                ('Aadhar_No', models.IntegerField()),
                ('Loan_amount', models.FloatField()),
                ('Time_Period', models.IntegerField()),
            ],
        ),
    ]
