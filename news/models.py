from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.db.models import Sum

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):

        # Обновление и расчёт рейтинга
        author_posts_rating = Post.objects.all().filter(author_id=self.pk).aggregate(posts_rating_sum =Sum('post_rating') * 3)
        author_comments_rating = Comment.objects.all().filter(user_id=self.user).aggregate(comments_rating_sum = Sum('comment_rating'))

        print(author_posts_rating)
        print(author_comments_rating)

        self.author_rating = author_posts_rating['posts_rating_sum'] + author_comments_rating['comments_rating_sum']
        self.save()

    def __str__(self):
        return f'{self.user.username}'

# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        #return self.name
        return self.name.title() # title

class CategorySubscribe(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subscriber = models.ForeignKey(User, on_delete=models.PROTECT)


class Post(models.Model):
    article = 'a'
    news = 'n'

    POST_TYPE = [
        (article, "Статья"),
        (news, "Новость")
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=1, choices=POST_TYPE, default=article)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    rating = models.IntegerField(default=0)


    #about = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self, length=124):
        return f"{self.text[:length]}..." if len(str(self.text)) > length else self.text


   # def __str__(self):
    #    return f'{self.category} : {self.author} : {self.title}: {self.text}: rating = {self.rating}'
    def __str__(self):
        return f'{self.title} : {self.text[:20]}'


 #   def get_absolute_url(self):
  #      return reverse('new_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #category = models.ManyToManyField(Category)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


# Товар для нашей витрины
#class New(models.Model):
 #   name = models.CharField(
  #      max_length=50,
   #     unique=True, # названия товаров не должны повторяться
    #)
#    description = models.TextField()
 #   quantity = models.IntegerField(
  #      validators=[MinValueValidator(0)],
   # )
    # поле категории будет ссылаться на модель категории
   # category = models.ForeignKey(
    #    to='Category',
     #   on_delete=models.CASCADE,
      #  related_name='news', # все продукты в категории будут доступны через поле products
   # )

    #def __str__(self):
     #   return f'{self.name.title()}: {self.description[:20]}'

    #def get_absolute_url(self):
     #   return reverse('new_detail', args=[str(self.id)])




