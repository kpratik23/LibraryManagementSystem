from django.urls import path,include
from django.contrib import admin
from .views import *

urlpatterns=[
    path('listbooks/',ShowMyBooks.as_view()),
    path('addbook/',AddBook.as_view()),
    path('getDetails/<int:studentid>',IssueBook.as_view()),
    path('issuebook/',IssueBook.as_view()),
    path('edit/',IssueBook.as_view()),
    path('delete/',IssueBook.as_view()),
    path('submit/',SubmitBook.as_view()),
    path('index/',index)
]