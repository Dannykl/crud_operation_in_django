from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    post = serializers.HyperlinkedRelatedField(many = True,view_name='post:post-detail',read_only=True)
    password = serializers.CharField(write_only=True)

    # complete object instances based on the validated data
    # CREATE and UPDATE are implemented to do that
    def create(self, validated_data):
        user = User(username = validated_data.get('username' ,None))
        user.set_password(validated_data.get('password',None))
        user.save()
        return user

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('url', 'id', 'username','password', 'first_name', 'last_name','email', 'post')
        extra_kwargs = {
            'url': {'view_name': 'user:user-detail',}
        }
