from rest_framework import serializers

from mysite.core.models import Book


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ('docfile',)
        fields = '__all__'

    def create(self, validated_data):
        return Book.objects.create(**validated_data)