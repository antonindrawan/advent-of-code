import java.io.File

class ReadFile {
    fun readFileAsLines(fileName: String): List<String> = File(fileName).useLines { it.toList() }
}