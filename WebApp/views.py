from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import JavaScriptQuestion1,JavaScriptQuestion2,JavaScriptQuestion3,JavaScriptQuestion4
from .models import PhpQuestion1,PhpQuestion2,PhpQuestion3,PhpQuestion4
from .models import PhpVideoPost,JavascriptVideoPost
from .models import PhpCreateProfile,MeetPhpExpert,JavascriptCreateProfile,MeetJavascriptExpert

from .forms import PhpProfile,MeetPhp,JavascriptProfile,MeetJavascript
from .forms import RegistrationForm

# php expertprofile view 
def phpexpertprofile(request):
	if request.method=="POST":
		profile=PhpProfile(request.POST,request.FILES)
		if profile.is_valid():
			try:
				profile.save()
				return redirect('showPhpExperts')
			except:
				pass

	else:
		profile=PhpProfile()
 
	context={
	"form":profile
	}
	return render(request,'phpexpertprofile.html',context)

def showPhpExperts(request):
    showPhpExperts=PhpCreateProfile.objects.all().order_by("name")
    context={
      "messages":"successfull profile created",
      "shows":showPhpExperts
    }
    return render(request,'showPhpExperts.html',context)
    
# javascript expertprofile view 
def javascriptexpertprofile(request):
	if request.method=="POST":
		profile=JavascriptProfile(request.POST,request.FILES)
		if profile.is_valid():
			try:
				profile.save()
				return redirect('showJSexperts')
			except:
				pass

	else:
		profile=JavascriptProfile()
   
	context={
	"form":profile
	}
	return render(request,'javascriptexpertprofile.html',context)

def showJSexperts(request):
    showJSexperts=JavascriptCreateProfile.objects.all().order_by("name")
    context={
      "messages":"successfull profile created",
      "shows":showJSexperts
    }
    return render(request,'showJSexperts.html',context)


def phpExperts(request):
    display=PhpCreateProfile.objects.all()
    context={
    "display":display
    }
    return render(request,'phpExperts.html',context)

# display php profile view 
def displayphpprofile(request):
	display=PhpCreateProfile.objects.all()
	context={
	"display":display
	}
	return render(request,'displayphpprofile.html',context)

# display javascript profile view 
def displayjavascriptprofile(request):
	display=JavascriptCreateProfile.objects.all()
	context={
	"display":display
	}
	return render(request,'displayjavascriptprofile.html',context)



# meet php expert view 
def meetphpexpert(request):
	if request.method=="POST":
		form=MeetPhp(request.POST,request.FILES)
		if form.is_valid():
			try:
				form.save()
				return redirect('meetphpexpert')
			except:
				pass

	else:
		form=MeetPhp()
		disp=MeetPhpExpert.objects.all()
    
	context={
	"form":form,
	"display":disp
	}
	return render(request,'meetphpexperts.html',context)


# meet javascript expert view 
def meetjavascriptexpert(request):
	if request.method=="POST":
		form=MeetJavascript(request.POST,request.FILES)
		if form.is_valid():
			try:
				form.save()
				return redirect('meetjavascriptexperts')
			except:
				pass

	else:
		form=MeetJavascript()
		
	context={
	"form":form,
	"display":MeetJavascriptExpert.objects.order_by('-time')
	}
	return render(request,'meetjavascriptexperts.html',context)




# we import random module
import random

# other views 
def index(request):
    context={}
    return render(request,'index.html',context)

def loginIndex(request):
    context={}
    return render(request,'loginIndex.html',context)

def home(request):
    context={}
    return render(request,'home.html',context)

def expertsHome(request):
    context={}
    return render(request,'expertsHome.html',context)

def expertsAnalysis(request):
    context={}
    return render(request,'expertsAnalysis.html',context)

def phpQuestions(request):
    context={}
    return render(request,'phpQuestions.html',context)

def pythonQuestions(request):
    context={}
    return render(request,'pythonQuestions.html',context)

def javaQuestions(request):
    context={}
    return render(request,'javaQuestions.html',context)

# javascript questions views

def javascriptQuestions1(request):
     if request.method=="POST":
        jsqns1=JavaScriptQuestion1.objects.all()
        
        correct=0
        incorrect=0
        score=0
        percent=0
        success="" 
        failure=""

        for q in jsqns1:
            if q.ans==request.POST.get(q.qns):
                correct+=1
                score+=10   

            else:
                incorrect+=1

        percent=(score/250)*100
        if percent>=75:
            success+="Congratulation your marks met our credit, sign up as:"    
        else:
            failure+="Your marks does not met our credit, sign up as:"  

        context={
            "correct":correct,
            "incorrect":incorrect,
            "percent":percent,
            "score":score,
            "success":success,
            "failure":failure
        }
        return render(request,'javascriptResult.html',context)

     else:
        jsqns1=JavaScriptQuestion1.objects.all()       

        context={
            "jsqns1":jsqns1

        }
        return render(request,'javascriptQuestions1.html',context)



