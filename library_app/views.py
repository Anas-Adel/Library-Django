from django.shortcuts import render, redirect
from .models import Book , Category
from .forms import addBook_form, CreateUserForm
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# @login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        return search(request , 'view-books.html')
    categories = Category.objects.all()
    return render(request, 'home-page.html', {'categories':categories})

def view_books(request):
    if request.method == 'POST':
        return search(request , 'view-books.html')
    return render(request, 'view-books.html',{'books':Book.objects.all(), 'categories':Category.objects.all()})




def sign_up(request):
    form = CreateUserForm()
    print("hello")
    if request.method == 'GET':
        return render(request, 'sign-up.html', {'form': form})

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was successfullty created')
            return redirect('login')
        lst = []
        dic = form.errors.as_data()
        for i in dic:
            lst1 = dic[i]
            for j in lst1:
                a = str(j)
                print(a[2:-2])
                lst.append(a[2:-2])


    return render(request, 'sign-up.html', {'form': form, 'messeges':messages, 'error_lst':lst})

def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('Username')
        passw = request.POST.get('password')

        user = authenticate(request, username=name, password=passw)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            err = "Username or password incorrect"
            return render(request, 'login.html', {'err':err})

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


# if user.is_authenticated and user.is_superuser:
def admin(request):
    if request.method == 'POST':
        return search(request, 'admin-page.html')

    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'admin-page.html', {'books':Book.objects.all()})
    else:
        return HttpResponse("You are not allowed to this page")

def view_borowed(request):
    if request.method == 'POST':
        return search(request, 'view-borowed.html')
    # user = request.user
    # borrowed_books = Book.objects.filter(borrowed_by=user.name)
    return render(request, 'view-borowed.html',{'books':Book.objects.all()})

def add_book(request):


    if request.method == 'POST':
        # name = request.POST['bookName']
        # auth = request.POST['author']
        # catg = request.POST['category']
        # desc = request.POST['description']



        # is_uniq = True
        # for instance in Book.objects.all():
        #         if instance.name == name:
        #             is_uniq = False
        # if is_uniq:
        #     new_book = Book(name=name, Author=auth, category=catg, description=desc)
        #     new_book.save()
        #     message = "book was added successfully"
        #     return render(request, 'add-book.html', {'message':message})
        # else:
        #     message = "Book was added before"
        #     return render(request, 'add-book.html', {'message': message})

        form = addBook_form(request.POST)
        if form.is_valid():
            form.save()
            message = "book was added successfully"
            return render(request, 'add-book.html', {'form':form, 'message':message})
        else:
            message = "book is not valid"
            return render(request, 'add-book.html', {'form':form, 'message': message})

    else:
        form = addBook_form()


    return render(request, 'add-book.html', {'form':form})


def edit_book(request , book_id):
    book = Book.objects.get(pk=book_id)
    form = addBook_form(request.POST or None,instance=book)

    if request.method == 'POST':
        # name = request.POST['bookName']
        # auth = request.POST['author']
        # catg = request.POST['category']
        # desc = request.POST['description']
        # book.name = name
        # book.Author = auth
        # book.category = catg
        # book.description = desc
        # book.save()
        if form.is_valid():
            form.save()
            return redirect('admin-page')

    return render(request, 'edit-book.html',{'form':form})

def book_page(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book-page.html', {'book':book})

def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('admin-page')

def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.borrowed_by = request.user
    book.availabilty = False
    book.save()
    return render(request, 'book-page.html', {'book':book})

def return_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.borrowed_by = None
    book.availabilty = True
    book.save()
    return render(request, 'book-page.html', {'book':book})


def search(request , path):
    search_by = request.POST['search_by']
    search = request.POST['search_value']
    categories = Category.objects.all()
    books = Book.objects.all()
    if search_by == "by Author":
        books = books.filter(Author = search)
    elif search_by == "by Category":
        categories = categories.filter(name = search)
        catg = Category.objects.get(name = search)
        books = books.filter(category = catg)
    else:
        books = Book.objects.filter(name = search)

    return render(request, path,{'books':books, 'categories':categories})