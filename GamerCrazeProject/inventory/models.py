from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not a positive number'),
            params={'value': value},
        )
        

class MTGSet(models.Model):
    # primary_key
    expansion_code = models.CharField(
        max_length = 3,
        primary_key=True
    )

    set_name = models.CharField(
        max_length = 20,
    )

    set_size = models.PositiveIntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.set_name


class MTGCard(models.Model):

    CARD_TYPE_CHOICES = (
        ('Artifact', 'Artifact'),
        ('Creature', 'Creature'),
        ('Enchantment', 'Enchantment'),
        ('Instant', 'Instant'),
        ('Land', 'Land'),
        ('Legendary', 'Legendary'),
        ('Planeswalker', 'Planeswalker'),
        ('Sorcery', 'Sorcery'),
    )

    COLOR_CHOICES = (
        ('W', 'White'),
        ('U', 'Blue'),
        ('B', 'Black'),
        ('R', 'Red'),
        ('G', 'Green'),
    )

    RARITY_CHOICES = (
        ('B', 'Basic'),
        ('C', 'Common'),
        ('U', 'Uncommon'),
        ('R', 'Rare'),
        ('M', 'Mythic Rare')
    )


    # First 3: set expansion code, last 3: card number
    SKU_ID = models.CharField(
        max_length =  6,
        primary_key=True
    )

    card_name = models.CharField(
        max_length = 30,
    )

    set = models.ForeignKey(
        'MTGSet',
        on_delete=models.SET_NULL,
        null=True)

    number = models.PositiveIntegerField()

    rarity = models.CharField(
        max_length = 1,
        choices = RARITY_CHOICES,
    )

    color = models.CharField(
        max_length = 1,
        choices = COLOR_CHOICES,
    )

    card_type = models.CharField(
        max_length = 12,
        choices = CARD_TYPE_CHOICES,
    )

    card_subtype = models.CharField(
        max_length = 20,
        blank = True,
    )

    converted_cost = models.PositiveIntegerField()

    rule_text = models.TextField(
        max_length = 400,
        blank = True,
    )

    image = models.ImageField()

    class Meta:
        ordering = ['number']

    def __str__(self):
        """String for representing the Model object."""
        return self.card_name


class MTGSingle(models.Model):

    CONDITION_CHOICES = (
        ('NM', 'Near Mint'),
        ('LP', 'Lightly Played'),
        ('MP', 'Moderately Played'),
        ('HP', 'Heavily Played'),
        ('DM', 'Damaged'),
    )

    LANGUAGE_CHOICE = (
        ('EN', 'English'),
        ('SP', 'Spanish'),
        ('FR', 'French'),
        ('DE', 'German'),
        ('IT', 'Italian'),
        ('PT', 'Portuguese'),
        ('JP', 'Japanese'),
        ('KR', 'Korean'),
        ('RU', 'Russian'),
        ('CS', 'Simplified Chinese'),
        ('CT', 'Traditional Chinese'),
    )

    SKU_ID = models.ForeignKey(
        'MTGCard',
        on_delete=models.SET_NULL,
        null=True)

    condition = models.CharField(
        max_length = 2,
        choices = CONDITION_CHOICES,
    )

    language = models.CharField(
        max_length = 2,
        choices = LANGUAGE_CHOICE,
    )

    qty = models.IntegerField(
        default = 0,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validate_positive],
    )

    class Meta:
        unique_together = (('SKU_ID', 'condition', 'language'),)

    def card_name(self):
        return self.SKU_ID.card_name

    def set(self):
        return self.SKU_ID.set

    def __str__(self):
        """String for representing the Model object."""
        return self.SKU_ID.SKU_ID + self.condition + self.language


class Order(models.Model):

    STATUS_CHOICES = (
        ('H', 'On Hold'),
        ('C', 'Completed'),
    )

    order_id = models.PositiveIntegerField(
        primary_key=True
    )

    customer_id = models.CharField(
        max_length = 20
    )

    def __str__(self):
        """String for representing the Model object."""
        return str(self.order_id)


class OrderItem(models.Model):

    order_id = models.ForeignKey(
        'Order',
        on_delete=models.SET_NULL,
        null=True)

    product = models.ForeignKey(
        'MTGSingle',
        on_delete=models.SET_NULL,
        null=True)

    qty = models.PositiveIntegerField(
        default = 0,
    )

    def __str__(self):
        """String for representing the Model object."""
        return str(self.pk)
