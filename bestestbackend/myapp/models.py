from django.db import models
from django.utils.timezone import now

# Create your models here.

class OrderStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending' # Ternyata value pertama itu value external dan yang value kedua yang internal server 
    ACCEPTED = 'Accepted', 'Accepted' # Absolutely kreizi
    REJECTED = 'Rejected', 'Rejected'
    @classmethod 
    def ColorChoices(cls, status):
        colorMap = {
           cls.PENDING: '#FFDE21',
           cls.ACCEPTED: '#56D47A',
           cls.REJECTED: '#FF3F41'
       }
        return colorMap.get(status, '#FFDE21')
    
class MixModelRequest(models.Model):
    # Auto increment number of orders
    orderName = models.AutoField(primary_key=True)

    # Status of job
    status = models.CharField(
        max_length = 10,
        choices = OrderStatus.choices,
        default = OrderStatus.PENDING.name,
    )

    # Name of job poster
    solicitor = models.CharField(max_length=100)

    # Date deadline for order
    date = models.DateField()

    # Duration of time until deadline
    @property
    def duration(self):
        delta = (self.date - now().date()).days
        return max(delta, 0)

    # Price of job
    price = models.IntegerField()

    # Color of status
    @property
    def status_color(self):
        return OrderStatus.ColorChoices(self.status)

    def __str__(self):
        return f"Order: {self.orderName} - {self.status} - By: {self.solicitor} - Due in: {self.duration} at {self.date} - {self.price} - Status Color: {self.status_color}"
    