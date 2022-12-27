from django.shortcuts import render, redirect, get_object_or_404
from .models import FbCrudModel
from .forms import FbCrudForm

# Create your views here.



def fbhome_list(request):
    #context = {}
    datalist = FbCrudModel.objects.all()
    #context['crud_list'] = FbCrudModel.objects.all()
    context = {
            'crud_list':datalist 
        }
    return render(request, 'fbvtemplate/fbindex.html', context)

#'''
def fbcrud_add(request):
    form = FbCrudForm()
    if request.method == 'POST':
        form = FbCrudForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('fbhome')
    context = {
        "form":form
        }
    return render(request, 'fbvtemplate/fbadd.html', context)

'''
def fbcrud_add(request):
    if request.method == 'POST':
        form = FbCrudForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('fbhome')
    else:
        form = FbCrudForm()
    return render(request, 'fbvtemplate/fbadd.html', {'form': form})

#'''

'''   
# this function for without image upload. only for text input
def fbcrud_add2(request):
    if request.method == 'POST':
        form = FbCrudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fbhome')
    form = FbCrudForm()
    return render(request, 'fbvtemplate/fbadd.html', {'form':form})
'''

def fbcrud_update(request, id):
    obj = FbCrudModel.objects.get(id=id)
    if request.method == 'POST':
        form = FbCrudForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('fbhome')
    else:
        form = FbCrudForm(instance=obj)

    #context = {"update_form":form }    
    return render(request, 'fbvtemplate/fbupdate.html', {"update_form":form }) #context)


'''
def fbcrud_update(request, id):
    #context ={}
    obj = FbCrudModel.objects.get(id=id) 
    #or, get_object_or_404(FbCrudModel, id = id)
    form = FbCrudForm(request.POST or None, instance = obj)
    if request.method == "POST": 
        if form.is_valid():
            form.save()
            return redirect ('fbhome')
    context = {
        'update_form':form
        }
    return render(request, 'fbvtemplate/fbupdate.html', context)
'''





'''
def fbcrud_update2(request, id):
	context ={}
	obj = get_object_or_404(FbCrudModel, id = id)
	form = FbCrudForm(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect('fbhome')
	context["update_form"] = form
	return render(request, 'fbvtemplate/fbupdate.html', context)
'''

 
def fblist_delete(request, id):
    datalist3 = FbCrudModel.objects.get(id=id)
    if request.method =='POST':
        datalist3.delete()
        return redirect('fbhome')
    context = {
        'crud_list_delete':datalist3
        }
    return render(request,  'fbvtemplate/fbdelete.html', context)


def fblist_details(request, id):
    datalist2 = FbCrudModel.objects.get(id=id)
    context = {
        'crud_list_detail':datalist2
        }
    return render(request, 'fbvtemplate/fbdetail.html', context)
























