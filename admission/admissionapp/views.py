from django.shortcuts import render
from admissionapp.models import Student
# Create your views here.

def index(request):
    return render(request,"index.html")

import re
def form1(request):
    if request.method=="POST":
        # amount=request.POST.get("button1")
        course=request.POST.get("course")
        board="state"
        # if request.POST.get("emitext"):
        #     emi=request.POST.get("emitext")
        #     result = re.search(r'\bEMI\b\s*→\s*(\d+\s*installment)', emi)
        #     if result:
        #         emi = result.group(1)
        #         print(emi)
        
        # print(amount)
        # print(course)

        # dp=5500
        # if emi==0:
        #     emt="full cash"
        #     dp=0
        #     rm=0
        #     return render(request,"gbill.html",{'amt':amount,'course':course,'emi':emt,'board':board,'dp':dp,'rm':rm})
        # else:
        #     dp=5500
        #     rmt=int(amount) - dp


        #     monthly_pay=rmt / 3
        return render(request,"gbill.html",{'board':board,'course':course})
    return render(request,"forms1.html")

def form2(request):
    if request.method=="POST":
        amount=request.POST.get("button1")
        course=request.POST.get("course")
        board="cbse"
        emi=0
        if request.POST.get("emitext"):
            emi=request.POST.get("emitext")
            result = re.search(r'\bEMI\b\s*→\s*(\d+\s*installment)', emi)
            if result:
                emi = result.group(1)
                print(emi)
        
        print(amount)
        print(course)
        if course:
            dp=5500
        if emi==0:
            emt="full cash"
            dp=0
            rm=0
            return render(request,"gbill.html",{'amt':amount,'course':course,'emi':emt,'board':board,'dp':dp,'rm':rm})
        else:
            dp=5500
            rmt=int(amount) - dp
            monthly_pay=rmt / 3
            return render(request,"gbill.html",{'amt':amount,'course':course,'emi':emi,'board':board,'dp':dp,'rmt':rmt,'monthly_pay':monthly_pay})
    return render(request,"forms1.html")

def form3(request):
    if request.method=="POST":
        amount=request.POST.get("button1")
        course=request.POST.get("course")
        board="icic"
        emi=0
        if request.POST.get("emitext"):
            emi=request.POST.get("emitext")
            result = re.search(r'\bEMI\b\s*→\s*(\d+\s*installment)', emi)
            if result:
                emi = result.group(1)
                print(emi)
        
        print(amount)
        print(course)
        if course:
            dp=5500
        if emi==0:
            emt="full cash"
            dp=0
            rm=0
            return render(request,"gbill.html",{'amt':amount,'course':course,'emi':emt,'board':board,'dp':dp,'rm':rm})
        else:
            dp=5500
            rmt=int(amount) - dp
            monthly_pay=rmt / 3
            return render(request,"gbill.html",{'amt':amount,'course':course,'emi':emi,'board':board,'dp':dp,'rmt':rmt,'monthly_pay':monthly_pay})
    return render(request,"forms3.html")

def gbill(request):
    if request.method=="POST":
        student_name=request.POST.get('studentName')
        start_date=request.POST.get('batchStartDate')
        classes=request.POST.get('classes')
        board=request.POST.get('board')
        mbno=request.POST.get('mobileNumber')
        ambno=request.POST.get('alternativeNumber')
        school=request.POST.get('schoolName')
        parent=request.POST.get('parentName')
        course=request.POST.get('course')
        cmt=request.POST.get('cAmount')
        emi=request.POST.get('emiOption')
        downp=request.POST.get('dpPaidAmount')
        rbalance=request.POST.get('remainingBalance')
        fullcash=request.POST.get('emiAmount')
        regfee=request.POST.get('Regfee')
        totalb=request.POST.get('Totalbalance')
        # if board=="state" and course=="Standard":
        #     first_installment=20500
        #     third_installment=22500
        #     fifth_installment=23500
        #     seventh_installment=24500
        # elif board=="state" and course=="Super":
        #     first_installment=17500
        #     third_installment=18500
        #     fifth_installment=20000
        # elif board=="state" and course=="Navodaya":
        #     first_installment=15500
        #     third_installment=16500
        #     fifth_installment=17700
        
        
        
        # if  emi=="EMI-1 installment":
        #     emv=first_installment
        #     monthly_pay=emv/3
        # elif emi=="EMI-3 installment":
        #     emv=third_installment
        #     monthly_pay=emv/3
        # elif emi=="EMI-5 installment":
        #     emv=fifth_installment
        #     monthly_pay=emv/3
        # elif emi=="EMI-7 installment":
        #     emv=seventh_installment
        #     monthly_pay=emv/3 
        # elif emi=="Trial class" or emi=="Full cash payment":
        #     emv=0
        #     monthly_pay=0
        
        details={
            "student_name":student_name,
            "start_date":start_date,
            "board":board,
            "mobile_no":mbno,
            "ambno":ambno,
            "school":school,
            "parent":parent,
            "cmt":cmt,
            "emi":emi,
            "downp":downp,
            "rbalance":rbalance,
            "fullcash":fullcash,
            "course":course,
            "regfee":regfee,
            "totalb":totalb,
            "classes":classes,
        }
        ob2=Student.objects.all().count()
        reciept=ob2+1
        print(reciept)
        import datetime
        date1=datetime.datetime.now().date()
        print(reciept,date1)
        return render(request,"billgenerate.html",{'details':details,'reciept':reciept,"date":date1})
    ob2=Student.objects.all().count()
    reciept=ob2+1
    print(reciept)
    import datetime
    date1=datetime.datetime.now().date()
    print(reciept,date1)
    return render(request,"billgenerate.html",{'reciept':reciept,"date":date1})
    # return render(request,"gbill.html")
        
def billgen(request):
    if request.method=="POST":
        student_name=request.POST.get("student_name")
        batch_start_date=request.POST.get("batch_start_date")
        class_name=request.POST.get("classes")
        print(class_name)
        board=request.POST.get("board")
        mobile_number=request.POST.get("mobile_number")
        alternate_mobile_number=request.POST.get("alternate_mobile_number")
        school_name=request.POST.get("school_name")
        parent_name=request.POST.get("parent_name")
        course=request.POST.get("course")
        registration_fee=request.POST.get("registration_fee")
        tution_fee=request.POST.get("tution_fee")
        dp_paid_amount=request.POST.get("dp_paid_amount")
        remaining_balance=request.POST.get("remaining_balance")
        emi=request.POST.get("emi")
        emi_per_month=request.POST.get("emi_per_month")
        total=request.POST.get("total")

        ob=Student.objects.create(student_name=student_name,batch_start_day=batch_start_date,class_name=class_name,board=board,mobile_number=mobile_number,alternate_mobile_number=alternate_mobile_number,school_name=school_name,parent_name=parent_name,course=course,registration_fee=registration_fee,tution_fee=tution_fee,dp_paid_amount=dp_paid_amount,remaining_balance=remaining_balance,emi=emi,emi_per_month=emi_per_month,total=total)
        ob.save()
        ob2=Student.objects.all().count()
        reciept=ob2+1
        print(reciept)
        import datetime
        date1=datetime.datetime.now().date()
        print(reciept,date1)
        return render(request,"billgenerate.html",{'reciept':reciept,"date":date1})
    ob2=Student.objects.count()
    reciept=ob2+1
    print(reciept)
    import datetime
    date1=datetime.datetime.now().date()
    print(reciept,date1)
    return render(request,"billgenerate.html",{'reciept':reciept,"date":date1})