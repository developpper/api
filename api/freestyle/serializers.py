from rest_framework import serializers
from .models import Freestyle

class FreestyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freestyle
        fields = ['id', 'document_id', 'second_party', 'nationality', 'date', 'occupation', 'paid_amount', 'type', 'manf_year', 'color', 'featured_no', 'body', 'length', 'width', 'depth', 'load', 'no_motor', 'engine_sr', 'engine_power', 'engine_type']
    
    def create(self, validated_data):
        # note = Freestyle(document_id=validated_data['document_id'], second_party=validated_data['second_party'], nationality=validated_data['nationality'], date=validated_data['date'], occupation=validated_data['occupation'], paid_amount=validated_data['paid_amount'], type=validated_data['type'], manf_year=validated_data['manf_year'], author=validated_data['author'], color=validated_data['color'], featured_no=validated_data['featured_no'], body=validated_data['body'], length=validated_data['length'], width=validated_data['width'], depth=validated_data['depth'], load=validated_data['load'], no_motor=validated_data['no_motor'], engine_sr=validated_data['engine_sr'], engine_power=validated_data['engine_power'], engine_type=validated_data['engine_type'])
        note = Freestyle(document_id=validated_data['document_id'], author=validated_data['author'], second_party=validated_data['second_party'], nationality=validated_data['nationality'], date=validated_data['date'], occupation=validated_data['occupation'], paid_amount=validated_data['paid_amount'], type=validated_data['type'], manf_year=validated_data['manf_year'], color=validated_data['color'], featured_no=validated_data['featured_no'], body=validated_data['body'], length=validated_data['length'], width=validated_data['width'], depth=validated_data['depth'], load=validated_data['load'], no_motor=validated_data['no_motor'], engine_sr=validated_data['engine_sr'], engine_power=validated_data['engine_power'], engine_type=validated_data['engine_type'])
        note.save()
        return note

class FSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freestyle
        fields = '__all__'