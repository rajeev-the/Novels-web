from rest_framework import serializers
from .models import Novel, Chapter

class ChapterSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField() 
    class Meta:
        model = Chapter
        fields = '__all__'
        
    def get_id(self, obj):
        # Calculate the chapter ID relative to its novel
        chapters = obj.novel.chapters.all().order_by('id')  # Ensure ordering
        return list(chapters).index(obj) + 1
        

class NovelSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, required=False)

    class Meta:
        model = Novel
        fields = '__all__'
