from pydantic import BaseModel

class TrackerDailyJournal(BaseModel):
	timestamp : str
	time : int = None
	site_id : int = None
	its : str = None
	ncu_id : str = None
	spc_name : str = None
	spc_id : str = None
	duration : float = None
	day_night : str = None
	plant_poa : float = None
	plant_ghi : float = None
	tracker_no_data : int = None
	online : float = None
	last_update_minutes : float = None
	tracker_stow : float = None
	night_stow : bool = None
	fault_hi : float = None
	fault_low : float = None
	motor_current : float = None
	auto_track : float = None
	current_position : float = None
	target_position : float = None
	angle_diff : float = None
	percent_production_factor : float = None
	percent_production_loss_angle_diff : float = None
	meter_name : str = None
	site_energy_delta : float = None
	active_power_count_by_its_k_w : int = None
	avg_active_power_by_its_k_w : float = None
	calc_energy_produced_by_its_k_w_h : float = None
	binned_energy_produced_by_its_k_w_h : float = None
	no_energy_flag : bool = None
	energy_dur : float = None
	no_energy_dur : float = None
	zero_energy_dur : float = None
	neg_energy_dur : float = None
	non_zero_energy_dur : float = None
	time_diff : float = None
	sys_status1 : str = None
	sys_status2 : str = None
	sys_status3 : str = None
	sys_status4 : str = None
	sys_status5 : float = None
	sunrise : str = None
	sunset : str = None
	record_inserted : str = None

class Inverter(BaseModel):
	id : int = None
	site_id : int = None
	record_date : str = None
	plant_serial : int = None
	inverter_id : int = None
	data_points : int = None
	energy_kwh : float = None
	theoretical_energy_kwh : float = None
	stop_time_hrs : float = None
	stop_time_pc : float = None
	lost_energy_kwh : float = None
	efficiency_kwh_kwp : float = None
	efficiency_pc : float = None
	comms_pc : float = None

class TrackerDailySummaryByIts(BaseModel):
	site_id : int = None
	its : str = None
	day : str = None
	its_uptime_o_f_s : float = None
	its_uptime_o_f_s_a : float = None
	no_data_sun_up : float = None
	dffline_sun_up : float = None
	stowed_sunup : float = None
	faulted_sun_up : float = None
	manual_sun_up : float = None
	angle_delta10_deg_sun_up : float = None
	night_stowed_total : float = None
	production_loss_by_angle_delta : float = None
	its_downtime_o_f_s : float = None
	its_downtime_o_f_s_a : float = None
	hr_tracker_count24 : int = None
	calc_expected_tracker_hrs : int = None
	rec_tracker_hrs : float = None
	cal_sun_hrs : float = None
	rec_sun_hrs : float = None
	sun_up_no_tracker_data_hrs_n_d : float = None
	sun_up_its_offline_hrs_o : float = None
	sun_up_its_manual_hrs_m : float = None
	sun_up_its_faulted_hrs_f : float = None
	sun_up_its_stowed_hrs_s : float = None
	sun_up_its_night_stowed_hrs_n_s : float = None
	sun_up_its_angle_delta10deg_hrs_a : float = None
	its_downtime_hrs_o_f_s : float = None
	its_downtime_hrs_o_f_s_a : float = None
	no_tracker_data_hrs_n_d_t : float = None
	its_offline_hrs_o_t : float = None
	its_faulted_hrs_f_t : float = None
	its_stowed_hrs_s_t : float = None
	its_night_stowed_hrs_n_s_t : float = None
	its_angle_delta10deg_hrs_a_t : float = None
	sun_up_rec_energy_hrs : float = None
	sun_up_no_energy_data_hrs_n_d_e : float = None
	sunup_negative_energy_hrs_n_e_g_e : float = None
	sun_up_zero_energy_hrs_z_e : float = None
	sun_up_positive_energy_hrs_p_o_s_e : float = None
	rec_energy_hrs : float = None
	no_energy_data_hrs_n_d_e_t : float = None
	negative_energy_hrs_n_e_g_e_t : float = None
	zero_energy_hrs_z_e_t : float = None
	positive_energy_hrs_p_o_s_e_t : float = None
	site : str = None
	sunrise : str = None
	sunset : str = None
	oem : str = None
	level : str = None
	ncu_count : int = None
	spc_count : int = None
	last_seen : str = None
	total_site_energy_delta_m_wh : float = None
	avg_active_power_by_its_k_w : float = None
	active_power_count_by_its_k_w : int = None
	binned_energy_produced_by_its_k_wh : float = None

class Comment(BaseModel):
	id : int = None
	site_id : int = None
	timestamp : str = None
	inv : int = None
	serial : int = None
	remarks : str = None

class InverterFault(BaseModel):
	its : int = None
	site_id : int = None
	fault_code : int = None
	from_t_stamp : int = None
	to_t_stamp : int = None
	lost_kwh : float = None
	minutes : int = None

class Plant(BaseModel):
	id : int = None
	site_id : int = None
	record_date : str = None
	record_period : int = None
	data_points : int = None
	reference_pr_pc : float = None
	total_ir_wh_sqm : float = None
	production_time_hrs : float = None
	stop_time_hrs : float = None
	produced_energy_kwh : float = None
	theoretical_energy_kwh : float = None
	lost_energy_kwh : float = None
	availability_pc : float = None
	grid_events_hrs : float = None
	grid_availability_pc : float = None
	grid_lost_energy_kwh : float = None
	energy_availability_pc : float = None
	yield_pc : float = None
	pr_pc : float = None
	rsd_pc : float = None
