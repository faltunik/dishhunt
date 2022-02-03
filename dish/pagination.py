from mmap import PAGESIZE
from rest_framework.pagination import PageNumberPagination

class PaginateView(PageNumberPagination):
    page_size = 2