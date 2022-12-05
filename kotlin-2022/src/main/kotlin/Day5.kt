class Day5 {
    val re = Regex("move (\\d+) from (\\d) to (\\d)")
    fun part(partNumber: Int, lines: List<String>): String {
        val cargoLines : MutableList<ArrayDeque<String>> = mutableListOf()

        // NOTE: I modified the input format for easy parsing
        // See <workspace>/input/day5-short.txt

        lines.forEach { it ->
            if (it.startsWith("move")) {
                re.find(it)?.apply {
                    var amount = 0; var from = 0; var to = 0
                    destructured.let { (amountStr, fromStr, toStr) ->
                        amount = amountStr.toInt()
                        from = fromStr.toInt() - 1
                        to = toStr.toInt() - 1
                    }

                    var cratesToMove : MutableList<String> = mutableListOf()
                    for (i in 1..amount) {
                        cratesToMove.add(cargoLines[from].removeLast())
                    }

                    if (partNumber == 2) {
                        cratesToMove = cratesToMove.asReversed()
                    }
                    cratesToMove.forEach { crate ->
                        cargoLines[to].add(crate)
                    }
                }
            } else if (it.isNotBlank()) {
                val stack = ArrayDeque(it.split(","))
                cargoLines.add(stack)
            }
        }

        var topCrates = String()
        cargoLines.forEach {
            topCrates += it.last()
        }
        return topCrates
    }
}

fun main() {
    var lines = ReadFile().readFileAsLines("input/day5.txt")
    println("Part 1: ${Day5().part(partNumber=1, lines)}")
    println("Part 2: ${Day5().part(partNumber=2, lines)}")
}