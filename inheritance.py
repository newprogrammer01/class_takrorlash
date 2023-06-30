# class Animal:
#     def description(self):
#         return "it is animal"

# class Dog(Animal):
#     pass

# qoplon=Dog()
# print(qoplon.description())

# class Animal:
#     def description(self):
#         return 'it is animal'
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass

# qoplon=Dog()
# mosh=Cat()
# print(qoplon.description())
# print(mosh.description())



# class Animal:
#     def description(self):
#         return 'it is animal'
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass


# qoplon = Dog()
# mosh = Cat()
# print(qoplon.description())
# print(mosh.description())


# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def description(self):
#         return 'I am animal'
# class Dog(Animal):
#     def description(self):
#         return 'I am dog'

# class Cat(Animal):
#     pass
# dog1 = Dog('qoplon')
# print(dog1.description())



# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def description(self):
#         return 'I am animal'
# class Dog(Animal):
#     def __init__(self,name, age):
#         Animal.__init__(self,name)
#         self.age=age
#     def description(self):
#         return 'I am dog'

# class Cat(Animal):
#     pass

# dog1 = Dog('qoplon',5)
# print(dog1.age)



# from polygon import Polygon
# class Square(Polygon):
#     def __init__(self, height):
#         super().__init__(height,height)

# x=Square(5)
# print(x.getArea())



# class Data:
#     pass

# data = Data()
# print((data))

# class Data(object):
#     pass

# data=Data()
# print(dir(data))



# class Definition syntax
# class Data:
#     pass

# data = Data()
# print(data.__class__)
# print(data)


class Data(object):
    pass

# data=Data()
# print(data.__class__)
# print(type(data))