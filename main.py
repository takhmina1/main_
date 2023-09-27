class Person():
    def name(self,name,age):
        self.name = name
        self.age = age
        return f'hi name {self.name} your age {self.age}'
    
    def age(self,age,name):
        self.age = age
        self.name = name
        return f'hi age {self.age} your name {self.name}'
    
    
per = Person()
per2 = Person()
print(per.name('Samat',22))
print(per2.age(22,'Samat'))
print('Hello World')
print()

class Per(Person):
    pass


    
per = Person()
per2 = Person()
print(per.name('Samat',22))
print(per2.age(22,'Samat'))



"Github"


"git confing --global user name ' takhmina'"
n = 'user gmail'

"""
1.cd ..
2.git init
3.git remote add origin (url)
4.main.py tolturuu
5..gitignore
6.git status
7.git add main.py   2.vainant git add .
8.git commit -m "soz"
9.git push origin master                git branch


"""