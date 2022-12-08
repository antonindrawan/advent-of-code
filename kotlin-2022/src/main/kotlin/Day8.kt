class Day8 {
    lateinit var visibilityStatus: Array<BooleanArray>

    fun prepare(lines: List<String>) {
        visibilityStatus = Array(lines.size) { BooleanArray(lines[0].length) { false } }

        // Mark the border to true
        lines.forEachIndexed { row, line ->
            if (row == 0 || row == lines.lastIndex) {
                for (col in line.indices) {
                    visibilityStatus[row][col] = true
                    visibilityStatus[col][row] = true
                }
            }
        }

        // check horizontally
        for (row in 1 until lines.lastIndex) {
            // left to right
            val line = lines[row]
            var maxValue = line[0]
            for (col in 1 until line.lastIndex) {
                if (line[col] > maxValue) {
                    maxValue = line[col]
                    visibilityStatus[row][col] = true
                }
            }

            // right to left
            maxValue = line[line.lastIndex]
            for (col in line.lastIndex - 1 downTo 1) {
                if (line[col] > maxValue) {
                    maxValue = line[col]
                    visibilityStatus[row][col] = true
                }
            }
        }

        // Check vertically
        for (col in 1 until lines[0].lastIndex) {
            // from top to bottom
            var maxValue = lines[0][col]
            for (row in 1 until lines.lastIndex) {
                if (lines[row][col] > maxValue) {
                    maxValue = lines[row][col]
                    visibilityStatus[row][col] = true
                }
            }

            // from bottom to top
            maxValue = lines[lines.lastIndex][col]
            for (row in lines.lastIndex - 1 downTo 1) {
                if (lines[row][col] > maxValue) {
                    maxValue = lines[row][col]
                    visibilityStatus[row][col] = true
                }
            }
        }
    }

    fun part1(lines: List<String>): Int {
        prepare(lines)
        return visibilityStatus.flatMap { it.asIterable() }.count { it }
    }


    fun part2(lines: List<String>): Int {
        val scenicScore = Array(lines.size) { IntArray(lines[0].length) { 0 } }

        // Mark the border to true
        lines.forEachIndexed { row, line ->
            if (row == 0 || row == lines.lastIndex) {
                for (col in line.indices) {
                    visibilityStatus[row][col] = true
                    visibilityStatus[col][row] = true
                }
            }
        }

        val maxColumn = lines[0].lastIndex
        for (row in 1 until lines.lastIndex) {
            for (col in 1 until maxColumn) {
                fun countLeftOrRight(left: Boolean): Int {
                    var count = 0
                    var range = if (left) (col - 1 downTo 0).toList() else (col + 1..maxColumn).toList()
                    run lit@{
                        range.forEach { i ->
                            if (lines[row][col] <= lines[row][i]) {
                                count += 1
                                return@lit
                            } else {
                                count += 1
                            }
                        }
                    }
                    return count
                }

                val left = countLeftOrRight(true)
                val right = countLeftOrRight(false)
                scenicScore[row][col] = left * right
            }
        }

        // top & down
        for (col in 1 until maxColumn) {
            for (row in 1 until lines.lastIndex) {
                fun countTopOrBottom(top: Boolean): Int {
                    var count = 0
                    var range = if (top) (row - 1 downTo 0).toList() else (row + 1..lines.lastIndex).toList()
                    run lit@{
                        range.forEach { i ->
                            if (lines[row][col] <= lines[i][col]) {
                                count += 1
                                return@lit
                            } else {
                                count += 1
                            }
                        }
                    }
                    return count
                }

                val top = countTopOrBottom(true)
                val bottom = countTopOrBottom(false)
                scenicScore[row][col] *= top * bottom
            }
        }

        return scenicScore.flatMap { it.asList() }.max()
    }
}
fun main() {
    val lines = ReadFile().readFileAsLines("input/day8.txt")
    Day8().apply {
        println("Part1: ${part1(lines)}")
        println("Part2: ${part2(lines)}")
    }
}