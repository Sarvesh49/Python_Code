print("Hospital Admission form:")
patient_Name = input("Enter Patient name: ")
patient_Age = input("Enter Patient age: ")
patient_Gender = input("Enter patient gender: ")
patient_Contact = input("Enter patient contact: ")
submit = input("Do you want to submit? (Enter 'y' for yes, 'n' for no): ")

if submit.lower() == 'y':
    print("Patient name:", patient_Name)
    print("Patient age:", patient_Age)
    print("Patient gender:", patient_Gender)
    print("Patient contact:", patient_Contact)
else:
    print("Hospital admission form not submitted.")