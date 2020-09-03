m = float(input("Insira um valor de metros: "))
dm = m*10
cm = m*100
mm = m*1000
dam = m/10
hm = m/100
km = m/1000

print("{}km, {}hm, {}dam, {}m, {:.0f}dm, {:.0f}cm, {:.0f}mm".format(km,hm,dam,m,dm,cm,mm))
