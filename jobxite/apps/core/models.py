from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('SCS', 'Scissor Lifts'),
    ('BOM', 'Boomlifts'),
    ('TEL', 'Telehandlers'),
    ('EXC', 'Excavators'),
    ('SKD', 'Skid Steers'),
    ('CMP', 'Compactors'),
    ('LDR', 'Loaders'),
    ('CRL', 'Cralwers'),
    ('FRK', 'Forklifts'),
    ('GEN', 'Generators'),
    ('LTR', 'Light Towers')
)


MAKE_CHOICES = (
    ('CAT', 'Catarpillar'),
    ('DTW', 'Ditch Witch'),
    ('BRT', 'Baretto'),
    ('GEN', 'Genie'),
    ('CPN', 'Chicago Pneumatic'),
    ('HUS', 'Husqvarna'),
    ('HYS', 'Hyster'),
    ('JCB', 'JCB'),
    ('JDR', 'John Deere'),
    ('MUS', 'Mustang'),
    ('VER', 'Vermeer'),
    ('TOR', 'Toro'),
    ('WNU', 'Wacker Neuson'),
    ('YNM', 'Yanmar'),
    )

class Item(models.Model):
    title       =   models.CharField(max_length=100)
    year        =   models.IntegerField()
    make        =   models.CharField(choices=MAKE_CHOICES, max_length=3)
    model       =   models.CharField(max_length=100)
    category    =   models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    price       =   models.DecimalField(max_digits=100, decimal_places=2)
    is_for_sale =   models.BooleanField(default=False)
    day_price   =   models.IntegerField(blank=True, null=True)
    week_price  =   models.IntegerField()
    month_price =   models.IntegerField()
    description =   models.TextField(max_length=255)
    long_description = models.TextField(blank=True, null=True)
    image_main  =   models.ImageField(blank=True, null=True, upload_to='static')

    def __str__(self):
        return self.title

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.title

