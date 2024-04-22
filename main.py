import cmath
import numpy as np
import matplotlib.pyplot as plt


pmin, pmax, qmin, qmax = -2, 2, -2, 2
# пусть c = p + iq и p меняется в диапазоне от pmin до pmax,
# а q меняется в диапазоне от qmin до qmax

xpoints, ypoints = 200, 200
# число точек по горизонтали и вертикали

max_iterations = 100
# максимальное количество итераций

infinity_border = 3
# если ушли на это расстояние, считаем, что ушли на бесконечность

image = np.zeros((xpoints, ypoints))
# image — это двумерный массив, в котором будет записана наша картинка
# по умолчанию он заполнен нулями

for ip, p in enumerate(np.linspace(pmin, pmax, xpoints)):
    for iq, q in enumerate(np.linspace(qmin, qmax, ypoints)):
        z = p + 1j * q
        # буквой j обозначается мнимая единица: чтобы Python понимал, что речь
        # идёт о комплексном числе, а не о переменной j, мы пишем 1j


        for k in range(max_iterations):
            z = z**2/(z**2 - 1)
            # Самая главная формула

            if abs(z) > infinity_border:
                image[ip, iq] = k
                break
plt.xticks([])
plt.yticks([])
# выключим метки на осях

plt.imshow(image.T, cmap='gist_stern')
plt.colorbar()
plt.title('Fractal of Rational Function')
plt.show()
# параметр cmap задаёт палитру