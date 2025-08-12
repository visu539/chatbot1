from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("contact", models.CharField(blank=True, max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("stage", models.CharField(blank=True, max_length=100)),
                ("probability", models.PositiveIntegerField(default=0)),
                ("expected_investment", models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("advisor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="clients", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Lead",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("contact", models.CharField(blank=True, max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("stage", models.CharField(blank=True, max_length=100)),
                ("probability", models.PositiveIntegerField(default=0)),
                ("expected_investment", models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("advisor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="leads", to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]