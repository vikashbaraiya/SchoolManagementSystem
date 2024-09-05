from rest_framework import pagination
from rest_framework.response import Response
class CustomPagination(pagination.PageNumberPagination):
    print("custom Pagination........")
    def get_paginated_response(self, data):
        print(data, 'data...')
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
