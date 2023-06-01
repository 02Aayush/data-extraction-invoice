from django.db import models

# Create your models here.

# By creating the InvoiceData model, we will have a database table to store the extracted data from the invoice, which
# can be accessed and manipulated using Django's ORM (Object-Relational Mapping).
class InvoiceData(models.Model):


    # The 'data' field will store the extracted data from the invoice as text.
    data = models.TextField()   # Working
    # 'Extraction_datetime' field of type DateTimeField to store the date and time of extraction.
    extraction_datetime = models.DateTimeField(auto_now_add=True)

    #The __str__ method is defined to provide a human-readable representation of each InvoiceData instance.
    # In this case, it will return "InvoiceData #ID" where ID is the primary key of the model instance.
    def __str__(self):
        return f"InvoiceData #{self.pk}"
