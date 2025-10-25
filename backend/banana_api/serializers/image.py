from rest_framework import serializers
from ..models import ImageUpload

class ImageSerializer(serializers.ModelSerializer):
    # file_url is read-only, generated from the file_path field
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = ImageUpload
        fields = ["image_id", "file_path", "file_url"]

    # Method to get the URL
    def get_file_url(self, obj):
        request = self.context.get('request')
        url = obj.file_path.url
        if request is not None:
            # Makes URL absolute (with domain) if request is passed in context
            return request.build_absolute_uri(url)
        return url
