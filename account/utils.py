from rest_framework_simplejwt.tokens import RefreshToken

# 해당하는 유저의 토큰을 구하는 함수입니다.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }