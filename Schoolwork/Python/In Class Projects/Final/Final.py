global patient_stay
patient_stay = input("Please type IN for in-patients and please type OUT for out-patients: ").upper()
valid_options_in = ['IN']
valid_options_out = ['OUT']
file_write = open("patient.txt", "w")

def patientstay():
    global patient_stay
    if patient_stay in valid_options_in:
        inpatient()
    if patient_stay in valid_options_out:
        outpatient()

def inpatient():
    global patient_days
    global daily_rate
    global hospital_charges
    global hospital_medication
    global patient_name_in
    patient_name_in = input("Please input your name: ")
    patient_days = input("Please input the number of days you spent at the hospital: ")
    lessthanzero(patient_days)
    daily_rate = input("Please input your daily rate at the hospital: ")
    lessthanzero(daily_rate)
    hospital_charges = input("Please input the total cost of hospital charges(lab tests, etc.): ")
    lessthanzero(hospital_charges)
    hospital_medication = input("Please input the total cost of your medication: ")
    lessthanzero(hospital_medication)
    inpatientcharges()
    
def outpatient():
    global hospital_charges_out
    global hospital_medication_out
    global patient_name_out
    patient_name_out = input("Please input your name: ")
    hospital_charges_out = input("Please input the total cost of hospital charges(lab tests, etc.): ")
    lessthanzero(hospital_charges_out)
    hospital_medication_out = input("Please input the total cost of your medication: ")
    lessthanzero(hospital_medication_out)
    outpatientcharges()
    
def inpatientcharges():
    final_cost = (float(patient_days) * float(daily_rate) + (float(hospital_charges) + float(hospital_medication)))
    file_write.write("Patient: " +patient_name_in+ "\n" "Inpatient or Ourpatient: "+patient_stay+ "\n" "Days spent in the hospital: "+patient_days+ "\n" "The daily rate: "+daily_rate+ "\n" "Charges for hospital services (lab tests, etc.): "+hospital_charges+ "\n" "Hospital medication charges: "+hospital_medication+ "\n" "Final Cost: "+str(final_cost))

def outpatientcharges():
    final_cost_out = float(hospital_charges_out) + float(hospital_medication_out)
    file_write.write("Patient: " +patient_name_out+ "\n" "Inpatient or Ourpatient: "+patient_stay+ "\n" "Charges for hospital services (lab tests, etc.): "+hospital_charges_out+ "\n" "Hospital medication charges: "+hospital_medication_out+ "\n" "Final Cost: "+str(final_cost_out))
    
    
def lessthanzero(check):
    if int(check) < 0:
        print("Please start the form over and input a value bigger than 0")
        exit()
        
patientstay()