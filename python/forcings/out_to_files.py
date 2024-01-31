import  diurnal_days as d_days 

def sam_forcing(exp,folder,label):
##############################################################################

    file11= open('%s/snd_%s'%(folder,label),  'w+')
    file22= open('%s/lsf_%s_h'%(folder,label),'w+')
    file23= open('%s/lsf_%s_p'%(folder,label),'w+')
    file33= open('%s/sfc_%s'%(folder,label)  ,'w+')
    
    file11.write("z[m]\tp[mb]\ttp[K]\tq[g/kg]\tu[m/s]\tv[m/s]\n")
    file22.write("z[m]\tp[mb]\tsls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
    file23.write("z[m]\tp[mb]\ttls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
    file33.write("day\t\tsst(K)\t\tH(W/m2)\t\tLE(W/m2)\tTAU(m2/s2) \n")
    
    ndtp =len(exp.time_sec)
    ndlev=len(exp.lev)

    #NOTE:the forcing was created in local time, MANAUS -4UTC
    ###Manaus time
    ##h =[0,3,6,9,12,15,17,20,23,02]
    #time=[0.0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1.0]
    
    #NOTE:the forcing was created in UTC TIME
    ###UTC time
    ##h =[0 ,3 ,6,9,12,15,18,21,24,3]
    ##to UTC-4
    ##h =[20,23,2,5,8 ,11,14,17,20,23]
    
    
    for k in range(0,ndtp-1): 
    
    
        file11.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp.time_sec[k],ndlev,exp.p[0]))
        file22.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp.time_sec[k],ndlev,exp.p[0]))
        file23.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp.time_sec[k],ndlev,exp.p[0]))
    
        Tau         =   d_days.velw_sfc_flx(exp.u[k,0],exp.v[k,0],exp.w[k,0]) 
    
    
        file33.write("%f\t%f\t%f\t%f\t%f\n"%(exp.time_sec[k],exp.T_skin[k],exp.sh[k],exp.lh[k],Tau[0])) 
    
        for i in range(0,ndlev):
    
            file11.write(
            "%f\t%f\t%f\t%f\t%f\t%f\n"%(exp.z[k,i],exp.p[i],exp.theta_inv[k,i],exp.q[k,i],exp.u[k,i],exp.v[k,i])) 
            file22.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(exp.z[k,i],exp.p[i],exp.s_ls[k,i],exp.q_ls[k,i],exp.u[k,i],exp.v[k,i],exp.w[k,i])) 
            file23.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(exp.z[k,i],exp.p[i],exp.t_ls[k,i],exp.q_ls[k,i],exp.u[k,i],exp.v[k,i],exp.w[k,i])) 
    
    file11.close()
    file22.close()
    file23.close()
    file33.close()

def sam_forcing_qmix_old(exp1,exp2,folder,label):
##############################################################################

    file11= open('%s/snd_%s'%(folder,label),  'w+')
    file22= open('%s/lsf_%s_h'%(folder,label),'w+')
    file23= open('%s/lsf_%s_p'%(folder,label),'w+')
    file33= open('%s/sfc_%s'%(folder,label)  ,'w+')
    
    file11.write("z[m]\tp[mb]\ttp[K]\tq[g/kg]\tu[m/s]\tv[m/s]\n")
    file22.write("z[m]\tp[mb]\tsls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
    file23.write("z[m]\tp[mb]\ttls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
    file33.write("day\t\tsst(K)\t\tH(W/m2)\t\tLE(W/m2)\tTAU(m2/s2) \n")
    
    ndtp =len(exp1.time_sec)
    ndlev=len(exp1.lev)

    #NOTE:the forcing was created in local time, MANAUS -4UTC
    ###Manaus time
    ##h =[0,3,6,9,12,15,17,20,23,02]
    #time=[0.0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1.0]
    
    #NOTE:the forcing was created in UTC TIME
    ###UTC time
    ##h =[0 ,3 ,6,9,12,15,18,21,24,3]
    ##to UTC-4
    ##h =[20,23,2,5,8 ,11,14,17,20,23]
    
    
    for k in range(0,ndtp-1): 
    
    
        file11.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp1.time_sec[k],ndlev,exp1.p[0]))
        file22.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp1.time_sec[k],ndlev,exp1.p[0]))
        file23.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp1.time_sec[k],ndlev,exp1.p[0]))
    
        Tau         =   d_days.velw_sfc_flx(exp1.u[k,0],exp1.v[k,0],exp1.w[k,0]) 
    
    
        file33.write("%f\t%f\t%f\t%f\t%f\n"%(exp1.time_sec[k],exp1.T_skin[k],exp1.sh[k],exp1.lh[k],Tau[0])) 
    
        for i in range(0,ndlev):
    
            file11.write(
            "%f\t%f\t%f\t%f\t%f\t%f\n"%(exp1.z[k,i],exp1.p[i],exp1.theta_inv[k,i],exp2.q[k,i],exp1.u[k,i],exp1.v[k,i])) 
            file22.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(exp1.z[k,i],exp1.p[i],exp1.s_ls[k,i],exp1.q_ls[k,i],exp1.u[k,i],exp1.v[k,i],exp1.w[k,i])) 
            file23.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(exp1.z[k,i],exp1.p[i],exp1.t_ls[k,i],exp1.q_ls[k,i],exp1.u[k,i],exp1.v[k,i],exp1.w[k,i])) 
    
    file11.close()
    file22.close()
    file23.close()
    file33.close()

