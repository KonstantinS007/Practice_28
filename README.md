![img.png](img.png)

Общество с ограниченной ответственностью
 «Ростелеком Информационные Технологии»
(ООО «РТК ИТ)
### Практика 28 Скиллфактори

<div>
  <div>
    <details><summary>Задание</summary>

  Заказчик передал вам следующее задание:

    1 Протестировать требования.
    2 Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
    3 Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс.
      Оформите свой набор автотестов в GitHub.
    4 Оформить описание обнаруженных дефектов.
      Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов.
      (если дефекты не будут обнаружены, то составить описание трех дефектов)

  Ожидаемый результат

    1 Перечислены инструменты, которые применялись для тестирования.

      1.1 Почему именно этот инструмент и эту технику.
      1.2 Что им проверялось.
      1.3 Что именно в нем сделано.
  К выполненному заданию прикреплены:

     . Набор тест-кейсов.
     . Набор автотестов на GitHub. Обратите внимание, что в репозитории должен находиться файл README.md, где будет описано,
       что именно проверяют данные тестовые сценарии и какие команды необходимо выполнить для запуска тестов.
       Описанные команды должны работать на любом компьютере с установленными Python3 и PyTest.
     . Описание оформленных дефектов.
  Если что-то не получилось выполнить, то распишите детально, чтобы у нас была возможность дать обратную связь:

     . Что именно не получилось?
     . Как пробовали решить задачу?
     . Что помешало решить?
   </details> 
  </div>
  <div>
    <details><summary>Требование.Спецификация.</summary>
     
  Стандартная авторизация по логину и паролю:

    1.	Система отображает форму «Авторизация», разделенную вертикально на два блока и содержащую:
    2.	В левой части:
      a.	Меню выбора типа аутентификации
        i.	Таб выбора аутентификации по номеру, "Номер"
        ii.	Таб выбора аутентификации по логину и паролю, "Почта"
        iii.	Таб выбора аутентификации по почте и паролю, "Логин"
        iv.	Таб выбора аутентификации по лицевому счету и паролю, “Лицевой счет”
      b.	Форма ввода "Номер" или "Логин" или "Почта" или “Лицевой счет” (По умолчанию выбрана форма авторизации по телефону)
      c.	Форма ввода "Пароль"
    3.	В правой части:
      a.	Продуктовый слоган ЛК "Ростелеком ID".
      b.	Вспомогательная информация для клиента.
      При вводе номера телефона/почты/логина/лицевого счета - таб выбора аутентификации меняется автоматически.

  Сценарий авторизации клиента по номеру телефона, кнопка "Номер":

    1.	Клиент вводит номер телефона и пароль
    2.	Система:
       a.	Проверяет корректность введенного номера;
       b.	Проверяет связку Номер+Пароль;
       c.	При успешной проверки Номера и пароля - система переходит к следующему шагу п.3. , иначе клиенту отображается ошибка, сценарий начинается с пункта 1.
       d.	При некорректном вводе связки Номер + Пароль, выводим сообщение "Неверный логин или пароль" и элемент "Забыл пароль" перекрашивается в оранжевый цвет.
    3.	Система:
       a.	Выполняет успешный поиск УЗ по введенному номеру телефона;
       b.	Аутентифицирует клиента;
       c.	Выполняет перенаправление клиента на страницу redirect_uri.

  Сценарий авторизации клиента по номеру телефона, кнопка "Почта":

    1.	Клиент вводит Почта и пароль
    2.	Система:
       a.	Проверяет корректность введенной почты;
       b.	Проверяет связку Почта+Пароль;
       c.	При успешной проверки почты и пароля - система переходит к следующему шагу п.3. , иначе клиенту отображается ошибка, сценарий начинается с пункта 1.
       d.	При некорректном вводе связки Номер + Пароль, выводим сообщение "Неверный логин или пароль" и элемент "Забыл пароль" перекрашивается в оранжевый цвет.
    3.	Система:
       a.	Выполняет успешный поиск УЗ по введенной почте;
       b.	Аутентифицирует клиента;
       c.	Выполняет перенаправление клиента на страницу redirect_uri.

  Сценарий авторизации клиента по номеру телефона, кнопка "Логин":

    1.	Клиент вводит Логин и пароль
    2.	Система:
       a.	Проверяет корректность введенного логина;
       b.	Проверяет связку Логин+Пароль;
       c.	При успешной проверки почты и пароля - система переходит к следующему шагу п.3. , иначе клиенту отображается ошибка, сценарий начинается с пункта 1.
       d.	При некорректном вводе связки Номер + Пароль, выводим сообщение "Неверный логин или пароль" и элемент "Забыл пароль" перекрашивается в оранжевый цвет.
    3.	Система:
       a.	Выполняет успешный поиск УЗ по введенному логину;
       b.	Аутентифицирует клиента;
       c.	Выполняет перенаправление клиента на страницу redirect_uri.

  Сценарий авторизации клиента по номеру телефона, кнопка "Лицевой счет":

    1.	Клиент вводит Лицевой счет и пароль
    2.	Система:
       a)	Проверяет корректность введенного лицевого счет и ищет логин связанный с лицевым счетом, в следующих шагах проверяется найденный логин;
       b)	Проверяет связку Логин+Пароль;
       c)	При успешной проверки логина и пароля - система переходит к следующему шагу п.3. , иначе клиенту отображается ошибка, сценарий начинается с пункта 1.
       d)	При некорректном вводе связки Номер + Пароль, выводим сообщение "Неверный логин или пароль" и элемент "Забыл пароль" перекрашивается в оранжевый цвет.
    3.	Система:
       a)	Выполняет успешный поиск УЗ по Лицевому счету;
       b)	Аутентифицирует клиента;
       c)	Выполняет перенаправление клиента на страницу redirect_uri.

  Авторизация по временному коду:

    1.	Система отображает форму «Авторизация по коду», содержащую:
       a)	Подсказку по работе с формой “Укажите контактный номер телефона или почту, на которые необходимо отправить код подтверждения”;
       b)	Поле ввода номера телефона или почты;
       c)	Кнопку "Получить код".
    2.	Клиент вводит номер телефона/почту и нажимает кнопку "Получить код";
    3.	Система:
       a)	Проверяет корректность введенного номера/почты;
       b)	Отправляет код на введенный номер телефон/почту;
    4.	Отображает форму ввода кода подтверждения, содержащую:
       a)	Номер телефона/Почту на который был отправлен код;
       b)	Ссылку "Изменить номер", если пользователь ввел телефон на 2 шаге или ссылку "Изменить почту",
            если пользователь ввел почту на шаге 2 (ссылка ведет на форму ввода номера телефона/почты);
       c)	Шесть отдельных полей для ввода кода подтверждения;
       d)	Текст с обратным отсчётом времени до повторной попытки отправки код, по завершении отсчёта отображается ссылка "Получить новый код";
    5.	Клиент начинает вводить полученный код;
    6.	Система:
       a)	После ввода каждой цифры переводит фокус ввода в следующее поле;
       b)	При событии заполнения всех 6 полей производит верификацию кода;
       c)	При успешной верификации кода система переходит к следующему шагу, иначе клиенту отображается ошибка, сценарий останавливается.
    7.	Система:
       a)	Выполняет поиск УЗ по введенному номеру телефона/почте: 
          i.	Если УЗ с таким телефоном/почтой не найдена, то создает новую без пароля, ФИО, Региона после чего переход на шаг 8;
         ii.	Если УЗ найдена – переход на шаг 8;
    8.	Аутентифицирует клиента;
    9.	Выполняет перенаправление клиента на страницу из redirect_uri;

  Восстановление пароля.   
  Окно выбора типа восстановления пароля:

    1.	Система отображает форму «Восстановление пароля» содержащую:
      a.	Меню выбора типа ввода контактных данных:
         i.	Таб выбора восстановления пароля по номеру, "Номер"
        ii.	Таб выбора восстановления пароля по логину и паролю, "Почта"
       iii.	Таб выбора восстановления пароля по почте и паролю, "Логин"
        iv.	Таб выбора восстановления пароля по ЛС, "Лицевой счет"
      b.	Форма ввода "Номер" или "Логин" или "Почта" или "Лицевой счет" (По умолчанию выбрана форма восстановления пароля по телефону)
      c.	Форма ввода "Капча"
      d.	Кнопка "Далее" переход в п.3. (Продолжить сценарий восстановления пароля)
         i.	Если к УЗ привязан только телефон, то переход в Сценарий восстановления пароля клиента по номеру телефона, кнопка "По SMS на номер телефона"
        ii.	Если к УЗ привязан только почту, то переход в Сценарий восстановления пароля клиента по номеру телефона, кнопка "По ссылке на почту"
      e.	Кнопка "Вернуться" (Вернуться на форму авторизации)
    2.	После введения телефона, почты, логина или ЛС отображается форма выбора восстановления пароля:
      a)	Выбор "По SMS на номер телефона" (Если телефон привязан к УЗ)
      b)	Выбор "По ссылке на почту" (Если почта привязана к УЗ)
      c)	Кнопка "Продолжить" (Продолжить сценарий восстановления пароля)
      d)	 Кнопка "Вернуться назад" (Вернуться на форму ввода контактных данных п.1 для восстановления пароля)

  Сценарий восстановления пароля клиента по номеру телефона, кнопка "По SMS на номер телефона":

    1.	Пользователь выбирает восстановить по номеру телефона;
    2.	Система отправляем пользователю смс с кодом на номер привязанный к УЗ SSO;
    3.	Открывается форма с полем для ввода кода из СМС которая содержит:  
      3.1 Кнопку "Получить код повторно" (Повторная отправка смс с новым кодом);
      3.2 Кнопка "Вернуться назад" (Вернуться на шаг ввода контактных данных для восстановления доступа);
      3.3 При вводе неправильного кода отображается ошибка "Неверный код. Повторите попытку"
      3.4 При вводе временного кода срок времени которого закончился отображается ошибка "Время жизни кода истекло"
    4.	Пользователь вводит корректный проверочный код (переход в п.5);
    5.	После ввода корректного кода из смс - открывается форма для ввода нового пароля, состоящая из:
      5.1 Поле ввода нового пароля
      5.2 Поле ввода для подтверждения нового пароля
      5.3 Кнопка "Сохранить" для подтверждения нового пароля (Переход в п.5)
      5.4 Правила для создания пароля
    6.	Пользователь вводит новый пароль, подтверждение пароля и нажимает кнопку "Сохранить";
    7.	Система проверяет корректность пароля по правилам и при успешной проверке отображается следующая форма, иначе отображается ошибка:
      7.1 Если пользователь ввел пароль менее 8 символов "Длина пароля должна быть не менее 8 символов" под полем "Новый пароль"
      7.2 Если пользователь ввел пароль без заглавных букв "Пароль должен содержать хотя бы одну заглавную букву" под полем "Новый пароль"
      7.3 Если пользователь ввел пароль не с латинскими буквами "Пароль должен содержать только латинские буквы" под полем "Новый пароль"
      7.4 Если пользователь ввел в поле "Подтверждение пароля" пароль отличный от пароль "Новый пароль" выводим "Пароли не совпадают" под полем "Подтверждение пароля"
    8.	Если пользователь ввел пароль согласно парольной политике, система проверяет введенный пароль с тремя предыдущими:
      8.1 Если пользователь ввел пароль, идентичный трем предыдущим  "Этот пароль уже использовался, укажите другой пароль"
      8.2 Если пользователь ввел пароль, отличный от трех предыдущих - переход на шаг 
    9.	Клиент перенаправляется на страницу авторизации.
 
  Сценарий восстановления пароля клиента по номеру телефона, кнопка "По ссылке на почту":

    1.	Пользователь выбирает восстановить по почте;
    2.	Открывается форма оповещающая пользователя об отправке письма на его почту, которая содержит:
      2.1 Текст оповещающий об отправке письма со ссылкой на почту;
      2.2 Кнопку "Вернуться назад" (Переход на форму авторизации)
    3.	Пользователь открывает письмо и переходит по ссылке.
    4.	Система отображает форму состоящую из:
      1.	Поле ввода нового пароля
      2.	Поле ввода для подтверждения нового пароля
      3.	Кнопка "Сохранить" для подтверждения нового пароля (Переход в п.5)
      4.	Правила для создания пароля
      5.	Система проверяет корректность пароля по правилам и при успешной проверке отображается следующая форма, иначе отображается ошибка:
        5.1 Если пользователь ввел пароль менее 8 символов "Длина пароля должна быть не менее 8 символов"
        5.2 Если пользователь ввел пароль без заглавных букв "Пароль должен содержать хотя бы одну заглавную букву"
        5.3 Если пользователь ввел пароль не с латинскими буквами "Пароль должен содержать только латинские буквы"
      6   Если пользователь ввел пароль согласно парольной политике, система проверяет введенный пароль с тремя предыдущими:
        6.1 Если пользователь ввел пароль, идентичный трем предыдущим  "Этот пароль уже использовался, укажите другой пароль"
        6.2 Если пользователь ввел пароль, отличный от трех предыдущих - переход на шаг 
      7	  Пользователь переходит на форму успешной смены пароля.
      8	  При нажатии на кнопку "Авторизоваться" пользователь перенаправляется на форму авторизации.
   </details>
  </div>
