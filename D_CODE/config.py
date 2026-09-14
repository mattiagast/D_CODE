from . import basis


def get_config_real(x_id=0):
    return real_config


def get_config(ode, x_id=0):
    if ode.name == 'GompertzODE':
        if ode.has_coef:
            return gompertz_config
        else:
            return gompertz_config_no_coef
    elif ode.name == 'GompertzODE_par_a':
        return gompertz_par_a_config
    elif ode.name == 'GompertzODE_par_b':
        return gompertz_par_b_config
    elif ode.name == 'GompertzODE_par_ab':
        return gompertz_par_ab_config
    elif ode.name == 'LogisticODE' or ode.name == 'LogisticODE_a':
        return logistic_config
    elif ode.name == 'LogisticODE_k':
        return logistic_config_k
    elif ode.name == 'SelkovODE' or ode.name == 'SelkovODE_rho' or ode.name == 'SelkovODE_sigma' or ode.name == 'SelkovODE_rho_03' or ode.name == 'SelkovODE_rho_04' or ode.name == 'SelkovODE_rho_06' or ode.name == 'SelkovODE_rho_09':
        return selkov_config
    elif ode.name == 'OscillatingSelkovODE' or ode.name == 'OscillatingSelkovODE_d':
        return oscillating_selkov_config
    elif ode.name == 'OscillatingLogisticODE':
        return oscillating_logistic_config
    elif ode.name == 'HillODE':
        return hill_config
    elif ode.name == 'HillODE_par_k':
        return hill_par_k_config
    elif ode.name == 'FracODE' or ode.name == 'FracODE_par_rho':
        return frac_config
    elif ode.name == 'TrigonometricODE':
        return trigonometric_config
    elif ode.name == 'Lorenz' or ode.name == 'Lorenz_sigma' or ode.name == 'Lorenz_rho' or ode.name == 'Lorenz_beta': 
        if x_id == 0:
            return lorenz_config_x0
        elif x_id == 1:
            print('loading config for X1')
            return lorenz_config_x1
        else:
            print('loading config for X2')
            return lorenz_config_x2
    elif ode.name == 'VdpODE':
        if x_id == 0:
            return vdp_config_x0
        elif x_id == 1:
            print('loading config for X1')
            return vdp_config_x1
    elif ode.name == 'OscilVdpODE':
        return oscilvdp_config
    elif ode.name == 'OscilVdpODE_par_w':
        return oscilvdp_par_w_config
    elif ode.name == 'TVLvODE' or ode.name == 'LvODE' or ode.name == 'TVLvODE2' or ode.name == 'TVLvODE2_d':
        return tvlv_config
    elif ode.name == 'TVSelkovODE':
        return tvselkov_config
    elif ode.name == 'TVVdpODE':
        return tvvdp_config
    elif ode.name == 'TVVdpODE2':
        return tvvdp2_config
    elif ode.name == 'ReactionDiffusion':
        return rd_config
    elif ode.name == 'DoubleGyre':
        return doublegyre_config


