from django.urls import path
from books.api.views import BookListCreateView, BookDetailCreateView, CommentCreateView, CommentDetailView


urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>', BookDetailCreateView.as_view(), name='book-datail'),
    path('books/<int:book_pk>/commentate', CommentCreateView.as_view(), name='commentate'),
    path('comments/<int:pk>', CommentDetailView.as_view(), name='comment-datail'),
]   