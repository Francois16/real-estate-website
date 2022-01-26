import uuid

from django.db import models


class PropertyQuerySet(models.QuerySet):
    def filter_from_form(self, form_data):
        qs = self.all()
        if form_data["property_status"] != Property.PropertyStatus.ANY:
            qs = qs.filter(property_status=form_data["property_status"])

        if form_data["property_type"] != Property.PropertyType.ANY:
            qs = qs.filter(property_type=form_data["property_type"])

        if form_data["province"] != Property.Provinces.ANY:
            qs = qs.filter(province=form_data["province"])

        return qs.order_by("-created_at")


class PropertyManager(models.Manager):
    def get_queryset(self):
        return PropertyQuerySet(self.model, using=self._db)

    def filter_from_form(self, form_data):
        return self.get_queryset().filter_from_form(form_data)


class Property(models.Model):
    class Meta:
        verbose_name_plural = "properties"

    class PropertyType(models.TextChoices):
        ANY = "ANY", ("Any")
        HOUSE = "H", ("House")
        APARTMENT = "AP", ("Apartment / Flat")
        TOWNHOUSE = "TH", ("Townhouse")
        PLOT = "P", ("Vacant Land / Plot")
        FARM = "F", ("Farm")
        COMMERCIAL = "C", ("Commercial Property")
        INDUSTRIAL = "I", ("Industrial Property")

    # Status of wheter its for sale on to rent etc.
    class PropertyStatus(models.TextChoices):
        ANY = "ANY", ("Any")
        SALE = "S", ("For Sale")
        RENT = "R", ("To Rent")
        FORCLOSURE = "F", ("Forclosure")
        AUCTION = "A", ("Auction")

    class Provinces(models.TextChoices):
        ANY = "ANY", ("Any")
        FS = "FS", ("Free State")
        G = "G", ("Gauteng")
        KZN = "KZN", ("KwaZulu-Natal")
        MPG = "MPG", ("Mpumalanga")
        NC = "NC", ("Northern Cape")
        NW = "NW", ("North West")
        EC = "EC", ("Eastern Cape")
        WC = "WC", ("Western Cape")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objects = PropertyManager()

    # Property info
    title = models.CharField(max_length=255, default="")
    property_type = models.CharField(
        max_length=4, choices=PropertyType.choices, default=PropertyType.ANY, null=True
    )
    property_status = models.CharField(
        max_length=4, choices=PropertyStatus.choices, default=PropertyStatus.ANY, null=True
    )
    price = models.PositiveBigIntegerField()
    description = models.TextField(default="")

    # Property Location
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    suburb = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=4, choices=Provinces.choices, default=Provinces.ANY, null=True)

    # Property details
    bedrooms = models.PositiveSmallIntegerField(null=True)
    bathrooms = models.PositiveSmallIntegerField(null=True)
    garage = models.PositiveSmallIntegerField(null=True)
    parking = models.PositiveSmallIntegerField(null=True)
    floor_size = models.PositiveSmallIntegerField(null=True)
    erf_size = models.PositiveSmallIntegerField(null=True)

    # Property features
    features = models.ManyToManyField("PropertyFeature", verbose_name="features")

    # Property Costs
    levies = models.SmallIntegerField(null=True, blank=True)
    rates_and_taxes = models.SmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_reduced = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def price_per_square_meter(self):
        return int(self.price / self.floor_size)


class PropertyFeature(models.Model):
    feature = models.CharField(max_length=20)

    def __str__(self):
        return self.feature


class PropertyImage(models.Model):
    property = models.ForeignKey("Property", related_name="images", on_delete=models.CASCADE)
    images = models.ImageField()
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.title}'s images"
