# gradient

## Первая стратегия:
1. Фиксированная длина шага градиентного спуска, изменяется вручную
2. Информация о градиентах на предыдущих шагах не сохраняется
3. Точка выбирается одна и вручную
4. Информация о минимумах не сохраняется
5. Остановка определяется количеством шагов заданных вручную

## Вторая стратегия:
1. Длина шага определятся моментом на основе вычисленного градиента
2. Информация о текущем градиенте сохраняется и используется для определяния длины шага
3. Выбирается 8 точек случайным образом
4. Минимумы для точек сохраняются и определятся наименьшее
5. Остановка осуществляется при условии, что значение функции в найденной точке на протяжении двух последних шагов остаётся неизменным с точностью до 0.0001 либо же при количестве шагов больше 2000