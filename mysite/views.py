from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import AccessMixin  # 적절한 권한을 갖추었는지 판별하는 클래스


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm  # 장고에서 제공하는 회원가입 폼
    success_url = reverse_lazy(
        'register_done')  # urls가 메모리에 다 올라와야 URL 패턴을 해석할 수 있으므로, 천천히 해석하도록 하는 reverse_lazy() 함수 사용.


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerMixin(AccessMixin):
    # True: 403 익셉션 처리
    # False: 로그인 페이지로 리다이렉트
    raise_exception = True
    # 403 응답시 보여줄 메시지 저장. 403.html에서 사용
    permission_denied_message = "Owner only can update/delete the object"


# 메인 메소드 get() 이전단계인 dispatch() 오버라이드
# 여기서 소유자 여부를 판단하는 것이 일반적
def dispatch(self, request, *args, **kwargs):
    # 대상이 되는 객체를 테이블로부터 가져옵니다.
    obj = self.get_object()
    if request.user != obj.owner:
        # handle_no_permission() 메소드 호출, 여기서 403 Exception 처리
        return self.handle_no_permission()
    # 사용자와 오너가 같으면, 상위 클래스의 dispatch()메소드 호출
    return super().dispatch(request, *args, **kwargs)
