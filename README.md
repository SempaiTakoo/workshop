# workshop
Personal programs for solving small household tasks, practice or training

***

### <u>I</u> Уравнения с разделяющимися переменными
Общий вид:<br>
  $f(x)dx = g(y)dy$

###### Метод разделения переменных
__Пример:__<br>
  $xy' - y =0$
1. Записать $y'$ как $\frac{dy}{dx}$<br>
  $x\frac{dy}{dx} - y = 0$ 
2. В одной стороны собрать все $x$, в другой — все $y$<br>
  $\frac{1}{x}dx = \frac{1}{y}dy$
3. Проинтегрировать<br>
  $\int\frac{1}{x}dx = \int\frac{1}{y}dy$<br>
  $ln|x| + C_{1} = ln|y| + C_{2}$<br>
  $ln|y| = ln|x| + C_{3}$
4. Выразить $y$<br>
  $e^{ln|y|} = e^{ln|x| + C_{3}}$<br>
  $|y| = |x| · e^{C_{3}}$<br>
  $|y| = |x| · C_{4}$<br>
  $y = x · C_{5}$<br>
  <i>Ответ: $y = Cx, C \in \mathbb{R}$ </i>


### <u>II</u> Неоднородные линейные дифф. ур. 1-го порядка (НЛДУ1П)
Общий вид:<br>
  $y' + p(x)·y = q(x)$ &ensp;&ensp; (где $q(x)$ обеспечивает неоднородность)<br>
  $p(x), q(x)$ — заданные функции<br>
  $y = y(x)$ — искомая функция

###### Метод вариации произвольных констант
__Пример:__<br>
  $y' - y·ctgx - sinx = 0$
1. Убедиться, что это действительно НЛДУ1П<br>
  $y' + (-ctgx)·y = sinx$
2. Записать соответствующее однородное дифф. ур. (вместл $q(x)$ записать $0$)<br>
  $y' - y·ctgx = 0$
3. Решить его (методом разделения переменных)<br>
  $[...]$<br>
  $y = C·sinx$
4. Записать фразу "Будем искать решение исходного уравнения в виде $y = ...C(x)...$"<br>
  <i>Будем искать решение исходного уравнения в виде $y = C(x)sinx$ </i>
5. Эту штуку (выражение справа) подставить в исходное уравнение<br>
  $(C(x)sinx)' - C(x)sinx·ctgx - sinx = 0$<br>
  $(C(x)sinx)' - C(x)cosx - sinx = 0$<br>
  $C'(x)sinx + C(x)cosx - C(x)cosx - sinx = 0$<br>
  $C'(x)sinx = sinx$ &ensp;&ensp; (на этом шаге C(x) должен пропасть)<br>
  $C'(x) = 1$<br>
  $C(x) = x + C_{1}$
6. Заглянуть в пункт 4 и записать ответ<br>
  <i>Ответ: $y = (x + C)sinx, C \in \mathbb{R}$ </i>

###### Метод Бернулли
__Пример:__<br>
  $y' - y·ctgx - sinx = 0$
1. Убедиться, что это действительно НЛДУ1П<br>
  $y' + (-ctgx)·y = sinx$
2. Заменить $y = uv$, где $u = u(x)$, $v = v(x)$ — пока неизвестные функции<br>
  $(uv)' + (tgx)(uv) = \frac{1}{cosx}$<br>
  $u'v + uv' + uv·tgx = \frac{1}{cosx}$
3. Выносим $u$ за скобки<br>
  $u'v + v(v' + vtgx) = \frac{1}{cosx}$
4. Находим какую-то конкретную функцию $v \neq 0$, которая обнуляется выражение в скобках<br>
  <i>Решим $v' + vtgx = 0$</i><br>
  $[...]$<br>
  $v = C_{1}cosx$<br>
  <i>Берём конкретное решение при $C_{1} = 0$ &ensp; $v = cosx$</i>
5. Подставляем подобранную функцию $v$ в уравнение из пункта 3<br>
  $u'cosx = \frac{1}{cosx}$<br>
  $u = tgx + C$
6. Заглянув в пункт 2, записать ответ<br>
  <i>Ответ: $y = Ccosx + sinx$</i>


### <u>III</u> Уравнение Бернулли
Общий вид:<br>
  $y' + p(x)·y = q(x)·y^b$ <i>(прим. где $b$ - число, $b \neq 0$)</i>

###### Метод замены
__Пример:__<br>
  $xy' = \frac{x}{y} + y$
1. Проверить, что это уравнение Бернулли<br>
  $y' - \frac{1}{x}y = y^{-1}$
