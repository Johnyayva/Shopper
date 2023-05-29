from django.contrib import admin
from .models import HomeBanner, SiteTitle, Products, ProductsCategory, Pages, Banners, OurBackground, TeamMembers, Services
from .models import AboutSixtennClothingList, AboutSixtennClothing

admin.site.register(HomeBanner)
admin.site.register(SiteTitle)
admin.site.register(Products)
admin.site.register(ProductsCategory)
admin.site.register(Pages)
admin.site.register(Banners)
admin.site.register(OurBackground)
admin.site.register(TeamMembers)
admin.site.register(Services)
admin.site.register(AboutSixtennClothingList)
admin.site.register(AboutSixtennClothing)

