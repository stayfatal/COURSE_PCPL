import Lab_3.lab_python_fp.field
import lab_python_fp.gen_random
import lab_python_fp.unique

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

rand = lab_python_fp.gen_random.gen_random(5,1,25)

print(rand)

lab_python_fp.field.field(goods,'color','title') 

iter=lab_python_fp.unique.Unique([1 , 2 ,2 ,4])

for i in iter:
    print(i)