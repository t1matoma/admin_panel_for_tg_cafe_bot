from django.contrib import admin
from .models import Client, Order, Category, Product, DeletedOrder
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.shortcuts import render, redirect
from .forms import DeletionReasonForm
from django.utils import timezone



# Для отображения email в клиенте
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
    search_fields = ("email",)


# Для кастомизации отображения заказов
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "client_email",
        "delivery_date",
        "total_price",
        "items_display",
    )
    list_filter = ("delivery_date",)
    search_fields = ("client__email",)

    def client_email(self, obj):
        return obj.client.email
    client_email.short_description = "Email клиента"

    def items_display(self, obj):
        return ", ".join([item["name"] for item in obj.items])
    items_display.short_description = "Товары"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "delete_with_reason/<int:order_id>/",
                self.admin_site.admin_view(self.delete_with_reason),
                name="order_delete_with_reason",
            ),
        ]
        return custom_urls + urls

    # Метод для кастомного удаления с причиной
    def delete_with_reason(self, request, order_id):
        order = self.get_object(request, order_id)
        
        if request.method == "POST":
            form = DeletionReasonForm(request.POST)
            if form.is_valid():
                reason = form.cleaned_data["reason"]
                DeletedOrder.objects.create(
                    order=order,
                    reason=reason,
                    deleted_at=timezone.now(),
                )
                order.delete()
                self.message_user(request, f"Заказ #{order.id} удален с причиной: {reason}")
                return HttpResponseRedirect("/admin/orders/order/")

        else:
            form = DeletionReasonForm()

        return render(
            request,
            "admin/delete_with_reason.html",
            {"form": form, "order": order},
        )

    # Переопределение стандартного delete_view
    def delete_view(self, request, object_id, extra_context=None):
        return redirect(reverse("admin:order_delete_with_reason", args=[object_id]))
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]  # Удаляем стандартное массовое удаление
        return actions


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name",)
    