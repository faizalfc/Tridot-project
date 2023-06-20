from django.shortcuts import render
from .models import Product, Location, ProductMovement
def empty(request):
   return render(request,"home.html")
def home(request):
    return render(request,"home.html")
def location(request):
    return render(request,"location.html")
def movement(request):
    return render(request,"movement.html")
def edit_product_id(request):
    return render(request,"update_product.html")
def edit_location_id(request):
    return render(request,"update_location.html")
def edit_pro_movement(request):
    return render(request,"update_movement.html")
def view(request):
    return render(request,"view.html")






def add_product_id(request):
    if request.method=="POST":
      try:
        product_id = int(request.POST['product_id'])
        pi=Product(product_id=product_id)
        pi.save()

        result = "Product Id Added"
        return render(request,"home.html",{'r':result})
      except:
        result = "Prodcut Id not Added"
        return render(request,"home.html",{'r':result})



def add_loction_id(request):
    if request.method=="POST":
      try:
        location_id = int(request.POST["location_id"])
        li=Location(location_id=location_id)
        li.save()
        
        result= "Location Id Added"
        return render(request,"location.html",{'r':result})
      except:
        result= "Location Id Not Added"
        return render(request,"location.html",{'r':result})


def add_product_movement(request):
     if request.method =="POST":
 
      try:
        product_id = int(request.POST['product_id'])
        from_location_id = request.POST['from_location']
        to_location_id = request.POST['to_location']
        product = request.POST['product']
        quantity = int(request.POST['quantity'])
        pm= ProductMovement(product_id=product_id,from_location=from_location_id,to_location=to_location_id,product=product,quantity=quantity)
        pm.save()

        result= "product movement Added"
        return render(request,"movement.html",{'r':result})
      except:
        result= "prooduct movement Not Added"
        return render(request,"movement.html",{'r':result})
     

def edit_pro(request):
    if request.method=="POST":
      try:
       product_id = int(request.POST['product_id'])
       prdt_id = int(request.POST['prdt_id'])
       pi=Product.objects.get(product_id=product_id)
       pi.product_id = prdt_id
       pi.save()

       result= "Product Id edited"
       return render(request,"update_product.html",{'r':result})
      
      except:
       result= "Product Id not edited"
       return render(request,"update_product.html",{'r':result})
    

def edit_location(request):
    if request.method=="POST":
     try:
       location_id = int(request.POST['location_id'])
       lct_id = int(request.POST['lct_id'])
       li=Location.objects.get(location_id=location_id)
       li.location_id = lct_id
       li.save()

       result= "Location Id edited"
       return render(request,"update_location.html",{'r':result})
     except:
       result= "Location Id not edited"
       return render(request,"update_location.html",{'r':result})

def edit_movement(request):
    if request.method=="POST":
      try:
        product_id = int(request.POST['product_id'])
        prdt_id = int(request.POST['prdt_id'])
        product = request.POST['product']
        quantity = int(request.POST['quantity'])
        pm=ProductMovement.objects.get(product_id=product_id)
        pm.product_id = prdt_id
        pm.quantity= quantity
        pm.product=product
        pm.save()

        result= "product movement edited"
        return render(request,"update_movement.html",{'r':result})
      except:
       result= "product movement not edited"
       return render(request,"update_movement.html",{'r':result})


def views(request):
    if request. method=="POST":
      try:

        product_id =int(request.POST['product_id'])
        pi=Product.objects.get(product_id=product_id)
        pm=ProductMovement.objects.get(product_id=product_id)
        return render(request,"display.html",{'pi':pi.product_id,'t':pm.timestamp,'fl':pm.from_location,'tl':pm.to_location,'p':pm.product,'q':pm.quantity})
      except:
        result= "Invalid product Id"
        return render(request,"view.html",{'r':result})

