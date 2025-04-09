from django.contrib.auth.models import User
from rest_framework import serializers

from ...models import Task

class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        fields = [
            "id",
            "author",
            "title",
            "complete",
            "absolute_url",
            "created_date",
            "updated_date",
        ]
        model = Task
        read_only_fields = ["author", "absolute_url"]

    def get_absolute_url(self, obj):
        requset = self.context.get("request")
        absolute_url = obj.get_absolute_api_url()
        return requset.build_absolute_uri(absolute_url)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = User.objects.get(id=request.user.id)
        return super().create(validated_data)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("absolute_url")
        return rep
