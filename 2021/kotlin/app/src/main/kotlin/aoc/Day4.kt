package aoc

import java.io.File
import kotlin.time.seconds

class Day4(input: File) {
    val lines: List<String>
    var numInputs: List<Int> = mutableListOf()
    var boards = mutableListOf<MutableList<Pair<Int, Boolean>>>()

    init {
        lines = input.readLines()

        numInputs = lines[0].split(",").map{ it.toInt() }.toList()
        var board = mutableListOf<Pair<Int, Boolean>>()
        for (row in 2..lines.size - 1) {
            if (lines[row].isEmpty()) {
                boards.add(board)
                board = mutableListOf<Pair<Int, Boolean>>()
            } else {
                board.addAll(lines[row].trim().split("\\s+".toRegex()).map { Pair(it.toInt(), false) }.toList())
            }
        }
        // adding the last board
        boards.add(board)

        println(numInputs)
        println("Nr of boards: ${boards.size}")
    }

    fun solve(): List<Int> {
        var boardBingos = mutableSetOf<Int>()
        var results = mutableListOf<Int>()
        for (num in numInputs) {
            boards.forEachIndexed { index, board ->
                // set number to true
                if (!boardBingos.contains(index)) {
                    setNumber(board, num)
                    if (isBingo(board)) {
                        boardBingos.add(index)
                        val sumUnMarkedNumbers = boards[index].filter { it.second == false }.sumOf {it.first}
                        results.add(sumUnMarkedNumbers * num)
                    }
                }
            }
        }
        return results
    }

    companion object {
        fun setNumber(board: MutableList<Pair<Int, Boolean>>, num: Int) {
            val returnVal = board.indexOfFirst { it.first == num }
            if (returnVal != -1) {
                board[returnVal] = Pair(board[returnVal].first, true)
            } else {
                assert(false)
            }
        }

        fun isBingo(board: List<Pair<Int, Boolean>>): Boolean {
            // check horizontally
            // row 1: 0, 1, 2, 3 ,4
            // row 2: 5, 6, 7, 8 ,9
            // etc
            for (i in 0..4) {
                var bingo = true
                for (j in 0..4) {
                    if (!board[i * 5 + j].second) {
                        bingo = false
                        break
                    }
                }
                if (bingo) return true
            }

            // check vertically
            // col 1: 0, 5, 10, 15, 20
            // col 2: 1, 6, 11, 16, 21
            // etc
            for (i in 0..4) {
                var bingo = true
                for (j in 0..4) {
                    if (!board[i + (j * 5)].second) {
                        bingo = false
                        break
                    }
                }
                if (bingo) return true
            }
            return false
        }
    }
}

fun main() {
    val resource = "./inputs/4/"
    val part1_short = Day4(File("${resource}/4-short.txt"))
    var results = part1_short.solve()
    println("Answer part 1: ${results.first()}")
    println("Answer part 2: ${results.last()}")

    val part1 = Day4(File("${resource}/4.txt"))
    results = part1.solve()
    println("Answer part 1: ${results.first()}")
    println("Answer part 2: ${results.last()}")
}