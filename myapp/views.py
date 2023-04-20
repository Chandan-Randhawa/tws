from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Products , ProductDetail
from .serializers import ProductSerializer , ProductDetailSerializer

from django.db.models import Count
import datetime


# Create your views here.

@api_view(['GET' , 'POST' , 'PATCH', 'DELETE'])
def product(request):
    if request.method == 'GET':
        x = request.query_params.get('id') 
        y = request.query_params.get('search')
        if  x and y:
            try:
                obj = ProductDetail.objects.filter(product = x).all()
                serializer = ProductDetailSerializer(obj , many = True)
                return Response(serializer.data)
            except Products.DoesNotExist:
                return Response({'error':'Product doesnot exist'}, status=404)
        elif x == 'all':        
            obj = Products.objects.all()
            print(obj)
            serializer = ProductSerializer(obj , many = True)
            return Response(serializer.data)
        elif x:
            obj = Products.objects.filter(id =x).first()
            print(obj)
            if obj:
                detail = ProductDetail.objects.create(product=obj, date_fetched=datetime.datetime.now().date())
                detail.save()
                serializer = ProductSerializer(obj , many = False)
                return Response([serializer.data])
            else:
                return Response({'error': f'Product {x} doesnot exist'},status=404)
        
    elif request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=404)
    elif request.method == 'PATCH':
        try:
            data = request.data
            obj = Products.objects.get(id=data['id'])
            for key, value in data.copy().items():
                if value == "":
                    del data[key]
            serializer = ProductSerializer(obj ,data = data , partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=404)
        except Products.DoesNotExist:
            return Response({'error':f'Product {data["id"]} doesnot exist'}, status=404)
    
    elif request.method == 'DELETE':
            data = request.data
            obj = Products.objects.filter(id = data['id']).first()
            if obj:
                print(obj)
                obj.delete()
                return Response({'message':f'product {data["id"]} is deleted'})
            else :
                return Response({'error':f'Product {data["id"]} doesnot exist'},status=404)
        
@api_view(['GET'])
def frequent_products(request):
    if request.method == 'GET':
        try:
            days = int(request.query_params.get('days'))
            datess = datetime.datetime.now().date()-datetime.timedelta(days)
            print(datess)
            queryset = ProductDetail.objects.filter(date_fetched__gte=datess).values('product').annotate(count=Count('product')).order_by('-count')[:5]
            print(queryset)
            obj_list =[]
            for i in queryset: 
                obj = Products.objects.filter(id = i['product']).first()
                serializer = ProductSerializer(obj )
                obj_list.append(serializer.data )
            print(obj_list)
            return Response(obj_list )
        except Exception as e:
            return Response({'error': 'provide a valid no. of days before'}, status=404)

        