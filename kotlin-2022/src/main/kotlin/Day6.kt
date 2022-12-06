class Day6 {
    fun part(nrDistinctChar: Int, lines: List<String>) {
        lines.forEach { line ->

            val charSet : MutableMap<Char, Int> = mutableMapOf()
            line.forEachIndexed lit@ { i, char ->
                charSet[char] = charSet.getOrDefault(char, 0) + 1

                if (i >= nrDistinctChar) {
                    val charToRemove = line[i - nrDistinctChar]
                    val count = charSet[charToRemove]
                    if (count != null) {
                        if (count == 1) {
                            charSet.remove(charToRemove)
                        } else {
                            charSet[charToRemove] = count.minus(1)
                        }
                    }
                }
                if (charSet.count() == nrDistinctChar) {
                    println(i + 1)
                    return@forEach
                }
            }
        }
    }

}

fun main() {
    var lines = ReadFile().readFileAsLines("input/day6-short.txt")
    println("Part 1:")
    Day6().part(nrDistinctChar=4, lines)
    println("Part 2:")
    Day6().part(nrDistinctChar=14, lines)
}