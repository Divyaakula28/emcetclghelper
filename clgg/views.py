from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import User
from django.db.models import Q
import json



def findurclg(req):
	def get_ip(req):
		address=req.META.get('HTTP_X_FORWARDED_FOR')
		if address:
			ip=address.split(',')[-1].strip()
		else:
			ip=req.META.get('REMOTE_ADDR')	
		return ip
	ip=get_ip(req)
	u=User(user=ip)	
	result=User.objects.filter(Q(user__icontains=ip))
	if len(result)==1:
		print("user exist")
	elif len(result)>1:
		print('user exist')	
	else:
		u.save()
		print('user')
	count=User.objects.all().count()	
	print("totoal users",count)	
	if 'Individual college cutoff' in req.POST:
		return render(req,'state1.html')
	return render(req,'buttonap.html')

def table1(req):
	if req.method=="POST":
		clg=req.POST['clg']
		print(clg)
		gender=req.POST['gender']
		caste=req.POST['branch1']
		if(gender=='MALE'):
			caste=caste+' '+'BOYS'
		else:
			caste=caste+' '+'GIRLS'
		a=req.session.get('ste')
		df=pd.read_excel(a)
		df1=(df[(df["inst_name"]==clg)])[["inst_code","inst_name","branch_ code",caste,"DIST","PLACE"]]
		df1=df1.values.tolist()
		print(df1)
		return render(req,'table1.html',{'df1':df1,'c':caste})
	return render(req,'buttonap.html')
def but1(req):
	if req.method=="POST":
		state=req.POST['state']
		if state=="AP-2019":
			a="AP2018.xlsx"
			df=pd.read_excel("AP2018.xlsx")
		elif state=="TS-1st phase":
			a="TSFirst.xlsx"
			df=pd.read_excel("TSFirst.xlsx")
		else:
			a="TSLast.xlsx"
			df=pd.read_excel("TSLast.xlsx")
		print(a)
		print("hello")
		df1=df["inst_name"]
		df1= df1.values.tolist()
		df1.sort()
		df1= list(dict.fromkeys(df1))
		print(df1)
		req.session['ste']=a
		return render(req,'clg.html',{'df1':df1,'a':a})
	return render(req,'state1.html')

def test(req):
	if 'Rank based college list' in req.POST:
		return render(req,'emcet.html')
	return render(req,'emcet.html')


def table(req):
	if req.method=="POST":
		rank=req.POST['Rank']
		rank=int(rank)
		branch=req.POST['branch']
		gender=req.POST['gender']
		caste=req.POST['branch1']
		state=req.POST['state']
		if(gender=='MALE'):
			caste=caste+' '+'BOYS'
		else:
			caste=caste+' '+'GIRLS'
		rk=rank
		
		if (rank<=10000):
			rank=10000
			rank1=1
		elif ((rank>10000) and (rank<=20000)):
			rank=20000
			rank1=10000
		elif ((rank>20000) and (rank<=30000)):
			rank=30000
			rank1=20000
		elif ((rank>30000) and (rank<=40000)):
			rank=40000
			rank1=30000
		elif ((rank>40000) and (rank<=50000)):
			rank=50000
			rank1=40000
		elif ((rank>50000) and (rank<=60000)):
			rank=60000
			rank1=50000
		elif ((rank>60000) and (rank<=70000)):
			rank=70000
			rank1=60000
		elif ((rank>70000) and (rank<=80000)):
			rank=80000
			rank1=70000
		elif ((rank>80000) and (rank<=90000)):
			rank=90000
			rank1=80000
		elif ((rank>90000) and (rank<=100000)):
			rank=100000
			rank1=90000
		else:
			rank=200000
			rank1=100000
		x={'COMPUTER SCIENCE  AND  ENGINEERING': 'CSE', 'ELECTRONICS AND COMMUNICATION ENGINEERING': 'ECE', 'ELECTRICAL AND ELECTRONICS ENGINEERING': 'EEE', 'MECHANICAL ENGINEERING': 'MEC', 'CIVIL ENGINEERING': 'CIV', 'INFORMATION TECHNOLOGY': 'INF', 'MINING ENGINEERING': 'MIN', 'BIO\xadMEDICAL ENGINEERING': 'BME', 'CHEMICAL ENGINEERING': 'CHE', 'PHARMACEUTICAL ENGINEERING': 'PHE', 'AGRICULTURAL ENGINEERING': 'AGR', 'BIO\xadTECHNOLOGY': 'BIO', 'INDUSTRIAL PRODUCTION ENGINEERING': 'IPE', 'PHARM \xad D (M.P.C. STREAM)': 'PHD', 'DAIRYING': 'DRG', 'FOOD SCIENCE': 'FDS', 'COMPUTER SCIENCE AND INFORMATION TECHNOLOGY': 'CSI', 'ELECTRONICS AND INSTRUMENTATION ENGINEERING': 'EIE', 'ARTIFICIAL INTELLIGENCE': 'AI', 'ELECTRONICS AND TELEMATICS': 'ETM', 'AERONAUTICAL ENGINEERING': 'ANE', 'ELECTRONICS AND COMPUTER ENGINEERING': 'ECM', 'DIGITAL TECHNIQUES FOR DESIGN AND PLANNING': 'DTD', 'FACILITIES AND SERVICES PLANNING': 'FSP', 'PLANNING': 'PLG', 'METALLURGICAL ENGINEERING': 'MET', 'BTECH MECHANICAL  WITH MTECH MANUFACTURING SYSTEMS': 'MMS', 'BTECH MECHANICAL  WITH MTECH THERMAL ENGG': 'MTE', 'COMPUTER SCIENCE & ENGINEERING (NETWORKS)': 'CSN', 'ELECTRONICS COMMUNICATION AND INSTRUMENTATION ENGINEERING': 'ECI', 'MECHANICAL (MECHTRONICS) ENGINEERING': 'MCT', 'METALLURGY AND MATERIAL ENGINEERING': 'MMT', 'INFORMATION TECHNOLOGY AND ENGINEERING': 'ITE', 'AUTOMOBILE ENGINEERING': 'AUT', 'FOOD PROCESSING TECHNOLOGY': 'FPT', 'TEXTILE TECHNOLOGY': 'TEX', 'COMPUTER ENGINEERING': 'CME', 'COMPUTER SCIENCE AND BUSINESS SYSTEM': 'CSB'}
		m=x.keys()
		n=x.values()
		m=list(m)
		n=list(n)
		for i in range(len(m)):
			if branch==m[i]:
				branch=n[i]
				break
			else:
				continue
		print(branch,caste,rank)
		if state=="AP-2019":
			df=pd.read_excel("emcetclghelper/clgg/AP2018.xlsx")
			print(branch,df)
		elif state=="TS-1st phase":
			df=pd.read_excel("TSFirst.xlsx")
		else:
			df=pd.read_excel("TSLast.xlsx")
		df1=(df[(df[caste]<=rank)&(df[caste]>=rank1)&(df["branch_ code"]==branch)])[["inst_code","inst_name","branch_ code",caste,"PLACE","DIST"]]
		df1.sort_values([caste], ascending=[True], inplace=True)
		df1=df1.values.tolist()
		r=[]
		s=[]
		print(len(df1))
		for i in range(len(df1)):
			k=int(df1[i][3])
			if k>=rk:
				r.append(k)
			else:
				s.append(k)
		r=r[:2]
		s=s[-2:]
		r.extend(s)
		print(r)
		return render(req,"table.html",{'df1':df1,'r':r,'caste':caste})

	return HttpResponse("hiii")
