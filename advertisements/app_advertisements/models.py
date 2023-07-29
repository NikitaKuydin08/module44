from django.db import models

class Meta:
    db_table = '"advertisements"'


class Advertisement(models.Model):
   
    # Товар
    # Cтроковое поле для небольших размеров
    # 'заголовок' - verbose_name - название поля извне
    title = models.CharField('заголовок', max_length=128)

    # Описание товара/информация о товаре
    # Большое текстовое поле, для больших текстов
    description = models.TextField('описание')

    # Цена
    # Специальный тип данных с фиксированной точкой
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    # Логический тип, два значения - правда или ложь
    auction = models.BooleanField('торг', help_text='Отметьте, уместен ли торг')
    
    # Дата публикации
    # Поле записывается при создании объявления
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения обновления
    # Поле записывается при каждом обновлении
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'

    # Имя продавца + контанты

    # Имя товара

    # Актуальность объявления

    # Количество товара

    # Возможен ли обмен

    # Адрес продажи

    # Б/у товар или нет

    # Возможность взять в долг/в рассрочку





