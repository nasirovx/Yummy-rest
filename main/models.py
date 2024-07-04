from django.db import models
from .utils import validate_phone_number as v_phone

class Starters(models.Model):
    image = models.ImageField(upload_to="starters/", verbose_name="Изображение")
    title = models.CharField(verbose_name="Название блюда",
    max_length=120)
    description = models.TextField(verbose_name="Ингридиенты", max_length=400)
    price = models.DecimalField(default=10.0, verbose_name="Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    def __str__(self):
        return f"{self.title}| Price {self.price} | {self.created_at}"
    
    class Meta:
        verbose_name = "Menu Starters"


class Breakfast(models.Model):
    image = models.ImageField(upload_to="breakfast/", verbose_name="Изображение")
    title = models.CharField(verbose_name="Название блюда",
    max_length=120)
    description = models.TextField(verbose_name="Ингридиенты", max_length=400)
    price = models.DecimalField(default=10.0, verbose_name="Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True,
            verbose_name="Дата создания")

    def __str__(self):
        return f"{self.title}| Price {self.price} | {self.created_at}"
    
    class Meta:
        verbose_name = "Menu Breakfast"


class Lunch(models.Model):
    image = models.ImageField(upload_to="lunch/", verbose_name="Изображение")
    title = models.CharField(verbose_name="Название блюда",
    max_length=120)
    description = models.TextField(verbose_name="Ингридиенты", max_length=400)
    price = models.DecimalField(default=10.0, verbose_name="Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    def __str__(self):
        return f"{self.title}| Price {self.price} | {self.created_at}"
    
    class Meta:
        verbose_name = "Menu Lunch"


class Dinner(models.Model):
    image = models.ImageField(upload_to="dinner/", verbose_name="Изображение")
    title = models.CharField(verbose_name="Название блюда",
    max_length=120)
    description = models.TextField(verbose_name="Ингридиенты", max_length=400)
    price = models.DecimalField(default=10.0, verbose_name="Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    def __str__(self):
        return f"{self.title}| Price {self.price} | {self.created_at}"
    
    class Meta:
        verbose_name = "Menu Dinner"


class Testimonials(models.Model):
    image = models.ImageField(upload_to="testimonials/", 
        verbose_name="Изображение", blank=True, null=True)
    first_name = models.CharField(verbose_name="Имя", max_length=120)
    last_name = models.CharField(verbose_name="Фамилия", max_length=120)
    description = models.TextField(verbose_name="Тематика", max_length=120)
    profession = models.CharField(verbose_name="Профессия", max_length=120)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | Профессия: {self.profession} | {self.created_at}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


class Events(models.Model):
    image = models.ImageField(upload_to="events/", 
        verbose_name="Изображение", blank=True, null=True)
    title = models.CharField(verbose_name="Название события",
        max_length=120)
    description = models.TextField(verbose_name="Описание", max_length=400)
    price = models.DecimalField(default=10.0, verbose_name="Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.title}| Price {self.price} | {self.created_at}"
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class Role(models.Model):
    title = models.CharField(verbose_name="Роль", max_length=120)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.title} | {self.created_at}"

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"


class Chefs(models.Model):
    image = models.ImageField(upload_to="shefs/",
        verbose_name="Изображение", blank=True, null=True)
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, 
        verbose_name="Роль павара")
    opinion = models.TextField(verbose_name="Содержание отзыва", max_length=400)
    twitter  = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="twitter", max_length=300)
    facebook = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="facebook", max_length=300)
    instagram = models.URLField(blank=True, null=True, unique=True,
        verbose_name="instagram", max_length=300)
    linkedin = models.URLField(blank=True, null=True, unique=True, 
        verbose_name="linkedin", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.role} | {self.created_at}"
    
    class Meta:
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"


class Book_A_Table(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    email = models.EmailField(verbose_name="Email", max_length=120)
    phone = models.CharField(verbose_name="Мобильный телефон", 
        max_length=12, validators=[v_phone])
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    people = models.PositiveIntegerField(verbose_name="Количество людей")
    message = models.TextField(verbose_name="Сообщение", max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.date} | {self.time} | {self.people} | {self.message} | {self.created_at}"

    class Meta:
        verbose_name = "Book a table"


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, 
        verbose_name="Дата создания")
    
    def __str__(self) -> str:
        return f"фотография была загружено в {self.created_at}"

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"


class Contact(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    email = models.EmailField(verbose_name="Email", max_length=120)
    subject = models.CharField(verbose_name="Тема", max_length=120)
    message = models.TextField(verbose_name="Сообщение", max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, 
            verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.subject} | {self.message} | {self.created_at}"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"