def get_interpolation_config(ode, x_id=0):
    if ode.name == 'GompertzODE':
        return gompertz_interp_config
    elif ode.name == 'GompertzODE_par_a':
        return gompertz_interp_config
    elif ode.name == 'GompertzODE_par_b':
        return gompertz_interp_config
    elif ode.name == 'GompertzODE_par_ab':
        return gompertz_interp_config
    elif ode.name == 'Lorenz' or ode.name == 'Lorenz_sigma' or ode.name == 'Lorenz_rho' or ode.name == 'Lorenz_beta':
        if x_id == 0:
            return lorenz_interp_config
        else:
            return lorenz_interp_config2
    elif ode.name == 'LogisticODE' or ode.name == 'LogisticODE_a' or ode.name == 'LogisticODE_k':
        return logistic_interp_config
    elif ode.name == 'OscillatingLogisticODE':
        return oscillating_logistic_interp_config
    elif ode.name == 'SelkovODE' or ode.name == 'SelkovODE_rho' or ode.name == 'SelkovODE_sigma' or ode.name == 'SelkovODE_rho_03' or ode.name == 'SelkovODE_rho_04' or ode.name == 'SelkovODE_rho_06' or ode.name == 'SelkovODE_rho_09' or ode.name == 'OscillatingSelkovODE' or ode.name == 'OscillatingSelkovODE_d':
        return selkov_interp_config
    elif ode.name == 'real':
        return real_interp_config
    elif ode.name == 'HillODE':
        return hill_interp_config
    elif ode.name == 'HillODE_par_k':
        return hill_par_k_interp_config
    elif ode.name == 'FracODE' or ode.name == 'FracODE_par_rho':
        return frac_interp_config
    elif ode.name == 'TrigonometricODE':
        return trigonometric_interp_config
    elif ode.name == 'VdpODE':
        if x_id == 0:
            return vdp_interp_config
        else:
            return vdp_interp_config2
    elif ode.name == 'OscilVdpODE':
        return oscilvdp_interp_config
    elif ode.name == 'OscilVdpODE_par_w':
        return oscilvdp_par_w_interp_config
    elif ode.name == 'OscilVdpODE_par_w_mu':
        return oscilvdp_par_w_mu_interp_config
    elif ode.name == 'OscilVdpODE_par_w_a':
        return oscilvdp_par_w_a_interp_config
    elif ode.name == 'TVLvODE' or ode.name == 'LvODE' or ode.name == 'TVLvODE2' or ode.name == 'TVLvODE2_d':
        return tvlv_interp_config
    elif ode.name == 'TVSelkovODE':
        return tvlv_interp_config
    elif ode.name == 'TVVdpODE':
        return tvvdp_interp_config
    elif ode.name == 'TVVdpODE2':
        return tvvdp2_interp_config
    elif ode.name == 'ReactionDiffusion':
        return rd_interp_config
    elif ode.name == 'DoubleGyre':
        return doublegyre_interp_config
    else:
        raise ValueError
    

