package aoc

import java.io.File
import kotlin.math.abs

class Day7(input: File) {
    var lines: List<Int>
    init {
        lines = input.readLines()[0].split(",").map { it.toInt() }
    }

    fun median(list: List<Int>): Int {
        val sortedList = list.sorted()
        if (list.size % 2 == 0) {
            return sortedList[list.size / 2]
        } else {
            return sortedList[list.size / 2] + sortedList[list.size / 2 + 1] / 2
        }
    }

    fun solve(): Int {
        val medianValue = median(lines)
        return lines.sumOf { abs(it - medianValue) }
    }
}

fun main() {
    val resource = "./inputs/7"
    val day7_short = Day7(File("${resource}/7-short.txt"))
    var cost = day7_short.solve()
    println("Answer part1 (short): ${cost}")

    val day7 = Day7(File("${resource}/7.txt"))
    cost = day7.solve()
    println("Answer part1: ${cost}")
}