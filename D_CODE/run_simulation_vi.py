import sys
from pathlib import Path
parent_dir = Path('..').resolve() 
sys.path.append(str(parent_dir)) 

import sympy
import argparse
import numpy as np
import pickle
import os
import time

from . import equations
from . import data
from .gp_utils import run_gp_ode
from .interpolate import get_ode_data



def run(ode_name, ode_param, x_id, freq, n_sample, noise_ratio, seed, n_seed, T0=0, T=15, idx=0):

    '''
    run D-CODE and return the building blocks 
    RMK. questa versione funziona per un unico seed, per estenderla bisogna allargare la libreria
    candidata ad ogni seed, controllando però di non inserire doppioni tramite una funzione ausiliaria
    tipo get_building_blocks(est_gp, ode)
    '''
    
    np.random.seed(999)

    # specify ODE:
    ode = equations.get_ode(ode_name, ode_param)
    # T = ode.T 
    init_low = ode.init_low
    init_high = ode.init_high
    noise_sigma = ode.std_base * noise_ratio
    # print('ODE specified: ', ode_name)

    # data simulation: 
    dg = data.DataGenerator(ode, T, freq, n_sample, noise_sigma, init_low, init_high) 
    yt = dg.generate_data() # dimensions: (41, 50, 1)
    if T0: # if T0>0, cut portion [0,T0] 
        yt = yt[int(T0*freq):, :, :]
    # print('Data generated')
    # print('Dataset shape before smoothing: ', np.shape(yt))

    # import matplotlib.pyplot as plt
    # t = np.arange(yt.shape[0])  # asse temporale (se non ne hai uno definito)
    # plt.figure(figsize=(8, 4))
    # for i in range(yt.shape[1]):  # loop sulle 50 traiettorie
    #     plt.plot(t, yt[:, i, x_id], alpha=0.5)  # prima dimensione (indice 0)

    # plt.title("Traiettorie della prima dimensione")
    # plt.xlabel("time step")
    # plt.ylabel("x₁(t)")
    # plt.grid(True, linestyle='--', alpha=0.3)
    # plt.tight_layout()
    # plt.show()

    t0 = time.time() # - Time beginning

    # smooth data with Gaussian Process regression:
    ode_data, X_ph, y_ph, t_new = get_ode_data(yt, x_id, dg, ode, T0=T0)
    print('Dataset shape: ', np.shape(ode_data['x_hat']))
    # print(ode_data['x_hat'][0:40, 0, 0]) # print first trajectory id_x = 0
    # print(ode_data['x_hat'][0:40, 0, 1]) # print second trajectory id_x = 1
    # print(ode_data['x_hat'][0:40, 0, 2]) # print third trajectory id_x = 2

    # import matplotlib.pyplot as plt
    # t = np.arange(ode_data['x_hat'].shape[0])  # asse temporale (se non ne hai uno definito)
    # plt.figure(figsize=(8, 4))
    # for i in range(ode_data['x_hat'].shape[1]):  # loop sulle 50 traiettorie
    #     plt.plot(t, ode_data['x_hat'][:, i, x_id], alpha=0.5)  # prima dimensione (indice 0)

    # plt.title("Traiettorie della prima dimensione")
    # plt.xlabel("time step")
    # plt.ylabel("x₁(t)")
    # plt.grid(True, linestyle='--', alpha=0.3)
    # plt.tight_layout()
    # plt.show()


    # run D-CODE:
    for s in range(seed, seed+n_seed): 

        # find the ODE f:
        f_hat, est_gp, building_blocks_lambda, function_names = run_gp_ode(ode_data, X_ph, y_ph, ode, x_id, s)

    t1 = time.time() # - Time end
    print("Total exectution time: ", t1-t0) # - Time print

    return building_blocks_lambda, function_names 



