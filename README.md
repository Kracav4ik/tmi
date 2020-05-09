# Turing Machine Implementation

## состовляющие компоненты
* вычислитель
  * кнопка запуска программы
  * 8ми битный счетчик для подсчета скобок для while
* це почка элементарн ячеек
  * блок памяти
    * 8 бит
    * комманды read, write, inc, dec
  * контакты слева
    * являемся ли мы головой головой
    * активировать себя
  * контакты справа
    * являемся ли мы хвостом
    * активировать следующего
  * сквозные контакты
    * комманды read, write, inc, dec, left, right
    * дополнительный контакт "режим исполнения комманд"
    * данные in
    * данные out
  * индикаторы голова, хвост, активная
* устройство с лентой комманд
  * может проматывать ленту вперед и назад на одну комманду
  * кадр перфоленты из 4х битов
  * комманды:
    * jump  0 0 0 0
    * while 0 0 0 1
    * in    0 0 1 0
    * out   0 0 1 1
    * right 0 1 0 0
    * left  0 1 0 1
    * inc   0 1 1 0
    * dec   0 1 1 1
    * begin 1 0 0 0
    * end   1 * * *
* устройство ввода (клавиатура)
  * неактивно пока не поступает комманда на инпут
  * показывает, что нужен инпут и отображает введенный символ
* устройство вывода (пишущая машинка)
  * печатает символы как пишущая машинка
  * работает перевод строки (\n)
  * таб заменяет на пробел
  * остальные управляющие символы (например \r) не работают