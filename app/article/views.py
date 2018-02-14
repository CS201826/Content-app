# Import packages
from flask import flash, request, redirect, render_template, url_for
import uuid

from . import article
from .. import dynamodb
from .forms import ArticleForm

table = dynamodb.Table('articles')

@article.route('/create', methods=['GET', 'POST'])
def create():
    """
    Method to create article
    """
    form = ArticleForm(request.form)

    # Check request method and validate form
    if request.method == 'POST' and form.validate():
        data = {}
        data['article_id'] = uuid.uuid4().hex
        data['title'] = form.title.data
        data['description'] = form.description.data

        data = dict((k, v) for k, v in data.items() if v)

        # Save data in DynamoDb table
        response = table.put_item(Item=data)

        if response:
            flash('Article is successfully added')
            return redirect(url_for('article.list'))

    return render_template('article/form.html', add_article=True,
                           form=form, title='Add Article')

@article.route('/edit/<string:article_id>', methods=['GET', 'POST'])
def edit(article_id):
    """
    Method to edit article
    """
    response = table.get_item(
        Key={'article_id': article_id}
        )
    data = response.get('Item')

    if data is None:
        flash('Unable to get Article')
        return redirect(url_for('article.list'))

    form = ArticleForm(title=data.get('title'), description=data.get('description'))

    # Check request method and validate form
    if request.method == 'POST' and form.validate():
        data = {}
        data['article_id'] = article_id
        data['title'] = form.title.data
        data['description'] = form.description.data

        data = dict((k, v) for k, v in data.items() if v)

        # Save data in DynamoDb to update table
        response = table.put_item(Item=data)

        if response:
            flash('Article is successfully updated')
            return redirect(url_for('article.list'))
    
    return render_template('article/form.html', add_article=False,
                           form=form, title='Edit Article', article_id=article_id)


@article.route('/delete/<string:article_id>', methods=['GET'])
def delete(article_id):
    """
    Method to delete articles
    """
    response = table.get_item(
        Key={'article_id': article_id}
        )
    data = response.get('Item')
    if data is None:
        flash('Unable to get Article')
        return redirect(url_for('article.list'))    

    # Delete article for a particular id
    response = table.delete_item(
        Key={'article_id':article_id}
        )

    if response:
            flash('Article is successfully deleted')

    return redirect(url_for('article.list'))

@article.route('/list', methods=['GET'])
def list():
    """
    Method to list articles
    """
    articles = []
    if request.method == 'GET':
        # Get all articles
        response = table.scan()
        articles = response.get('Items')

    return render_template('article/articles.html', articles=articles, title='List Articles')