def sam_forcing_exp(exp1,folder,label):

    u        = exp1.u
    v        = exp1.v
    w        = exp1.w
    q        = exp1.q
    q_ls     = exp1.q_ls
    sh       = exp1.sh
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qinitmix(exp1,exp2,folder,label):

##############################################################################
    q        = exp2.q
##############################################################################
    q_ls     = exp1.q_ls
    u        = exp1.u
    v        = exp1.v
    w        = exp1.w
    sh       = exp1.sh
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return
def sam_forcing_tadvmix(exp1,exp2,folder,label):

##############################################################################
    t_ls     = exp2.t_ls
##############################################################################
    q        = exp1.q
    q_ls     = exp1.q_ls
    u        = exp1.u
    v        = exp1.v
    w        = exp1.w
    sh       = exp1.sh
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qadvmix(exp1,exp2,folder,label):

##############################################################################
    q_ls     = exp2.q_ls
##############################################################################
    q        = exp1.q
    u        = exp1.u
    v        = exp1.v
    w        = exp1.w
    sh       = exp1.sh
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return
def sam_forcing_qmix(exp1,exp2,folder,label):

##############################################################################
    q        = exp2.q
    q_ls     = exp2.q_ls
##############################################################################
    u        = exp1.u
    v        = exp1.v
    w        = exp1.w
    sh       = exp1.sh
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qtmix(exp1,exp2,folder,label):

