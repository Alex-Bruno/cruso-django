from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe


class Category(models.Model):
    nome = models.CharField(max_length=100)
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, blank=False)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ('-criado', )

    def __str__(self):
        return self.nome


class PublisherManager(models.Manager):
    def get_queryset(self):
        return super(PublisherManager, self).get_queryset()\
            .filter(status='publicado')


class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=250, verbose_name='Título')
    slug = models.CharField(max_length=250, unique=True, blank=False)
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Category,
                                       related_name="get_posts")
    imagem = models.ImageField(upload_to="blog", blank=True, null=True)
    conteudo = RichTextField(verbose_name='Conteúdo')
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')

    objects = models.Manager()
    published = PublisherManager()

    def get_absolute_url(self):
        return reverse("post_detalhe", args={self.slug})

    def get_absolute_url_edit(self):
        return reverse("post_edit", args={self.slug})

    def get_absolute_url_delete(self):
        return reverse("post_delete", args={self.slug})

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />'%self.imagem.url)   
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True    
        
    class Meta:
        ordering = ('-publicado', )

    def __str__(self):
        return self.titulo


@receiver(post_save,sender=Post)
def insert_slug(sender,instance,**kwargs):
    if not instance.slug:
        slug = slugify(instance.titulo)
        posts = Post.objects.filter(slug=slug)
        if(len(posts) > 0):
            index = len(posts) + 1
            slug = slug + str(index)
            
        instance.slug = slug
        return instance.save()



'''
Criando multiplos registros
Post.objects.bulk_create([]);
'''
