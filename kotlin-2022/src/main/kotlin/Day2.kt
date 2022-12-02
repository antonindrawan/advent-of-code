
class Day2 {
    enum class RockPaperScissorsChoice (val rps: Int) {
        Rock(0),
        Paper(1),
        Scissors(2)
    }

    fun calculateScore(opponentChoice: RockPaperScissorsChoice, myChoice: RockPaperScissorsChoice): Int {
        var score = 0
        when (opponentChoice) {
            RockPaperScissorsChoice.Rock -> {
                score += when (myChoice) {
                    RockPaperScissorsChoice.Rock -> 1 + 3
                    RockPaperScissorsChoice.Paper -> 2 + 6
                    RockPaperScissorsChoice.Scissors -> 3 + 0
                }
            }
            RockPaperScissorsChoice.Paper -> {
                score += when (myChoice) {
                    RockPaperScissorsChoice.Rock -> 1 + 0
                    RockPaperScissorsChoice.Paper -> 2 + 3
                    RockPaperScissorsChoice.Scissors -> 3 + 6
                }
            }
            RockPaperScissorsChoice.Scissors -> {
                score += when (myChoice) {
                    RockPaperScissorsChoice.Rock -> 1 + 6
                    RockPaperScissorsChoice.Paper -> 2 + 0
                    RockPaperScissorsChoice.Scissors -> 3 + 3
                }
            }
        }
        return score
    }

    fun part1(lines: List<String>) {
        var score = 0
        lines.forEach {
            // A = Rock
            // B = Paper
            // C = Scissors
            val opponentChoice = RockPaperScissorsChoice.values()[it[0] - 'A']
            val myChoice = RockPaperScissorsChoice.values()[it[2] - 'X']

            score += calculateScore(opponentChoice, myChoice)
        }
        println(score)
    }

    fun part2(lines: List<String>) {
        var score = 0
        lines.forEach {
            // A = Rock
            // B = Paper
            // C = Scissors
            val opponentChoice = RockPaperScissorsChoice.values()[it[0] - 'A']
            var myChoice = RockPaperScissorsChoice.Paper
            when (it[2]) {
                'X' -> {
                    //we need to lose
                    myChoice = when (opponentChoice) {
                        RockPaperScissorsChoice.Rock -> RockPaperScissorsChoice.Scissors
                        RockPaperScissorsChoice.Paper -> RockPaperScissorsChoice.Rock
                        RockPaperScissorsChoice.Scissors -> RockPaperScissorsChoice.Paper
                    }
                }
                'Y' -> {
                    // we need to draw
                    myChoice = opponentChoice
                }
                'Z' -> {
                    // we need to win
                    myChoice = when (opponentChoice) {
                        RockPaperScissorsChoice.Rock -> RockPaperScissorsChoice.Paper
                        RockPaperScissorsChoice.Paper -> RockPaperScissorsChoice.Scissors
                        RockPaperScissorsChoice.Scissors -> RockPaperScissorsChoice.Rock
                    }
                }
            }

            score += calculateScore(opponentChoice, myChoice)
        }
        println(score)
    }
}
fun main() {
    var lines = ReadFile().readFileAsLines("input/day2.txt")
    Day2().part1(lines)
    Day2().part2(lines)
}