def javascriptQuestions2(request):
     if request.method=="POST":
        jsqns2=JavaScriptQuestion2.objects.all()
        
        correct=0
        incorrect=0
        score=0
        percent=0
        success="" 
        failure=""
        

        for q in jsqns2:
            if q.ans==request.POST.get(q.qns):
                correct+=1
                score+=10   
                 
            else:
                incorrect+=1
        
        percent=(score/250)*100
        if percent>=75:
            success+="Congratulation your marks met our credit, sign up as:"    
        else:
            failure+="Your marks does not met our credit, sign up as:" 

        context={
            "correct":correct,
            "incorrect":incorrect,
            "percent":percent,
            "score":score,
            "success":success,
            "failure":failure
        }
        return render(request,'javascriptResult.html',context)

     else:
        jsqns2=JavaScriptQuestion2.objects.all()       

        context={
            "jsqns2":jsqns2

        }
        return render(request,'javascriptQuestions2.html',context)


def javascriptQuestions3(request):
     if request.method=="POST":
        jsqns3=JavaScriptQuestion3.objects.all()
        
        correct=0
        incorrect=0
        score=0
        percent=0
        success="" 
        failure=""

        for q in jsqns3:
            if q.ans==request.POST.get(q.qns):
                correct+=1
                score+=10   
               
            else:
                incorrect+=1

        percent=(score/250)*100
        if percent>=75:
            success+="Congratulation your marks met our credit, sign up as:"    
        else:
            failure+="Your marks does not met our credit, sign up as:"  

        context={
            "correct":correct,
            "incorrect":incorrect,
            "percent":percent,
            "score":score,
            "success":success,
            "failure":failure
        }
        return render(request,'javascriptResult.html',context)

     else:
        jsqns3=JavaScriptQuestion3.objects.all()       

        context={
            "jsqns3":jsqns3

        }
        return render(request,'javascriptQuestions3.html',context)

def javascriptQuestions4(request):
     if request.method=="POST":
        jsqns4=JavaScriptQuestion4.objects.all()
        
        correct=0
        incorrect=0
        score=0
        percent=0
        success="" 
        failure=""

        for q in jsqns4:
            if q.ans==request.POST.get(q.qns):
                correct+=1
                score+=10   

            else:
                incorrect+=1

        percent=(score/250)*100
        if percent>=75:
            success+="Congratulation your marks met our credit, sign up as:"    
        else:
            failure+="Your marks does not met our credit, sign up as:"  

        context={
            "correct":correct,
            "incorrect":incorrect,
            "percent":percent,
            "score":score,
            "success":success,
            "failure":failure
        }
        return render(request,'javascriptResult.html',context)

     else:
        jsqns4=JavaScriptQuestion4.objects.all()       

        context={
            "jsqns4":jsqns4

        }
        return render(request,'javascriptQuestions4.html',context)

        


# php questions views
def phpQuestions1(request):
     if request.method=="POST":
        phpqns1=PhpQuestion1.objects.all()
        
        correct=0
        incorrect=0
        score=0
        percent=0
        success="" 
        failure=""

        for q in phpqns1:
            if q.ans==request.POST.get(q.qns):
                correct+=1
                score+=10   
 
            else:
                incorrect+=1

        percent=(score/250)*100
        if percent>=75:
            success+="Congratulation your marks met our credit, sign up as:"    
        else:
            failure+="Your marks does not met our credit, sign up as:"  


        context={
            "correct":correct,
            "incorrect":incorrect,
            "percent":percent,
            "score":score,
            "success":success,
            "failure":failure
        }
        return render(request,'phpResult.html',context)

     else:
        phpqns1=PhpQuestion1.objects.all()       

        context={
            "phpqns1":phpqns1

        }
        return render(request,'phpQuestions1.html',context)


def phpQuestions2(request):
     if request.method=="POST":
        phpqns2=PhpQuestion2.objects.all()
 
        correct=0
        incorrect=0
        score=0
        percent=0
        success="" 
        failure=""

        for q in phpqns2:
            if q.ans==request.POST.get(q.qns):
                correct+=1
                score+=10   
 
            else:
                incorrect+=1

        percent=(score/250)*100
        if percent>=75:
            success+="Congratulation your marks met our credit, sign up as:"    
        else:
            failure+="Your marks does not met our credit, sign up as:"  

        context={
            "correct":correct,
            "incorrect":incorrect,
            "percent":percent,
            "score":score,
            "success":success,
            "failure":failure
        }
        return render(request,'phpResult.html',context)

     else:
        phpqns2=PhpQuestion2.objects.all()

        context={
            "phpqns2":phpqns2
        }
        return render(request,'phpQuestions2.html',context)


