
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200708_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='sellername',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.CharField(default='', max_length=300),
       
       
       
        ),
    ]




