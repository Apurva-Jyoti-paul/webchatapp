from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import gchat,wpgc
from .forms import txtform,groupform





@login_required
def send(request):
    dod=wpgc.objects.filter(members=request.user)
    cdod=dod.count()
    print(cdod)
    for j in dod:
        lo=j.members.all()
        ti=lo.count()
        print(lo[0])
        print(j.name)
    
    if request.method=='POST':
        txt=txtform(request.POST)
        print('1')
        k=[]
        
        #txt.writer.username=request.user.username
        #txt.writer.id=request.user.id
        #txt.writer.password=request.user.password
        if txt.is_valid:
            print('3')
            f=txt.save(commit=False)
            f.writer=request.user
            f.save()
            print('2')
            m=gchat.objects.order_by('time')
            txt=txtform()
            for i in m:
                print(i.groups.id)
                l=str(i.time)
                day=''
                ti=''
                t=1
                print(l)
                for k in l:
                    if k==' ':
                        t=0
                    elif t:
                        day=day+k
                    else :
                        ti=ti+k
                    
                    if k=='.':
                        break
                print(day)
                print(ti)
                r=request.user
                print(r)
               


            m.reverse()
            return render(request,'groupchat1.html',{'m':m,'txt':txt,'r':r})
    else:
        txt=txtform()
        m=gchat.objects.order_by('time')
        m.reverse()
        return render(request,'groupchat1.html',{'m':m,'txt':txt})



def mainv(request):
    a=wpgc.objects.filter(members=request.user)
    namu=str(request.user)
    return render(request,'main.html',{'a':a,'namu':namu})

@login_required
def create(request):
    if request.method=='POST':
        g=groupform(request.POST)
        if g.is_valid():
            l=g.save(commit=False)
            l.save()
            l.members.add(request.user)
            l.save()
            return redirect('main.html')
    else:
        print('amd')
        form=groupform()
        return render(request,'create.html',{'form':form})

        

# Create your views here.


def see(request,key):
    pass