def phpQuestions3(request):
     if request.method=="POST":
        phpqns3=PhpQuestion3.objects.all()
 
        correct=0
        incorrect=0
        score=0
        percent=0
        success="" 
        failure=""

        for q in phpqns3:
            if q.ans==request.POST.get(q.qns):
                correct+=1
                score+=10   
                
            else:
                incorrect+=1

        percent=(score/250)*100
        if percent>=75:
            success+="Congratulation your marks met our credit, sign up as:"    
        else:
            failure+="Your marks does not met our credit, sign up as:"  

        context={
            "correct":correct,
            "incorrect":incorrect,
            "percent":percent,
            "score":score,
            "success":success,
            "failure":failure
        }
        return render(request,'phpResult.html',context)

     else:
        phpqns3=PhpQuestion3.objects.all()

        context={
            "phpqns3":phpqns3
        }
        return render(request,'phpQuestions3.html',context)


def phpQuestions4(request):
     if request.method=="POST":
        phpqns4=PhpQuestion4.objects.all()
 
        correct=0
        incorrect=0
        score=0
        percent=0
        success="" 
        failure=""

        for q in phpqns4:
            if q.ans==request.POST.get(q.qns):
                correct+=1
                score+=10   

            else:
                incorrect+=1

        percent=(score/250)*100
        if percent>=75:
            success+="Congratulation your marks met our credit, sign up as:"    
        else:
            failure+="Your marks does not met our credit, sign up as:"  

        context={
            "correct":correct,
            "incorrect":incorrect,
            "percent":percent,
            "score":score,
            "success":success,
            "failure":failure
        }
        return render(request,'phpResult.html',context)

     else:
        phpqns4=PhpQuestion4.objects.all()

        context={
            "phpqns4":phpqns4
        }
        return render(request,'phpQuestions4.html',context)
        


def androidQuestions(request):
    context={}
    return render(request,'androidQuestions.html',context)

def cplusplusQuestions(request):
    context={}
    return render(request,'cplusplusQuestions.html',context)

def csharpQuestions(request):
    context={}
    return render(request,'csharpQuestions.html',context)

def flutterQuestions(request):
    context={}
    return render(request,'flutterQuestions.html',context)

def reactNativeQuestions(request):
    context={}
    return render(request,'reactNativeQuestions.html',context)

