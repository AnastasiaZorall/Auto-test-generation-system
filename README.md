**Аннотация**

**Цель курсовой работы** : Разработать систему автоматической генерации тестов по дисциплине «Информатика» и реализовать выдачу тестовых материалов в текстовом редакторе Word.

В дальнейшем планируется внедрение этой системы в учебный процесс и использование для генерации тестов учащимся по дисциплине «Информатика».

Передо мной были поставлены следующие задачи:

1. Обзор аналогов систем генерации тестов
2. Выбор программного обеспечения;
3. Разработка эргономичного интерфейса для пользователей
4. Программирование тестов по заданным разделам
5. Выдача тестовых материалов в документе Word
6. Выдача ответов к тестовым материалам

В процессе выполнения курсовой работы осуществлено более углублённое изучение языка Python, освоены графическая библиотека Tkinter для оконного интерфейса и модуль python-docx для работы с документами Word.Кроме того, получен опыт в создании UserFriendly интерфейса, а также в группировке отдельных тем заданий в смысловые разделы.

Каждое из заданий прошло тестирование; ответы, предложенные системой, оказались правильными.

Разработанная система имеет следующие преимущества по сравнению с существующими аналогами:

- _Адресность_ - ориентированность на задания, используемые именно в НИУ ВШЭ для изучения дисциплины «Информатика»;
- _Поддержка пользователя -_ Cведение возможности ошибки пользователя к минимуму;
- _Дружественность_ - максимальная простота и удобство интерфейса;
- _Многовариантность_ - возможность получения практически неограниченного количества вариантов тестов, благодаря использованию функции выбора случайных чисел;
- _Редактируемость_ - выдача вариантов для тестирования в удобной форме для правки;
- _Полнота_ - выдача ответов ко всем полученным вариантам.

Объем данной работы составляет 27 страниц, включая 12 рисунков и 1 таблицу.


# Введение

Педагогический тест - это инструмент, предназначенный для измерения знаний учащегося, состоящий из системы тестовых заданий и стандартизованной процедуры проведения, обработки и анализа результатов.

Контроль знаний студентов является одной из проблем высшего образования, а тестирование позволяет дать предварительную оценку знаний обучающегося, как студенту (для самоконтроля), так и преподавателю.

Выполнение данной курсовой работы даст возможность ознакомиться с различными системами генерации тестов, позволит провести их сравнительный анализ, а также углубить знание языков программирования и получить опыт и навыки в разработке практически значимых систем.

Тема является актуальной, поскольку тестовый контроль знаний в настоящее время является в высшем образовании одной из самых распространенных форм оценки знаний обучаемых и, согласно нормативным документам в образовании и соответствующим рабочим планам изучаемых дисциплин, является обязательным компонентом освоения практически всех изучаемых дисциплин. Система автоматической генерации тестов будет не только хорошим помощником преподавателю, позволив снизить объем его рутинной работы в проверке знаний студентов, но и поможет студентам в изучении учебного материала.

# Анализ существующих технических решений

Рассмотрим различные аналоги генератора тестов.

1. **Knowing**** 1****(рис. 1)**