##############################################################################
    q        = exp2.q
    q_ls     = exp2.q_ls
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    w        = exp1.w
    sh       = exp1.sh
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_t_w_3mix(exp1,exp2,exp3,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    w        = exp3.w
##############################################################################
    q        = exp1.q
    q_ls     = exp1.q_ls
    sh       = exp1.sh
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_t_q_3mix(exp1,exp2,exp3,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    q        = exp3.q
    q_ls     = exp3.q_ls
##############################################################################
    sh       = exp1.sh
    lh       = exp1.lh
    w        = exp1.w
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qt_w_3mix(exp1,exp2,exp3,folder,label):

##############################################################################
    q        = exp2.q
    q_ls     = exp2.q_ls
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    w        = exp3.w
##############################################################################
    sh       = exp1.sh
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_t_shf_3mix(exp1,exp2,exp3,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    sh       = exp3.sh
##############################################################################
    q        = exp1.q
    q_ls     = exp1.q_ls
    w        = exp1.w
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qt_shf_3mix(exp1,exp2,exp3,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    q        = exp2.q
    q_ls     = exp2.q_ls
    sh       = exp3.sh
##############################################################################
    w        = exp1.w
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_t_wshf_3mix(exp1,exp2,exp3,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    sh       = exp3.sh
    w        = exp3.w
##############################################################################
    q        = exp1.q
    q_ls     = exp1.q_ls
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qt_wshf_3mix(exp1,exp2,exp3,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    q        = exp2.q
    q_ls     = exp2.q_ls
    sh       = exp3.sh
    w        = exp3.w
##############################################################################
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wqthfuvmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
    lh       = exp2.lh
    q        = exp2.q
    q_ls     = exp2.q_ls
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    u        = exp2.u
    v        = exp2.v
##############################################################################
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wqthfmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
    lh       = exp2.lh
    q        = exp2.q
    q_ls     = exp2.q_ls
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wqhfmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
    lh       = exp2.lh
    q        = exp2.q
    q_ls     = exp2.q_ls
##############################################################################
    u        = exp1.u
    v        = exp1.v
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wtmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    q        = exp1.q
    q_ls     = exp1.q_ls
    sh       = exp1.sh
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qshfmix(exp1,exp2,folder,label):

##############################################################################
    sh       = exp2.sh
    q        = exp2.q
    q_ls     = exp2.q_ls
##############################################################################
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    w        = exp1.w
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wqshfmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
    q        = exp2.q
    q_ls     = exp2.q_ls
##############################################################################
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_shftmix(exp1,exp2,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
    sh       = exp2.sh
##############################################################################
    w        = exp1.w
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    q        = exp1.q
    q_ls     = exp1.q_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_tmix(exp1,exp2,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    w        = exp1.w
    sh       = exp1.sh
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    q        = exp1.q
    q_ls     = exp1.q_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_tinitmix(exp1,exp2,folder,label):

##############################################################################
    theta_inv= exp2.theta_inv
##############################################################################
    w        = exp1.w
    sh       = exp1.sh
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    q        = exp1.q
    t_ls     = exp1.t_ls
    q_ls     = exp1.q_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wshftmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    lh       = exp1.lh
    u        = exp1.u
    v        = exp1.v
    q        = exp1.q
    q_ls     = exp1.q_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_whfmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
    lh       = exp2.lh
##############################################################################
    u        = exp1.u
    v        = exp1.v
    theta_inv= exp1.theta_inv
    q        = exp1.q
    q_ls     = exp1.q_ls
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_halflhf(exp1,exp2,folder,label):

##############################################################################
    lh       = exp1.lh[:]/2.0
##############################################################################
    w        = exp1.w
    u        = exp1.u
    v        = exp1.v
    sh       = exp1.sh
    theta_inv= exp1.theta_inv
    q        = exp1.q
    q_ls     = exp1.q_ls
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

def sam_forcing_wlhfmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    lh       = exp2.lh
##############################################################################
    u        = exp1.u
    v        = exp1.v
    sh       = exp1.sh
    theta_inv= exp1.theta_inv
    q        = exp1.q
    q_ls     = exp1.q_ls
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wshfmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
##############################################################################
    u        = exp1.u
    v        = exp1.v
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    q        = exp1.q
    q_ls     = exp1.q_ls
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
##############################################################################
    u        = exp1.u
    v        = exp1.v
    sh       = exp1.sh
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    q        = exp1.q
    q_ls     = exp1.q_ls
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wqtmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    q        = exp2.q
    q_ls     = exp2.q_ls
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    u        = exp1.u
    v        = exp1.v
    sh       = exp1.sh
    lh       = exp1.lh
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qshftmix(exp1,exp2,folder,label):

##############################################################################
    q        = exp2.q
    q_ls     = exp2.q_ls
    sh       = exp2.sh
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    u        = exp1.u
    v        = exp1.v
    w        = exp1.w
    lh       = exp1.lh
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wshfmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
##############################################################################
    q        = exp1.q
    q_ls     = exp1.q_ls
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    u        = exp1.u
    v        = exp1.v
    lh       = exp1.lh
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wshftmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    sh       = exp2.sh
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    q        = exp1.q
    q_ls     = exp1.q_ls
    u        = exp1.u
    v        = exp1.v
    lh       = exp1.lh
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_qwshftmix(exp1,exp2,folder,label):

##############################################################################
    q        = exp2.q
    q_ls     = exp2.q_ls
    w        = exp2.w
    sh       = exp2.sh
    theta_inv= exp2.theta_inv
    t_ls     = exp2.t_ls
##############################################################################
    u        = exp1.u
    v        = exp1.v
    lh       = exp1.lh
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_wqmix(exp1,exp2,folder,label):

##############################################################################
    w        = exp2.w
    q        = exp2.q
    q_ls     = exp2.q_ls
##############################################################################
    u        = exp1.u
    v        = exp1.v
    sh       = exp1.sh
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_shfmix(exp1,exp2,folder,label):

##############################################################################
    sh       = exp2.sh
##############################################################################
    w        = exp1.w
    q        = exp1.q
    u        = exp1.u
    v        = exp1.v
    lh       = exp1.lh
    theta_inv= exp1.theta_inv
    q_ls     = exp1.q_ls
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_lhfmix(exp1,exp2,folder,label):

##############################################################################
    lh       = exp2.lh
##############################################################################
    w        = exp1.w
    q        = exp1.q
    u        = exp1.u
    v        = exp1.v
    sh       = exp1.sh
    theta_inv= exp1.theta_inv
    q_ls     = exp1.q_ls
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

def sam_forcing_hfmix(exp1,exp2,folder,label):

##############################################################################
    lh       = exp2.lh
    sh       = exp2.sh
##############################################################################
    w        = exp1.w
    q        = exp1.q
    u        = exp1.u
    v        = exp1.v
    theta_inv= exp1.theta_inv
    q_ls     = exp1.q_ls
    t_ls     = exp1.t_ls
    s_ls     = exp1.s_ls

    to_file_sam(exp1,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls)

    return

########################################

def to_file_sam(ex,folder,label,u,v,w,sh,lh,theta_inv,q,q_ls,t_ls,s_ls):

    file11= open('%s/snd_%s'%(folder,label),  'w+')
    file22= open('%s/lsf_%s_h'%(folder,label),'w+')
    file23= open('%s/lsf_%s_p'%(folder,label),'w+')
    file33= open('%s/sfc_%s'%(folder,label)  ,'w+')
    
    file11.write("z[m]\tp[mb]\ttp[K]\tq[g/kg]\tu[m/s]\tv[m/s]\n")
    file22.write("z[m]\tp[mb]\tsls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
    file23.write("z[m]\tp[mb]\ttls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
    file33.write("day\t\tsst(K)\t\tH(W/m2)\t\tLE(W/m2)\tTAU(m2/s2) \n")
    
    ndtp =len(ex.time_sec)
    ndlev=len(ex.lev)

    for k in range(0,ndtp-1): 
    
    
        file11.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(ex.time_sec[k],ndlev,ex.p[0]))
        file22.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(ex.time_sec[k],ndlev,ex.p[0]))
        file23.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(ex.time_sec[k],ndlev,ex.p[0]))


    
        Tau         =   d_days.velw_sfc_flx(u[k,0],v[k,0],w[k,0]) 
    
        file33.write("%f\t%f\t%f\t%f\t%f\n"%(ex.time_sec[k],ex.T_skin[k],sh[k],lh[k],Tau[0])) 
    
        for i in range(0,ndlev):
    
            file11.write("%f\t%f\t%f\t%f\t%f\t%f\n"%(ex.z[k,i],ex.p[i],theta_inv[k,i],q[k,i],u[k,i],v[k,i])) 
            file22.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(ex.z[k,i],ex.p[i],s_ls[k,i],q_ls[k,i],u[k,i],v[k,i],w[k,i])) 
            file23.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(ex.z[k,i],ex.p[i],t_ls[k,i],q_ls[k,i],u[k,i],v[k,i],w[k,i])) 
    
    file11.close()
    file22.close()
    file23.close()
    file33.close()

def sam_forcing_wq(exp1,exp2,folder,label):
##############################################################################

    file11= open('%s/snd_%s'%(folder,label),  'w+')
    file22= open('%s/lsf_%s_h'%(folder,label),'w+')
    file23= open('%s/lsf_%s_p'%(folder,label),'w+')
    file33= open('%s/sfc_%s'%(folder,label)  ,'w+')
    
    file11.write("z[m]\tp[mb]\ttp[K]\tq[g/kg]\tu[m/s]\tv[m/s]\n")
    file22.write("z[m]\tp[mb]\tsls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
    file23.write("z[m]\tp[mb]\ttls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
    file33.write("day\t\tsst(K)\t\tH(W/m2)\t\tLE(W/m2)\tTAU(m2/s2) \n")
    
    ndtp =len(exp1.time_sec)
    ndlev=len(exp1.lev)

    for k in range(0,ndtp-1): 
    
    
        file11.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp1.time_sec[k],ndlev,exp1.p[0]))
        file22.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp1.time_sec[k],ndlev,exp1.p[0]))
        file23.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(exp1.time_sec[k],ndlev,exp1.p[0]))
    
        Tau         =   d_days.velw_sfc_flx(exp2.u[k,0],exp2.v[k,0],exp2.w[k,0]) 
    
    
        file33.write("%f\t%f\t%f\t%f\t%f\n"%(exp1.time_sec[k],exp1.T_skin[k],exp1.sh[k],exp1.lh[k],Tau[0])) 
    
        for i in range(0,ndlev):
    
            file11.write(
            "%f\t%f\t%f\t%f\t%f\t%f\n"%(exp1.z[k,i],exp1.p[i],exp1.theta_inv[k,i],exp2.q[k,i],exp1.u[k,i],exp1.v[k,i])) 
            file22.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(exp1.z[k,i],exp1.p[i],exp1.s_ls[k,i],exp1.q_ls[k,i],exp1.u[k,i],exp2.v[k,i],exp2.w[k,i])) 
            file23.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(exp1.z[k,i],exp1.p[i],exp1.t_ls[k,i],exp1.q_ls[k,i],exp2.u[k,i],exp2.v[k,i],exp2.w[k,i])) 
    
    file11.close()
    file22.close()
    file23.close()
    file33.close()

