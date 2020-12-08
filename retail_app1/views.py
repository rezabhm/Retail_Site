from django.shortcuts import render
from django.shortcuts import HttpResponse , HttpResponseRedirect
from django.template import loader , context
from .models import user , product , comment
from .models import order as ordering_user
from django.shortcuts import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission
import time

# Create your views here.

def index(requests):

    if requests.user.is_authenticated:
        usr_name = requests.user.username
        user_state = True
    else :
        usr_name = "ورود/ثبت نام"
        user_state = False

    prods = product.objects.all()

    chiken_list = []
    fish_list = []
    meat_list = []
    else_list = []
    turkey_list = []

    for prod in prods:

        typ = prod.type_product
        x = []

        img1 = prod.main_image.name
        img2 = prod.image2.name
        img3 = prod.image3.name
        img4 = prod.image4.name

        if typ[0] == "C" and (len(chiken_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)

            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            chiken_list.append(x)


        elif typ[0] == "M" and (len(meat_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)


            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            meat_list.append(x)

        elif typ[0] == "F" and (len(fish_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)


            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            fish_list.append(x)

        elif typ[0] == "T" and (len(turkey_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)


            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            turkey_list.append(x)


        elif typ[0] == "E" and (len(else_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)


            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            else_list.append(x)


    special_list = []

    prods = product.objects.all().filter(suggestion__exact="T")

    for prod in prods:

        img1 = prod.main_image.name
        img2 = prod.image2.name
        img3 = prod.image3.name
        img4 = prod.image4.name

        if len(special_list) < 5:

            x = []

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)

            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            special_list.append(x)

    template = loader.get_template("retail_app1/index.html")

    data = [

    [ "بیشنهاد ویژه" , special_list],
    [ "گوشت مرغ" , chiken_list],
    [ "ماهی" , fish_list],
    [ "محصولات گوشتی" , meat_list],
    [ "بوقلمون" , turkey_list],
    [ "سایر محصولات" , else_list],

    ]

    context = {
        "username" : usr_name,
        "data" : data ,
        "user_state" : user_state
    }

    return HttpResponse(template.render(context))


def createuser(requests):

    template = loader.get_template("retail_app1/create_user.html")
    if requests.user.is_authenticated:
        usr_name = requests.user.username
        user_state = True
    else :
        usr_name = "ورود/ثبت نام"
        user_state = False

    context = {
        "username" : usr_name,
        "error" : "" ,
        "user_state" : user_state
    }

    return HttpResponse(template.render(context))



def check(requests):

    template = loader.get_template("retail_app1/create_user.html")

    return HttpResponse("hello")

@csrf_exempt
def user_created(requests) :

    template = loader.get_template("retail_app1/finish.html")
    template2 = loader.get_template("retail_app1/create_user.html")

    if requests.user.is_authenticated :
        user_state = True
    else :
        user_state = False

    username = requests.POST.get('username')
    pass1 = requests.POST.get('password1')
    pass2 = requests.POST.get('password2')
    email = requests.POST.get('email')
    firstname = requests.POST.get('first_name')
    lastname = requests.POST.get('last_name')
    phonenumber = requests.POST.get('phone_number')
    address = requests.POST.get('address')
    sex = requests.POST.get('sex')

    context = {

        "username" : username,
        "lastname": lastname,
        "firstname": firstname,
        "pass1": pass1,
        "pass2": pass2,
        "email": email,
        "phonenumber": phonenumber,
        "address": address,
        "sex": sex,
        "user_state" : user_state

    }

    try:
        userlt = user.objects.all()
        userlist = ["admin"]
        for i in userlt:
            usrname = i.username
            userlist.append(usrname)
    except:
        context2 = {

            "error": "user not ",
            "user_state ": user_state
        }
        return HttpResponse(template2.render(context2))

    try:
        phonenumber = int(phonenumber)
    except:

        context2 = {

            "error": "شماره موبایل شما باید فقط از اعداد تشکیل شود",
            "user_state ": user_state

        }

        return HttpResponse(template2.render(context2))



    if username in userlt:

        context2 = {

            "error" : "نام کاربری که انتخاب کرده اید موجود میباشد.",
            "user_state ": user_state

        }

        return HttpResponse(template2.render(context2))

    elif pass1 != pass2 :

        context2 = {

            "error": "رمز های شما با هم مطابقت ندارد",
            "user_state ": user_state

        }

        return HttpResponse(template2.render(context2))


    else :

        usr = User.objects.create_user(username=username , email=email , password=pass1 )
        usr.set_password(pass1)
        usr.first_name = firstname
        usr.last_name = lastname

        usr.save()

        usr2 = user()
        usr2.username = username
        usr2.password = pass1
        usr2.phone_number = phonenumber
        usr2.address = address
        usr2.email = email

        if sex == "men" :
            usr2.sex = "men"
        elif sex == "women":
            usr2.sex = "women"


        usr2.save()


        return HttpResponse(template.render(context))

@csrf_exempt
def order(requests):

    if requests.user.is_authenticated:

        username = requests.user.username
        information = requests.POST.get("information")

        ord_prod = product.objects.all().filter(name_EN =information)[0]
        ord_user = user.objects.all().filter(username = username)[0]

        name = ord_prod.name

        price = ord_prod.price
        off_price = ord_prod.off_percent
        off = off_price / 100
        off = off * price
        price = price - off

        total = requests.POST.get("total")

        t = time.time()
        t = time.ctime(t)
        t = t.split()

        day = t[0]
        month = t[1]
        day_month = t[2]
        year = t[-1]

        t = t[-2]
        t = t.split(":")

        hour   = t[0]
        minute = t[1]
        second = t[2]

        deliver = "F"

        o = ordering_user(

            username = name,
            user_key = ord_user,
            price = price,
            total = total,
            day = day,
            month = month,
            day_month = day_month,
            year = year,
            hour = hour,
            minute = minute,
            seconde = second,
            deliver = deliver,

        )

        o.save()

        template = loader.get_template("retail_app1/order.html")

        context = {
            "statement" : True,

        }

        return HttpResponse(template.render(context))


    else :

        template = loader.get_template("retail_app1/order.html")

        context = {
            "statement": False,

        }

        return HttpResponse(template.render(context))

def product_explain(requests , id):

    template = loader.get_template("retail_app1/product_explain.html")
    if requests.user.is_authenticated:
        usr_name = requests.user.username
        user_state = True

    else :
        usr_name = "ورود/ثبت نام"
        user_state = False

    prods = product.objects.all().filter(name_EN=id)

    chiken_list = []
    fish_list = []
    meat_list = []
    else_list = []
    turkey_list = []

    for prod in prods:

        typ = prod.type_product
        x = []

        img1 = prod.main_image.name
        img2 = prod.image2.name
        img3 = prod.image3.name
        img4 = prod.image4.name

        if typ[0] == "C" and (len(chiken_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)

            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            chiken_list.append(x)


        elif typ[0] == "M" and (len(meat_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)


            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            meat_list.append(x)

        elif typ[0] == "F" and (len(fish_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)


            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            fish_list.append(x)

        elif typ[0] == "T" and (len(turkey_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)


            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            turkey_list.append(x)


        elif typ[0] == "E" and (len(else_list) < 5):

            x.append(img1[7:])
            x.append(prod.name)
            x.append("")

            price = prod.price
            off_price = prod.off_percent
            off = off_price / 100
            off = off * price
            price = price - off

            x.append(price)
            x.append(prod.price)
            x.append(prod.description)


            x.append(img2[7:])
            x.append(img3[7:])
            x.append(img4[7:])

            x.append(str(prod.name_EN))

            else_list.append(x)



    data = [

    [ "گوشت مرغ" , chiken_list],
    [ "ماهی" , fish_list],
    [ "محصولات گوشتی" , meat_list],
    [ "بوقلمون" , turkey_list],
    [ "سایر محصولات" , else_list],

    ]

    data_final = []

    for i in range(5):
        if len(data[i][1]) > 0:
            data_final.append([data[i][0] , data[i][1]])


    cmnt_whole = comment.objects.all().filter(product__name_EN = id)

    cmnt = []

    for x in cmnt_whole:
        cmnt.append([

            x.user.username ,
            x.comment_text

        ])

    context = {
        "username" : usr_name,
        "data" : data_final,
        "product_id" : data_final[0][1][-1][-1],
        "cmnt" : cmnt,
        "user_state ": user_state

    }

    return HttpResponse(template.render(context))


def UserComment(requests):

    usrname = requests.GET.get("username")
    prod = requests.GET.get("product")
    cmnt = requests.GET.get("comment")

    usr = user.objects.all().filter(username=usrname)[0]
    prod = product.objects.all().filter(name_EN = prod)[0]


    CreateComment = comment()

    CreateComment.product = prod
    CreateComment.user = usr
    CreateComment.comment_text = cmnt

    t = time.time()
    t = time.ctime(t)
    t = t.split()

    CreateComment.day = t[0]
    CreateComment.month = t[1]
    CreateComment.day_month = t[2]
    CreateComment.year = t[-1]

    t = t[-2]
    t = t.split(":")

    CreateComment.hour = t[0]
    CreateComment.minute = t[1]
    CreateComment.second = t[2]

    CreateComment.save()

    template = loader.get_template("retail_app1/comment.html")

    if requests.user.is_authenticated :
        user_state = True
    else:
        user_state = False

    context = {
        "urls" : "/product/{0}/".format(str(prod.name_EN)),
        "user_state ": user_state

    }
    return HttpResponse(template.render(context))

def UserProfile(requests , username):


    if requests.user.is_authenticated or requests.user.is_superuser :

        if requests.user.username == username or requests.user.is_superuser :

            user_state = True


            usr = user.objects.all().filter(username=username)[0]

            password = usr.password
            email = usr.email
            phone_number = usr.phone_number
            address = usr.address
            reg_time = usr.reg_time
            picture = usr.picture.name[7:]
            sex = usr.sex

            UsrInf = [

                ("نام کاربری" , username),
                ("رمز عبور", password),
                ("ایمیل", email),
                ("شماره تماس", phone_number),
                ("آدرس", address),
                ("زمان ثبت نام", reg_time),
                ("جنسیت", sex),

            ]

            user_order = ordering_user.objects.all().filter(user_key__username = username)

            UsrOrd = []
            ct = 0

            for Order in user_order :

                total = Order.total
                product_name = Order.username
                price = Order.price

                day = str(Order.day)
                month = str(Order.month)
                day_month = str(Order.day_month)

                hour = str(Order.hour)
                minute = str(Order.minute)
                seconde = str(Order.seconde)

                if Order.deliver == "T":
                    statement = "محصول دریافت شده است"
                else :
                    statement = "ارسال نشده است"

                if ct % 2 == 0 :
                    class_name = "row_first"
                else:
                    class_name = "row_second"

                ct += 1

                data = [

                    ( product_name ,
                     price  ,
                    total,
                    day +" "+ month +" "+ day_month +" "+ hour+":" + minute+":" + seconde,
                    statement ) ,
                    class_name,
                    ct

                ]

                UsrOrd.append(data)

            UserComment = comment.objects.all().filter(user__username = username )

            UsrCom = []
            ct =0

            for cmnt in UserComment:

                prod = cmnt.product.name
                comment_txt = cmnt.comment_text

                day = str(cmnt.day)
                month = str(cmnt.month)
                day_month = str(cmnt.day_month)

                hour = str(cmnt.hour)
                minute = str(cmnt.minute)
                seconde = str(cmnt.seconde)

                if ct % 2 == 0:
                    class_name = "row_first"
                else:
                    class_name = "row_second"

                ct += 1

                data = [

                    (prod,
                    day +" "+ month +" "+ day_month +" "+ hour +":"+ minute +":"+ seconde,
                    comment_txt),
                    class_name ,
                    ct
                ]

                UsrCom.append(data)

            template = loader.get_template("retail_app1/profile.html")

            context = {

                "username" : username ,
                "UserInfo" : UsrInf ,
                "UserOrd"  : UsrOrd ,
                "UserCom"  : UsrCom ,
                "user_state ": user_state

            }


            return HttpResponse(template.render(context))

        else:


            template = loader.get_template("retail_app1/profile_error.html")

            context = {

                "error" : "خطا : شما با این اکانت اجازه ی دسترسی به این صفحه را ندارید !!!"
                ,"user_state ": True

            }

            return HttpResponse(template.render(context))

    else:

        template = loader.get_template("retail_app1/profile_error.html")

        context = {

            "error": "خطا : شما باید ثبت نام کنید و یا اگر دارای اکانت هستید باید با اکانت خود وارد شوید !!!"
            ,"user_state ": False

        }

        return HttpResponse(template.render(context))

def AllProfile(requests):

    if requests.user.is_superuser :

        usrs = user.objects.all()

        usrs_list = []
        ct = 1
        for usr in usrs:

            name = usr.username
            password = usr.password
            email = usr.email
            phonenumber = usr.phone_number
            sex = usr.sex
            reg_time = usr.reg_time

            if ct % 2 == 1:
                class_name = "first_class"
            else :
                class_name = "second_class"

            data = [

                ct ,
                name ,
                password ,
                email ,
                phonenumber,
                email ,
                sex ,
                reg_time,
                class_name
            ]

            ct += 1

            usrs_list.append(data)

        template = loader.get_template("retail_app1/all_profile.html")

        context = {

            "data" : usrs_list,
            "user_state ": True

        }

        return HttpResponse(template.render(context))

    else :

        template = loader.get_template("retail_app1/profile_error.html")

        if requests.user.is_authenticated :
            user_state = True
        else :
            user_state = False


        context = {

            "error" : "خطا : شما اجازه ی دسترسی به این صفحه را ندارید !!!"
            ,"user_state ": user_state

        }

        return HttpResponse(template.render(context))


"""def order_query_state(requests):

    if requests.user.is_superuser :

        delivery = requests.GET.get("delivery")

        order_list = ordering_user.objects.all().filter(deliver=delivery)



    else :

        template = loader.get_template("retail_app1/profile_error.html")

        if requests.user.is_authenticated :
            user_state = True
        else :
            user_state = False


        context = {

            "error" : "خطا : شما اجازه ی دسترسی به این صفحه را ندارید !!!"
            ,"user_state ": user_state

        }

        return HttpResponse(template.render(context))
"""