gompertz_interp_config = {
    'r': 2,
    'sigma_in_mul': 2.,
    'freq_int': 20,
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

real_interp_config = {
    'r': 4,
    'sigma_in': 0.15,
    'freq_int': 365*2,
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

logistic_interp_config = {
    'r': 3,
    'sigma_in_mul': 2.,
    'freq_int': 20,
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

oscillating_logistic_interp_config = {
    'r': 3,
    'sigma_in_mul': 2.,
    'freq_int': 30, # 20 # 40
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

lorenz_interp_config = {
    'r': -1,
    'sigma_in_mul': 2.,
    'freq_int': 100,
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

lorenz_interp_config2 = {
    'r': -1,
    'sigma_in': 0.1,
    'freq_int': 100,
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

selkov_interp_config = {
    'r': 2,
    'sigma_in': 0.2,
    'freq_int': 30, # 20 # TODO
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

hill_interp_config = {
    'r': 3,
    'sigma_in_mul': 2.,
    'freq_int': 20,
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

hill_par_k_interp_config = {
    'r': 3,
    'sigma_in_mul': 2.,
    'freq_int': 20,
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

frac_interp_config = {
    'r': 2,
    'sigma_in': 0.2,
    'freq_int': 10,
    'new_sample': 5,
    'n_basis': 20,
    'basis': basis.CubicSplineBasis,
}

trigonometric_interp_config = {
    'r': 2,
    'sigma_in_mul': 2.,
    'freq_int': 20,
    'new_sample': 5,
    'n_basis': 50,
    'basis': basis.FourierBasis,
}

vdp_interp_config = {
    'r': 2,                       
    'sigma_in': 0.1,               
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,               
    'basis': basis.FourierBasis,   
}

vdp_interp_config2 = {
    'r': 2,                       
    'sigma_in': 2.,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.FourierBasis,   
}

oscilvdp_interp_config = {
    'r': 7,                       
    'sigma_in': 0.2,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.FourierBasis,   
}

oscilvdp_par_w_interp_config = {
    'r': 7,                       
    'sigma_in': 0.2,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.CubicSplineBasis,   
}

oscilvdp_par_w_mu_interp_config = {
    'r': 7,                       
    'sigma_in': 0.2,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.CubicSplineBasis,   
}

oscilvdp_par_w_a_interp_config = {
    'r': 7,                       
    'sigma_in': 0.2,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.CubicSplineBasis,   
}

tvlv_interp_config = {
    'r': 2,                       
    'sigma_in': 0.1,              
    'freq_int': 10, # 20, # NOTE: Diminuito per evitare l'overfitting all'aumento del rumore              
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.FourierBasis,   
}

tvselkov_interp_config = {
    'r': 2,                       
    'sigma_in': 2.,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.FourierBasis,   
}

tvvdp_interp_config = {
    'r': 4,                       
    'sigma_in': 0.1,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.FourierBasis,   
}

tvvdp2_interp_config = {
    'r': 6,                       
    'sigma_in': 0.2,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.FourierBasis,   
}


# HD interpolation configurations:
rd_interp_config = {
    'r': 4,                       
    'sigma_in': 0.5,              
    'freq_int': 10,               
    'new_sample': 5,               
    'n_basis': 20,                
    'basis': basis.FourierBasis,   
}

doublegyre_interp_config = {
    'r': 4,                       
    'sigma_in': 0.2,              
    'freq_int': 20,               
    'new_sample': 5,               
    'n_basis': 50,                
    'basis': basis.FourierBasis,   
}



gompertz_config = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   # 'function_set': {'neg': 1, 'mul': 3, 'log': 1, 'add': 1}, # original function set
                   # 'function_set': {'neg': 1, 'mul': 1, 'log': 1, 'add': 1, 'sub': 1, 'div': 1, 'pow': 1, 'sin': 1, 'cos': 1},
                   'function_set': {'add': 1, 'mul': 1, 'sub': 1, 'neg': 1, 'log': 1}, # HD configuration
                   'const_range': (1, 2),
                   #'generations': 20, # original number of generations
                   'generations': 6,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

gompertz_par_a_config = {'population_size': 30000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'neg': 1, 'mul': 3, 'log': 1, 'add': 1},
                   'const_range': (1, 2),
                   'generations': 20,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

gompertz_par_b_config = {'population_size': 30000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'neg': 1, 'mul': 1, 'log': 1, 'add': 1, 'sub': 1, 'div': 1, 'pow': 1, 'sin': 1, 'cos': 1},
                   'const_range': (1, 2),
                   'generations': 6, 
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

gompertz_par_ab_config = {'population_size': 30000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'neg': 1, 'mul': 1, 'log': 1, 'add': 1, 'sub': 1, 'div': 1, 'pow': 1, 'sin': 1, 'cos': 1},
                   'const_range': (1, 2),
                   'generations': 6,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

real_config = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'neg': 1, 'mul': 3, 'log': 1, 'add': 1},
                   'const_range': (0, 10),
                   'generations': 20,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

logistic_config = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   #'function_set': {'sub': 1, 'mul': 1, 'pow': 1, 'add': 1},
                   #'function_set': {'sub': 1, 'mul': 1, 'pow': 1, 'add': 1, 'neg': 1, 'div': 1, 'log': 1, 'sin': 1, 'cos': 1}, # corretta
                   'function_set': {'sub': 1, 'mul': 1, 'pow': 1, 'add': 1, 'neg': 1, 'div': 1, 'log': 1}, # dev, per oscillating prima parte
                   'const_range': (1., 2.),
                   #'generations': 20,
                   'generations': 6,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

logistic_config_k = {'population_size': 20000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'sub': 1, 'mul': 1, 'pow': 1, 'add': 1, 'neg': 1, 'div': 1, 'log': 1, 'sin': 1, 'cos': 1},
                   'const_range': (1., 2.),
                   'generations': 6,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }


selkov_config = {'population_size': 30000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   #'function_set': {'sub': 1, 'mul': 1, 'add': 1}, # original function set
                   'function_set': {'neg': 1, 'mul': 1, 'log': 1, 'add': 1, 'sub': 1, 'div': 1, 'pow': 1, 'sin': 1, 'cos': 1}, 
                   'const_range': (0.01, 1.), # the range of constants to include in the formulas -> we specify a unique range for all constants 
                   'generations': 20, # original number of generations
                   #'generations': 6,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01, # 0.001
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

oscillating_selkov_config = {'population_size': 30000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   #'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'pow': 1}, 
                   'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'pow': 1, 'log': 1}, 
                   'const_range': (0.01, 4.), # x oscillating 
                   'generations': 6,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

lorenz_config_x0 = {'population_size': 20000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'sub': 1, 'mul': 3, 'add': 1},
                   'const_range': (5, 15),
                   'generations': 20,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

lorenz_config_x1 = {'population_size': 20000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'sub': 1, 'mul': 3, 'add': 1},
                   'const_range': (25, 30),
                   'generations': 20,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

lorenz_config_x2 = {'population_size': 20000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'sub': 1, 'mul': 3, 'add': 1},
                   'const_range': (1.1, 5),
                   'generations': 20,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

# dev: 
oscillating_logistic_config = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   #'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'pow': 1, 'log': 1},
                   'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'pow': 1},
                   #'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1},  
                   'const_range': (0.1, 7.), # !!!
                   #'generations': 20,
                   'generations': 11,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

gompertz_config_no_coef = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set': {'neg': 1, 'mul': 3, 'log': 1, 'add': 1},
                   'const_range': None,
                   'generations': 20,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }


hill_config = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   # 'function_set': {'neg': 1, 'mul': 1, 'pow': 1, 'add': 1, 'div': 1, 'log': 1}, -> troppo largo 
                   'function_set': {'neg': 1, 'mul': 1, 'pow': 1, 'add': 1, 'div': 1},
                   'const_range': (1, 4),
                   'generations': 20,     # Symbolic Regression
                   # 'generations': 16,     # Symbolic SINDy -> still good but keep 20
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

hill_par_k_config = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   # 'function_set': {'neg': 1, 'mul': 1, 'pow': 1, 'add': 1, 'div': 1, 'log': 1}, -> troppo largo 
                   'function_set': {'neg': 1, 'mul': 1, 'pow': 1, 'add': 1, 'div': 1},
                   'const_range': (1, 4),
                   # 'generations': 30,     # Symbolic Regression -> crash del kernel -> tieni 20
                   'generations': 20,     # Symbolic SINDy
                   'stopping_criteria': 0.001,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

frac_config = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   # 'function_set': {'neg': 1, 'mul': 1, 'div': 1, 'add': 1, 'pow': 1},  # Symbolic Regression
                   'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'pow': 1, 'log': 1, 'div': 1}, # Symbolic-SINDy
                   'const_range': (1, 2),
                   # 'generations': 20,       # Symbolic Regression
                   'generations': 6,      # Symbolic-SINDy
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }

trigonometric_config = {'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   #'function_set': {'neg': 1, 'mul': 3, 'log': 1, 'add': 1},
                   'function_set': {'neg': 1, 'mul': 3, 'add': 1, 'sin': 1, 'cos': 1},
                   #'function_set': {'neg': 1, 'mul': 3, 'log': 1, 'add': 1, 'div': 1, 'pow': 1, 'sin': 1, 'cos': 1},
                   'const_range': (1, 2),
                   #'generations': 20,
                   'generations': 6,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 0,
                   'parsimony_coefficient': 0.01,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                   }


vdp_config_x0 = {
                    'population_size': 10000,          # ridotto per velocità, 10000 se hai tempo
                    'p_crossover': 0.6903,
                    'p_subtree_mutation': 0.133,
                    'p_hoist_mutation': 0.0361,
                    'p_point_mutation': 0.0905,
                    'function_set': {'sub': 1, 'mul': 3, 'add': 1, 'pow': 1},
                    'const_range': (0, 5),           # permetti anche costanti negative
                    'generations': 20,                # più evoluzioni per convergere
                    'stopping_criteria': 0.001,       # più realistico
                    'max_samples': 0.9,
                    'verbose': 1,
                    'parsimony_coefficient': 0.01,
                    'init_depth': (1, 6),
                    'n_jobs': 2,
                }

vdp_config_x1 = {
                    'population_size': 10000,          
                    'p_crossover': 0.69,
                    'p_subtree_mutation': 0.133,
                    'p_hoist_mutation': 0.0361,
                    'p_point_mutation': 0.0905,
                    'function_set': {'sub': 1, 'mul': 3, 'add': 1, 'pow': 1},
                    'const_range': (0, 5),           
                    'generations': 20,                # più evoluzioni per convergere
                    'stopping_criteria': 0.001,       # più realistico
                    'max_samples': 0.9,
                    'verbose': 1,
                    'parsimony_coefficient': 0.01,
                    'init_depth': (1, 6),
                    'n_jobs': 2,
                }


oscilvdp_config = {
                   'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set':  {'neg': 1, 'mul': 1, 'add': 1, 'sub': 1, 'pow': 1, 'sin': 1, 'cos': 1},           # Function set SR
                   # 'function_set':  {'neg': 1, 'mul': 1, 'log': 1, 'add': 1, 'sub': 1, 'pow': 1, 'sin': 1, 'cos': 1},   # Function set Symbolic-SINDy
                   'const_range': (1, 5),
                   'generations': 20,       # Generations for SR
                   # 'generations': 6,     # Generations for Symbolic-SINDy
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   # 'parsimony_coefficient': 0.01, # SR-T e Symbolic-SINDy
                   # 'parsimony_coefficient': 2, # D-CODE: alzato perche altrimenti senza senso
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                  }


oscilvdp_par_w_config = {
                   'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set':  {'neg': 1, 'mul': 2, 'add': 1, 'sub': 1, 'sin': 1},           # Best Function set SR
                   # 'function_set':  {'neg': 1, 'mul': 2, 'log': 1, 'add': 1, 'sub': 1, 'sin': 1},   # Function set Symbolic-SINDy
                   'const_range': (1, 5),
                   'generations': 20,       # Generations for SR
                   # 'generations': 11,       # Generations for Symbolic-SINDy
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.004, # SR-T
                   # 'parsimony_coefficient': 0.5, # D-CODE
                   # 'parsimony_coefficient': 0.004, # 0.001, # NOTE: abbassato per permettere soluzioni piu complesse a SR-T in poche simulazioni
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                  }



tvlv_config =  {
                'population_size': 15000,
                'p_crossover': 0.6903,
                'p_subtree_mutation': 0.133,
                'p_hoist_mutation': 0.0361,
                'p_point_mutation': 0.0905,
                'function_set': {'neg': 1, 'mul': 1, 'add': 1, 'sub': 1, 'sin': 1},
                # 'function_set': {'neg': 1, 'mul': 1, 'log': 1, 'add': 1, 'sub': 1, 'div': 1, 'pow': 1, 'sin': 1, 'cos': 1},
                # 'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'log': 1},
                # 'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'pow': 1, 'log': 1}, 
                'const_range': (0.01, 6),
                'generations': 14, # 20, #11,
                'stopping_criteria': 0.01,
                'max_samples': 0.9,
                'verbose': 1,
                'parsimony_coefficient': 0.5, #0.01, # NOTE: Alzato la regolarizzazione per prevenire forme troppo complesse (e.g. sin(sin(sin(5t))) )
                'init_depth': (1, 6),
                'n_jobs': 2,
                'low_memory': True
                }


tvselkov_config =  {
                'population_size': 15000,
                'p_crossover': 0.6903,
                'p_subtree_mutation': 0.133,
                'p_hoist_mutation': 0.0361,
                'p_point_mutation': 0.0905,
                # 'function_set': {'neg': 1, 'mul': 1, 'add': 1, 'sub': 1, 'cos': 1},
                'function_set': {'neg': 1, 'mul': 1, 'log': 1, 'add': 1, 'sub': 1, 'pow': 1, 'sin': 1, 'sig': 1},
                # 'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'pow': 1},
                # 'function_set': {'sub': 1, 'mul': 1, 'add': 1, 'neg': 1, 'sin': 1, 'pow': 1, 'log': 1}, 
                'const_range': (0.01, 2),
                'generations': 11,
                'stopping_criteria': 0.01,
                'max_samples': 0.9,
                'verbose': 1,
                'parsimony_coefficient': 0.01, # 0.001, #0.01,
                'init_depth': (1, 6),
                'n_jobs': 2,
                'low_memory': True
                }



tvvdp_config = {
                'population_size': 15000,
                'p_crossover': 0.6903,
                'p_subtree_mutation': 0.133,
                'p_hoist_mutation': 0.0361,
                'p_point_mutation': 0.0905,
                'function_set':  {'neg': 1, 'mul': 2, 'add': 1, 'sub': 1, 'cos': 1},
                   'const_range': (0.01, 5),
                   'generations': 20,
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 0.05, # 0.01, 
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                }


tvvdp2_config = {
                'population_size': 15000,
                'p_crossover': 0.6903,
                'p_subtree_mutation': 0.133,
                'p_hoist_mutation': 0.0361,
                'p_point_mutation': 0.0905,
                'function_set':  {'neg': 1, 'mul': 2, 'add': 1, 'sub': 1, 'cos': 1},
                # 'function_set':  {'neg': 1, 'mul': 2, 'add': 1, 'sub': 1, 'cos': 1, 'log': 1}, -> non funziona
                # 'const_range': (2, 5), # -> SR-T trova 4.028
                'const_range': (3, 5), # SR-T trova 4.008
                'generations': 11,
                'stopping_criteria': 0.01,
                'max_samples': 0.9,
                'verbose': 1,
                'parsimony_coefficient':0.01, #  0.02, # 0.01,
                # 'parsimony_coefficient': 40, # 0.4, # D-CODE, 
                'init_depth': (1, 6),
                'n_jobs': 2,
                'low_memory': True
                }



## HD Config

rd_config = {
    'population_size': 15000,
    'p_crossover': 0.6903,
    'p_subtree_mutation': 0.133,
    'p_hoist_mutation': 0.0361,
    'p_point_mutation': 0.0905,
    'function_set': {'add': 1, 'mul': 1, 'sub': 1, 'neg': 1, 'sin': 1}, # HD configuration
    'const_range': (1, 5),
    'generations': 6,
    'stopping_criteria': 0.01,
    'max_samples': 0.9,
    'verbose': 1,
    'parsimony_coefficient': 0.01,
    'init_depth': (1, 6),
    'n_jobs': 2,
    'low_memory': True
}

# config per cos (5t)
doublegyre_config = {
                   'population_size': 15000,
                   'p_crossover': 0.6903,
                   'p_subtree_mutation': 0.133,
                   'p_hoist_mutation': 0.0361,
                   'p_point_mutation': 0.0905,
                   'function_set':  {'neg': 1, 'mul': 1, 'add': 1, 'sub': 1, 'sin': 1, 'cos':1}, 
                   'const_range': (0, 6),
                   'generations': 11, 
                   'stopping_criteria': 0.01,
                   'max_samples': 0.9,
                   'verbose': 1,
                   'parsimony_coefficient': 1,
                   'init_depth': (1, 6),
                   'n_jobs': 2,
                   'low_memory': True
                  }

# Config per cos(0.628t)
# doublegyre_config = {
#                    'population_size': 15000,
#                    'p_crossover': 0.6903,
#                    'p_subtree_mutation': 0.133,
#                    'p_hoist_mutation': 0.0361,
#                    'p_point_mutation': 0.0905,
#                    'function_set':  {'neg': 1, 'mul': 1, 'add': 1, 'sub': 1, 'sin': 1, 'cos':1}, 
#                    'const_range': (-1, 1), # (0, 6),
#                    'generations': 20, 
#                    'stopping_criteria': 0.01,
#                    'max_samples': 0.9,
#                    'verbose': 1,
#                    'parsimony_coefficient': 7, # 1, NOTA: con 2 ce
#                    'init_depth': (1, 6),
#                    'n_jobs': 2,
#                    'low_memory': True
#                   }







