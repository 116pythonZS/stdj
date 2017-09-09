from django.contrib import admin
from blog.models import Publisher, Author, Book

# Register your models here.
# 管理界面增加表 - 标准方法
# admin.site.register(Publisher)
# admin.site.register(Author)
# admin.site.register(Book)


# 自定义表Author的显示方式
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')
	fields = ('last_name', 'first_name',)
	
admin.site.register(Author, AuthorAdmin)


# 自定义表Book的显示
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)       # publication_date 降序
	# ordering = ('publication_date',)        # publication_date 升序
	# fields = ('title', 'authors', 'publisher', 'publication_date')
	filter_horizontal = ('authors',)
	raw_id_fields = ('publisher',)
	
admin.site.register(Book, BookAdmin)

admin.site.register(Publisher)



