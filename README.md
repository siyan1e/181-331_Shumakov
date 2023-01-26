# 181_331_Shumakov
## Исходные данные
Исходный код: Функция шифрования данных с помощью использования алгоритма "Шифр Цезаря"

Для тестирования была использована библиотека unittest

## Последовательность работы:
1) Взят исходный код "Шифр Цезаря" с функцией шифрования "encrypt";
2) Функция протестирована на работоспособность;
3) Написан unittest  

    Для позитивного тестирования были использованы следующие данные:
    
        'input_string': 'съешь ещё этих мягких французских булок, да выпей чаю',
      
        'shift': 3,
        
        'output_string': 'фэиыятудоиьитудоахлштудопвжнлштудочугрщцкфнлштудодцоснктхтудозгтудоеютимтудоъгб'


    Правильность выходных данных в позитивном тестировании была проверена с помощью онлайн сервисов и ручного высчета.
    В исходном коде есть функция "replace_base_symbols", которая заменяет базовые символы на заданные параметры:
    
        * 'ё' -> 'е'
        
        * ',' -> 'зпт'
        
        * '.' -> 'тчк'
        
        * '-' -> 'тире'
        
        * ' ' -> 'прбл'
        
     При проверке правильности работы функции на онлайн сервисах данные замены были учтены.

     Для негативного тестирования были использованы следующие данные:
     
        'input_string': 'съешь ещё этих мягких французских булок, да выпей чаю',
        
        'shift': 3,
        
        'output_string': 'бйфзляарыфихяарымвшеяарыьотъшеяарыдапэёгчбъшеяарыргыюъчявяарыупяарыскяфщяарыжпн'

## Результат тестирования с позитивным сценарием:
![image](https://user-images.githubusercontent.com/71716482/214787376-2449a9bc-73cf-43fd-9c71-6086320fa07f.png)
Входные данные в тесте совпали с данными на выходе тестируемой функции, поэтому программа просто вывела результат работы функции.

## Результат тестирования с негативным сценарием:
![image](https://user-images.githubusercontent.com/71716482/214785831-029c6b33-3bf6-42f7-a517-5a4c8d738789.png)
