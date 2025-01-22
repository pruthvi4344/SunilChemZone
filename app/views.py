from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_backends
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from .models import Standard, Chapter, StudyMaterial, Post, myphoto, myinfo, skills, myemail, mycontact  , insta, Tele, yt
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .models import Question,Quiz


# User Signup
def user_signup(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered. Please log in.')
            return render(request, 'account/signup.html') 
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken. Please choose another one.')
            return render(request, 'account/signup.html') 

        if password != password1:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'account/signup.html')

        # Create a new user in the auth_user table
        hashed_password = make_password(password)
        user = User.objects.create(
            username=username,  
            email=email,
            password=hashed_password
        )
        user.save()
                # Send the email confirmation
        email_address = EmailAddress.objects.create(user=user, email=email, verified=False)
        send_email_confirmation(request, user)
        messages.info(request, f"A verification email has been sent to {user.email} Please check your inbox. ")
        return redirect('verification')

        # # Get the default authentication backend
        # backend = get_backends()[0]  # Usually the first backend is the one you want
        # user.backend = f'{backend.__module__}.{backend.__class__.__name__}'

        # login(request, user)
        # messages.success(request, f"'Welcome!, {user.username} '")
        # return redirect('home')

    return render(request, 'signup.html')


# User Login
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
            # Authenticate using the username and password
        user = authenticate(request, username=user.username, password=password)
        # user = authenticate(username=email, password=password)  # Authenticate by username (email) and password
        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, f'Login successful, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'account/login.html')

    return render(request, 'login.html')


# User Logout
def user_logout(request):
    request.session.flush() # Log out the user
    messages.success(request, 'You have been logged out.')
    return redirect('login')


# Home Page (Protected)

@login_required
def home(request):
    photos = myphoto.objects.first()
    aboutme = myinfo.objects.first()
    aboutskills = skills.objects.all()
    emailad = myemail.objects.all()
    contacts = mycontact.objects.all()
    instagrams = insta.objects.all()
    telegrams = Tele.objects.all()
    youtubes = yt.objects.all()
    posts = Post.objects.all().order_by('-id')

    print(emailad)
    print(contacts)
    # print(youtubes)
    # print(instagrams)
    # print(telegrams)


    paginator = Paginator(posts, 7)  # 5 posts per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the page object for the current page

    materials = None
    selected_chapter_id = None
    chapters = []
    
    if request.method == 'POST':
        # Handle the contact form submission
        if 'contact_form' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            subject = "New Contact Form Submission"
            email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            from_email = 'sunilchemzone2403@gmail.com'
            recipient_list = ['sunilchemzone2403@gmail.com']

            try:
                send_mail(subject, email_message, from_email, recipient_list)
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, f"Failed to send email: {e}")
            return redirect('home')

        # Handle material filter form submission
        elif 'filter_materials' in request.POST:
            chapter_id = request.POST.get('chapter')
            standard_id = request.POST.get('standard')
            
            if chapter_id:
                materials = StudyMaterial.objects.filter(chapter_id=chapter_id)
                selected_chapter_id = chapter_id
                chapters = Chapter.objects.filter(std_id=standard_id)
    

    
    return render(request, 'index.html', {
        'standards': Standard.objects.all(),
        'materials': materials,
        'selected_chapter_id': selected_chapter_id,
        'chapters': chapters,
        'page_obj': page_obj,
        'photos': photos,
        'aboutme': aboutme,
        'aboutskills': aboutskills,
        'emailad':emailad,
        'contacts': contacts,
        'telegrams': telegrams,
        'youtubes': youtubes,
        'instagrams': instagrams,
    })


def get_chapters(request):
    standard_id = request.GET.get('standard_id')
    if standard_id:
        chapters = Chapter.objects.filter(std_id=standard_id)
        data = list(chapters.values('id', 'name'))
        return JsonResponse({'chapters': data})
    return JsonResponse({'chapters': []})
@login_required
def blog(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'blog.html', {'post': post})

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})

def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()
    user_answers = request.POST

    results = []
    for question in questions:
        user_answer = user_answers.get(str(question.id))
        correct = user_answer == question.correct_answer
        results.append({'question': question.text, 'correct': correct, 'user_answer': user_answer, 'correct_answer': question.correct_answer})

    return render(request, 'quiz_result.html', {'quiz': quiz, 'results': results})

