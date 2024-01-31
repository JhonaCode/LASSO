# python library to work with netcdf4 
#from    netcdf4         import dataset

# to save the time coordinate in specific format 
from    netCDF4         import num2date, date2num

# Python standard library datetime  module
import datetime as dt


#Function to know 
#the data interval to make 
#the statitics analysis of that interval.
#CREATED:Jhonatan Aguirre
#Covid19
#Data   :27-04-2020

#In:
#    idi: first data to search  
#    idf: last data to search  
#    data: data arrange

#Out:
#    ni:initial interval data indix
#    ni: final interval data indix


def time_n_calendar(idi,data): 
#TO find the calendar day given the data

    #idi = dt.datetime(2014, 9, 26, 1) 
    #idf = dt.datetime(2014, 10,01, 1) 
    
    #Which type of calendar 
    tu = "days  since 2013-12-31 00:00:00 -00:00:00"
    tc = "gregorian"
    
    idin=date2num(idi,units=tu,calendar=tc)

    #indices achados
    ni=0

    #banderas 
    b1=0

    for i in range(0,data.shape[0]):

        if data[i]>=idin and b1==0: 

            ni =i  
            b1 =1
            print("Data1:", data[i],i)
            break

    return ni,data[i]

def time_n(idi,idf,data): 

    #idi = dt.datetime(2014, 9, 26, 1) 
    #idf = dt.datetime(2014, 10,01, 1) 
    
    tu = "days  since 2013-12-31 00:00:00 -00:00:00"
    tc = "gregorian"
    
    idin=date2num(idi,units=tu,calendar=tc)
    idfn=date2num(idf,units=tu,calendar=tc)

    #indices achados
    ni=0
    nf=0

    #banderas 
    b1=0
    b2=0

    for i in range(0,data.shape[0]):

        if data[i]>=idin and b1==0: 

            ni =i  
            b1 =1
            print("Data1:", data[i],i)

        print(data[i])

        if data[i]>=idfn and b2==0:  

            nf =i  
            b2 =1
            print("Data2:", data[i],i) 

    return ni,nf

def data_n(idi,idf,data): 
    

    #indices achados
    ni=0
    nf=0

    #banderas 
    b1=0
    b2=0

    for i in range(0,len(data)):

        if data[i]>=idi and b1==0: 

            ni =i  
            b1 =1
            print("Data1:", data[i],i)

        if data[i]>=idf and b2==0:  

            nf =i  
            b2 =1
            print("Data2:", data[i],i) 

    return ni,nf

def level_n(idi,idf,data): 

    #indices achados
    ni=0
    nf=0

    #banderas 
    b1=0
    b2=0

    for i in range(0,data.shape[0]-1):

        if data[i]>=idi and b1==0: 
            ni =i  
            b1 =1
            print("Level1:", data[i]) 

        if data[i]>=idf and b2==0:  
            nf =i  
            b2 =1
            print("Level2:", data[i]) 
    return ni,nf

def data_n_goa(idi,idf,data): 

    #idi = dt.datetime(2014, 9, 26, 1) 
    #idf = dt.datetime(2014, 10,01, 1) 
    
    #tu = "days  since 2013-12-31"
    tu = "days  since 2013-12-31 00:00:00 +04:00:00"
    tc = "gregorian"
    
    idin=date2num(idi,units=tu,calendar=tc)
    idfn=date2num(idf,units=tu,calendar=tc)

    #indices achados
    ni=0
    nf=0

    #banderas 
    b1=0
    b2=0

    for i in range(0,data.shape[0]-1):

        if data[i]>=idi and b1==0: 
            ni =i  
            b1 =1
            print( "Data1:", data[i]) 

        if data[i]>=idf and b2==0:  
            nf =i  
            b2 =1
            print( "Data2:", data[i]) 
    
    return ni,nf

def data_to_reference(data,tsec):

    i=0

    data_ref = dt.datetime(2022,1,1,0)

    #tsec= [float(t)*1.0/3600.0 for t in tsec]
    tsec= [float(t)*24.0 for t in tsec]

    offset=dt.timedelta(hours=4)

    # List of all times in the file as datetime objects
    #dt_time = [ dt.datetime(2021, 12, 31,20) + dt.timedelta(hours=t)  \
    dt_time = [ dt.datetime(2022, 1, 1,0) + dt.timedelta(hours=t)  \
    - offset
    for t in tsec]


    return dt_time
