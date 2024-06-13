from django.db import models
from pytils.translit import slugify
from django_editorjs_fields import EditorJsJSONField


def upload_to(instance, filename):
    foldername = instance.__class__.__name__.lower()
    return '{foldername}/{filename}'.format(filename=filename,foldername=foldername)

class postContentFilesUpload(models.Model):
    file = models.FileField(upload_to="media/uploads")

cat_choices = (('blog','blog'),('projects','projects'))

class post(models.Model):
    title = models.TextField(max_length=255)
    excerpt = models.TextField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(upload_to = upload_to, default='posts/moon.jpg')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)
    category = models.CharField(max_length=10, choices=cat_choices, default='blog')
    content = EditorJsJSONField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

#class postCategory(models.Model):
#    name = models.TextField(max_length=255)
#    slug = models.SlugField(max_length=255, unique=True, db_index=True)
#
#    def __str__(self):
#        return self.name
#    
#    def save(self, *args, **kwargs):
#        if not self.slug:
#            self.slug = slugify(self.name)
#        super(postCategory, self).save(*args, **kwargs)

class docs(models.Model):
    name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to = upload_to, default='docs/ИБ.docx')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
       storage, path = self.file.storage, self.file.path
       super(docs, self).delete(*args, **kwargs)
       storage.delete(path)    

class reportsGroup(models.Model):
    name = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    

class reports(models.Model):
    name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to = upload_to, default='reports/%D0%98%D0%91_YdeVSTs.docx')
    group = models.ForeignKey('reportsGroup', on_delete= models.CASCADE , null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
       storage, path = self.file.storage, self.file.path
       super(reports, self).delete(*args, **kwargs)
       storage.delete(path)

class faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class products(models.Model):
    name = models.TextField()
    preview_image = models.ImageField(upload_to = upload_to, default='products/moon.jpg')
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        storage, path = self.preview_image.storage, self.preview_image.path
        super(products, self).delete(*args, **kwargs)
        storage.delete(path)

class dataFromForms(models.Model):
    name = models.TextField(150, null=True)
    phone = models.IntegerField(11, null=True)
    email = models.TextField()
    message = models.TextField(null=True)

    def __str__(self):
        return self.email
        



