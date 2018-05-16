from django.db.models import Q
from rest_framework import generics, mixins
from util.api.serializers import ConnectionSettingSerializer,FeedBackSerializer
from util.models import ConnectionSetting,FeedBack



class ConnectionSettingAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ConnectionSettingSerializer
    

    def get_queryset(self):
        qs = ConnectionSetting.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__iexact = query)
                ).distinct()
        return qs



    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ConnectionSettingRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = ConnectionSettingSerializer

    def get_queryset(self):
        return ConnectionSetting.objects.all()



class FeedBackAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = FeedBackSerializer

    def get_queryset(self):
        qs = FeedBack.objects.all()
        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FeedBackRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = FeedBackSerializer

    def get_queryset(self):
        qs = FeedBack.objects.all()
        return qs