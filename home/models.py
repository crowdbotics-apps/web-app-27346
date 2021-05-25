from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class App(models.Model):

    """
    Model responsible for registering apps on the platform
    """

    TYPE_CHOICES = [
        ('Web', 'Web'),
        ('Mobile', 'Mobile'),
    ]

    FRAMEWORK_CHOICES = [
        ('Django', 'Django'),
        ('React Native', 'React Native'),
    ]
    
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", blank=True)
    type = models.CharField("Type", max_length=10, choices=TYPE_CHOICES)
    framework = models.CharField("Framework", max_length=20, choices=FRAMEWORK_CHOICES)

    domain_name = models.CharField("Domain Name", max_length=50, blank=True)
    screenshot = models.URLField("Screenshot", blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apps")

    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'

    def __str__(self):
        return f"(App Object) {self.id}, {self.name}, {self.type}, {self.framework}, {self.user}"

    @property
    def subscription(self):
        subscription = self.subscriptions.filter(active=True).first()
        return subscription.id if subscription else None


class Plan(models.Model):

    """
    Model responsible for registering plans available for each app
    """

    name = models.CharField("Name", max_length=20)
    description = models.TextField("Description")

    price = models.DecimalField(max_digits=19, decimal_places=2)

    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return f"(Plan Object) {self.id}, {self.name}, {self.price}"


class Subscription(models.Model):

    """
    Model responsible for registering apps associated subscriptions
    """

    plan = models.ForeignKey("home.Plan", on_delete=models.PROTECT, related_name="subscriptions")
    app = models.ForeignKey("home.App", on_delete=models.CASCADE, related_name="subscriptions")

    active = models.BooleanField("Active", default=True)

    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return f"(Subscription Object) {self.id}, {self.app.name}, {self.plan.name}, {self.user}, {self.active}"

    @property
    def user(self):
        return self.app.user.id

    def delete(self, *args, **kwargs):
        self.active = False
        self.save()