![](https://github.com/AnastasiaZorall/Auto-test-generation-system/blob/master/images/knowing1.png) ![](RackMultipart20200605-4-66draq_html_9d9e8946d363440f.png) 

Рис. 1. - Внешний вид программы Knowing.

Knowing – программа для создания тестов. Данная программа может использоваться для создания тестов по любым темам. Выделим основные особенности:

1. Два режима создания тестов:

- Простой (вопросы добавляются поочередно, изменить или добавить пропущенный вопрос можно только по завершении работы)
- Текстовый (вопросы добавляются исходя из желаний создателя, прямо в процессе создания каждый из вопросов и его параметры доступны к редактированию)

2. Типы вопросов:

- Единичный выбор
- Множественный выбор
- Ручной ввод ответа
- Диапазон значений
- Принадлежность к интервалу
- Последовательность вариантов
- Сопоставление вариантов
- Истинность утверждения

3. Присутствует возможность добавления картинок или таблиц

4. Выставление оценки в заданном диапазоне после окончания

5. Защита тестов и их настроек от изменения паролем

1. **ADTester**** 2 **** (рис. 2)**

![](RackMultipart20200605-4-66draq_html_774aa7f26308d922.png) ![](RackMultipart20200605-4-66draq_html_9adc1531bbafeb2c.png)

Рис. 2. - Внешний вид программы ADTester.

Программы пакета:

- Конструктор тестов - программа для создания тестов. Позволяет создавать и редактировать тесты;
- Тестер - программа для проведения тестирования. Имеет простой интерфейс и параметры проведения тестирования;
- Админ панель - программа администрирования. Позволяет производить манипуляции с пользователями и группами пользователей, строить матрицы правильности и производить анализ результатов тестирования.

В тестах можно использовать различные шрифты, формулы, схемы, таблицы, HTML документы и любые OLE-объекты. Вопросы и ответы можно полноценно форматировать - различные шрифты, абзацы, списки и т.д.

Возможности пакета:

Достаточно большое возможное количество вопросов в тесте и вариантов ответа.

Типы вопросов:

- одиночный выбор;
- множественный выбор;
- ввод ответа с клавиатуры;
- соответствие;
- порядок.

Возможно установить режим тестирования: контроль и обучение. В режиме обучения при неправильном ответе можно посмотреть подсказку по данному вопросу, результаты тестирования не учитываются. В режиме контроля ведется статистика прохождения теста. Каждый вопрос имеет свой «вес» (цену в баллах). Каждый вопрос может сопровождаться подсказкой для тестируемого. Редактирование теста может быть защищено паролем. Тестирование может быть ограничено по времени.

1. **Moodle**** 3 **** (рис.3)**

![](RackMultipart20200605-4-66draq_html_91926678d37cb4bc.jpg) ![](RackMultipart20200605-4-66draq_html_e6e0575b47004f9a.png)

Рис. 3. - Внешний вид системы Moodle.

Moodle (Modular Object-Oriented Dynamic Learning Environment) - бесплатная система электронного обучения, ориентированная прежде всего на организацию взаимодействия между преподавателем и учениками, подходит и для организации традиционных дистанционных курсов, и для поддержки очного обучения.

Несмотря на то, что создание тестов не является целевой задачей платформы, оно реализовано как одна из возможностей для дистанционного курса. Тест Moodle невозможно создать без привязки к банку заданий, то есть генерация теста возможна только после заполнения банка вопросов. Для создания вопроса необходимо заполнить такие поля как: категория вопроса, название вопроса, текст вопроса, балл по умолчанию (то есть можно создавать тесты с разными по сложности вопросами, что будет учитываться в оценивании) и штраф за неправильную попытку.

# Темы, включённые в систему автоматической генерации

По предложению руководителя для курсовой были выбраны следующие темы:

1. Математические основы ВТ (Действия с числами в разных системах счисления)
  1. Перевод из одной системы счисления в другую
    1. Перевод целых чисел из 10-ичной системы в 2-ичную систему счисления
    2. Перевод целых чисел из 2-ичной системы в 10-ичную систему счисления
    3. Перевод целых чисел из одной системы счисления в другую
    4. Перевод чисел с плавающей запятой
  2. Перевод целых чисел в дополнительный код
  3. Двоичная арифметика с целыми числами
2. Логические основы ВТ (Алгебра логики)
  1. Приведение к совершенной нормальной форме
    1. Приведение к совершенной конъюнктивной нормальной форме (СКНФ)
    2. Приведение к совершенной дизъюнктивной нормальной форме (СДНФ)
  2. Приведение к минимальной нормальной форме
    1. Приведение к минимальной конъюнктивной нормальной форме (МКНФ)
    2. Приведение к минимальной дизъюнктивной нормальной форме (МДНФ)
  3. Операции булевой алгебры
3. Основы теории информации
  1. Применение формулы сочетания без повторений
  2. Применение формулы сочетания с повторениями
  3. Применение формулы размещения без повторений
  4. Применение формулы размещения с повторениями

Задания для генерации были выбраны в соответствии с ПУД по дисциплине «Информатика».

# Анализ технических решений объекта разработки

1.
## Выбор языка программирования для создания системы

Язык программирования Python был выбран по нескольким существенным критериям:

- Имеется существенный задел в изучении этого языка программирования (его основы были изучены на 1-м курсе), что позволяет ускорить процесс решения задачи;
- Реализуется возможность углубить полученные знания в программировании на языке Python;
- Python имеетдостаточное количество библиотек, которые облегчают работу и делают код более читаемым и понятным;
- Python неприхотлив к платформе запуска, что упрощает тестирование работы ПО;
- Графическая библиотека Tkinter делает процесс создания интерфейса достаточно удобным;
- Имеется возможность выдавать результаты в файлы docxc помощью специального модуля;
- Максимальная читаемость и понятность кода на языке Python позволяет в дальнейшем редактировать его в зависимости от изменения потребностей.

1.
## Используемые встроенные библиотеки и конкретные задачи, ими выполняемые

Для каждого из разделов используются свои специфические библиотеки. Ниже приведён их список.

| **Для какого раздела** | **Название** | **Что делает** |
| --- | --- | --- |
| Выдача результатов | python-docx | Работа с документами Word |
| Оконный интерфейс | Tkinter | Графическая библиотека |
| Основы теории информации | Itertools4 | Библиотека для работы с различными формулами комбинаторики |
| Функции рандомной генерации | Random | Библиотека, позволяющая получить псевдорандомные числа |
| Создание датафрейма, содержащего значения переменных a, b, c и значение функции F (применяется в разделе «Алгебра логики») | Pandas | Высокоуровневая библиотека, необходимая для анализа данных |
| Создание типа numpyarray в заданиях на создание МКНФ, МДНФ, СКНФ и СДНФ | Numpy | Наиболее часто используемая Python библиотека |
| Связь программных файлов 3 разделов | Os | Модуль, позволяющий работать с операционной системой |

##

1.
## Описание принципа работы программы

Приложение состоит из двух оконных форм. Первая форма используется для выбора темы разделов, по которой необходимо сформировать варианты задания (рис. 4).

![](RackMultipart20200605-4-66draq_html_d869fe8a7b5a6b8f.png)

Рис. 4. Оконная форма выбора темы раздела.

Вторая оконная форма имеет три различных варианта, зависящих от выбора на рис. 4: оконная форма для формирования заданий по теме «Действия с числами в разных системах счисления» (рис.5), оконная форма для формирования заданий по теме «Алгебра логики» (рис.6), оконная форма для формирования заданий по теме «Формулы комбинаторики» (рис.7)

![](RackMultipart20200605-4-66draq_html_3d61cb584d1f888a.png)

Рис. 5. Оконная форма для формирования заданий по теме

«Действия с числами в разных системах счисления»

![](RackMultipart20200605-4-66draq_html_8da31c4fff262c4f.png)

Рис. 6. Оконная форма для формирования заданий по теме «Алгебра логики».

![](RackMultipart20200605-4-66draq_html_f437bd05d8beafe5.png)

Рис 7. Оконная форма для формирования заданий по теме

«Формулы комбинаторики».

Каждый из вариантов может содержать более одного задания по необходимой теме. Количество заданий определяется пользователем во время формирования вариантов. Для ввода количества заданий необходимо вписать натуральное число в предназначенную для этого ячейку (рис. 8).

![](RackMultipart20200605-4-66draq_html_25ef2fba18d802ac.png)

Рис. 8. Оконная форма, готовая для ввода количества заданий

Для подтверждения выбора и начала формирования вариантов пользователю необходимо активировать checkbutton в графе «Выбрать». После записи числа заданий, указанного в графе «Количество заданий», на месте checkbutton появится надпись «Выполнено» (рис. 9).

![](RackMultipart20200605-4-66draq_html_33f9c4c912aa8a16.png)

Рис. 9. Вид оконной формы после завершения записи заданий в файл

Для выполнения одного из описанных выше требований к системе, при активации checkbutton производится проверка введенного числа заданий на допустимость. Допустимыми для ввода считаются только натуральные числа. Поскольку это требование является естественным, дополнительная подсказка пользователю до ввода не является необходимой. В случае ошибки при введении количества заданий запись заданий в файл не производится и на экран выводится текст «Onlyintegernumbersareavailable» (рис. 10).

![](RackMultipart20200605-4-66draq_html_2c3f654a20dfaed2.png)

Рис. 10. Проверка на допустимость введённых значений

**Ввод имени файла для тестовых вариантов**

Для начала выбора необходимого задания и записи его в файл пользователю необходимо ввести название файла. По согласованиюс научным руководителем курсовой работы было принято решение о том, что система будет формировать пять различных подобных вариантов. Дополнительно формируются файлы ответов к каждому из вариантов.

Название файлов с заданиями для учащегося строится по следующему принципу: \&lt; введённое пользователем название \&gt; + \_\&lt;номер варианта по порядку\&gt; + .docx

Название файлов с заданиями для преподавателя строится по следующему принципу: \&lt; введённое пользователем название \&gt; + \&lt;номер варианта по порядку\&gt; + \_О.docx

Файл с заданиями для преподавателя (рис. 11) идентичен файлу с заданиями для студента (рис. 12) с одним исключением. Для преподавателя так же выводятся ответы для каждого из заданий.

![](RackMultipart20200605-4-66draq_html_b82f0b6a9a004c31.png)

Рисунок 11. Файл с заданиями для студентов

![](RackMultipart20200605-4-66draq_html_94afe218b886acfa.png)

Рис. 12. Файл с заданиями для преподавателя

# Описание создания программного интерфейса

1. Главное окно для выбора раздела
  
```window = Tk()
  window.geometry('400x250')
  combo = Combobox(values=["Действия с числами в разных СС", "Алгебра логики", "Формулы комбинаторики"], width=30)
  combo.bind('<<ComboboxSelected>>', get_selected)
  combo.place(x=10, y=10)
  mainloop()
  ```

Основной часть главного окна является Combobox, позволяющий пользователю выбрать раздел из 3 представленных вариантов. После выбора начинает работу функция get_selected, описанная в следующем разделе.

2. Общие параметры окон для формирования заданий по каждому из разделов
```
window1.geometry('1200x600')
btnputinfile = Button(window1, text="OK:, font=14, command=put_filename, foreground="#000080")
btnputinfile.place(x=750, y=20)
btnClose=Button(window1, text="Закрыть", font=14, сommand=window1.destroy, foreground="#000080")
btnClose.place(x=20, y=500)
lbl2 = Label(window1, font=("Arial Bold", 14), text="ТЕМА")
lbl2.place(x=10, y=100)
lbl3 = Label(window1, font=("Arial Bold", 14), text="КОЛ-ВО ЗАДАНИЙ     ВЫБРАТЬ")
lbl3.place(x=600, y=100)
window1.mainloop()
```
Приведённый выше код создаёт общий вид оконной формы, он универсален для всех трех разделов.

3. Ввод имени файла
```
fn = Entry(window1, width=40)
fn.focus_set()
fn.place(x=390, y=30)
lbl8 = Label(window1, font=("Arial Bold", 14), text="Название файла для записи")
lbl8.place(x=100, y=30)
lbl9 = Label(window1, font=("Arial Bold", 14), text=".docx")
lbl9.place(x=640, y=30)
```
Данный код создаёт место, куда пользователь будет вводить название файла. Так же сразу после места для ввода указано расширение, чтобы показать, что его можно не вводить, а оно будет задано автоматически.

4. Добавление названия заданий (приведён пример для третьего раздела)
```
lbl4 = Label(window1, font=("Arial Bold", 14), text="Сочетания без повторений")
lbl5 = Label(window1, font=("Arial Bold", 14), text="Сочетания c повторениями")
lbl6 = Label(window1, font=("Arial Bold", 14), text="Размещения с повторениями")
lbl7 = Label(window1, font=("Arial Bold", 14), text="Размещения без повторений")
lbl4.place(x=10, y=210)
lbl5.place(x=10, y=270)
lbl6.place(x=10, y=330)
lbl7.place(x=10, y=390)
```
В данном случае создается 4 надписи, для которых затем задается расположение в окне.

5. В третьем разделе помимо названия задания используется формула, которая в нём используется. Приведён пример вставки формулы в окно.
```
path4 = 'rbp.jpg'
img4 = ImageTk.PhotoImage(Image.open(path4))
panel4 = tk.Label(window1, image=img4)
panel4.pack(side="bottom", fill="both", expand="yes")
panel4.place(x=300, y=380)
```
Для вставки формулы было принято решение использовать изображение из-за максимальной простоты работы с ним. При необходимости поместить другое изображение, размещенное на компьютере пользователя, достаточно изменить path4.

# Описание работы ключевых фрагментов программы

Структурно программа состоит из 3 файлов, создающих задания для каждого из разделов, и файла, объединяющего и связывающего из работу.

Обратим внимание на ключевые фрагменты, определяющие работоспособность системы.

1. Функция добавления задания и ответа к нему в соответствующие файлы
```
def input_file_docx(str_write, str_answer):
  paragraph = dti.add_paragraph(str_write)
  paragraph_format = paragraph.paragraph_format
  paragraph_format.space_after = Pt(1.0)
  paragraph = dti1.add_paragraph(str_answer)
  paragraph_format = paragraph.paragraph_format
  paragraph_format.space_after = Pt(1.0)
```
Данная функция вызывается в конце работы функций, автоматически генерирующих задания с ответами по заданной теме. Она взаимодействует непосредственно с файлом .docx, записывая в него строки, поданные на вход функции.

2. Функция, добавляющая графу для записи имени, группы и даты проведения работы в файл, создающийся для учащегося
```
def fio_add(dti):
  paragraph = dti.add_paragraph('Фамилия, Имя, Группа' + '_'* 72)
  paragraph_format = paragraph.paragraph_format
  paragraph_format.space_after = Pt(3.0)
  paragraph = dti.add_paragraph('Дата выполнения' + '_'* 80 + '\n')
  paragraph_format = paragraph.paragraph_format
  paragraph_format.space_after = Pt(2.0)
```
Данная функция вызывается сразу после ввода пользователем имени файла и созданием программой файлов, взаимодействует непосредственно с файлами .docx, предназначенными для учащегося.

3. Функция, регистрирующая нажатие на Checkbutton и запускающая соответствующую ему команду.
```
def flag(i, com, xi, yi):
  chk = Checkbutton(window1, variable=list_cb[i], command=com)
  chk.focus()
  chk.place(x=xi, y=yi)
  return
```
Данная функция используется для связи расположения checkbutton и команды, которая должна запускаться при его активации.

4. Функции, обеспечивающие корректность вводимых данных
  1. Проверка является ли введенная строка натуральным числом
```
def only_int(p):
  if p.isdigit():
    return True
  return False
```
На вход функции передаётся строка, которая проверяется на то, является ли она натуральным числом. На выход функции подаётся ложь или истина в зависимости от строки.

  2. Функция, выводящая подсказку для пользователя о введении неверного значения строки
```
def num_check(xi, yi, li):
  lb_f = Label(window1, font=("Arial Bold", 14), text='only integer number available')
  lb_f.place(x=xi, y=yi)
  list_cb[li].set(0)
  return
```
Функция активируется в случае, если на выходе функции only_int оказалось значение False. Подсказка выводится рядом с Checkbutton, соответствующему месту ввода неверного значения.

5. Функция, определяющая какой из 3 файлов программ необходимо запустить для продолжения работы.
```
def get_selected(param):
  icombo = combo.current() + 1
  if icombo == 1:
    os.system('python part_1_otl_1.py')
  elif icombo == 2:
    os.system('python part_2_otl_1.py')
  else:
    os.system('python part_3_otl_1.py')
```
Фиксируется номер по порядку выбранного раздела в combobox, и в зависимости от него запускается необходимая программа.

6. Связующая функция для каждого из разделов. Приведён пример для третьего раздела.
```
def combin():
  question_amount_1.place(x=550, y=215)
  question_amount_2.place(x=550, y=275)
  question_amount_3.place(x=550, y=335)
  question_amount_4.place(x=550, y=395)
  flag(1, comb_n_k, 800, 215)
  flag(2, comp_n_k_rep, 800, 275)
  flag(3, accom_n_k_rep, 800, 335)
  flag(4, accom_n_k, 800, 395)
```
Данная функция считывает числа, введённые в поля question_amount и последовательно вызывает функцию flag для каждого из заданий. В ходе выполнения данной функции в файлы заданий для учащихся и преподавателя добавляются выбранные задания, если значения, введёные в question_amount являются натуральными числами, иначе для каждой ошибочно введённой строки необходимо повторить ввод.

# Заключение

В процессе выполнения курсовой работы было выполнено ознакомление с тестовыми системами, усовершенствование навыков программирования на языке программирования Python, освоение принципов использования библиотек этого языка, получила опыт в создании пользовательского интерфейса, изучены основные принципы тестирования программ. Была выполнена работа, которая будет иметь практическое использование.

Процесс работы над курсовой дал возможность применить, полученные в ходе обучения, знания на практике, приобретен опыт взаимодействия с постановщиком задачи.

#

# Список источников

1. Knowing [Электронный ресурс]. – Режим доступа : [http://www.globalpage.ru/](http://www.globalpage.ru/) (Дата обращения 15.11.2019)
2. AdTester [Электронный ресурс]. – Режим доступа: [https://www.adtester.org/](https://www.adtester.org/) (Дата обращения 16.11.2019)
3. Moodle [Электронный ресурс]. – Режим доступа: [https://moodle.org/](https://moodle.org/) (Дата обращения 16.11.2019)
4. Python 3.8.3 documentation [Электронный ресурс]. – Режим доступа [https://docs.python.org/](https://docs.python.org/) (Дата обращения 03.01.2020 – 05.05.2020)
5. Matthes, Python Crash Course //No Starch Press, 2016
6. Обучение Tkinter [Электронный ресурс]. – Режим доступа: [https://younglinux.info/tkinter/tkinter.php](https://younglinux.info/tkinter/tkinter.php) (Дата обращения 03.01.2020 - 05.05.2020)
