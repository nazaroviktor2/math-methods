# Задача 1
1) Результат по функции = -0.0005002450796476321
2) Результат по горнеру = -0.0005002450796474608
3) Погрешность: 1.713039432527097e-16

# Задача 2 
1) (1+(2^-51+2^-52+2^-54))-1 = 1 - 1 + 4.4408921*10^-16 + 2.220446*10^-16 + 5.5511151*10^-17 = 0.000000000000000721644961 = 7.21644961*10^-16
- в питоне = 6.661338147750939e-16
2) (1+(2^-52+2^-53+2^-60))-1 = 1-1 + 2.220446*10^-16 +  1.110223*10^-16 + 8.6736174*10^-19 = 0.00000000000000033393426174 = 3.3393426174*10^-16
- в питоне = 4.440892098500626e-16

# Задача 3
- sqrt(9.01)-3 = 0.0016662039607266976 = 0.002
- Ответ: 0.002

# Задача 4
## 1
𝑎 + sqrt(𝑎^2 + 𝑏^2), a = -12345678987654321, b = 123

1. Так как a - отрицательное, b - положительное => при вычислениях возник погрешность, чтобы ее уменьшить домножим на сопряженное
=> выражение примет вид b^2 / sqrt(a^2+b^2) - a
2. 15129 / sqrt(152415789666209420210333789971041+15129) +12345678987654321  = 15129 / sqrt(152415789666209420210333789986170) + 12345678987654321 = 15129 / 12345678987654320 + 12345678987654321 = 15129 / 24691357975308641 = 0.0000000000006127 =6.127*10^-13
3. Округляем до 4-х десятичных знаков = 0

## 2
sqrt(a^2+b^2) - a, a = 2468864224688642, 𝑏 = 13579

1. Так как под коренное выражение всегда положительное, а-положительно. Но из-под коренного выражения мы вычитаем a => sqrt(a^2+b^2) + (- a) => положительно число складываем с отрицательным.
Из-за этого будет погрешность, для того чтобы ее уменьшить домножим на сопряженное => b^2 / sqrt(a^2+b^2) + a  
2. 184389241 / sqrt(6095290559947449370361843804164 + 184389241) + 2468864224688642 = 84389241 / sqrt(6095290559947449370362028193405) + 2468864224688642 = 84389241 / 2468864224688642 + 2468864224688642 =  84389241 / 4937728449377284 = 1.7090701091641168*10^-08
3. Округляем до 4-х десятичных знаков = 0
