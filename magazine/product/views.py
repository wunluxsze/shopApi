from rest_framework.response import Response
from rest_framework import status
from .models import Prod
from .serializers import ProductsSerializer
from rest_framework.views import APIView


class ProductView(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            queryset = Prod.objects.all()
            serializer = ProductsSerializer(queryset, many=True)
        else:
            queryset = Prod.objects.get(id=pk)
            serializer = ProductsSerializer(queryset)
        if not pk:
            return Response({"Products": serializer.data})
        else:
            return Response({"Product": serializer.data})

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Product": serializer.data})

    def put(self, request, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "status PUT is not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Prod.objects.get(id=pk)
        except Prod.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductsSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"product": serializer.data})

    def delete(self, request, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "status PUT is not allowed"})

        try:
            instance = Prod.objects.get(id=pk)
        except Prod.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()

        return Response({"product": instance.id})
