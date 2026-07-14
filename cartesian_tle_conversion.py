import csv
import numpy as np
import geodesy as gd

"""take in a tle"""
def elements_from_tle(file):
    with open(file , 'r') as f:
        rows = f.readlines()

        elements = [i for i in csv.reader(rows , delimiter = ' ')]
        
        sat_name = elements[0][0] #string
        norad_id = int(elements[1][1][0:5]) #integer
        classification = elements[1][1][5] #string
        internal_designator = elements[1][2:5] #string
        tle_validity = float(elements[1][5]) #float
        oneder_meanmotion = float(elements[1][7]) #float

        twoder_meanmotion = elements[1][9] #string
        twoder_plus = twoder_meanmotion.rfind('+')
        twoder_minus = twoder_meanmotion.rfind('-')

        if twoder_plus != -1:
            twoder_float = float(twoder_meanmotion[:twoder_plus]) * 10**(float(twoder_meanmotion[twoder_plus:])) #float
        
        elif twoder_minus != -1:
            twoder_float = float(twoder_meanmotion[:twoder_minus]) * 10**(float(twoder_meanmotion[twoder_minus:]))

        drag_term = elements[1][10]
        cntplus = drag_term.rfind('+') #finding last occurrence
        cntminus = drag_term.rfind('-')
                
        if cntplus != -1:
            dragfloat = float(drag_term[:cntplus]) * 10**(float(drag_term[cntplus:]))
        
        elif cntminus != -1:
            dragfloat = float(drag_term[:cntminus]) * 10**(float(drag_term[cntminus:]))
            
        eph_type = int(elements[1][11])
        elementno_checksum = int(elements[1][13][-1]) #mod10
        inclination = float(elements[2][4])
        raan = float(elements[2][5]) #right ascention of the ascending node
        eccentricity = float(elements[2][6]) / 10**6 #float
        arg_perigee = float(elements[2][8])
        mean_anomaly = float(elements[2][9])
        mean_motion = float(elements[2][10])
        revno_checksum = float(elements[2][12]) #final element is checksum mod 10

        orb_elements = []


if __name__ == "__main__":
    elements_from_tle(r"C:\Users\xa360\Documents\div\NUSTAR.txt")


   
