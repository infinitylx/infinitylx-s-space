+++
Title = "Code review"
Date = 2013-07-08
Tags = ["rtfm", "howto", "alpha-centauri"]
Author = "Wladislaw Merezhko"
Summary = "
After a few of unsuccesfull codereview I came up with idea to create perfect codereview procedure. Afterwhat make it real. So, what is the most important thing to look at during codereview? As boring as it can be it's how things are named.
Після кількох невдалих переглядів коду спало на думку описати ідеальний варіант. Після чого довести його до реальності. Отож, на що в першу чергу слід звернути увагу під час перегляду кода. Банально, але це так, на імена змінних та всього іншого."
+++

Main purpose of codereview, imho, is a detecting of architectural issues (the one that is most hard to fix after). Also with a help of codereview the whole team is staing informed with what who is doing. One more benefit is geting to know new algorithms and realization of different patterns to solve real problems.
Основною метою код ревью, на мою думку, є виявлення архітектурних помилок. Також за допомогою код ревью команда залишається в курсі хто над чим працює. Ще одним бенефітом є ознайомлення із різноманітними алгоритмами та практичними реалізаціями різних патернів для вирішення реальних проблем.

Who?
Who should take part in codereview? At least the whole team. Also should be invited thouse whom will affect recent changes.
Почну із хто? Хто повинен приймати участь у перегляді коду? Відповідь щонайменше вся команда. Повинні також долучатись ті на кого можуть вплинути впроваджені зміни або виправлення.

How?
Best way to do it is when whole team is engaged. Author can send a link to changes for introduction and comments. Comments should be public.
Як? Оптимальним варіантом перегляду коду, на мою думку, є груповим. Автор розсилає усім код для поперднього ознайомлення і вказує час перегляду. Всі мають можливість ознайомитись із кодом і вже на перегляді можуть обміркувати запропонований код.

Review should consists from a few obligatory parts. Firstly, an introductory part when author defines his motives behaind changes. Without this continue is meaningless.
Ревью повино містити декілька обов’язкових частин. Спочатку, можливо навіть у листі із кодом на перегляд (залежить від використовуваних тулзів), автор кода повинен пояснити, яку проблему він намагається вирішити. Без цього подальший перегляд немає сенсу.

Next, author is explaining what he is about to change and ofcourse shows code. Explaining part is can be done separatly during definition of task.
Далі, автор коду повинен пояснити, як само він хоче вирішити поставлену проблему. Ну і звісно навести код.

Discussion 
Далі, у чітко визначений час всі збираються і обговорюють вибраний автором шлях вирішення проблеми. Автор не зобов’язаний враховувати всі побажання.

Потім, після врахування всіх побажань, які вважає автро слушними, процедура повторюється.

Ревью можна проводити по факту або у чітко визначений день. Звісно, якщо теке дозволяє проект. Мені особиство здається, проведення у чітко визначений день більш оптимальним, оскільки дає змогу заздалегідь підготуватись та спланувати час. А одже і якість такого перегляду буде вище.

Особливо хочеться звірнути увагу на що потрібно звернути увагу в першу чергу.

    Відповідність конверціям.
    Назви змінних.
    Відповідність використаних алгоритмів поставленій задачі.
    Відповідність документації та комментарів коду.
    Актуальність та наявність юніттестів.

Також, варто використовувати надбання сучасності у перегляді коду. Які надають змогу занотовувати коментарі до коду та вести дискусію, в разі необхідності.

Такі сайти як github.com, bitbucket та безліч інших дають змогу проводити перегляд коду.
