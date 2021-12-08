from rest_framework import serializers
from .models import Review, Comment

# Serializer의 존재이유
# 1. 데이터 검증
# 2. JSON 생성

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'       # JSON 에는 모든 필드가 포함되고
        read_only_fields = ('review', 'user',) # CUD 관련 vaildation은 포함 하지 않는다.


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # 원래는 그냥 user 객체를 보여줘야 하는데, 장고 내부적으로 할 때에는 그 처리를 해 주지 않아도 username을 보여줬었다.
        # 하지만 serializer는 user를 그냥 보여준다고 할 때, 그냥 db의 pk값을 보여주는게 맞다.
        # 해결 방법 1. ReviewSerializer의 depth를 1로 줘서. 더 파고 들어갈 depth가 있을 때에만 더 들어간다.
        fields = '__all__'
        depth = 1
        read_only_fields = ('user', 'like_users',)



# class ReviewSerializer(serializers.ModelSerializer):
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     # Comment 관련한 JSON도 포함해야 하므로 => CommentSerializer 가 들어가 줘야함
#     #related_name과 동일하게 작성함.
#     comment_set = CommentSerializer(many=True, read_only=True)

#     #없는 필드(댓글개수)를 만들어서 JSON 구성 -> QuerySet API 코드를 string으로 넘긴다.
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     class Meta:
#         model = Review
#         fields = '__all__'
#         depth = 1
#         read_only_fields = ('comment_set', 'comment_count',)








# from rest_framework import serializers
# from .models import Review, Comment

# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from movies.models import Movie

# # Serializer의 존재이유
# # 1. 데이터 검증
# # 2. JSON 생성

# class ReviewListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ('title', 'movie', 'rank', 'content',)
    
#     class MovieSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Movie
#             fields = '__all__'

#     movie = MovieSerializer(read_only=True,)
    
#     class Meta:
#         model = Review
#         # fields = ('title', 'content', 'rank',)
#         fields = '__all__'




# class CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = '__all__'       # JSON 에는 모든 필드가 포함되고
#         read_only_fields = ('review',) # CUD 관련 vaildation은 포함 하지 않는다.



# class ReviewSerializer(serializers.ModelSerializer):
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     # Comment 관련한 JSON도 포함해야 하므로 => CommentSerializer 가 들어가 줘야함
#     #related_name과 동일하게 작성함.
#     comment_set = CommentSerializer(many=True, read_only=True)

#     #없는 필드(댓글개수)를 만들어서 JSON 구성 -> QuerySet API 코드를 string으로 넘긴다.
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     class Meta:
#         model = Review
#         fields = '__all__'
#         # read_only_fields = ('comment_set', 'comment_count',)