

let machines= [{name:"MachineA",personeel:2,historyRecord:4, demand:"High", parts:"Engine"},{name:"MachineB",personeel:4,historyRecord:4,demand:"low" , parts:"Lever"} ]

function checkPriority(){
    for (i=0;i<machines.length;i++ ){
        let machine =machines[i]

        if(machine.personeel<=4 && machine.historyRecord<=4 && machine.demand=="High" && machine.parts=="Engine"){
            console.log(`This ${machine.name} gets the priority  to be serviced`)}

        
      else if
      (machine.personeel>4 &&
       machine.personeel<10 &&
       machine.parts=="Lever"&&
        machine.historyRecord>4 && 
        machine.historyRecord<10){
        console.log(`This ${machine.name} gets mid priority  to be serviced`)

      }

      else{
        console.log(`This ${machine.name} gets the leaset priority  to be serviced`)
      }  
        
    }}
    checkPriority()

