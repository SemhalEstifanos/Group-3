Design a maintenance sceduling system for industrial equipment used in manufacturing. 
This system must optimize the timing of maintenance to minimize downtime and ensure machine 
operates at peak efficiency .Consider the operational demands of the plant ,the availability
 of maintenance personnel and parts and the historical data of equipment wears and failures.


data class Maintain(var name: String, var demand: String, var historicalData: Int, var personnel: Int, var part: String)
fun maintenancePriority(machines: List<Maintain>) {
    for (item in machines) {
        if (item.demand == "High" && item.historicalData <= 3 && item.personnel <= 4 && item.part == "Engine") {
            println("${item.name}:Takes high priority")
        }
        else if (item.demand == "Medium" && item.historicalData 4 to 7 && item.personnel 5..7){
            println("${item.name}:Takes average priority")
        }
        else {
            println("${item.name}:Takes low priority")
        }
    }
}

fun main() {
    val machines = listOf(
        Maintain("Machine A", "Low", 2, 4, "Gear"),
        Maintain("Machine B", "High", 3, 3, "Engine"),
    )
    maintenancePriority(machines)
}