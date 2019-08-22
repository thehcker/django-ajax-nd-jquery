from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import BookForm
from book.models import Book

# Create your views here.

def books_list(request):
	template = 'books.html'
	books = Book.objects.all()
	return render(request, template, {'books': books})

def base(request):
	form = BookForm()
	context = {'form': form}
	html_form = render_to_string('books/partial_book_create.html', context, request=request,)
	return render(request, template, {})


def save_book_form(request, form, template_name):
	data = dict ()
	if request.method == 'POST':
		# form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			books = Book.objects.all()
			data['html_book_list'] = render_to_string('partial_book_list.html', {'books': books})

		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data['html_form'] = render_to_string(template_name, context, request=request)

	return JsonResponse(data)

def book_create(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
	else:
		form = BookForm()
	return save_book_form(request, form, 'partial_book_create.html')


def book_update(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		form = BookForm(request.POST, instance=Book)
	else:
		form = BookForm(instance=book)
	return save_book_form(request, form, 'partial_book_update.html') 


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        books = Book.objects.all()
        data['html_book_list'] = render_to_string('partial_book_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('partial_book_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)