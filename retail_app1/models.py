from django.db import models
import uuid
import hashlib

hash_cod = hashlib.md5()
# Create your models here.


class product(models.Model):

    # relation

    #user = models.ForeignKey(user , on_delete=models.CASCADE())

    # information

    id_product = models.UUIDField(default= uuid.uuid4 , primary_key= True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default= 0)

    name_EN = models.CharField(max_length=50 , default="product")


    # this atribute is our product path

    main_image = models.ImageField(upload_to="static/media" , default="static/media/index.png")
    image2 = models.ImageField(upload_to="static/media" , default="static/media/index.png")
    image3 = models.ImageField(upload_to="static/media" , default="static/media/index.png")
    image4 = models.ImageField(upload_to="static/media" , default="static/media/index.png")

    total_number = models.IntegerField(default= 1)
    weight = models.IntegerField(default=1000)

    # this attribute show we have this product or we don't have

    statement_dict = (
        ("T" , "Full"),
        ("F" , "Empety")
    )

    statement = models.CharField(max_length=1 , choices=statement_dict)

    # how many percent we decrease our price

    off_percent = models.IntegerField()

    classes = (
        ("C" , "Chicken"),
        ("M" , "Meat"),
        ("F" , "Fish"),
        ("T" , "Turkey"),
        ("E" , "else")
    )

    type_product = models.CharField(max_length=1 , choices= classes)

    sug = (
        ("T" , "Suggest"),
        ("F" , "Normal")
    )

    suggestion = models.CharField(max_length=1 , choices=sug)

    description = models.TextField(default=" ...")

    ommit_ = (
        ("T", "active"),
        ("F", "ommit")
    )

    ommit = models.CharField(max_length=1, choices=ommit_)

    def __str__(self):
        return self.name

### user

class user(models.Model):

    id_user = models.UUIDField(default= uuid.uuid4 , primary_key= True)

    # user information

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length= 50 , null=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    reg_time = models.DateField(auto_now=True)
    picture = models.ImageField(verbose_name="/media/" ,default="/media/1.jfif")

    sex_t = (

        ("m" , "men"),
        ("w", "women"),

    )

    sex = models.CharField(max_length=1 , choices=sex_t , default="men")


    def __str__(self):
        return self.username


class order(models.Model):

    id_user = models.UUIDField(default= uuid.uuid4 , primary_key= True)

    # relation
    user_key = models.ForeignKey(user , on_delete=models.CASCADE )

    username = models.CharField(max_length=50 , default="admin")


    price = models.IntegerField(default= 0)
    # number of order
    total = models.IntegerField()

    # date
    # [Sat , Sun , Mon , Tue , Wed , Thu , Fri]
    day = models.CharField(max_length=3 , help_text="[Sat , Sun , Mon , Tue , Wed , Thu , Fri]")
    # month
    # [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
    month = models.CharField(max_length=3 , help_text="Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec")
    # day
    # 1-31
    day_month = models.IntegerField()
    #year
    year = models.IntegerField()
    #hourse
    hour = models.IntegerField()
    #minute
    minute = models.IntegerField()
    #second
    seconde = models.IntegerField(default=1)

    state_deliver = (
        ("T" , "deliver"),
        ("F" , "don't deliver")
    )

    deliver = models.CharField(max_length=1 , choices=state_deliver)


    def __str__(self):
        return self.username


class comment(models.Model):

    user = models.ForeignKey(user , on_delete=models.CASCADE)
    product = models.ForeignKey(product , on_delete=models.CASCADE)

    comment_text = models.TextField()

    # date

    # [Sat , Sun , Mon , Tue , Wed , Thu , Fri]
    day = models.CharField(max_length=3 , help_text="[Sat , Sun , Mon , Tue , Wed , Thu , Fri]")

    # month
    # [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
    month = models.CharField(max_length=3 , help_text="[Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]")

    # day
    # 1-31
    day_month = models.IntegerField()

    #year
    year = models.IntegerField()

    #hourse
    hour = models.IntegerField()

    #minute
    minute = models.IntegerField()

    #second
    seconde = models.IntegerField(default=1)

    def __str__(self):
        return(self.product)
