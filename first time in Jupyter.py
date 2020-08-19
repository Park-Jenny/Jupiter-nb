#!/usr/bin/env python
# coding: utf-8

# ## Hello, world!

# In[1]:


print("Hello, world!")


# In[2]:


print("Try to start the new experience here:)")


# In[3]:


# 10진수


# In[4]:


a=365


# In[5]:


print(a)


# In[6]:


# 2진수


# In[7]:


b=0b101101101


# In[8]:


print(b)


# In[9]:


# 8진수


# In[10]:


c=0o555


# In[11]:


print(c)


# In[12]:


# 16진수


# In[13]:


d=0x16d


# In[14]:


print(d)


# In[15]:


fa=3.14


# In[16]:


print(fa)


# In[17]:


fb=-3.14


# In[18]:


print(fb)


# In[19]:


fc=3.1415e2


# In[20]:


print(fc)


# In[21]:


fd=3.1415e-2


# In[22]:


print(fd)


# In[23]:


print("이제부터는 복소수 타입")


# In[24]:


a=6+4j


# In[25]:


print(a)


# In[26]:


b=complex(6,4)


# In[27]:


print(b)


# In[28]:


a.real


# In[29]:


a.imag


# In[33]:


print("이제부턴 불리언 타입 즉, 값은 True나 False만 가질 수 있음")


# In[31]:


ba=True


# In[32]:


bb=False


# In[34]:


ba and bb


# In[35]:


ba or bb


# In[36]:


6==6


# In[37]:


6>4


# In[38]:


6<4


# In[39]:


bool("ABC")


# In[40]:


bool("")


# In[41]:


bool([1,2,3])


# In[42]:


bool([])


# In[43]:


bool()


# In[44]:


bool({})


# In[45]:


bool(1)


# In[46]:


bool(0)


# In[47]:


bool(None)


# In[52]:


a="don't tell me that you didn't start yet"


# In[53]:


print(a)


# In[54]:


b='"You are right.", I said.'


# In[55]:


print(b)


# In[56]:


# Escape 문자


# In[57]:


s="12\n34"


# In[58]:


print(s)


# In[60]:


sd='"This is a longer string that spans multiple lines"'


# In[61]:


print(sd)


# In[62]:


se=r"this\has\no\special\characters"


# In[63]:


print(se)


# In[64]:


# 문자열 연산


# In[69]:


a="this is the first half "


# In[70]:


b="and this is the second half"


# In[71]:


print(a+b)


# In[72]:


a="*"


# In[73]:


print(a*10)


# In[74]:


# 문자열의 길이 


# In[75]:


a="this is the first half"


# In[76]:


len(a)


# In[77]:


len(b)


# In[78]:


# 문자열 인덱싱


# In[79]:


a= "this is a string"


# In[80]:


print(a[2])


# In[81]:


print(a[0])


# In[82]:


print(a[-1])


# In[83]:


print(a[-0])


# In[85]:


# Slicing


# In[86]:


b="20010331 Rainy"


# In[87]:


print(b[:8])


# In[89]:


print(b[8:])


# In[90]:


print(b[:])


# In[91]:


print(b[:-5])


# In[92]:


# 문자열 수정


# In[93]:


a="this is a string"


# In[94]:


a[10:]="rope"


# In[95]:


b="rope"


# In[96]:


a[:10]+b


# In[97]:


c=a.replace("string", "rope")


# In[98]:


print(c)


# In[99]:


# 문자열 foramt


# In[100]:


"I have %d children" %3


# In[101]:


"I have %s children" %"three"


# In[102]:


e=3


# In[103]:


"I have %d children" %e


# In[105]:


"I have %d children so I don't have time %s days." %(3, "these")


# In[107]:


# %s(어떤 코드든지), %c(문자 1개), %d(정수), %f(소수자리 수), %o(8진수), %x(16진수)


# In[108]:


"This is %s%% True!" %100


# In[110]:


"%10s" %"Good"


# In[111]:


"%-10s" %"Good"


# In[112]:


"%0.5f" %3.141592


# In[113]:


"%20.5f" %3.141592


# In[114]:


