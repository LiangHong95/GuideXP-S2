from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):

	if request.method == 'POST':
		request.session['is_login'] = True
		# print(request.session['is_login'])
		return redirect('/home/')

	if request.method == 'GET':
		return render(request, 'login/login.html', {})

# def home_view(request):
# 	if request.method == 'GET':
# 		return render(request, "login/home.html", {})

# 	if request.method == 'POST':
# 		request.session['is_login'] = False
# 		return redirect('/login/')


def home_try_view(request):
	if request.method == 'GET':
		if not request.session.get('is_login', None):
			return redirect('/login/')
		else:
			return render(request, "login/home.html", {})

	if request.method == 'POST':
		request.session.flush()
		return redirect('/login/') 
