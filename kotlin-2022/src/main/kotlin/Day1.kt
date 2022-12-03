import java.io.File
import java.util.Scanner
import kotlin.math.max

fun part1(lines: List<String>) {
    var sum = 0
    var maxSum = 0
    lines.forEach {
        if (it.isBlank()) {
            maxSum = max(sum, maxSum)
            sum = 0

        } else {
            sum += it.toInt()
        }
    }
    maxSum = max(sum, maxSum)
    println("Part2 answer: ${maxSum}")
}

fun part2(lines: List<String>) {
    var sum = 0
    var sumList = mutableListOf<Int>()
    lines.forEach {
        if (it.isBlank()) {
            sumList.add(sum)
            sum = 0

        } else {
            sum += it.toInt()
        }
    }
    sumList.add(sum)

    sumList.sortByDescending { it }
    println("Part2 answer: ${sumList[0] + sumList[1] + sumList[2]}")
}

fun main() {
    var lines = ReadFile().readFileAsLines("input/day1.txt")

    part1(lines)
    part2(lines)
}