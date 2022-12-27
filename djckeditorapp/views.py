from django.shortcuts import render, redirect
from .models import CKEditorModel
from .forms import CKEditorForm
 

# Create your views here.

def ckindex(request):
    ckdata = CKEditorModel.objects.all().order_by('-date')
    context = {'cke_list':ckdata}
    return render(request, 'ckeditortemplate/ckindex.html', context)

def ck_add(request):
    if request.method == 'POST':
        form = CKEditorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ckhome') 
    else:
        form = CKEditorForm()
    return render(request, 'ckeditortemplate/ckadd.html', {'ckadd_form':form} )

def ck_update(request, id):
    obj = CKEditorModel.objects.get(id=id)
    if request.method == 'POST':
        form = CKEditorForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('ckhome')
    else:
        form = CKEditorForm(instance=obj)
    return render(request,'ckeditortemplate/ckupdate.html', {'update_form':form} )

def ck_delete(request, id):
    ckdatadelete = CKEditorModel.objects.get(id=id)
    if request.method == 'POST':
        ckdatadelete.delete()
        return redirect('ckhome')
    return render(request,'ckeditortemplate/ckdelete.html', {'cklist_delete':ckdatadelete} )

def ck_details(request,id):
    ckdatadetail= CKEditorModel.objects.get(id=id)
    return render(request, 'ckeditortemplate/ckdetail.html', {'cklist_detail':ckdatadetail})






































