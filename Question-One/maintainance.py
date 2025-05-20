# def maintainance_priority(machines):
#     machines=[{"name":"MachineA","personnel":2,"historicaldata":4, "demand":"High"},{"name":"MachineB","personnel":4,"historicaldata":4,"demand":"low"}]
    

#     for machine in machines:
#         if machine["personnel"]<=4 and machine["historicaldata"]<=4 and machine["demand"] =='High':
#             print(f'{machine["name"]} is of high priority')
#         elif machine["personnel"]<=3 and machine["historicaldata"]<=5 and machine["demand"] =='Low':
#             print(f'{machine["name"]} is of low priority')
#         else :
#             print('machine doesnt need service')



def maintainance_priority(machines):

   for machine in machines:
    
    if machine['personnel'] <= 4 and machine['historicaldata'] <= 4 and machine['demand'] == 'High': and machine['parts'] =='Engine'
        print(f'{machine["name"]} is of high priority')
    elif machine['personnel'] <= 3 and machine['historicaldata'] <= 5 and machine['demand'] == 'Low': and machine['parts']=='Brakes'
        print(f'{machine["name"]} is of low priority')
    else:
        print(f'{machine["name"]} doesn’t need service')
        
machines = [
    {"name": "MachineA", "personnel": 2, "historicaldata": 4, "demand": "High","parts":"Engine"},
    {"name": "MachineB", "personnel": 4, "historicaldata": 4, "demand": "Low","parts":"Brakes"}
]