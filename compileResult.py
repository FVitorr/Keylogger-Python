from datetime import datetime
now = datetime.now()
date_hour = str([now.day,now.month,now.year,now.hour,now.minute,now.second])
print (date_hour)


def sub (old,new):
      for word in arq_read:
            if word == old:
                  arq_read[arq_read.index(old)]= new


arq   = open("result.txt","r")
arq_read = arq.readlines()
result_var = " "

for index in range(len(arq_read)):
    arq_read[index] = arq_read[index].rstrip('\n') #remove quebra de linha
for word in arq_read :
      sub ("Key.backspace","")
      sub ("Key.esc"," finishExecute ")
      sub ("Key.space"," ")
      sub ("Key.shift","")
      sub ("Key.enter","\n")

result = result_var.join(arq_read)

with open ("resultfinal.txt","a") as save: #saval no arquivo txt compilado
      save.write(date_hour + result)
      save.close()
#print(arq_read)
print(result)

arq.close()
