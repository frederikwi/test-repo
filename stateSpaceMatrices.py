##############################################
# Matricerne fra State-space model
##############################################


import numpy as np

def inputMatrixA(Omega_m,Gamma_m,kappa,g):
    return np.array([
        [-Gamma_m,Omega_m,0,0],
        [-Omega_m,-Gamma_m,-2*g,0],
        [0,0,-kappa/2,0],
        [-2*g,0,0,-kappa/2],
    ])

def inputMatrixB(kappa_in):
    return np.array([
        [0,0],
        [0,0],
        [np.sqrt(kappa_in),0],
        [0,np.sqrt(kappa_in)]
    ])

def inputMatrixC(theta,eta,kappa_out):
    return np.sqrt(2*eta*kappa_out)*np.array(
        [0,0,np.cos(theta),np.sin(theta)]
    )


def inputmatrixD(Gamma_m,kappa,nbar):
    return np.array([
        [2*Gamma_m*(nbar+0.5),0,0,0],
        [0,2*Gamma_m*(nbar+0.5),0,0],
        [0,0,kappa/2,0],
        [0,0,0,kappa/2]
    ])

def inputmatrixE(Gamma_m,kappa,nbar):
    return np.sqrt(inputmatrixD(Gamma_m,kappa,nbar))

def inputmatrixGamma(theta,eta,kappa_out):
    return np.sqrt(eta*kappa_out/2)*np.array(
        [0,0,-np.cos(theta),-np.sin(theta)]
    )