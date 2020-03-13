from django.db import models

# Create your models here.



# class Category(models.Model):
#     # id = models.IntegerField()
#     name = models.CharField(max_length=255, blank=False, null=True)
#     # product_id = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='product', null=True)

#     def __str__(self):
#         return self.name
    
# class SubCategory(models.Model):
#     name =     

class Category (models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class SubCategory (models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    parent_id = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True,related_name="subcategory")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Brand (models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    # category_count = models.PositiveIntegerField("product's count", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    image = models.ImageField(upload_to='product', blank=False, null=False)
    price = models.CharField(max_length=255, blank=False, null=True)
    category = models.ForeignKey(SubCategory, related_name='pro_category', on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, related_name='pro_brand', on_delete=models.CASCADE, null=True, blank=True)
    # product_property = models.ForeignKey(ProductProperty, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.title


# class CategoryProperty (models.Model):
#     title = models.CharField(max_length=255, blank=False, null=True)
#     category = models.ForeignKey(Category, related_name='category_property', on_delete=models.CASCADE, null=True, blank=True)

#     class Meta: 
#         verbose_name = 'CategoryProperty'
#         verbose_name_plural = 'CategoryProperties'
#     def __str__(self):
#         return self.title   



class ProductProperty(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    productproperty_id = models.ForeignKey(SubCategory, related_name='product_properties', on_delete=models.CASCADE, null=True, blank=True)
    # category_property = models.ForeignKey(CategoryProperty, related_name='product_property', on_delete=models.CASCADE, null=True, blank=True)

    class Meta: 
        verbose_name = 'ProductProperty'
        verbose_name_plural = 'ProductProperties'
    def __str__(self):
        return self.title



