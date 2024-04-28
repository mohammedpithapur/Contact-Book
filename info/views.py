from django.shortcuts import render,redirect
from .models import InfoModel
import random

# Create your views here.
def list(request):
    owner=request.user.id
    contact=InfoModel.objects.filter(owner=owner)
    print(contact)
    
    return render(request, 'contact_list.html', {"contact":contact})


def add_contact(request, contact_id=None):
    owner=request.user.id
    # If contact_id is provided, it means we are editing an existing contact
    if contact_id:
        contact = InfoModel.objects.get(rollnumber=contact_id)
    else:
        contact = None

    if request.method == 'POST':

        ids={1,2,3}
        num=random.randint(0,1000)
        flage=True
        while flage:
            if num not in ids:
                ids.add(num)
                number = num
                flage=False
            else:
                num=random.randint(0,1000)
            

        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        
        # Handle dynamic fields
        dynamic_data={}
        dynamic_fields = request.POST.getlist('new_field[]')
        dynamic_label = request.POST.getlist('label')
        for i in range(len(dynamic_fields)):
            dynamic_data[dynamic_label[i]]=dynamic_fields[i]
        print(dynamic_data)

        if contact:
            contact = InfoModel.objects.get(rollnumber=contact_id)
            # If editing an existing contact, update the contact object
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.extra_data=dynamic_data
            # for key, value in dynamic_data.items():
                
            #     print(value)
            contact.save(update_fields=["name", "email", "phone","extra_data"],)
            dynamic_data={}
        else:
            # If adding a new contact, create a new Contact object
            contact = InfoModel.objects.create(owner=owner,rollnumber=number, name=name, email=email, phone=phone, extra_data=dynamic_data)
            dynamic_data={}
        return redirect('/')  # Redirect to the contact list page after adding/editing a contact
    else:
        dynamic_data={}
        return render(request, 'contact_form.html', {'contact': contact})
    
def contact_detail (request, contact_id):
    details = InfoModel.objects.get(rollnumber=contact_id)
    return render(request,"contact_detail.html",{"contact":details})
def delete(request, contact_id):
    InfoModel.objects.filter(rollnumber=contact_id).delete()
    return redirect('/')
