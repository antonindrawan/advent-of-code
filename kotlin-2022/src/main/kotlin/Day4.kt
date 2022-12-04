class ElfPair(s: String) {

    val value : Pair<Int, Int>;
    init {
        s.split("-").also {
            value = Pair(it[0].toInt(), it[1].toInt())
        }
    }

    fun getNumberOfSections() : Int {
        return value.second - value.first + 1
    }
}

class Day4 {

    fun part1(lines: List<String>) : Int {
        var overlap = 0
        lines.forEach {
            val pairs = it.split(",")
            val pair1 = ElfPair(pairs[0])
            val pair2 = ElfPair(pairs[1])

            var minPair = pair1
            var maxPair = pair2
            if (pair1.getNumberOfSections() > pair2.getNumberOfSections()) {
                minPair = pair2
                maxPair = pair1
            }

            if (maxPair.value.first <= minPair.value.first && maxPair.value.second >= minPair.value.second) {
                overlap += 1
            }
        }
        return overlap
    }

    fun part2(lines: List<String>) : Int {
        var overlap = 0
        lines.forEach {
            val pairs = it.split(",")
            val pair1 = ElfPair(pairs[0])
            val pair2 = ElfPair(pairs[1])

            var minPair = pair1
            var maxPair = pair2
            if (pair1.value.first > pair2.value.first) {
                minPair = pair2
                maxPair = pair1
            }

            if (minPair.value.second >= maxPair.value.first) {
                overlap += 1
            }
        }
        return overlap
    }
}

fun main() {
    var lines = ReadFile().readFileAsLines("input/day4.txt")
    println("Part 1: ${Day4().part1(lines)}")
    println("Part 2: ${Day4().part2(lines)}")
}