from PIL import Image, ImageFilter
import pandas
import numpy
import matplotlib.pyplot as pl

def pandas_():
    s = pandas.Series(numpy.arange(5), index=["a", "b", "c", "d", "e"]) # аналог словаря
    print(s)
    print()
    s = pandas.Series(numpy.linspace(0, 5, 5))
    print(s)
    print()
    index = ["a", "b", "c"]
    print(pandas.Series(5, index=index))

def pillow_():
    myimage = Image.open('Image.jpg')
    myimage.load()
    print('Данные о файле: ', myimage.format, myimage.size, myimage.mode)
    myimage = myimage.filter(ImageFilter.BLUR)
    myimage = myimage.filter(ImageFilter.CONTOUR)
    myimage.show()
    # myimage.save()

def matplotlib_():
    x = [1, 2, 3, 4, 5]
    y = [25, 32, 34, 20, 25]
    pl.plot(x, y)
    pl.title("Линейный график")
    pl.show()

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [25, 32, 34, 20, 25, 23, 21, 33, 19, 28]
    pl.scatter(x, y)
    pl.title("Диаграмма рассеяния")
    pl.show()

    vals = [24, 17, 53, 11, 7]
    labels = ["Intel", "AMD", "Nvidia", "Dell", "IBM"]
    pl.pie(vals, labels=labels, autopct='%1.2f%%')
    pl.title("Круговая диаграмма\nРаспределение компаний")
    pl.show()

# pandas_()
# pillow_()
matplotlib_()
