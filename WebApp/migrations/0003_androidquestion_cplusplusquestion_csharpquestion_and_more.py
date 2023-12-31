# Generated by Django 4.0.3 on 2022-05-05 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebApp', '0002_meetphpexpert'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CplusplusQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CsharpQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FlutterQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JavaQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JavaScriptQuestion1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JavaScriptQuestion2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JavaScriptQuestion3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JavaScriptQuestion4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PhpQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PythonQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReactnativeQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=200)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='meetphpexpert',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='MeetPhp Images/'),
        ),
        migrations.CreateModel(
            name='PhpVideoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('video', models.FileField(upload_to='phpVideo/')),
                ('create_at', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
