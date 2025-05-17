from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('view-books/', views.view_books , name='view-books'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='login'),
    path('admin-page/', views.admin, name='admin-page'),
    path('view-borowed/', views.view_borowed, name='view-borowed'),
    path('admin-page/add-book/', views.add_book, name='add-book'),
    path('book-page/<int:book_id>', views.book_page, name='book-page'),
    path('admin-page/edit-book/<int:book_id>', views.edit_book, name='edit-book'),
    path('delete-book/<int:book_id>', views.delete_book, name= 'delete-book'),
    path('borrow-book/<int:book_id>', views.borrow_book, name= 'borrow-book'),
    path('return-book/<int:book_id>', views.return_book, name= 'return-book'),
    path('search/', views.search, name='search'),
]