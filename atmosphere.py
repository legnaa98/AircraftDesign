from numpy import exp

def atmosphere(h):

	Tsl_ISA = 15 # [ºC] Temperature at sea level. ISA satndard
	deltaT = 0 # [ºC] latitude temperature deviation. ISA standard
	Tsl_C = Tsl_ISA + deltaT # [ºC] temperature at mean sea level
	Tsl = Tsl_C + 273.15; # [K] absolute temperature at mean sea level 

	g = 9.80665 # [m/s2] gravity acceleration
	Psl = 101325 # [Pa] Pressure at mean sea level. ISA standard
	L = 0.0065 # [K/m] lapse rate
	Rstar = 8.31432 # [J/mole°K] universal gas constant 
	M = 0.0289644 # [kg/mole] mean molecular mass of air 
	R = Rstar/M # [J/(kg.K)] gas constant for air 
	gamma = 1.4 # ratio of specific heat capacities of air, cp/cv
	n = g/(R*L);

	hs = 11000 # [m] ISA atmosphere troposphere altitude 
	Ts = Tsl - L*hs # [K] ISA atmosphere temperature at stratosphere 

	if h < hs: # in troposphere
		T = Tsl-L*h # [K] temperature at altitude
		P = Psl*(T/Tsl)**n; # pressure at altitude
	else: # in stratosphere
		T = Ts;
		P = Ps*exp(g*(hs-h)/(R*Ts)); # pressure at altitude

	rho = P/(R*T) # density at altitude

	a = (gamma*R*T)**(0.5) # speed of sound according to ISA standard model

	return(rho,P,T,a)