</div>

### Решение:
<div>
  <div>
   <details><summary>Способ решения</summary>

                        Тестирование сайта
       Тестирование интерфейса страниц регистрации, авторизации и восстановления пароля в личном кабинете
     «Ростелеком» проведено исходя из отсутствия Личного кабинета у пользователя (тестировщик не является клиентом Ростелекома),
     а также без имеющегося тестового доступа к системе либо тестовых учетных данных и капчи, вследствие чего все тестовые сценарии в автоматизации имели и имеют затруднения в реализациии.
     Проведено тестирование форм регистрации (разными способами), авторизации (разными способами) и восстановления пароля (разными способами).
     Всего составлено 20 автоматизированных тестов, включая параметризованные параметрами (отдельные кейсы), в т. ч.:
     •	Форма регистрации – 9 тестов и 36 параметров,
     •	Форма авторизации – 8 тестов,
     •	Форма восстановления пароля – 4 тестов.
       21 Тестов Скип из-за отсуствия данных капчи и кодов, а тестовых данных.

     Код построен на реализации методов действий над локаторами для построения тестовых сценарий.

     Техники тест-дизайна, используемые при составлении тестовых сценариев и тест кейсов:

     •	разбиение на классы эквивалентности и анализ граничных значений;
     •	таблицы причинно-следственных решений, состояний и переходов;
     •	предугадывание ошибки;
     •	диаграмма пользовательских ролей;
     •	исследовательское и свободное тестирование.
   </details>
  </div>
  <div>
   <details><summary>Описание репозитория</summary>

                     Репозиторий содержит:
     Директорию SCR для файлов автоматизированного тестирования, где:
     settings.py - файл данных для тестов

     requiments.txt - зависимости
     chromedriver.exe - драйвер Хрома
     conftest.py - фикстура запуска драйвера браузера
     директории pages - файлов методов страниц (авторизации auth_page.py,
     восстановления pass_rec_page.py, регистрации pass_rec_page.py
     и их локаторов locators.py,
     а также базовым файлом base.py для всех страниц и декораторов ожидания локаторов.
     директории tests - файлов тестов и логов myoutput.log, а также дериктории скриншотов тестов.

   </details>
  </div>
  <div>
   <details><summary>Тестирование</summary>

     Ввести данные в файл settings
     Установить зависимости из requirements.txt
     Все тесты с капчей и кодами скип

     Тесты запускать в терминале с \tests

     Тесты регистрации
     pytest test_registr.py > myoutput_registr.log

     Тесты авторизации
     pytest test_auth.py > myoutput_auth.log

     Тесты восстанавление
     pytest scr/tests/test_pass_rec.py > myoutput_pass_rec.log

     Тесты по маркеру
     pytest -v -m norm > myoutput_norm.log
    
     без скип (8авто,4пасс,9регистр и 26параметр)
   </details>
  </div>
  <div>
    <details><summary>Результат</summary>

     Тестами выевлен:
     - дефект страницы регистрации и восстановление пароля отсуствие слогана
     - дефект ввода полей паролей на обработку пароля с юникодом
     - дефект перехода на авторизацию через yandex
     Ручным тестированием, иследования бага отсуствия слогана по скриншоту 
     выевлен:
     - дефект по требованию расположения блоков авторизации и слогана

   </details>
  </div>
</div>

