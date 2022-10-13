from rest_framework import serializers
from .models import AmazonProducts

class AmazonProductsSerializer(serializers.ModelSerializer):
    profit = serializers.SerializerMethodField()
    class Meta:
        model = AmazonProducts
        fields = ['id', 'amazon_link','fee', 'name','my_price','amazon_price', 'cost', 'stock', 'bought_from', 'profit','image']
    
    def get_profit(self, obj):
        cost = float(obj.cost) + float(obj.fee)
        profit = float(obj.my_price) - cost
        # here write the logic to compute the value based on object
        return round(profit, 2)
    # def create(self, validated_data):
    #     # note = Freestyle(document_id=validated_data['document_id'], second_party=validated_data['second_party'], nationality=validated_data['nationality'], date=validated_data['date'], occupation=validated_data['occupation'], paid_amount=validated_data['paid_amount'], type=validated_data['type'], manf_year=validated_data['manf_year'], author=validated_data['author'], color=validated_data['color'], featured_no=validated_data['featured_no'], body=validated_data['body'], length=validated_data['length'], width=validated_data['width'], depth=validated_data['depth'], load=validated_data['load'], no_motor=validated_data['no_motor'], engine_sr=validated_data['engine_sr'], engine_power=validated_data['engine_power'], engine_type=validated_data['engine_type'])
    #     note = AmazonProducts(amazon_link=validated_data['amazon_link'], name=validated_data['name'], cost=validated_data['cost'], fee=validated_data['fee'], stock=validated_data['stock'], bought_from=validated_data['bought_from'])
    #     note.save()
    #     return note

# class FSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Freestyle
#         fields = '__all__'