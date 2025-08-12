import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from crm.models import Client


class Command(BaseCommand):
    help = "Seed demo data for advisors and clients"

    def handle(self, *args, **options):
        User = get_user_model()
        data_path = Path(__file__).resolve().parents[3] / "backend_seed_data.json"
        if not data_path.exists():
            data_path = Path(__file__).resolve().parents[4] / "backend" / "backend_seed_data.json"
        with open(data_path) as f:
            data = json.load(f)

        advisors = data.get("advisors", [])
        for adv in advisors:
            username = adv["username"]
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=adv.get("email", ""),
                    password=adv["password"],
                    first_name=adv.get("first_name", ""),
                    last_name=adv.get("last_name", ""),
                )
                if adv.get("role"):
                    user.role = adv["role"]
                    user.is_staff = True if adv["role"] == "ADMIN" else False
                    user.is_superuser = True if adv["role"] == "ADMIN" else False
                    user.save()
                self.stdout.write(self.style.SUCCESS(f"Created user {username}"))
            else:
                self.stdout.write(f"User {username} exists")

        advisor = User.objects.filter(role="ADVISOR").first()
        if advisor:
            for c in data.get("clients", []):
                Client.objects.get_or_create(advisor=advisor, name=c["name"], defaults=c)
            self.stdout.write(self.style.SUCCESS("Seeded clients"))
        else:
            self.stdout.write(self.style.WARNING("No advisor found to assign clients"))