def run_HD(ode_name, ode_param, x_id, freq, n_sample, noise_ratio, seed, n_seed, T0=0, T=15, latent_data=None):

    '''
    High Dimensional version
    '''
    
    np.random.seed(999)

    # specify ODE:
    ode = equations.get_ode(ode_name, ode_param)
    init_low = ode.init_low
    init_high = ode.init_high
    noise_sigma = ode.std_base * noise_ratio

    # Necessario per avere buone performace D-CODE a livello latente non necessariamente la ode è positiva
    # ode.positive = False
    # NOTE: se aggiusti a mano spazio latente commentare questa riga

    # data simulation: 
    dg = data.DataGenerator(ode, T, freq, n_sample, noise_sigma, init_low, init_high)
    #yt = dg.generate_data()
    #print(np.shape(yt))


    # al posto dei dati simulati, usiamo i dati ricostruiti dall'AE
    yt = latent_data
    # print(np.shape(yt))


    # import matplotlib.pyplot as plt
    # t = np.arange(latent_data.shape[0])  # asse temporale (se non ne hai uno definito)
    # plt.figure(figsize=(8, 4))
    # for i in range(latent_data.shape[1]):  # loop sulle 50 traiettorie
    #     plt.plot(t, latent_data[:, i, 0], alpha=0.5)  # prima dimensione (indice 0)

    # plt.title("Traiettorie vere della prima dimensione")
    # plt.xlabel("time step")
    # plt.ylabel("z1(t)")
    # plt.grid(True, linestyle='--', alpha=0.3)
    # plt.tight_layout()
    # plt.show()

    # plt.figure(figsize=(8, 4))
    # for i in range(latent_data.shape[1]):  # loop sulle 50 traiettorie
    #     plt.plot(t, latent_data[:, i, 1], alpha=0.5)  # prima dimensione (indice 0)

    # plt.title("Traiettorie vere della seconda dimensione")
    # plt.xlabel("time step")
    # plt.ylabel("z2(t)")
    # plt.grid(True, linestyle='--', alpha=0.3)
    # plt.tight_layout()
    # plt.show()

    

    if T0: # if T0>0, cut portion [0,T0] 
        yt = yt[int(T0*freq):, :, :]


    # smooth data:
    ode_data, X_ph, y_ph, t_new = get_ode_data(yt, x_id, dg, ode, T0=T0)
    print('Dataset shape: ', np.shape(ode_data['x_hat']))
    # print(ode_data['x_hat'][0:20, 0, 0]) # print first trajectory
    # print(ode_data['g']) # shape (300, 50)
    # print(ode_data['c']) # shape (1, 50)
    # print(ode_data['weights']) # shape (300,)

    # print("x_hat contains NaN:", np.isnan(ode_data['x_hat']).any())
    # print("g contains NaN:", np.isnan(ode_data['g']).any())
    # print("c contains NaN:", np.isnan(ode_data['c']).any())
    # print("weights contains NaN:", np.isnan(ode_data['weights']).any())

    
    # Plot command
    # import matplotlib.pyplot as plt
    # t = np.arange(ode_data['x_hat'].shape[0])  # asse temporale (se non ne hai uno definito)
    # plt.figure(figsize=(8, 4))
    # for i in range(ode_data['x_hat'].shape[1]):  # loop sulle 50 traiettorie
    #     plt.plot(t, ode_data['x_hat'][:, i, 0], alpha=0.5)  # prima dimensione (indice 0)

    # plt.title("Traiettorie della prima dimensione")
    # plt.xlabel("time step")
    # plt.ylabel("z1(t)")
    # plt.grid(True, linestyle='--', alpha=0.3)
    # plt.tight_layout()
    # plt.show()

    # plt.figure(figsize=(8, 4))
    # for i in range(ode_data['x_hat'].shape[1]):  # loop sulle 50 traiettorie
    #     plt.plot(t, ode_data['x_hat'][:, i, 1], alpha=0.5)  # prima dimensione (indice 0)

    # plt.title("Traiettorie della seconda dimensione")
    # plt.xlabel("time step")
    # plt.ylabel("z2(t)")
    # plt.grid(True, linestyle='--', alpha=0.3)
    # plt.tight_layout()
    # plt.show()


    # run D-CODE:
    for s in range(seed, seed+n_seed): 

        # find the ODE f:
        f_hat, est_gp, building_blocks_lambda, function_names = run_gp_ode(ode_data, X_ph, y_ph, ode, x_id, s)

    
    return building_blocks_lambda, function_names 




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ode_name", help="name of the ode", type=str)
    parser.add_argument("--ode_param", help="parameters of the ode (default: None)", type=str, default=None)
    parser.add_argument("--x_id", help="ID of the equation to be learned", type=int, default=0)
    parser.add_argument("--freq", help="sampling frequency", type=float, default=10)
    parser.add_argument("--n_sample", help="number of trajectories", type=int, default=100)
    parser.add_argument("--noise_sigma", help="noise level (default 0)", type=float, default=0.)
    parser.add_argument("--seed", help="random seed", type=int, default=0)
    parser.add_argument("--n_seed", help="random seed", type=int, default=10)

    args = parser.parse_args()
    print('Running with: ', args)

    if args.ode_param is not None:
        param = [float(x) for x in args.ode_param.split(',')]
    else:
        param = None
    if args.freq >= 1:
        freq = int(args.freq)
    else:
        freq = args.freq
    run(args.ode_name, param, args.x_id, freq, args.n_sample, args.noise_sigma, seed=args.seed, n_seed=args.n_seed)
