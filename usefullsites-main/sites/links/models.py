from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=50)
    colour_code= models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    description = models.TextField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
defaultvalue = ()

class BunchOfLinks(models.Model):

    def get_default():
        return list(defaultvalue)


    name=models.CharField(max_length=100)
    brandlogo=models.URLField(max_length=250)
    url=models.URLField(max_length=250)
    description=models.TextField(max_length=1000)
    # tags = models.ForeignKey(Tag, on_delete=models.SET_NULL,null=True,blank=True)
    # taglist=ArrayField(models.CharField(max_length=250, null=True),default=get_default)
    upvote=models.IntegerField(default=0,null=True)
    downvote=models.IntegerField(default=0,null=True)
    bookmark = models.BooleanField(default=False,null=True)
    followers=models.IntegerField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    


    def __str__(self):
        return (str(self.name)
        +" "
        +str(self.brandlogo)
                +" "
        +str(self.url)
                +" "
        +str(self.description)
                +" "
        +str(self.upvote)
                +" "
        +str(self.downvote)
                +" "
        +str(self.bookmark)
                +" "
        +str(self.followers)
        )


class CommentsModel(models.Model):


    def get_default():
        return list(defaultvalue)
    comments=models.TextField(blank=True,null=True)
    upvote=models.BooleanField(default=False)
    downvote=models.BooleanField(default=False)
    bunch_of_links=models.ForeignKey(BunchOfLinks, on_delete=models.CASCADE,blank=True,null=True,related_name="bunch_of_links")
    # followers=models.ForeignKey(BunchOfLinks,on_delete=models.CASCADE,blank=False,null=True,related_name="followers")
    followers=models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        # return (str(self.comments)
        # +" "
        # +str(self.upvote)

        # )
        return self.comments
class ReportsModel(models.Model):
    bunch_of_links=models.ForeignKey(BunchOfLinks,on_delete=models.CASCADE,blank=True,null=True,related_name="report")
    report=models.TextField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.report