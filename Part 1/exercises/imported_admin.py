# 25/06/2021
from privileges import Privileges, Admin

mika = Privileges(['can add post', 'can delete post', 'can ban user'])
mika_admin = Admin('Mori', 'Jin', 'Monkey King', 'Korea', 17, 5, mika.privileges)

mika.show_privileges()