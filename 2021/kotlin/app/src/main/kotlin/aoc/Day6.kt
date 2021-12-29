package aoc

import java.io.File
import kotlin.math.abs

class Day6(input: File) {

    var lines: List<String>
    var lanternFishes: List<Int> = mutableListOf()
    init {
        lines = input.readLines()[0].split(",")
    }

    fun solve(days: Int): Long {
        lanternFishes = lines.map { it.toInt() }.toList()

        var mapFish = mutableMapOf<Int, Long>()
        for (fish in lanternFishes) {
            mapFish[fish] = mapFish[fish]?.inc() ?: 1
        }

        for (day in 1..days) {
            var newMapFish = mutableMapOf<Int, Long>()
            mapFish.forEach { (fish, counter) ->
                if (fish == 0) {
                    newMapFish[6] = newMapFish[6]?.plus(counter) ?: counter
                    newMapFish[8] = newMapFish[8]?.plus(counter) ?: counter
                } else {
                    newMapFish[fish - 1] = newMapFish[fish - 1]?.plus(counter) ?: counter
                }
            }

            mapFish = newMapFish
        }

        return mapFish.map { it.value }.sum()
    }
}

fun main() {
    val resource = "./inputs/6/"
    val day6_short = Day6(File("${resource}/6-short.txt"))
    var results = day6_short.solve(80)
    println("Answer part 1 (short): ${results}")

    val day6 = Day6(File("${resource}/6.txt"))
    results = day6.solve(80)
    println("Answer part 1: ${results}")

    // part 2
    results = day6_short.solve(256)
    println("Answer part 2 (short): ${results}")

    results = day6.solve(256)
    println("Answer part 2: ${results}")
}