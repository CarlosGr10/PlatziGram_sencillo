#Django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

#Forms
from post.forms import PostForm

#Models
from post.models import Post

nombres = [{'titulo':'Hola',
            'usuario':{
                'nombre':'Carlos',
                'perfil':'https://picsum.photos/id/80/200/300'
            },
            'fecha':'Nov-2019',
            'foto':'https://picsum.photos/id/868/200/300'
            },
            {'titulo':'Hello fuck yeah',
            'usuario':{
                'nombre':'Rick Sanchez',
                'perfil':'https://picsum.photos/id/96/200/300'
            },
            'fecha':'Nov-2019',
            'foto':'https://picsum.photos/id/867/200/300'
            },
            {'titulo':'great Day',
            'usuario':{
                'nombre':'Evil Morty',
                'perfil':'https://picsum.photos/id/73/300'
            },
            'fecha':'Nov-2019',
            'foto':'https://picsum.photos/id/866/200/300'
            }
            ]

@login_required
def lista_post(request):
    posts = Post.objects.all().order_by('-created')
    return render(request,'post/feed.html',{'var_django':posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='post/new.html',
        context={
            'form':form,
            'user':request.user,
            'profile': request.user.profile
        }
    )
