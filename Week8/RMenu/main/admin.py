from django.contrib import admin
from .models import City, Restaurant, RestReview, Dish, DishReview


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'telephone', 'city', 'user')
    list_display_links = ('id', 'name', 'number', 'telephone', 'city', 'user')


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'user', 'restaurant')
    list_display_links = ('name', 'description', 'price', 'user', 'restaurant')


class RestReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'date', 'restaurant', 'user')
    list_display_links = ('rating', 'comment', 'date', 'restaurant', 'user')


class DishReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'date', 'dish', 'user')
    list_display_links = ('rating', 'comment', 'date', 'dish', 'user')


admin.site.register(City, CityAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(RestReview, RestReviewAdmin)
admin.site.register(DishReview, DishReviewAdmin)

# 1. Restaurant
# a. name
# b. number
# c. telephone
# d. city
# e. user (fk)
# 2. Dish
# a. name
# b. description
# c. price
# d. user (fk)
# e. restaurant (fk)
# 3. Review
# a. rating
# b. comment
# c. date
# 4. RestaurantReview
# a. restaurant (fk)
# b. review (fk)
# c. user (fk)
# 5. DishReview
# a. dish (fk)
# b. review (fk)
# c. user (fk)