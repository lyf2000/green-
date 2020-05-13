from rest_framework.pagination import PageNumberPagination, CursorPagination


class MyPaginator(PageNumberPagination):
    page_size = 2
    ordering = '-created'

