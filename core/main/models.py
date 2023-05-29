from django.db import models
from users.models import CustomUser

class SiteTitle(models.Model):
    pt_1 = models.CharField("Title part 1", max_length = 50)
    pt_2 = models.CharField("Title part 2", max_length = 50)


    class Meta:
        verbose_name = "Site Title"
        verbose_name_plural = "Site Title"


    def __str__(self) -> str:
        return f"{self.pt_1} {self.pt_2}"

class HomeBanner(models.Model):
    img = models.ImageField("Banner Image", upload_to = "images")
    title = models.CharField("Banner Title", max_length = 150)
    text = models.CharField("Banner Text", max_length = 150)
    
    
    class Meta:
        verbose_name = "Home Banner"
        verbose_name_plural = "Home Banners"

    
    def __str__(self) -> str:
        return self.title


class ProductsCategory(models.Model):
    name = models.CharField("Category name", max_length = 100)
    tag = models.CharField("Categor Teg", max_length = 50)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name + "||" + self.tag

class Products(models.Model):
    category = models.ForeignKey(ProductsCategory, on_delete= models.CASCADE, related_name = "category")
    img = models.ImageField("Product Image", upload_to = "images")
    title = models.CharField("Product Title", max_length = 50)
    price = models.FloatField('Product price')
    text = models.TextField('Text', max_length=60)
    reviews = models.ManyToManyField(CustomUser, blank=True)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
        
        
class HeppyCustomers(models.Model):
    img = models.ImageField("Customer Image")

    class Meta:
        verbose_name = "Heppy Customer"
        verbose_name_plural = "Heppy Customers"



class Pages(models.Model):
    name = models.CharField("Page Name", max_length = 255)
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


    def __str__(self) -> str:
        return self.name
    
    
class Banners(models.Model):  
    page = models.ForeignKey("Pages", on_delete = models.CASCADE)
    img = models.ImageField("Banner Image")
    title = models.CharField("Banner Title", max_length = 255)
    text = models.TextField("Banner Text")
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    
    def __str__(self) -> str:
        return f"{self.title}" 
    
    
class OurBackground(models.Model):
    title = models.CharField("Title", max_length = 255)
    text_1 = models.TextField("Text 1")
    text_2 = models.TextField("Text 2")
    img = models.ImageField("Image", default = "")
    facebook_url = models.URLField("Facebook Url", blank = True)
    twitter_url = models.URLField("Twitter Url", blank = True)
    linked_in_url = models.URLField("Linked in Url", blank = True)
    be_url = models.URLField("Be Url", blank = True)
    
    class Meta:
        verbose_name = "Our Background"
        verbose_name_plural = "Our Background"

    
    def __str__(self) -> str:
        return self.title
    
    
    

class TeamMembers(models.Model):
    name = models.CharField("Member Name", max_length= 50)
    profession = models.CharField("Member Profession", max_length=100)
    about = models.TextField("About Member")
    img = models.ImageField('Member Photo', upload_to="images")
    
    fb = models.URLField("facebook URL", blank = True)
    linkedin = models.URLField("Linkedin URL", blank = True)
    twitter = models.URLField("twitter URL", blank = True)
    be = models.URLField("behance URL", blank = True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self) -> str:
        return f"{self.name} | {self.profession}"
    
    
class Services(models.Model):
    img = models.ImageField("Service Image")
    title = models.CharField("Service Title", max_length = 100)
    description = models.TextField("Service Description")
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self) -> str:
        return self.title
    
    
class AboutSixtennClothingList(models.Model):
    title = models.CharField("Title", max_length = 255)
    
    class Meta:
        verbose_name = "About Sixtenn Clothing List"
        verbose_name_plural = "About Sixtenn Clothing List"
    
    
    def __str__(self) -> str:
        return self.title
    
class AboutSixtennClothing(models.Model):
    title = models.CharField("Title", max_length = 255)
    description = models.TextField("Description")
    ul = models.ManyToManyField(AboutSixtennClothingList)
    
    
    class Meta:
        verbose_name = "About Sixtenn Clothing"
        verbose_name_plural = "About Sixtenn Clothing"
    
    def __str__(self) -> str:
        return self.title    