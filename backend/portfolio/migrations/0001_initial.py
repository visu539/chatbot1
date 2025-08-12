from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("crm", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150)),
                ("type", models.CharField(blank=True, max_length=50)),
                ("client", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="accounts", to="crm.client")),
            ],
        ),
        migrations.CreateModel(
            name="Holding",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fund_name", models.CharField(max_length=200)),
                ("units", models.DecimalField(decimal_places=4, default=0, max_digits=18)),
                ("average_cost", models.DecimalField(decimal_places=4, default=0, max_digits=14)),
                ("current_nav", models.DecimalField(decimal_places=4, default=0, max_digits=14)),
                ("account", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="holdings", to="portfolio.account")),
            ],
        ),
        migrations.CreateModel(
            name="SIP",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fund_name", models.CharField(max_length=200)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=14)),
                ("day_of_month", models.PositiveSmallIntegerField(default=1)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("account", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="sips", to="portfolio.account")),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fund_name", models.CharField(max_length=200)),
                ("type", models.CharField(choices=[("BUY", "Buy"), ("SELL", "Sell")], max_length=10)),
                ("units", models.DecimalField(decimal_places=4, max_digits=18)),
                ("nav", models.DecimalField(decimal_places=4, max_digits=14)),
                ("date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("account", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="transactions", to="portfolio.account")),
            ],
        ),
    ]