import requests

# API 키와 리디렉션 URI 설정
client_id = '253277e87cab9489a7427c6658ab1f66' # 발급받은 App key
client_secret = '253277e87cab9489a7427c6658ab1f66cdd2db0cb9a3dfc1ce1bdf6e0312d9805218a8f8' # 발급받은 Secret key
redirect_uri = 'https://hoon-ssam.tistory.com/' # API 신청시에 기입한 리디렉션 URI
state = 'SOME_VALUE'

# 인증 페이지 URL 생성
auth_url = f'https://www.tistory.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&state={state}'

# 인증 페이지로 리디렉션
print('다음 URL로 이동하여 인증을 완료하세요:')
print(auth_url)

# 리디렉션된 URL에서 code 받기
code = input('code를 입력하세요: ')

# Access Token 요청
token_url = 'https://www.tistory.com/oauth/access_token'
params = {
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'code': code,
    'grant_type': 'authorization_code'
}

response = requests.get(token_url, params=params)
access_token = response.json()['access_token']
https://hoon-ssam.tistory.com/?code=d88d4623c63b184eab2f3a5fa4453f5b9e58b43a3db3affb1fd14761695ca6e5077586e5&state=SOME_VALUE
print(f'Access Token: {access_token}')

ac="5db023cd350548a12faa99b2c11a2005d110ade85d65283f907f1f55ebbc0418e74b8a7e"