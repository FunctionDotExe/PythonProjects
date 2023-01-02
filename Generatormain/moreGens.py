def processorcompanies(cpu):
  for cpu in cpu:
    yield(cpu)

processorlist = ['AMD Ryzen 9','Core i9 9900ks','Nvidia RTX 2080 ti']

output = processorcompanies(processorlist)

for j in output:
  print(j)