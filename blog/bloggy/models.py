from django.db import models, IntegrityError, transaction
from django.template.defaultfilters import slugify

from .fields import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=40)
    body = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False, unique=True)
    
    def save(self, *args, **kwargs):
        """
        Based on the Tag save() method in django-taggit, this method simply
        stores a slugified version of the title, ensuring that the unique
        constraint is observed
        """
        self.slug = slug = slugify(self.title)
        i = 0
        while True:
            try:
                savepoint = transaction.savepoint()
                res = super(Article, self).save(*args, **kwargs)
                transaction.savepoint_commit(savepoint)
                return res
            except IntegrityError:
                transaction.savepoint_rollback(savepoint)
                i += 1
                self.slug = '%s_%d' % (slug, i)

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('article', (), {'slug': self.slug,
                                }
                )
        
    class Meta(object):
        ordering = ('-date',)