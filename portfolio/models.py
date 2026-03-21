from django.db import models

class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    


class CryptoAsset(models.Model):
    member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='assets')
    crypto_id = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return f"{self.crypto_id} - {self.member.name}"
    



# Create your models here.
