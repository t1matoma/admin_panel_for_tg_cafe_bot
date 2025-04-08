from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        unique_together = ("category", "name")  # Имя уникально в рамках категории

    def __str__(self):
        return f"{self.name} ({self.price} сом)"
    
    
class Client(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "clients"  # Имя таблицы в PostgreSQL

    def __str__(self):
        return self.email


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.JSONField()  # Здесь хранится список товаров

    class Meta:
        db_table = "orders"  # Имя таблицы в PostgreSQL

    def __str__(self):
        return f"Заказ #{self.id} от {self.client.email}"


class DeletedOrder(models.Model):
    REASON_CHOICES = [
        ("insufficient_funds", "У клиента недостаточно средств"),
        ("wrong_product", "Клиент указал не тот товар"),
        ("out_of_stock", "Товара нет в наличии"),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)  
    reason = models.CharField(max_length=255, choices=REASON_CHOICES) 
    deleted_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        db_table = "deleted_orders"  

    def __str__(self):
        return f"Удалённый заказ #{self.order.id} по причине {self.get_reason_display()}"

