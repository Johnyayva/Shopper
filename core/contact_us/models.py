from django.db import models

class AboutOfice(models.Model):
    title = models.CharField("Title", max_length = 255)
    text_1 = models.TextField("Text 1")
    text_2 = models.TextField("Text 2")
    map_url = models.URLField("Map Url", default = "")
    
    facebook_url = models.URLField("Facebook Url", blank = True)
    twitter_url = models.URLField("Twitter Url", blank = True)
    linked_in_url = models.URLField("Linked in Url", blank = True)
    be_url = models.URLField("Be Url", blank = True)
    
    class Meta:
        verbose_name = "About Ofice"
        verbose_name_plural = "About Ofice"

    
    def __str__(self) -> str:
        return self.title
    
    
class Accordion(models.Model):
    title = models.CharField("Title", max_length = 150)
    text = models.TextField("Text")
    
    
    class Meta:
        verbose_name = "Accordion"
        verbose_name_plural = "Accordions"

    
    def __str__(self) -> str:
        return self.title
    
    
    
class ContactUs(models.Model):
    full_name = models.CharField("Full Name", max_length = 250)
    email = models.EmailField("User Email")
    subject = models.CharField("Subject", max_length = 250)
    message = models.TextField("Message")
    
    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    
    def __str__(self) -> str:
        return f"{self.full_name} | {self.email}"