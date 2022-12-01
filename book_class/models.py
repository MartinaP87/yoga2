from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date

DAY_SLOT = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)
TIME_SLOT = (
    ("9:00 - 10:00", "9:00 - 10:00"),
    ("10:00 - 11:00", "10:00 - 11:00"),
    ("11:00 - 12:00", "11:00 - 12:00"),
    ("14:00 - 15:00", "14:00 - 15:00"),
    ("15:00 - 16:00", "15:00 - 16:00"),
    ("16:00 - 17:00", "16:00 - 17:00"),
    ("17:00 - 18:00", "17:00 - 18:00"),
    ("20:00 - 21:00", "20:00 - 21:00"),
    )
STATUS = ((0, "Draft"), (1, "Published"))


class YogaType(models.Model):
    title = models.CharField(
        max_length=90, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    introduction = models.CharField(
        max_length=300, blank=False, default="intro")
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class YogaClass(models.Model):
    yoga_type = models.ForeignKey(
        YogaType, on_delete=models.CASCADE, related_name="chosen_type"
    )
    days = models.DateField(null=False, blank=False, default=date.today)
    times = models.CharField(
         max_length=15, choices=TIME_SLOT, default="9:00 - 10:00", null=False)
    available_spaces = models.IntegerField(default=20)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return str(self.yoga_type)


class Reservation(models.Model):
    yoga_class = models.ForeignKey(
        YogaClass, on_delete=models.CASCADE, related_name="chosen_type")
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member"
    )
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation: by {self.member}"

# {self.days}, {self.times} {self.yoga_type}"
# day = models.DateField(null=False, blank=False)
#     time = models.CharField(
#         max_length=15, choices=TIME_SLOT, default="9:00 - 10:00", null=False)

    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
