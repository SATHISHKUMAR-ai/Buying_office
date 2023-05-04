from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from myapp1.models import *
from django.forms import DateField
from django.utils.datastructures import MultiValueDictKeyError
from matplotlib import pyplot as plt
from datetime import *  

# Create your views here.
def index(request):
     return render(request,'index.html')
     
def prelr(request):
     return render(request,'pre_log_reg.html')
     
def reg(request):
     return render(request,'reg.html')

def login(request):
     return render(request,'login.html')


def logout(request):
	del request.session['user']
	return render(request,'login.html')

def login_act(request):
     if request.method=='POST':
          cun=request.POST['un']
          cps=request.POST['ps']
          if(cun=="admin" and cps=="admin"):
               request.session['user']=cun
               return render(request,'admin.html')
          elif comreg1.objects.filter(commob=cun,compassword=cps).exists():               
               request.session['user']=cun
               return render(request,'index.html')
          else :
               res="Your Username or Password is Wrong !!!"
               return render(request,'login.html',{'result':res})

#company registration

def regcom(request):
     if request.method=='POST':
          cn=request.POST['name']
          cg=request.POST['gst']
          cm=request.POST['mobile']
          ce=request.POST['email']
          ca=request.POST['adres']
          cp=request.POST['ps']
          crp=request.POST['reps']
          cpc=request.FILES['dp']
          
          cr=comreg1()
          
          cr.comname=cn
          cr.comgstno=cg
          cr.commob=cm
          cr.comemail=ce
          cr.comaddress=ca
          cr.compassword=cp
          cr.comrepassword=crp
          cr.comgstcopy=cpc

          cr.save()
          res="Your Company Register Successfully"          
          return render(request,'pre_log_reg.html',{'result':res})


def proview(request):
     if request.session.has_key('user'):
          un=request.session['user']
          res=proddetails1.objects.all()	
          return render(request,'c_proview.html',{'prod':res,'cun':un})
     else:
           return render(request,'pre_log_reg.html',)

def viewcom(request):
     if request.session.has_key('user'):
          un=request.session['user']
          res=comreg1.objects.all()
          return render(request,'a_view_comdetails.html',{'comp':res,'cun':un})          
     else:
           return render(request,'login.html')


#adminpanel

def admin1(request):
     if request.session.has_key('user'):
          un=request.session['user']
          return render(request,'admin.html',{'cun':un})

def addproduct(request):
     return render(request,'a_add_product.html')


def admin2(request):
     if request.session.has_key('user'):
          un=request.session['user']
          count= comreg1.objects.all().count()  
          count1= proddetails1.objects.all().count()  
          count2= quatationdet.objects.all().count()  
          count3= activeorder1.objects.all().count()
          return render(request,'a_dashboard_admin.html',{'cou':count,'cou1':count1,'cou2':count2,'cou3':count3,'cun':un})         
     else:
          return render(request,'login.html')


#product details

def prodetails(request):     
     if request.session.has_key('user'):
          un=request.session['user']
          if request.method=='POST':
               
               pi=request.POST['pid']
               pn=request.POST['pname']
               pc=request.POST['prot_catag']
               pt=request.POST['prot_catag']
               pq=request.POST['pquant']
               ppic=request.FILES['pp']
               ppri=request.POST['pprice']
               pdisc=request.POST['pdis']
               pbst=request.POST['bsd']
               pbed=request.POST['bed']
               
               pd=proddetails1()
               
               pd.proid=pi
               pd.proname=pn
               pd.procatag=pc
               pd.protype=pt
               pd.proquant=pq
               pd.propic=ppic
               pd.proprice=ppri
               pd.prodisc=pdisc
               pd.Bidstartdate=pbst
               pd.Bidenddate=pbed

               pd.save()

               res="Product Stored Successfully"
               return render(request,'a_add_product.html',{'result':res,'admin':un})
     else:
          return render(request,'login.html')


def viewprod(request):
     if request.session.has_key('user'):
          un=request.session['user']
          res=proddetails1.objects.all()
          return render(request,'a_view_product.html',{'prod':res,'admin':un})
     else:
          return render(request,'login.html')


def selprod1(request,id):
     if request.session.has_key('user'):
          un=request.session['user']
          sp=proddetails1.objects.get(proid=id)	
          return render(request,'a_select_product.html',{'selprod':sp,'cun':un})


def prodelete(request,id):
     if request.session.has_key('user'):
          un=request.session['user']
          d=print("Product Deleted Successfully")
          proddetails1.objects.get(proid=id).delete()
          return render(request,'a_dashboard_admin.html.html',{'cun':un,'delete':d})