"I have {0} children so I don't have time {1} days.".format(3,"these")


# In[115]:


"{0:<20}".format("good")


# In[116]:


"{0:>20}".format("good")


# In[117]:


"{0:^20}".format("good")


# In[118]:


"{0:*^20}".format("good")


# In[119]:


f'{"good":*^20}'


# In[120]:


# 문자열 내장함수


# In[121]:


a="Korean culture"


# In[122]:


a.count("u")


# In[124]:


a.find("u")


# In[125]:


a.find("k")


# In[126]:


a.index("u")


# In[127]:


",".join("Korean culture")


# In[128]:


a.upper()


# In[129]:


a.lower()


# In[132]:


b=" Korean culture "


# In[133]:


b.strip()


# In[134]:


b.lstrip()


# In[135]:


b.rstrip()


# In[136]:


a.replace("Korean", "American")


# In[137]:


a.split()


# In[138]:


a.split("u")


# In[139]:


# 리스트 생성


# In[140]:


a=[]


# In[141]:


b=[1,2,3,4,5]


# In[142]:


c=["red", "blue", "yellow"]


# In[143]:


print(a, b, c)


# In[144]:


d=[1,2,["red", "blue"]]


# In[145]:


print(d)


# In[146]:


#인덱싱


# In[147]:


b[0]


# In[148]:


b[0]+b[2]


# In[149]:


a=[1,2,3,4,5,["a","b","c","d"],7,8,9]


# In[150]:


a[0]


# In[151]:


a[-1]


# In[152]:


a[5]


# In[153]:


a[5][2]


# In[154]:


# 슬라이싱


# In[155]:


b=[1,2,3,4,5]


# In[156]:


b[0:4]


# In[157]:


c="12345"


# In[158]:


c[0:4]


# In[159]:


b[:3]


# In[160]:


b[3:]


# In[161]:


a[0:6]


# In[162]:


a[0:6:2]


# In[163]:


a[5]


# In[164]:


a[5][:2]


# In[165]:


#연산


# In[172]:


a=[1,2,3,4]


# In[173]:


b=[6,7,8,9]


# In[174]:


a+b


# In[176]:


a*2


# In[177]:


len(a)


# In[178]:


k=[12345]


# In[179]:


len(k)


# In[180]:


m="12345"


# In[181]:


len(m)


# In[184]:


c=["good"]


# In[185]:


b+c


# In[186]:


a[3]=9


# In[187]:


print(a)


# In[188]:


n="1234"


# In[189]:


n[3]


# In[190]:


# 리스트는 수정 가능, 문자열은 수정 불가


# In[191]:


#function


# In[192]:


a=[1,2,3,4,[a,b,c]]


# In[193]:


b=[6,7,8,9]


# In[194]:


len(a)


# In[195]:


len(b)


# In[197]:


sum(b)


# In[198]:


max(b)


# In[199]:


min(b)


# In[200]:


del(b[0])


# In[201]:


print(b)


# In[202]:


b=[6,7,8,9]


# In[203]:


del b[:3]


# In[204]:


print(b)


# In[205]:


str(b[0])


# In[206]:


b=["6","7","8","9"]


# In[207]:


b.append("10")


# In[208]:


print(b)


# In[209]:


b.append(["11","12"])


# In[210]:


print(b)


# In[211]:


c=["6","9","8","7"]


# In[212]:


print(c)


# In[213]:


c.sort()


# In[214]:


print(c)


# In[216]:


c=["6","9","8","7"]


# In[217]:


c.reverse()


# In[218]:


print(c)


# In[219]:


c.index("9")


# In[221]:


c.insert(4,"10")


# In[222]:


print(c)


# In[223]:


e=["3","4","3","4","5"]


# In[226]:


e.remove("4") #중복 될 경우 가장 앞에 값을 제거


# In[225]:


print(e)


# In[228]:


e.pop()


# In[229]:


print(e)


# In[230]:


e.pop(1)


# In[231]:


print(e)


# In[232]:


e.pop(0)


# In[233]:


print(e)


# In[234]:


c=[6,6,6,6,6,7,8,9]


# In[235]:


c.count(6)


# In[236]:


c.count(5)


