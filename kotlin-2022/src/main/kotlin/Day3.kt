class Day3 {
    private fun calculateScore(duplicateContent: Set<Char>): Int {
        var score = 0
        for (content in duplicateContent) {
            if (content in 'a'..'z') {
                score += content - 'a' + 1
            } else if (content in 'A' .. 'Z') {
                score += content - 'A' + 27
            }
        }
        return score
    }

    private fun getDuplicateContent(compartment: Set<Char>, otherCompartment: String) : Set<Char> {
        var duplicateContent = mutableSetOf<Char>()
        for (char in otherCompartment) {
            if (char in compartment) {
                duplicateContent.add(char)
            }
        }
        return duplicateContent
    }

    fun part1(lines: List<String>) : Int {
        var score = 0
        lines.forEach {
            var compartmentContent = mutableSetOf<Char>()

            val compartments = it.chunked(it.length / 2)
            for (char in compartments[0]) {
                compartmentContent.add(char)
            }

            var duplicateContent = getDuplicateContent(compartmentContent, compartments[1])
            score += calculateScore(duplicateContent)
        }
        return score
    }

    fun part2(lines: List<String>) : Int {
        var score = 0
        for (i in lines.indices step 3) {
            var compartmentContent = mutableSetOf<Char>()
            for (char in lines[i]) {
                compartmentContent.add(char)
            }

            var duplicateContent = getDuplicateContent(compartmentContent, lines[i + 1])
            duplicateContent = getDuplicateContent(duplicateContent, lines[i + 2])

            score += calculateScore(duplicateContent)
        }
        return score
    }
}

fun main() {
    var lines = ReadFile().readFileAsLines("input/day3.txt")
    println("Part 1: ${Day3().part1(lines)}")
    println("Part 2: ${Day3().part2(lines)}")
}