def proupdate(request):
     if request.session.has_key('user'):
          un=request.session['user']
          if request.method=='POST':
               pi=request.POST['pid']
               pn=request.POST['pn']
               pc=request.POST['pc']
               pt=request.POST['pt']
               pq=request.POST['pq']
               ppri=request.POST['pp']
               pdisc=request.POST['pd']
          if proddetails1.objects.get(proid=pi):
               pd=proddetails1()
               pd.proid=pi
               pd.proname=pn
               pd.procatag=pc
               pd.protype=pt
               pd.proquant=pq
               pd.proprice=ppri
               pd.prodisc=pdisc
               pd.save()
     return render(request,'a_view_product.html',{'cun':un,})

#order details

#quatation

def quat(request,id):
     if request.session.has_key('user'):
          un=request.session['user']
          res=proddetails1.objects.get(proid=id)
          res1=comreg1.objects.get(commob=un)
          return render(request,'Quatation.html',{'cun':un,'res':res,'res1':res1})
     else:
          return render(request,'login.html')

def quat1(request):
     if request.session.has_key('user'):
          un=request.session['user']
          if request.method=='POST':
               qid=request.POST['proid']
               qn=request.POST['proname']
               qcn=request.POST['comname']
               qcm=request.POST['comob']
               qp=request.POST['qpri']               
               qdd=request.POST['ddate']
               
               qt=quatationdet()
               
               qt.prod_id=qid
               qt.prod_name=qn
               qt.com_name=qcn
               qt.com_mob=qcm
               qt.price=qp
               qt.delev_date=qdd
               qt.save()
               res1="Quatation send Successfully"
               return render(request,'quatation.html',{'res1':res1,'admin':un})
     else:
          return render(request,'login.html')


def quatviewadmin(request):
     if request.session.has_key('user'):
          un=request.session['user']
          res=quatationdet.objects.all()
          return render(request,'a_view_quatation.html',{'quatv':res,'cun':un})          
     else:
           return render(request,'login.html')


def activeorder(request,id):     
     if request.session.has_key('user'):
          un=request.session['user'] 
          res=quatationdet.objects.get(prod_id=id)
          return render(request,'a_update_quatation.html',{'ao':res,'cun':un})
     
def updatestatus(request):     
     if request.session.has_key('user'):
          un=request.session['user']
          if request.method=='POST':
               sid=request.POST['pid']
               print(sid)
               quid=request.POST['uid']
               qupn=request.POST['upn']
               qucn=request.POST['ucn']
               qucm=request.POST['umn']
               qup=request.POST['up']
               qud=request.POST['udd']
               qus=request.POST['us']
               ao1=activeorder1()
               ao=quatationdet()
               if quatationdet.objects.filter(id=sid).exists():
                    ao1.proid=quid
                    ao1.proname=qupn
                    ao1.com_name=qucn
                    ao1.com_mob=qucm
                    ao1.price=qup
                    ao1.delev_date=qud
                    ao1.status=qus
                    ao1.save()
                    return render(request,'a_view_quatation.html',{'cun':un})

def orderdetails(request):     
     if request.session.has_key('user'):
          un=request.session['user']    
          res=activeorder1.objects.filter(com_mob=un)
          return render(request,'order_details_update.html',{'cun':un,'ao':res})

def activeorderstatus(request,id):
     if request.session.has_key('user'):
          un=request.session['user'] 
          res=activeorder1.objects.get(proid=id)
          return render(request,'c_active_order.html',{'ao2':res,'cun':un})

def orderstatus(request):     
     if request.session.has_key('user'):
          un=request.session['user']
          if request.method=='POST':
               sid=request.POST['pid']
               quid=request.POST['uid']
               qupn=request.POST['upn']
               qucn=request.POST['ucn']
               qucm=request.POST['umn']
               qup=request.POST['up']
               qud=request.POST['udd']
               qus=request.POST['aos']
               ao1=orderstatus1()
               if activeorder1.objects.filter(proid=quid).exists():
                    ao1.proid=quid
                    ao1.proname=qupn
                    ao1.com_name=qucn
                    ao1.com_mob=qucm
                    ao1.price=qup
                    ao1.delev_date=qud
                    ao1.Order_Status=qus
                    ao1.save()
               return render(request,'c_active_order.html',{'cun':un})

def orderstatusview(request):     
     if request.session.has_key('user'):
          un=request.session['user']
          res=orderstatus1.objects.all()
          return render(request,'a_active_order.html',{'ao3':res,'cun':un})