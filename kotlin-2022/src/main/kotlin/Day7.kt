class Node(val type: Type, val name: String, var size: Int = 0) {
    enum class Type {
        file,
        dir
    }
    var child: MutableList<Node> = mutableListOf()
    var parentDir: Node? = null
}



class Day7 {
    val cd_pattern = "^\\$ cd (.*)".toRegex()

    val mkdir_pattern = "^dir (.*)".toRegex()
    val file_pattern = "^(\\d+) (.*)".toRegex()

    var root: Node = Node(Node.Type.dir, "/")
    var currentDirectory: Node? = null

    val dirnameToNode: MutableMap<String, Node> = mutableMapOf()

    private fun _printNode(node: Node?, depth: Int = 0) {
        node?.let {
            for (i in 1..depth) print(">")
            println("Dir: ${node.name}, ${node.size}")
            for (c in it.child) {

                when (c.type) {
                    Node.Type.file -> {
                        for (i in 1..depth+1) print(">")
                        println("File: ${c.name}, ${c.size}")
                    }
                    Node.Type.dir -> {
                        _printNode(c, depth + 1)
                    }
                }
            }
        }
    }

    private fun _setDirectorySize(node: Node?, depth: Int = 0) {
        node?.let {
            for (c in it.child) {
                when (c.type) {
                    Node.Type.file -> {
                        node.size += c.size
                    }
                    Node.Type.dir -> {
                        _setDirectorySize(c, depth + 1)
                        node.size += c.size
                    }
                }
            }
        }
    }

    private fun _getDirectories(node: Node?, maxValue: Int, nodes: MutableList<Node>)  {
        node?.let {
            for (c in it.child) {
                if (c.type == Node.Type.dir) {
                    if (c.size <= maxValue) {
                        nodes.add(c)
                    }
                    _getDirectories(c, maxValue, nodes)
                }
            }
        }
    }

    fun prepare(lines: List<String>) {
        // A shortcut to go to the root directory
        dirnameToNode["/"] = root

        lines.forEach { it ->
            cd_pattern.find(it)?.apply {
                val (dirname) = destructured
                // println("Entering $dirname")
                when (dirname) {
                    "/" -> {
                        currentDirectory = root
                    }
                    ".." -> {
                        // one directory up
                        currentDirectory = currentDirectory?.parentDir
                    }
                    else -> {
                        var found = false
                        for (child in currentDirectory?.child!!) {
                            if (child.name == dirname) {
                                currentDirectory = child
                                found = true
                                break
                            }
                        }
                        if (!found) throw Exception("No directory with named $dirname")
                    }
                }
            }

            mkdir_pattern.find(it)?.apply {
                val (dirname) = destructured
                // println("Creating $dirname")

                Node(Node.Type.dir, dirname).let {
                    it.parentDir = currentDirectory
                    currentDirectory?.child?.add(it)
                }
            }

            file_pattern.find(it)?.apply {
                val (size, filename) = destructured
                // println("Creating $filename, size=$size")
                Node(Node.Type.file, filename, size.toInt()).let {
                    it.parentDir = currentDirectory
                    currentDirectory?.child?.add(it)
                }
            }
        }
        _setDirectorySize(root)
        // _printNode(root)
    }

    fun part1(maxValue: Int) : Int {
        val dirs = mutableListOf<Node>()
        _getDirectories(root, maxValue, dirs)
        return dirs.sumOf { it.size }
    }

    fun part2(maxDiskSpace: Int, minUnusedSpace: Int): Int {
        val currentUnused = maxDiskSpace - root.size
        val need = minUnusedSpace - currentUnused

        val dirs = mutableListOf<Node>()
        _getDirectories(root, root.size, dirs)

        dirs.sortBy { it.size }
        dirs.forEach {
            if (it.size > need) {
                return it.size
            }
        }
        return 0
    }
}

fun main() {
    val lines = ReadFile().readFileAsLines("input/day7.txt")
    Day7().apply {
        prepare(lines)
        println("Part1: ${part1(maxValue = 100000)}")
        println("Part2: ${part2(70000000, 30000000)}")
    }
}