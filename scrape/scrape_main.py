from scrape import naukri
from scrape import simply_hired
from dbms import mdb
from thefuzz import fuzz

def arrange(l):
    p=list(map(str.lower,l))
    m={}
    for i in p:
        if i in m:
            m[i]+=1
        else:
            m[i]=1
    s=[k for k, v in sorted(m.items(), key=lambda item: item[1], reverse=True)]
    b=[True for i in range(len(s))]
    nm={}
    for i in range(len(s)):
        if b[i]==False:
            continue
        if s[i] not in nm:
            nm[s[i]]=m[s[i]]
        for j in range(i+1,len(s)):
            if b[j]==False:
                continue
            if fuzz.ratio(s[i],s[j])>80:
                b[j]=False
                nm[s[i]]+=m[s[j]]
            else:
                if s[j] not in nm:
                    nm[s[j]]=m[s[j]]
    return [k for k, v in sorted(nm.items(), key=lambda item: item[1], reverse=True)]
            

def getSkills(searchString, noOfPages=5):
    l=mdb.queryList(searchString)
    if l!=[]:
        return l
    skills = naukri.naukri(searchString, noOfPages)
    skills.extend(simply_hired.simplyHired(searchString, noOfPages))
    skills = arrange(skills)
    mdb.insert(searchString, skills)
    return skills