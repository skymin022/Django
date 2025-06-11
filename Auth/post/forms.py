from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content' ]
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '제목을 입력하세요'
            }),
            'content' : forms.Textarea(attrs={
                'class' : 'form-control',
                'rows' : 5,
                'placeholder' : '내용을 입력하세요'
            }),
        }

    # title 필드에 대한 유효성 검사
    def clean_title(self):
        # self.cleaned_data : 폼이 제출된 후 유효성 검사를 통과한 데이터
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('제목을 입력해주세요!')
        return title

    # content 필드에 대한 유효성 검사
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError('내용을 입력해주세요!')
        return content

    # 공통 유효성 검사
    def clean(self):
        # 2차 유효성 검사
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if not title and not content:
            raise forms.ValidationError('제목과 내용 모두 입력해주세요')

        return cleaned_data





# class ReadForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']


# class UpdateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']
#     def __init__(self, *args, **kwargs):
#         super(UpdateForm, self).__init__(*args, **kwargs)
#         # 필드 공통 설정
#         for field in self.fields.values():
#             field.widget.attrs.update({'class' : 'form-control'})

#         self.fields['title'].widget.attrs.update({'placeholder' : '아이디'})
#         self.fields['content'].widget.attrs.update({'placeholder' : '비밀번호'})



