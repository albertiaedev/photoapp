from django.db import models


# Database for categories

class Category(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return self.name

# End


# Database for photos

class Photo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    image=models.ImageField(null=False,blank=False)
    description=models.TextField(max_length=300,null=False,blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description

# End
