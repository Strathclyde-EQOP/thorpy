from thorpy.comm.discovery import discover_stages

if __name__ == '__main__':
    from thorpy.message import *
    
    stages = list(discover_stages())
    print(stages)
    s = stages[0]
    
    s.home_velocity = s._conf_home_vel
    s.max_velocity = s._conf_def_max_vel
    s.acceleration = s._conf_def_accn
    s.home_offset_distance = s._conf_home_zero_offset
    s.cw_hard_limit = s._conf_cw_hard_limit
    s.ccw_hard_limit = s._conf_ccw_hard_limit
    s.cw_soft_limit = s._conf_cw_soft_limit
    s.ccw_soft_limit = s._conf_ccw_soft_limit
    s.software_limit_mode = s._conf_soft_limit_mode
    s.backlash_dist = s._conf_backlash_dist
    if s._port._info_message['model_number'].decode('ascii')[:5] == 'SCC20': # BSC20x
        s.rest_power = s._conf_rest_factor
        s.move_power = s._conf_move_factor
        s._port.send_message(MGMSG_MOT_SET_KCUBEKSTLOOPPARAMS(s._chan_ident, 1, 200000, 1000, 100, 100000000, 200, 0, 0, 0))    # as set by APT
    else:
        s._port.send_message(MGMSG_MOT_SET_BUTTONPARAMS(s._chan_ident, 2, 0, 61440000, 2000, 2000))

    s.home(force = True)
    
    s.print_state()
    
    import IPython
    IPython.embed()
    
    #del s, stages
