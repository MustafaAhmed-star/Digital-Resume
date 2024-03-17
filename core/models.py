from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Skill(models.Model):
    name =models.CharField(max_length=150,blank=True,null=True)
    score = models.IntegerField(default=70,blank=True,null=True)
    image = models.FileField(blank=True,null=True,upload_to='skills')
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self:str):
        return self.name
        
        
class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True,null=True , upload_to='avatar')
    title = models.CharField(max_length=150,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    skills = models.ManyToManyField(Skill,blank=True,null=True)
    cv = models.FileField(blank=True,null=True,upload_to='cv')
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
        
class ContactProfile(models.Model):
    class Meta:
        ordering = ['timestamp']
    name =models.CharField(max_length=50,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    message = models.TextField(verbose_name='message')
    
    def __str__(self):
        return self.name
        
class Testimonial(models.Model):
    class Meta:
        ordering = ['name']
        
    thumbnaill = models.ImageField(blank=True,null = True,upload_to='thumbnaill')
    name =models.CharField(max_length=150,blank=True,null=True)
    role =models.CharField(max_length=150,blank=True,null=True)
    quote = models.CharField(max_length=550,blank=True,null=True)
    is_active = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
        
class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name    
        
class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"
        
        
        

class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return self.name
        return 'Unkonwn'
    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name