def scam_forcing(exp):
    ##############################################################################
    
    ## Writing NetCDF files to scam 
    #
    ## Open a new NetCDF file to write the data to. For format, you can choose from
    ## 'NETCDF3_CLASSIC', 'NETCDF3_64BIT', 'NETCDF4_CLASSIC', and 'NETCDF4'
    
    
    nc_out              = Dataset('%s/%s.nc'%(folder,label_nc[0]), 'w', format='NETCDF4')
    nc_out.description  = " FORCING TO REPRESENT A COMPOSITE OF  \
    PURE SHALLOW CONVECTION COLECTED IN THE OBSERTATIONAL CAMPAIGN \
    GOAMAZON THROUGHT THE IOP1 AND IOP2. THE DATA IS REPRESENTED IN THE FIRST DAY OF 2014"
    
    
    nc_out.history = "Created " + today.strftime("%d/%m/%y")
    nc_out.author = "Jhonatan A. A manco"
    
    
    time_nc = nc_out.createVariable('bdate', 'i4',())
    nc_out.variables['bdate'][:] =  20140101 
    
    # we can create the new dimension
    ## Even though we know the size, we are going to set the size to unknown
    nc_out.createDimension('lon', 1)
    nc_out.createDimension('lat', 1)
    
    dtime =len(exp.time_sec)
    dlev=len(lev)
    nc_out.createDimension('lev',dlev )
    nc_out.createDimension('time', dtime)
    
    ##########################################
    #time_nc = nc_out.createVariable('time', 'f4',('time',))
    #
    ### Assign the dimension data to the new NetCDF file.
    #nc_out.variables['time'][:] = time[:]
    
    
    tsec_nc = nc_out.createVariable('tsec', 'f4',('time',))
    tsec_nc.setncatts({'long_name': u"Time in seconds after 0Z on base date",\
                        'units': u"s",\
                        'statistic': u'none'})
    
    
    nc_out.variables['tsec'][:] = time_sec[:]
    
    ##############################
    
    lon_nc = nc_out.createVariable('lon', 'f4', ('lon'))
    lon_nc.setncatts({'long_name': u"Longitude",\
                        'units': u"degrees",\
                        'var_desc': u"Longitude of ARM SITE MANACAPURU AMAZONAS",\
                        'statistic': u'none'})
    
    nc_out.variables['lon'][:] = -60.00
    
    ##############################
    
    lat_nc = nc_out.createVariable('lat', 'f4', ('lat'))
    lat_nc.setncatts({'long_name': u"Latitude",\
                        'units': u"degrees",\
                        'var_desc': u"latidude of ARM SITE MANACAPURU AMAZONAS",\
                        'statistic': u'none'})
    
    nc_out.variables['lat'][:] = -3.15
    
    
    ##############################
    
    p_nc = nc_out.createVariable('lev', 'f4', ('lev',))
    p_nc.setncatts({'long_name': u"Pressure",\
                        'units': u"Pa", 'level_desc': u'Surface',\
                        'var_desc': u"pressure from varanal analysis",\
                        'statistic': u'none'})
    
    nc_out.variables['lev'][:] = pa[::-1]
    
    
    ##############################
    
    sh_nc = nc_out.createVariable('shflx', 'f4', ('time','lat','lon'))
    sh_nc.setncatts({'long_name': u"Surface sensible heat flux",\
                        'units': u"W/m2", 'level_desc': u'Surface',\
                        'var_desc': u"Surface Sensible heat flux from varanal analysis",\
                        'statistic': u'none\nM'})
    
    
    sh_3d=np.zeros([SH_mean.shape[0],1,1])
    
    sh_3d[:,0,0]=SH_mean[:]
    
    
    nc_out.variables['shflx'][:] = sh_3d[:,0,0]
    
    
    ##############################
    lh_nc = nc_out.createVariable('lhflx', 'f4', ('time','lat','lon'))
    lh_nc.setncatts({'long_name': u"Surface latent heat flux",\
                        'units': u"W/m2", 'level_desc': u'Surface',\
                        'var_desc': u"Surface Latent  heat flux from varanal analysis",\
                        'statistic': u'none\nM'})
    #nc_out.variables['lhflx'][:] = LH_mean[:]
    
    lh_3d=np.zeros([LH_mean.shape[0],1,1])
    
    lh_3d[:,0,0]=LH_mean[:]
    
    nc_out.variables['lhflx'][:] = lh_3d[:]
    
    ##############################
    phis_nc = nc_out.createVariable('phis', 'f4', ('lon','lat',))
    phis_nc.setncatts({'long_name': u"Surface geopotential",\
                        'units': u"m2/s2", 'level_desc': u'Surface',\
                        'var_desc': u"Surface geopotential bomex has ",\
                        'statistic': u'none\nM'})
    
    phis_3d=np.zeros([1,1])
    
    phis_3d[0,0]=0.0
    
    nc_out.variables['phis'][:] = phis_3d[:]
    
    ################################
    ustar_nc = nc_out.createVariable('ustar', 'f4', ('time','lat','lon'))
    
    ustar_nc.setncatts({'long_name': u"Surface frictional velocity",\
                        'units': u"m/s",\
                        'var_desc': u"Surface frictional velocity, bomex has",\
                        'statistic': u'none'})
    
    ustar_3d=np.zeros([theta_inv.shape[0],1,1])
    
    #bomex value
    ustar_3d[:,0,0]=0.28
    
    nc_out.variables['ustar'][:] = ustar_3d[:]
    
    
    ##############################
    
    Tg_nc = nc_out.createVariable('Tg', 'f4', ('time','lat','lon'))
    
    Tg_nc.setncatts({'long_name': u"Ground Temperature",\
                        'units': u"K",\
                        'var_desc': u"Ground Temperature from varanal analysis",\
                        'statistic': u'none'})
    
    Tg_3d=np.zeros([theta_inv.shape[0],1,1])
    
    Tg_3d[:,0,0]=T_skin_mean[:]
    
    nc_out.variables['Tg'][:] = Tg_3d[:]
    
    ################################
    ##
    
    Ps_nc = nc_out.createVariable('Ps', 'f4', ('time','lat','lon',))
    
    Ps_nc.setncatts({'long_name': u"Surface pressure",\
                        'units': u"Pa",\
                        'var_desc': u"Surface pressure from varanal analysis",\
                        'statistic': u'none'})
    
    Ps_3d=np.zeros([theta_inv.shape[0],1,1])
    
    Ps_3d[:,0,0]=pa[0]
    
    nc_out.variables['Ps'][:] = Ps_3d[:]
    
    ################################
    ##
    
    Pt_nc = nc_out.createVariable('Ptend', 'f4', ('time','lat','lon',))
    
    Pt_nc.setncatts({'long_name': u"Surface pressure tendency",\
                        'units': u"Pa/s",\
                        'var_desc': u"Surface pressure tendency, bomex has",\
                        'statistic': u'none'})
    
    Pt_3d=np.zeros([theta_inv.shape[0],1,1])
    
    Pt_3d[:,0,0]= 0.0
    
    nc_out.variables['Ptend'][:] = Pt_3d[:]
    
    
    
    ##############################
    
    T_nc = nc_out.createVariable('T', 'f4', ('time','lev','lat','lon'))
    T_nc.setncatts({'long_name': u"Air Temperature",\
                        'units': u"K", 'level_desc': u'Surface',\
                        'var_desc': u"Air Temperature from varanal analysis",\
                        'statistic': u'none\nM'})
    
    theta_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])
    
    #theta_4d[:,:,0,0]=theta[:,:]
    theta_4d[:,:,0,0]=T_mean[:,::-1]
    
    nc_out.variables['T'][:] = theta_4d[:]
    
    ##############################
    q_nc = nc_out.createVariable('q', 'f4', ('time','lev','lat','lon'))
    q_nc.setncatts({'long_name': u"Water vapor mixing ratio",\
                        'units': u"kg/kg", 'level_desc': u'Surface',\
                        'var_desc': u"Water vapor mixin ratio from varanal analysis",\
                        'statistic': u'none\nM'})
    
    q_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])
    
    q_4d[:,:,0,0]=q[:,::-1]
    
    nc_out.variables['q'][:] = q_4d[:]
    
    ##############################
    
    u_nc = nc_out.createVariable('u', 'f4', ('time','lev','lat','lon'))
    u_nc.setncatts({'long_name': u"u wind velocity ",\
                        'units': u"m/s", 'level_desc': u'Surface',\
                        'var_desc': u"u zonal  wind velocity  from varanal analysis",\
                        'statistic': u'none\nM'})
    
    u_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])
    
    u_4d[:,:,0,0]=u[:,::-1]
    
    nc_out.variables['u'][:] = u_4d[:]
    
    ##############################
    
    v_nc = nc_out.createVariable('v', 'f4', ('time','lev','lat','lon'))
    v_nc.setncatts({'long_name': u"v wind velocity ",\
                        'units': u"m/s", 'level_desc': u'Surface',\
                        'var_desc': u"v meridional  wind velocity  from varanal analysis",\
                        'statistic': u'none\nM'})
    
    v_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])
    
    v_4d[:,:,0,0]=v[:,::-1]
    
    nc_out.variables['v'][:] = v_4d[:]
    
    ##############################
    
    o_nc = nc_out.createVariable('omega', 'f4', ('time','lev','lat','lon'))
    o_nc.setncatts({'long_name': u"omega",\
                        'units': u"Pa/s", 'level_desc': u'Surface',\
                        'var_desc': u" vertical pressure velocity  from varanal analysis",\
                        'statistic': u'none\nM'})
    
    o_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])
    
    o_4d[:,:,0,0]=omega_mean[:,::-1]
    
    nc_out.variables['omega'][:] = o_4d[:]
    
    ##############################
    
    tls_nc = nc_out.createVariable('divT', 'f4', ('time','lev','lat','lon'))
    tls_nc.setncatts({'long_name': u"Large scale temperature forcing",\
                          'units': u"K/s", 'level_desc': u'Surface',\
                          'var_desc': u" Large scale temperature forcing from varanal analysis",\
                          'statistic': u'none\nM'})
       
    tls_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])
    
    tls_4d[:,:,0,0]=t_ls[:,::-1]
    
    nc_out.variables['divT'][:] = tls_4d[:]
    
    ##############################
    
    qls_nc = nc_out.createVariable('divq', 'f4', ('time','lev','lat','lon'))
    qls_nc.setncatts({'long_name': u" Large scale water vapor mixing ratio forcing",\
                          'units': u"kg/kg/s", 'level_desc': u'Surface',\
                          'var_desc': u" Large scale water vapor mixing ratio forcing from varanal analysis",\
                          'statistic': u'none\nM'})
       
    qls_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])
    
    qls_4d[:,:,0,0]=q_ls[:,::-1]
    
    nc_out.variables['divq'][:] = qls_4d[:]
    
    ##############################
    
    
    
    nc_out.close()  # close the new file
    print('Files were created' )
    print('lsf_%s'%(explabel[0]) )
    print('snd_%s'%(explabel[0]) )
    print('sfd_%s'%(explabel[0]) )
    print('%s.nc'%(explabel[0]) )
    
    
    ################################3
    
    
    #Initial day
    idi = dt.datetime(2022, 1, 1, 6)
    idf = dt.datetime(2022, 1, 1, 19)
    
    
    #time of the composite day 
    time=time_sec
    lev = exp[0].lev[::-1]
    
    
    #data= down.data_to_reference(data,exp[0].tsec[:])
    data= down.data_to_reference(data,time[:])
    
    ni,nf=down.data_n(idi,idf,data)
    
    ################################
    #fig   = plt.figure()
    #ax   = plt.axes()
    #
    #color = 'black'
    #ax.set_xlabel(r'hour(UTC-4)', color=color)
    ##ax.set_ylabel('z [km]')
    #plt.ylabel(r'') 
    #
    #color = 'black'
    #
    #ax.axis([idi,idf,0,400])
    #
    ##-4 MANAUS LOCAL TIME
    #ax.plot(data,SH_mean, color=color)
    #
    #ax.legend(frameon=False,loc='upper right')
    
    #plt.savefig('%s/forcing_shf.pdf'%file_out, format='pdf',bbox_inches='tight' , dpi=1000)
    
    
    hp        =   [6]
    
    #used user parameter to plot(plotparameter.py
    ###########################################3
    
    size_wg = 0.20
    size_hf = 1.50
    
    
    #plotsize(size_wg,size_hf, 1.0,'diurnal')
    plotsize(size_wg,size_hf, 0.0,'diurnal')
    
    fig   = plt.figure()
    ax1   = plt.axes()
    
    color = 'tab:red'
    color2 = 'tab:green'
    #ax1.set_xlabel(r'$\mathrm{\theta_{inv}\ [K]}$', color=color)
    ax1.set_ylabel('z [km]')
    
    ax2 = ax1.twiny()  # instantiate a second axes that shares the same x-axis
    #color = 'tab:blue'
    #ax2.set_xlabel(r'q [g/kg]', color=color)
    
    ax1.axis([296,320,0,5])
    ax2.axis([3,18.0,0,5])
    
    #fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    
    for k in range(0,len(time)): 
    
            for i in range(0,len(hp)): 
    
                if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 
    
                    line,color=h_color.color_hours(hp[i])
    
                    #-4 MANAUS LOCAL TIME,it is in the reference time, ffrom 2021,12,31,20 horas
                    ax1.plot(theta_inv[k,:], z[k,:]/1000.0,color=color,label='%d'%(hp[i]),dashes=line)
    
                    ax2.plot(q[k,:]*1000.0, z[k,:]/1000.0,color=color,dashes=line)
    
    #ax1.legend(frameon=False,loc='center right')
    ax1.text(302, 4.5, r'a)$\mathrm{\theta}$&q', fontsize=6, color='black')
    
    
    plt.savefig('%s/forcing_mean_tq.pdf'%file_out,format='pdf',bbox_inches='tight' , dpi=1000)
    
    
    hp        =   [6,9,12,15,18]
    
    ################################################################3
    
    #plotsize(size_wg,size_hf, 1.0,'diurnal')
    #plotsize(size_wg,size_hf, 0.0,'diurnal')
    
    fig   = plt.figure()
    ax   = plt.axes()
    
    #ax.legend(frameon=False)
    
    ax.axis([-12,5,0,5])
    
    ax.text(-11.8, 3, r'u $\rightarrow$ ')
    ax.text( 1, 3, r'$\leftarrow$ v')
    
    #plt.ylabel(r'z [km]') 
    plt.ylabel(r'') 
    #plt.xlabel(r' $\mathrm{ [ms^{-1}]}$ ') 
    
    
    for k in range(0,len(time)): 
    
            for i in range(0,len(hp)): 
    
                if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 
    
                    line,color=h_color.color_hours(hp[i])
    
                    #-4 MANAUS LOCAL TIME
                    ax.plot(u[k,:] ,z[k,:]/1000.0,label='%d'%(hp[i]),dashes=line,color=color)
                    ax.plot(v[k,:] ,z[k,:]/1000.0,dashes=line,color=color)
    
    #ax.legend(frameon=False,loc='lower right')
    #ax1.legend(frameon=False,loc='center right')
    ax.text(-11, 4.5, r'b)', fontsize=6, color='black')
    
    
    plt.savefig('%s/forcing_mean_uv.pdf'%file_out, bbox_inches='tight' ,format='pdf', dpi=1000)
    
    
    ############################################################
    
    fig   = plt.figure()
    ax    = plt.axes()
    
    #ax.legend(frameon=False)
    
    ax.axis([-0.70,0.30,0,5])
    
    #plt.ylabel(r'z [km]') 
    #plt.xlabel(r'w  $\mathrm{ [cms^{-1}]}$ ') 
    plt.ylabel(r'') 
    
    for k in range(0,len(time)): 
    
            for i in range(0,len(hp)): 
    
                if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 
    
                    line,color=h_color.color_hours(hp[i])
    
                    #-4 MANAUS LOCAL TIME
                    ax.plot(w[k,:]*100.0 ,z[k,:]/1000.0,label='%d'%(hp[i]),dashes=line,color=color)
    
    #ax.legend(frameon=False,loc='lower right')
    ax.text(-0.65, 4.5, r'c)w', fontsize=6, color='black')
    
    plt.savefig('%s/forcing_mean_w.pdf'%file_out, bbox_inches='tight' ,format='pdf', dpi=1000)
    ############################################################
    
    
    
    ################################
    fig   = plt.figure()
    ax   = plt.axes()
    
    color = 'black'
    ax.set_ylabel('')
    #ax.set_xlabel(r'$\mathrm{\theta_{ls}\ [Ks^{-1}]}$', color=color)
    #ax.set_ylabel('z [km]')
    
    ax.axis([-3e-5, 1.5e-5,0,5])
    ax.xaxis.set_major_locator(ticker.LinearLocator(3))
    
    #fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    plt.ylabel(r'') 
    #plt.xlabel(r'$\mathrm{ \theta_{ls}[Ks^{-1}]}$ ') 
    
    
    ##to plot with scientific notation 
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    
    for k in range(0,len(time)): 
    
            for i in range(0,len(hp)): 
    
                if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 
    
                    line,color=h_color.color_hours(hp[i])
    
                    #-4 MANAUS LOCAL TIME
                    ax.plot(t_ls[k,:] ,z[k,:]/1000.0,dashes=line,color=color)
    
    
    #ax.legend(frameon=False,loc='lower right')
    #ax.text(-2.9e-5, 4.5, r'd)$\mathrm{\theta_{ls}x10^{-5}}$', fontsize=6, color='black')
    ax.text(-2.9e-5, 4.5, r'd)$\mathrm{\theta_{ls}}$', fontsize=6, color='black')
    ax.xaxis.get_offset_text().set_visible(False)
    
    plt.savefig('%s/forcing_mean_tls.pdf'%file_out, format='pdf',bbox_inches='tight' , dpi=1000)
    
    ################################
    fig   = plt.figure()
    ax   = plt.axes()
    
    color = 'black'
    #ax.set_xlabel(r'$\mathrm{q_{ls} [g kg^{-1} s^{-1}]}$', color=color)
    #ax.set_ylabel('z [km]')
    plt.ylabel(r'') 
    
    color = 'black'
    
    ax.axis([-2.50e-8,1.5e-8,0,5])
    
    ax.xaxis.set_major_locator(ticker.LinearLocator(3))
    
    #plt.tight_layout()  # otherwise the right y-label is slightly clipped
    ##to plot with scientific notation 
    #ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    
    #ax.xaxis.set_minor_locator(locatormin)
    
    for k in range(0,len(time)): 
    
            for i in range(0,len(hp)): 
    
                if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 
    
                    line,color=h_color.color_hours(hp[i])
    
                    #-4 MANAUS LOCAL TIME
                    ax.plot(q_ls[k,:] ,z[k,:]/1000.0,label='%d'%(hp[i]),dashes=line,color=color)
    
    ax.legend(frameon=False,loc='upper right')
    
    #ax.text(-2.5e-8, 4.5, r'e)$\mathrm{q_{ls}x10^{-8}}$', fontsize=6, color='black')
    ax.text(-2.5e-8, 4.5, r'e)$\mathrm{q_{ls}}$', fontsize=6, color='black')
    #ax.xaxis.get_offset_text().set_fontsize(10)
    #ax.xaxis.set_offset_position('right')
    ax.xaxis.get_offset_text().set_visible(False)
    #ax.text( 1.8e-8, -0.1, '1e-8', fontsize=6)
    
    
    plt.savefig('%s/forcing_mean_qls.pdf'%file_out, format='pdf',bbox_inches='tight' , dpi=1000)
    
    
