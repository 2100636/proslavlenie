# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib import admin
from project.core.models import Article, Page, SliderItem,\
    ArticleGalleryImage, NewsGalleryImage, PageGalleryImage, \
    News, Review, Testimony, TestimonyGalleryImage, Video,\
    VideoCategory, Ministry, MinistryImage, Need, Question, AdvertCategory, Advert

from image_cropping import ImageCroppingMixin


class ArticleImagesInline(ImageCroppingMixin, admin.StackedInline):
    """Вывод заказов списком"""
    model = ArticleGalleryImage
    extra = 0


class NewsImagesInline(ArticleImagesInline):
    model = NewsGalleryImage


class TestimonyImagesInline(ArticleImagesInline):
    model = TestimonyGalleryImage


class PageImagesInline(ArticleImagesInline):
    model = PageGalleryImage


class VideoCategoryInline(admin.StackedInline):
    """Вывод заказов списком"""
    model = VideoCategory
    extra = 0


class ArticleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Article
    inlines = [ArticleImagesInline]
    prepopulated_fields = {'slug': ('name', ), }


class NewsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = News
    inlines = [NewsImagesInline]
    fields = ('name', 'date', 'description', 'meta_title', 'meta_description', 'image', 'cropping')


class TestimonyAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = News
    inlines = [TestimonyImagesInline]
    fields = ('name', 'description', 'meta_title', 'meta_description', 'image')


class PageAdmin(admin.ModelAdmin):
    model = Page
    inlines = [PageImagesInline]
    prepopulated_fields = {'slug': ('name', ), }


class ReviewAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Review


class SliderItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = SliderItem


class VideoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Video
    fields = (
        'name', 'description', 'video', 'category', 'cover',
        ('cropping', 'cropping_pritch', 'cropping_videoblog'))


class MinistryImageInline(ImageCroppingMixin, admin.StackedInline):
    model = MinistryImage


class MinistryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Ministry
    fields = (
        'name', 'slug', ('baner', 'baner_text'), 'video', 'description',
        ('color', 'allocate_description'), 'meta_title', 'meta_description', 'leader', 'date')

    inlines = [MinistryImageInline, ]
    prepopulated_fields = {'slug': ('name',)}


class AdvertCategoryInline(admin.StackedInline):
    """Вывод заказов списком"""
    model = AdvertCategory
    extra = 0

class AdvertAdmin(admin.ModelAdmin):
    model = Advert
    list_display = ('name', 'text', 'phone', 'cost', 'category', 'author')
    list_display_links = ('name',)
    search_fields = ['text']
    fields = (
        'name', 'slug', 'text', 'image', 'phone', 'cost', 'category', 'author', 'member', 'pswd', 'date','status')
    prepopulated_fields = {'slug': ('name', ), }




admin.site.register(Article, ArticleAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(SliderItem, SliderItemAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Review)
admin.site.register(Testimony, TestimonyAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoCategory)
admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Need)
admin.site.register(Question)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(AdvertCategory)
