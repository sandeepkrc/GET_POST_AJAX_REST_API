from rest_framework import serializers
from .models import Students



class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
    #object level validation
    # def validate_age(self,data):
    #     if data['age']<=10:
    #          raise serializers.ValidationError("age must be more then 10 years")
    #     return data
    def validate_age(self,age):
        age1= int(age)
        if age1<=10:
            raise serializers.ValidationError("age is lesst then 10")
        return age
        
    # field level  validation
    #RAJ.SANDIP96@GMAIL.COM
    
    def validate_first_name(self,first_names):
        if Students.objects.filter(first_name =first_names).exists():#User
            raise serializers.ValidationError('first_name already---- exist.')
        return first_names