def amateurSignUp(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
           if User.objects.filter(email=email).exists():
               messages.info(request,'Sorry, your email already exists')
               return redirect('amateurSignUp')
          
           elif User.objects.filter(username=username).exists():
                 messages.info(request,'Sorry, your username already exists')
                 return redirect('amateurSignUp')

           else:
               user=User.objects.create_user(username=username,email=email,password=password)
               user.save()
               return redirect('amateurLogin')
      
        else:
            messages.info(request,'Password you entered are not the same')
            return redirect('amateurSignUp')

    else: 
       return render(request,'amateurSignUp.html')
# 

def expertSignUp(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
           if User.objects.filter(email=email).exists():
               messages.info(request,'Sorry, your email already exists')
               return redirect('expertSignUp')
          
           elif User.objects.filter(username=username).exists():
                 messages.info(request,'Sorry, your username already exists')
                 return redirect('expertSignUp')

           else:
               user=User.objects.create_user(username=username,email=email,password=password)
               user.save()
               return redirect('expertLogin')
      
        else:
            messages.info(request,'Password you entered are not the same')
            return redirect('expertSignUp')

    else: 
       return render(request,'expertSignUp.html')

#new expert signup form
# for later use
def newexpertsignup(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('expertLogin')
        else:
            messages.info(request,'invalid form ')
    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'newexpertsignup.html',context)

def amateurLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
       
        else:
            messages.info(request,'Sorry, your credentials are not valid')
            return redirect('amateurLogin')        
    
    else:
        return render(request,'amateurLogin.html')


def expertLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('expertsHome')
       
        else:
            messages.info(request,'Sorry, your credentials are not valid')
            return redirect('expertLogin')        
    
    else:
        return render(request,'expertLogin.html')



def mylogout(request):
    auth.logout(request)
    return redirect('loginIndex')



def about(request):
    context={}
    return render(request,'about.html',context)

def web(request):
    context={}
    return render(request,'web.html',context)

def mobile(request):
    context={}
    return render(request,'mobile.html',context)

def desktop(request):
    context={}
    return render(request,'desktop.html',context)

def pythonExperts(request):
    context={}
    return render(request,'pythonExperts.html',context)

def javascriptExperts(request):
    display=JavascriptCreateProfile.objects.all()
    context={
    "display":display
    }
    return render(request,'javascriptExperts.html',context)

def cplusplusExperts(request):
    context={}
    return render(request,'cplusplusExperts.html',context)

def csharpExperts(request):
    context={}
    return render(request,'csharpExperts.html',context)

def javaExperts(request):
    context={}
    return render(request,'javaExperts.html',context)

def reactnativeExperts(request):
    context={}
    return render(request,'reactnativeExperts.html',context)

def androidExperts(request):
    context={}
    return render(request,'androidExperts.html',context)

def flutterExperts(request):
    context={}
    return render(request,'flutterExperts.html',context)

def askphp(request):
    if request.method=="POST":
        form=MeetPhp(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('askphp')
            except:
                pass

    else:
        form=MeetPhp()
        disp=MeetPhpExpert.objects.all()
    context={
    "form":form,
    "display":disp
    }
    return render(request,'askphp.html',context)
 

def askjava(request):
    context={}
    return render(request,'askjava.html',context)

def askjavascript(request):
    if request.method=="POST":
        form=MeetJavascript(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('askjavascript')
            except:
                pass

    else:
        form=MeetJavascript()
        disp=MeetJavascriptExpert.objects.all()
    context={
    "form":form,
    "display":disp
    }
    return render(request,'askjavascript.html',context)

def askpython(request):
    context={}
    return render(request,'askpython.html',context)

def askcplusplus(request):
    context={}
    return render(request,'askcplusplus.html',context)

def askcsharp(request):
    context={}
    return render(request,'askcsharp.html',context)


def askandroid(request):
    context={}
    return render(request,'askandroid.html',context)

def askflutter(request):
    context={}
    return render(request,'askflutter.html',context)


def askreactnative(request):
    context={}
    return render(request,'askreactnative.html',context)

def javascriptResult(request):
    return render(request, 'javascriptResult.html', {})

# all questions for javascript views
def alljsQuestions(request):
    js_questions_list=['javascriptQuestions1','javascriptQuestions2','javascriptQuestions3','javascriptQuestions4'] 
    js_bundle=random.choice(js_questions_list) 

    js_bundles="Javascript language is one among the most popular programming languages."

    js_bundle_question1=''
    js_bundle_question2=''
    js_bundle_question3=''
    js_bundle_question4=''
    


    if js_bundle=='javascriptQuestions1':
        js_bundle_question1+="Are you already for our survey?"
    
    elif js_bundle=='javascriptQuestions2':
          js_bundle_question2+="Are you already for our survey?"
    
    elif js_bundle=='javascriptQuestions3':
          js_bundle_question3+="Are you already for our survey?"

    elif js_bundle=='javascriptQuestions4':
          js_bundle_question4+="Are you already for our survey?"
    
   
    context={
        "js_bundles":js_bundles,
        "js_bundle_question1":js_bundle_question1,
        "js_bundle_question2":js_bundle_question2,
        "js_bundle_question3":js_bundle_question3,
        "js_bundle_question4":js_bundle_question4,
   

    }
    return render(request, 'alljsQuestions.html', context)
    


# all questions for php view
def allphpQuestions(request):
    php_questions_list=['phpQuestions1','phpQuestions2','phpQuestions3','phpQuestions4'] 
    php_bundle=random.choice(php_questions_list) 

    php_bundles="Php language is one among the most popular programming languages."

    php_bundle_question1=''
    php_bundle_question2=''
    php_bundle_question3=''
    php_bundle_question4=''
    


    if php_bundle=='phpQuestions1':
        php_bundle_question1+="Are you already for our survey?"
    
    elif php_bundle=='phpQuestions2':
          php_bundle_question2+="Are you already for our survey?"
    
    elif php_bundle=='phpQuestions3':
          php_bundle_question3+="Are you already for our survey?"

    elif php_bundle=='phpQuestions4':
          php_bundle_question4+="Are you already for our survey?"
    
   
    context={
        "php_bundles":php_bundles,
        "php_bundle_question1":php_bundle_question1,
        "php_bundle_question2":php_bundle_question2,
        "php_bundle_question3":php_bundle_question3,
        "php_bundle_question4":php_bundle_question4,
   

    }
    return render(request, 'allphpQuestions.html', context)


def kaham(request):
     return render(request, 'kaham.html', {"kaham":kaham})
        

def phpExpertHome(request):
    php_post_video =PhpVideoPost.objects.all()
    context={
        "php_post_video":php_post_video 
        }
    return render(request, 'phpExpertHome.html',context)

def jsExpertHome(request):
    js_post_video =JavascriptVideoPost.objects.all()
    context={
        "js_post_video":js_post_video
        }
    return render(request, 'jsExpertHome.html',context)


def phpResult(request):
    context={}
    return render(request,'phpResult.html',context)

def aboutExpert(request):
    context={}
    return render(request,'aboutExpert.html',context)
    

    