# In[237]:


c.extend([4,5])


# In[238]:


print(c)


# In[239]:


# 튜플의 생성


# In[240]:


a=tuple()


# In[241]:


a=()


# In[242]:


type(a)


# In[243]:


b=(1,)


# In[244]:


type(b)


# In[247]:


c=(1,2,3)


# In[248]:


type(c)


# In[249]:


d=1,2,3


# In[250]:


type(d)


# In[251]:


e=(1,2,("ab","cd"), 3, 4)


# In[252]:


type(e)


# In[253]:


# 튜플은 수정 및 변경 불가


# In[254]:


e=(1,2,("ab","cd"),3,4)


# In[255]:


e[0]


# In[256]:


del e[0]


# In[257]:


e.remove(1)


# In[258]:


e.pop(0)


# In[259]:


# 정말로 투플은 수정 및 변경 불가임!!


# In[260]:


e[:]


# In[261]:


c+e


# In[262]:


c*2


# In[263]:


len(c)


# In[264]:


x,y,z=(1,2,3)


# In[265]:


print(x,y,z)


# In[266]:


print(x)


# In[267]:


print(y)


# In[268]:


print(z)


# In[269]:


#사전의 생성


# In[270]:


#{key1:value1, key2:value2, ...}


# In[271]:


a={"gender":"Female", "age":30, "name":"Kristina"}


# In[272]:


print(a)


# In[273]:


type(a)


# In[274]:


a["gender"]


# In[275]:


a["age"]


# In[276]:


a["name"]


# In[278]:


b={1:"good"}


# In[279]:


print(b)


# In[282]:


# 사전의 추가


# In[283]:


a={"gender":"Female"}


# In[284]:


a["age"]=30


# In[285]:


print(a)


# In[286]:


a["name"]="Kristina"


# In[287]:


print(a)


# In[288]:


# 사전의 삭제


# In[290]:


del a["name"]


# In[291]:


print(a)


# In[292]:


del a["age"]


# In[293]:


print(a)


# In[294]:


# 사전의 장점


# In[295]:


result={"학생A":99, "학생B":91, "학생C":83, "학생D":100}


# In[296]:


result["학생A"]


# In[297]:


# 중복 key 값


# In[298]:


a={"fule":"gasoline", "fuel":"diesel"}


# In[299]:


print(a)


# In[300]:


a={"fuel":"gasoline", "fuel":"diesel", "fuel":"LPG"}


# In[301]:


print(a)


# In[302]:


#사전 함수


# In[303]:


a={"gender":"Female", "age":"30", "name":"Kristina"}


# In[304]:


a.keys()


# In[305]:


list(a.keys())


# In[306]:


a.values()


# In[307]:


a.items()


# In[308]:


a.clear()


# In[309]:


print(a)


# In[310]:


a={"gender":"Female", "age":"30", "name":"Kristina"}


# In[311]:


a.get("gender")


# In[312]:


a.get("height","?")


# In[313]:


"gender" in a


# In[314]:


#집합의 생성


# In[315]:


a=set([1,2,3,4,5])


# In[317]:


print(a)


# In[318]:


type({1,2,3,4,5})


# In[319]:


type((1,2,3,4,5))


# In[320]:


type([1,2,3,4,5])


# In[321]:


type({1:2,3:4,5:6})


# In[322]:


b=set("Kristina")


# In[323]:


b


# In[324]:


# 집합은 중복 허용이 안되며 순서가 없음 때문에, 인덱싱을 지원하지 않음


# In[325]:


#교집합, 합집합, 차집합


# In[326]:


x={1,2,3,4,5}


# In[327]:


y={3,4,5,6,7}


# In[328]:


x&y


# In[329]:


x.intersection(y)


# In[330]:


x|y


# In[331]:


x.union(y)


# In[332]:


y.union(x)


# In[333]:


x-y


# In[334]:


y-x


# In[335]:


x.difference(y)


# In[337]:


x^y #대칭 차집합 (차집합의 합집합)


# In[338]:


(x-y)|(y-x)


# In[339]:


#집합 함수


# In[340]:


x.add(10)


# In[341]:


print(x)