2. Заменить $y = z^a$, где $a$ — пока неизвестное число, $z = z(x) - пока неизвестная функция$<br>
  $(z^a)' - \frac{1}{x}z^a = (z^a)^{-1}$<br>
  > $(z(x)^a)'_{x} \Rightarrow (z^a)' = az^{a - 1}·z'$<br>
  $az^{a - 1}·z' - \frac{1}{x}z^a = z^{-a}$
3. Делим обе части уравнения на выражение, стоящее перед $z'$<br>
  $z' - \frac{1}{ax}z = \frac{1}{a}z^{-2a + 1}$
4. Подобрать число $a$ так, чтобы в правой части было $z^0$<br>
  $-2a + 1 = 0 \Rightarrow a = 1/2$
5. Подобранное $a$ подставим в уравнение из пункта 3<br>
  $z' - \frac{2}{x}z = 2$
6. Решим это уравнение (НЛДУ1П)<br>
  [...]<br>
  $z = C_{7}x^2-2x$
7. Гляду в пункт 2, пишем ответ<br>
  <i>Ответ: $y = \sqrt{Cx^2 - 2x}$</i>


### Уравнения, допускающие понижение порядка
> Порядок — это наибольший встречающийся порядок производной в уравнении. <br>
> Например: <br>
> $y' - \frac{1}{x}y = \frac{1}{x^2}$ — дифф. ур. 1-го порядка
> $y'' - sin(e^{y'''} + \frac{4}{y''}) = \frac{1}{sqrt{y}}$ — дифф. ур. 3-го порядка

#### <u>IV</u> Дифф. ур-я вида $y^{n} = f(x)$
###### Метод n-кратного интегрирования
__Пример:__
<br>
  $y''' = 3x^2 + 6$<br>
  $y''  = x^3 + 6x + C_{1}$<br>
  $y'   = \frac{x^4}{4} + 3x^2 + C_{1}x + C_{2}$<br>
  $y    = \frac{x^5}{20} + x^3 + C_{4}x^2 + C_{2}x + C_{3}$

#### <u>V</u> Дифф. ур-я, в которых нет $y$ (без $'$) и которые содержат как минимум две производные
###### Метод замены $z = z(x) = y^{(...)}$
__Пример:__
<br>
  $y'''' - y''' = e^x$
1. Заменить $z = z(x) = y^{(...)}$, где $(...)$ — наименьший встречающийся порядок производной<br>
  <i>Замена $z = z(x) = y'''$</i>
2. Переписать уравнение через $z$<br>
  $z' - z = e^x$<br>
  $[...]$<br>
  $z = (x + C)e^x$
3. Заменитт обратно<br>
  y''' = e^x(x + C)<br>
  <i>Решим методом n-кратного интегрирования</i><br>
  [...]<br>
  $y = e^x(x + C - 3) + C_{7} + C_{2}x + C_{8}x^2$<br>
  <i>Ответ: $y = e^x(x + C - 3) + C_{7} + C_{2}x + C_{8}x^2$</i>
#### <u>VI</u> Дифф. ур-я, в которых нет $x$
###### Метод замены $z = z(y) = y'$
__Пример:__
<br>
  $y''·y = y'^{2}$
1. Заменить $z = z(y) = y'$<br>
  <i>Введём новую функцию $z = z(y) = y'$</i>
2. Выразить через $z$ все производные, встречающиеся в уравнении<br>
  > - $y' = z$<br>
  > - $y'' = y''_{xx} = (y'_{x})'_{x} = \frac{d(y'_{x})}{dx} · \frac{dy}{dx} = \frac{dz}{dy} · \frac{dy}{dx} = z'·y' = z'·z$<br>
  > - $y''' = [...] = (z''z + z'^2)·z$<br>
  > - $y'''' = [...]$
<br>
  <i>Имеем: $z'·z·y = z^2$</i> <i>(прим. искомая функция $z = z(y)$)</i><br>
  $z'·y = z$<br>
  $\frac{dz}{dy}·y = z$<br>
  $\frac{dz}{z} = \frac{dy}{y}$<br>
  $ln|z| = ln|y| + C_{1}$<br>
  $z = C_{2}y$
3. Заменим обратно<br>
  $y' = C_{2}y$<br>
  $\frac{dy}{dx} = C_{2}dx$<br>
  $ln|y| = C_{2}x + C_{3}$<br>
  $y = e^{C_2{x}} · C_4$<br>
  <i>Ответ: $y = C_1e^{C_2x}, C_1, C_2 \in \mathbb{R}$</i>

### Уравнение <u>VII</u> Лагранжа и <u>VIII</u> Клеро
Общий вид ур-я Лагранжа:<br>
  $y = x·F(y') + G(y')$
Общий вид ур-я Клеро:<br>
  $y = xy' + G(y')$
> Уравнение Клеро — частный случай ур-я Лагранжа
> $F(y'), G(y')$ — выражения, в которых нет $y, y'', y'''$ и т. д.

__Пример ур-я Лагранжа, не являющегося ур-ем Клеро:__<br>
  $y + 3y'^2 = 2xy'$ $(*)$
1. Проверить, что это УЛНЯУК<br>
  $t = x·2.y' + (-3y'^2)$
2. Заменить $p = p(x) = y'$<br>
  _Пусть_  $p = p(x) = y' \Rightarrow y = 2px - 3p^2$ $(**)$
3. Продифференцировать обе части<br>
  $y' = 2p'x + 2p - 6pp'$
4. Заменить $y'$ на $p$<br>
  $p = 2p'x + 2p - 6pp'$
5. Все слагаемые с $p'$ перенести влево, вынести за скобку $p'$, а всё остальное — вправо.
6. Переписать $p'$ как $\frac{dp}{dx}$ и умножить обе части на $\frac{dx}{dp}$<br>
  $(6p - 2x)\frac{dp}{dx} = p\frac{dx}{dp}$<br>
  $6p - 2x = p\frac{dx}{dp}$<br>
  $6p - 2x = px'$
> НЛДУ1П $\uparrow$
> Искомая $x = x(p)$
7. Рассмотреть случай $p = 0$<br>
  * 7а) $p = 0$<br>
      $y' = 0$<br>
      $y = A$<br>
  * 7б) Полученное выражение подставим в $(*)$<br>
      $A + 3·0^2 = 2x·0$<br>
      $A = 0$<br>
  * 7в) Первое решение дифф. ур-я<br>
      $y = 0$
8. Рассмотреть случай $p \neq 0$<br>
  * 8а)  Делим на $p'$<br>
      $6 - \frac{2x}{p} = x'$<br>
      $x' + \frac{2}{p}x = 6$<br>
      $[...]$<br>
      $x = 2p + \frac{B}{p^2}$<br>
  * 8б) Полученное выражение для $x$ подставим в $(**)$<br>
      $y = 2p · (2p + \frac{B}{p^2}) - 3p^2 = p^2 + \frac{2B}{p}$
9. Записать ответ
> учитывая результат 7в
> учитывая результат 8а и 8б
> зааменяя константы на $C$
> заменяя $p$ на $x$

Ответ:<br>
  $\left[
      \begin{gathered}
          y = 0; \\
          \begin{cases}
              x = 2t + \frac{C}{t^2} \\
              y = t^2 + \frac{2C}{t}
          \end{cases}
      \end{gathered}
  \right.$


__Пример ур-я Клеро:__<br>
  $y - y'^2 = xy'$ $(***)$
> Шаги 1—5 точное такие же

6. Рассмотрим случай $p' = 0$<br>
  * 6а)<br>
      $p' = 0$<br>
      $y'' = 0$<br>
      $y = Ax + B$<br>
  * 6б) Подставить выражения в $(***)$<br>
      $Ax + B - A^2 = Ax$<br>
  * 6в) Выразить обе константы через какую-то одну<br>
      $\begin{cases}<br>
          A = A \\<br>
          B = A^2<br>
      \end{cases}$<br>
  * 6г) Записать первую серию решений ур-я<br>
      $y = Ax + A^2$
7. Рассмотреть случай, когда множитель равен нулю<br>
  * 7а)<br>
      $x + 2p = 0$<br>
      $x = -2p$<br>
  * 7б) Подставим выражение в пункт 2<br>
      $y = xp + p^2$<br>
      $y = (-2)p + p^2$<br>
      $y = -p^2$
8. Записать ответ
> учитывая результат 6г <br>
> учитывая результат 7а и 7б <br>
> заменяя константы на $C$ <br>
> заменяя $p$ на $t$ <br>

Ответ:<br>
  $\left[
      \begin{gathered}
          y = Cx + C^2 \\
          \begin{cases}
              x = -2t \\
              y = -t^2
          \end{cases}
      \end{gathered}
  \right.
  \Leftrightarrow
  \left[
      \begin{gathered}
          y = Cx + C^2 \\
          y = -\frac{x^2}{4}
      \end{gathered}
  \right.$