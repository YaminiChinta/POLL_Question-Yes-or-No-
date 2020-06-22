from django.shortcuts import render,redirect
from django.http import HttpResponse
from pollapp.forms import Myform
from pollapp.models import Spoll,POLL,Names
import random
import qrcode
# Create your views here.
gotp=0

def login(request):
	otp=random.randint(10000,99999)
	image=qrcode.make("otp is"+str(otp))
	image.save(r"pollapp/static/qrcode/otp.jpg")
	global gotp
	if gotp==0:
		gotp=otp
		print(gotp)

	if request.method=="POST":
		uotp=request.POST['otp']
		print(uotp)
		if str(gotp)==str(uotp):
			gotp=0
			return redirect("/admin_page")
		else:
			gotp=0
			return HttpResponse("Invalid")
	else:
		return render(request,'pollapp/login.html')

def poll_q(req):
	if req.method=="POST":
		que=req.POST['question']
		data=POLL(question=que)
		data.save()
		sp=Spoll.objects.all().delete()
		#p=POLL.objects.all().delete()
		n=Names.objects.all().delete()
		return redirect('/admin_page')
	return render(req,'pollapp/poll_q.html',{})

def answer(req):
	if req.method =="POST":
		data=Names(name=req.POST['name'])
		data.save()
		return redirect('/submit')
	return render(req,'pollapp/answer.html')

def submit(req):
	if req.method=="POST":
		data=Myform(req.POST)
		data.save()
		return HttpResponse("<h1>Done</h1>")
	form=Myform()
	data=POLL.objects.last()
	# data={'data':data.question}
	return render(req,'pollapp/submit.html',{'form':form,'data':data.question})

def admin_page(req):
	data=Spoll.objects.all()
	y=0
	n=0
	for i in data:
		if i.opt=="Yes":
			y=y+1
		else:
			n=n+1
	data={'Yes':y,"No":n}
	return render(req,"pollapp/result.html",{'data':data})