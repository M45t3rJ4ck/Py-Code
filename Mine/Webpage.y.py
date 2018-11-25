from django.db import models

# Create your models here.
class Article(models.Model):
    content = models.CharField(max_length=200)
    written_date = models.DateTimeField('date written')
    def __unicode__(self):
        return self.content

# Create your views here.
from blog.models import Article  # Article data models
from django.shortcuts import render # shortcuts to call template
from django.http import HttpResponseRedirect # Redirection Module
from django.template import context
from django.utils import timezone # time Module

# blog.views.index
# retrieve all content and display in reverse of order of written_date
# call the template after sorting.
def index(request):
    all_articles = Article.objects.all().order_by('-written_date')
    return render(request, 'blog/index.html',
             context={'all_articles': all_articles, 'message': 'Write something!'})

# blog.views.submit
# Receive POST request submitted from user FORM, save the request
# redirect user to index.html

def submit(request):
    try:
        cont = request.POST['content']
    except (KeyError):
        return render(request, 'blog/index.html',
             context={'all_articles': all_articles, 'message': 'Write something!'})
    else:
        article = Article(content=cont, written_date=timezone.now())
        article.save()
        return HttpResponseRedirect('/blog')

# blog.views.remove
# delete content which has primary key matched to article_id
# redirect user after deleting content
def remove(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return HttpResponseRedirect('/blog')

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>One Line Blog</title>
    <link rel="stylesheet" href="{{ STATIC_URL }}styles/blog.css" type="text/css">
  </head>
  <body>
    <div id="header">
      <h2>One Line Blog</h2>
    </div>
    <div id="writer">
      <div>
        {% if message %}<p><strong>{{ message }}</strong></p>{% endif %}
      </div>
      <form action="/blog/submit" method="post">
        {% csrf_token %}
        <input type="text" max-length=200 style="width:500px;" name="content">
        <input type="submit" value="Submit">
      </form>
    </div>
    <div>
    {% if all_articles %}
      <table>
        <tr>
          <th>No. </th>
          <th width="300px">Content</th>
          <th>Date</th>
          <th>Delete</th>
        </tr>
        { % for article in all_articles %}
        <tr>
          <td>{{ article.id }}</td>
          <td>{{ article.content }}</td>
          <td>{{ article.written_date }}</td>
          <td align="center"><a href="/blog/{{ article.id }}/remove">[x]</a></td>
        </tr>
        { % endfor %}
      </table>
      {% else %}
      <p>No articles available</p>
      {% endif %}
    </div>
  </body>
</html>

