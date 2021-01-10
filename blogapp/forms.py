from django import forms


class CommentForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea, max_length=2000, min_length=5)

'''
class PostForm(forms.Form):
    title
    text
    picture
    '''
# TODO: Создать форму с валидацией. Поле picture не обязательное дляя заполнения.