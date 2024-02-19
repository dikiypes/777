from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        order_by = self.request.query_params.get('order_by')
        course_id = self.request.query_params.get('course_id')
        lesson_id = self.request.query_params.get('lesson_id')
        payment_method = self.request.query_params.get('payment_method')

        if order_by:
            queryset = queryset.order_by(order_by)
        if course_id:
            queryset = queryset.filter(paid_course_id=course_id)
        if lesson_id:
            queryset = queryset.filter(paid_lesson_id=lesson_id)
        if payment_method:
            queryset = queryset.filter(payment_method=payment_method)

        return queryset
