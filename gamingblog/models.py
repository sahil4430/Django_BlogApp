from django.db import models

# Create your models here.\
class BlogDetail(models.Model):
    Blog_id = models.AutoField( primary_key=True)
    Blog_Title = models.CharField(max_length=50)
    Blog_Desc= models.CharField(max_length=400)
    Blog_Date= models.DateTimeField()
    class Meta:
        db_table="BlogTable"

        def __str__(self):
            return self.blog_title



