
# Эксперименты с IO-bound задачей  
- Итак, время синхронной проверки ссылок с Википедии (запускался файл tryexept.py):
- ![Фотка](https://github.com/HeavyPunk/PythonTask/blob/main/sync_call_http.png)

- Время проверки с 5 воркерами:
- ![](https://github.com/HeavyPunk/PythonTask/blob/main/async_call_http_5_proc.png)

- Время проверки с 10 воркерами:
- ![](https://github.com/HeavyPunk/PythonTask/blob/main/async_call_http_10_proc.png)
  - Системный монитор (скакнул трафик через сетевой интерфейс):
  - ![](https://github.com/HeavyPunk/PythonTask/blob/main/sys_mon_10_proc.png)

- Время проверки с 100 воркерами:
- ![](https://github.com/HeavyPunk/PythonTask/blob/main/async_call_http_100_proc.png)
  - Cистемный монитор:
  - ![](https://github.com/HeavyPunk/PythonTask/blob/main/sys_mon_100_proc.jpg)

# Дальше - интереснее. CPU-bound задача!
- Генерация денюжек в одном воркере:
  - ![](https://github.com/HeavyPunk/PythonTask/blob/main/sys_mon_generate_1_proc.png)
- Генерация в 2 воркерах:
  - ![](https://github.com/HeavyPunk/PythonTask/blob/main/sys_mon_generate_2_workers.png)
- Генерация в 4 воркерах:
  - ![](https://github.com/HeavyPunk/PythonTask/blob/main/sys_mon_generate_4_proc.png)
- Генерация в 16 воркерах:
  - ![](https://github.com/HeavyPunk/PythonTask/blob/main/sys_mon_generate_16_proc.png)
# Выводы
Так как задача CPU-bound так или иначе должна выполняться процессором, то абсолютно без разницы сколько воркеров под этузадачу отводит (возможно, большое кол-во воркеров даже увеличит время выполнения задачи из-за множественной перезаписи кеша процессора), что видно на графиках.  
Время генерации было абсолютно случайным, так как простой брутфорс хеш-алгоритма это вещь не обладающая закономерностью.  
С IO-bound задачей увеличение кол-ва воркеров действительно дало результаты, ведь мы перекладываем обработку CPU-bound задачи на сервер. И тогда намного лучше быстро раздать команды и ждать ответа на какую-либо из них
