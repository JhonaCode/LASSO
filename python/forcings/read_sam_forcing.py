import  numpy as np

def read(path,tipe):

    #Read to know the size of the file

    file11= open('%s/%s'%(path,tipe)  ,'r')

    #Time count 
    i=0
    #Lev count 
    counlev=0
    #Line file count 
    count=0

    for line in file11:
        
        if count>0: 
    
            if counlev==0:
    
                l1=line.split()
                tim=float(l1[0])
                lev=int(l1[1])
                p0 =float(l1[2])
    
            counlev+=1
    
            if counlev-1==lev:
                counlev=0
                i+=1
        count += 1
    
    ##########################
    #size found to make the matrices
    ndtp=i
    ndlev=lev

    time      =np.zeros(ndtp)
    z         =np.zeros([ndtp,ndlev])
    pressure  =np.zeros([ndtp,ndlev])
    tpls      =np.zeros([ndtp,ndlev])
    qls       =np.zeros([ndtp,ndlev])
    uls       =np.zeros([ndtp,ndlev])
    vls       =np.zeros([ndtp,ndlev])
    wls       =np.zeros([ndtp,ndlev])

    file11= open('%s/%s'%(path,tipe)  ,'r')

    #Time count 
    i=0
    #Lev count 
    counlev=0
    #Line file count 
    count=0

    for line in file11:
        
        if count>0: 
    
            if counlev==0:
    
                l1     =line.split()
                time[i]=float(l1[0])
                lev    =int(l1[1])
                p0     =float(l1[2])
    
            else:
                ll=line.split()
                z[i][counlev-1]           =(ll[0])
                pressure[i][counlev-1]    =(ll[1])
                tpls[i][counlev-1]        =(ll[2])
                qls[i][counlev-1]         =(ll[3])
                uls[i][counlev-1]         =(ll[4])
                vls[i][counlev-1]         =(ll[5])

                if(tipe=='lsf'):
                    wls[i][counlev-1]         =(ll[6])
    
            counlev+=1
    
            if counlev-1==lev:
                counlev=0
                i+=1
    
        count += 1
    
    return time,z,pressure,tpls,qls,uls,vls,wls


def read_1d(path,tipe):

    file11= open('%s/%s'%(path,tipe)  ,'r')

    #Line file count 
    count=0

    for line in file11:

        count += 1
    
    ##########################
    #size found to make the matrices
    ndtp=count-1
    
    ##########################

    time     =np.zeros(ndtp)
    sst      =np.zeros(ndtp)
    shf      =np.zeros(ndtp)
    lhf      =np.zeros(ndtp)
    tau      =np.zeros(ndtp)

    file11= open('%s/%s'%(path,tipe)  ,'r')

    #Time count 
    count=0
    for line in file11:
        
        if count>0: 
    
            ll=line.split()
            time[count-1]         =(ll[0])
            sst[count-1]          =(ll[1])
            shf[count-1]          =(ll[2])
            lhf[count-1]          =(ll[3])
            tau[count-1]          =(ll[4])

        count += 1
    
    return time,sst,shf,lhf,tau 
    
