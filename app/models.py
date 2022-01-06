from django.db import models


class Detail(models.Model):
    email = models.EmailField(max_length=50)
    receiver_name = models.CharField(max_length=255)
    city = models.CharField(max_length=10)
    time_of_sending = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receiver_name
