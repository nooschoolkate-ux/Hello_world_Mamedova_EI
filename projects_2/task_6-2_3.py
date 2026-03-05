blood_number_donor = float(input("Введите группу крови донора: "))
blood_number_patient = float(input("Введите группу крови пациента: "))
if blood_number_donor == blood_number_patient or blood_number_donor == "0":
    print("Донор подходит")
else:
    print("Донор не подходит")
