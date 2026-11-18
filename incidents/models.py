from django.db import models

class Incident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(
        max_length=50,
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')],
        default='Medium'
    )
    status = models.CharField(
        max_length=50,
        choices=[('Open', 'Open'), ('Under Investigation', 'Under Investigation'), ('Resolved', 'Resolved')],
        default='Open'
    )
    reported_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
