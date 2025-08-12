from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("crm", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Proposal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(choices=[("DRAFT", "Draft"), ("FINAL", "Final")], default="DRAFT", max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("advisor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="proposals", to="users.user")),
                ("client", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="proposals", to="crm.client")),
            ],
        ),
        migrations.CreateModel(
            name="ProposalItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fund_name", models.CharField(max_length=200)),
                ("allocation_percent", models.DecimalField(decimal_places=2, max_digits=5)),
                ("proposal", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="proposals.proposal")),
            ],
        ),
    ]