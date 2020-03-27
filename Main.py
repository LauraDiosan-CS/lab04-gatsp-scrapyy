from repository.Reader import Reader
from service.Service import Service

reader = Reader()
param = reader.read2("file.txt")

service = Service(param)
r = service.solve(80,50,0.9,0.9)

f = open("out.txt","w")
for i in r.findAll():
    f.write(str(i))
    f.write("\n")
f.close()


