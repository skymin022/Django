from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    # 쿠키 확인
    no_event_popup = 'no_event_popup' in request.COOKIES
    print("팝업 숨김 여부 : {}".format( no_event_popup ) )

    # 현재 로그인된 사용자 아이디
    username =request.user.username if request.user.is_authenticated else ''
    print("현재 로그인된 사용자 아이디 : {}".format(username))
    return render(request, 'cookie/index.html', {'no_event_popup' : no_event_popup})

# /cookie/event-popup
def event_popup(request):
    response = JsonResponse({'status':'ok'})
    # 쿠키 설정 : no_event_popup, 값은 true, 유효기간은 하루
    response.set_cookie('no_event_popup', 'true', max_age=60*60*24) # 하루
    return response

# /login
def login_view(request):
    if request.method == 'GET':
        # 쿠키 확인
        if 'login_username' in request.COOKIES:
            login_username = request.COOKIES['login_username']
        else:
            login_username = ''

        return render(request, 'cookie/login.html', {'login_username' : login_username})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 아이디 저장
        remember_id = request.POST.get('remember_id', 'off') == 'on'
        # 자동 로그인
        remember_me = request.POST.get('remember_me', 'off') == 'on'

        # 로그인 인증
        user = authenticate(request, username=username, password=password)

        response = redirect('/')

        if user:
            # 로그인 처리
            login(request, user)
            # ✅자동 로그인
            if remember_me:
                # 세션에 정보 저장
                request.session.set_expiry(60*60*24*30) # 30일
            else:
                request.session.set_expiry(0)       # 브라우저 종료 시 세션 만료

            # ✅아이디 저장
            if remember_id:
                # 쿠키 설정
                response.set_cookie('login_username', username, max_age=60*60*7) # 7일
            else:
                # 쿠키 삭제
                response.delete_cookie('login_username')
        else:
            return redirect('/login?error=1') # 로그인 실패 시 에러 페이지로 리다이렉트

        return