# In[342]:


x.update([11,12,13])


# In[343]:


print(x)


# In[344]:


x.remove(13)


# In[345]:


print(x)


# In[346]:


x.remove(15) # 존재하지 않는 것을 삭제하려고 할 때는 오류 메세지가 뜸


# In[1]:


# 대입 연산자


# In[2]:


a=20


# In[3]:


a+=5


# In[4]:


print(a)


# In[5]:


a-=10


# In[6]:


print(a)


# In[7]:


a*=2


# In[8]:


print(a)


# In[9]:


a/=3


# In[10]:


print(a)


# In[11]:


# 비교 연산자


# In[12]:


a=95


# In[13]:


a==90


# In[14]:


a>90


# In[15]:


a<90


# In[16]:


90<=a<=100


# In[18]:


a=[1,2,"Hello World"]


# In[19]:


b=[1,2,"Hello World"]


# In[20]:


id(a)==id(b)


# In[21]:


id(a)


# In[22]:


id(b)


# In[23]:


# a와 b의 내용은 같지만 주소는 다른 것을 알 수 있음


# In[24]:


a.append("A")


# In[26]:


print(a)


# In[27]:


id(a)


# In[28]:


a.remove("A")


# In[29]:


a==b # 출력값이 같기 때문임


# In[30]:


# 논리 연산자


# In[31]:


a=True


# In[32]:


b=False


# In[33]:


a and b


# In[34]:


a or b #둘 중 하나만 참이어도 참


# In[35]:


not a


# In[36]:


not b


# In[38]:


# if문의 구조


# In[40]:


if True:
    print("well, you are genius!!")
else:
    print("hahaha you fool!!")


# In[41]:


a=1000


# In[43]:


if a>5000:
    print("택시를 타세요")
else:
    print("버스를 타세요")


# In[44]:


# for ans


# In[46]:


for a in [1,2,3]:
    print(a)


# In[47]:


for (a,b) in [(1,2),(3,4),(5,6)]:
    print(a+b)


# In[48]:


a="Hello!"
b=["Hello!", "World"]
c=(1,2,3)


# In[49]:


for x in a:
    print(x)


# In[50]:


for x in a:
    print(x, end=" ")


# In[51]:


for x in b:
    print(x)


# In[52]:


for x in c:
    print(x)


# In[53]:


d={"circle":2, "rectangle":3, "line":1}
e={"red","green","blue","red"}


# In[54]:


for x in d:
    print(x)


# In[55]:


for x in e:
    print(x)


# In[56]:


# Continue


# In[57]:


Score=[100,7,75,32]


# In[58]:


num=0


# In[59]:


for a in Score:
    num=num+1
    if a<70:
        continue
    else:
        print("%d번 합격"%num)


# In[60]:


# Continue, range


# In[61]:


a=[100,7,75,32]


# In[62]:


for b in range(len(a)):
    if a[b]<60:
        continue
    print("%d번 합격" %(b+1))


# In[64]:


a=0
for b in [1,2,3,4,5,6,7,8,9,10]:
    a=a+b
    print("1부터 10까지 합은", a, "입니다.")


# In[66]:


a=1
b=0
while a<=100:
    b=b+a
    a=a+1
print("1부터 100까지의 합은:", b)


# In[67]:


# break


# In[68]:


candy=4
money=300
while money:
    print("지불했으니 사탕을 줄게요")
    candy=candy-1
    print("남은 사탕의 양은 %d개 입니다." %candy)
    if candy==0:
        print("사탕이 다 떨어졌습니다. 판매를 중지합니다.")
        break


# In[72]:


a=input("중단할 문자를 입력하시오")

for b in "python":
    if b==a:
        break
    print(b,end=" ")
else:
    print("모든 문자 출력 완료!")


# In[73]:


#pass


# In[76]:


a=input("중단할 문자를 입력하시오:")

for b in "python":
    if b==a:
        pass #그대로 다음 문장으로 넘겨줌
    print(b)


# In[77]:


# 사용자 정의 함수의 구조


# In[78]:


def add(a,b):
    return a+b

print(add(1,3))


# In[1]:


# Class


# In[ ]:




