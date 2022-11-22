from django.contrib.gis.db import models


class Tippers(models.Model):
    board_number = models.CharField(verbose_name='Бортовой номер', max_length=4)
    model = models.CharField(verbose_name='Модель', max_length=20)
    max_load_capacity = models.IntegerField(verbose_name='Максимальная гразоподъемность')
    cargo = models.IntegerField(verbose_name='Груз везет')
    cargo_characteristics = models.JSONField(verbose_name='Качественные характеристики груза')

    def __str__(self):
        return f'{self.board_number}, {self.model}'


class Storages(models.Model):
    name = models.CharField(verbose_name='Название склада', max_length=20)
    fullness = models.IntegerField(verbose_name='Объем груза в наличии')
    poly = models.PolygonField(verbose_name='Полигон')
    cargo_characteristics = models.JSONField(verbose_name='Качественные характеристики груза')

    def __str__(self):
        return self.name
