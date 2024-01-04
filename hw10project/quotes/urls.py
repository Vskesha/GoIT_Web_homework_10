from django.urls import path

from . import views


app_name = "quotes"

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),

    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),

    path('tag/<int:tag_id>/', views.tag_detail, name='tag_detail'),
    path('add_tag/', views.add_tag, name='add_tag'),

    path('quote/<int:quote_id>', views.quote_detail, name='quote_detail'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('edit_quote/<int:quote_id>/', views.edit_quote, name='edit_quote'),
    path('delete_quote/<int:quote_id>/', views.delete_quote, name='delete_quote'),
]