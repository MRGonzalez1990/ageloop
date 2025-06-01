#author Mauro Ruben Gonzalez
adult=['18','19','20','21','22','23','24','25''26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45',]
while True:
  age = input('what is your age:')
  if age in adult:
      print('Thanks, one moment while we fetch the data')
      break
  elif  age == 'end':
      break
  else:
      continue


Copyright [2025] [Mauro Ruben Gonzalez]
